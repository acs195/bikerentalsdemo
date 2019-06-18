import logging
import config
from rentals.models import BikeRental

logger = logging.getLogger(config.LOGGER_NAME)


class Client:
    """
    A class to represent a client.

    Attributes
    ----------
    client_id : int
        the client unique internal identifier
    first_name : str
        the first name of the client
    last_name : str
        the last name of the client
    rentals : list
        the list of the client's rentals
    promotions : list
        the list of the client's promotions

    Methods
    -------
    None
    """

    # Keeps the last id
    _id_counter = 0
    # Keeps the list of clients
    clients_list = []

    def __init__(self, first_name, last_name):
        """
        Parameters
        ----------
        first_name : str
            the first name of the client
        last_name : str
            the last name of the client
        """

        self.client_id = Client._id_counter
        self.first_name = first_name
        self.last_name = last_name
        self.rentals = []
        self.promotions = []
        Client._id_counter += 1
        Client.clients_list.append(self)
        logger.debug('Client created.')

    def rent_bike(self, rental_type, bike, amount_of_units):
        """The client rents a bike.

        Parameters
        ----------
        rental_type : RentalType
            The RentalType type of the client's choice.
        bike : Bike
            The Bike of the client's choice.
        amount_of_units
            The amount of units (hours, days, weeks) of the client's choice.
        """

        bike_rental = BikeRental(
            rental_type=rental_type,
            bike=bike,
            amount_of_units=amount_of_units
        )
        bike.register_rent()
        self.rentals.append(bike_rental)
        logger.debug('Bike rental added to client.')

    def rent_bikes_with_promotion(self, promotion):
        """The client takes a promotion.

        Parameters
        ----------
        promotion : PromotionRental
            The PromotionRental of the client's choice.

        Raises
        ------
        None
        """

        self.promotions.append(promotion)
        logger.debug('Promotion added to client.')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
