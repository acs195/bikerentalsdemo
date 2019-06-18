import logging
import config
from bikes.models import Bike
from rentals.models import RentalType
from promotions.models import Promotion
from clients.models import Client


class BikeRentalApp:
    """ A class to represent the application.

    Attributes
    ----------
    logger : object
        the application logger

    Methods
    -------
    setup_logger()
        it configures the application logger
    """

    def __init__(self):
        """
        Parameters
        ----------
        None
        """
        self.logger = self.setup_logger()

    def setup_logger(self):
        """ The application logger is configured.

        Parameters
        ----------
        None
        """

        log_level = getattr(logging, config.LOG_LEVEL)
        logger = logging.getLogger(config.LOGGER_NAME)
        logger.setLevel(log_level)
        handler = logging.FileHandler(config.LOG_FILENAME)
        formatter = logging.Formatter(config.LOG_FORMAT)
        handler.setFormatter(formatter)
        handler.setLevel(log_level)
        logger.addHandler(handler)
        return logger

    def initial_load(self):
        # Add bikes
        Bike(
            make='Vairo',
            model='Mountain',
            serial_number='V001'
            ),
        Bike(
            make='Vairo',
            model='Street',
            serial_number='V002'
            ),
        Bike(
            make='Argon',
            model='Mountain',
            serial_number='A001'
            ),
        Bike(
            make='Argon',
            model='Racing',
            serial_number='A002'
            )

        # Add rental types
        rental_types = [('hour', 5.0), ('day', 20.0), ('week', 60.0)]
        for unit, price in rental_types:
            RentalType(
                unit_of_measure=unit,
                price=price
                )

        # Add promotion
        Promotion(
            discount_pct=30.0,
            min_rentals_to_apply=3,
            max_rentals_to_apply=5
            )

        # Add clients
        Client(
                first_name='John',
                last_name='Frusciante'
                ),
        Client(
            first_name='Serj',
            last_name='Tankian'
            )

    def start(self):
        """ The application starts.

        Parameters
        ----------
        None
        """

        self.logger.info('App started.')

        self.initial_load()
        self.logger.info('Initial load completed.')

        print([str(bike) for bike in Bike.bikes_list])
        print([str(rt) for rt in RentalType.rental_types_list])
        print([str(promotion) for promotion in Promotion.promotions_list])
        print([str(client) for client in Client.clients_list])

        while True:
            break

        self.logger.info('App ended. Good bye!')


if __name__ == '__main__':
    my_app = BikeRentalApp()
    my_app.start()
