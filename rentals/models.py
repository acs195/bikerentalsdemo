import logging
import config

logger = logging.getLogger(config.LOGGER_NAME)


class RentalType:
    """
    A class to represent a rental type.

    Attributes
    ----------
    rental_type_id : int
        the rental unique internal identifier
    unit_of_measure : str
        it indicates the unit of measure for the rental period such as
        hours, days or weeks
    price : float
        the price for the unit of the rental period defined by unit_of_measure

    Methods
    -------
    None
    """

    # Keeps the last id
    _id_counter = 0
    # Keeps the list of rental types
    rental_types_list = []

    def __init__(self, unit_of_measure, price):
        """
        Parameters
        ----------
        unit_of_measure : str
            it indicates the unit of measure for the rental period such as
            hours, days or weeks
        price : float
            the price for the unit of the rental period defined by
            unit_of_measure
        """

        self.rental_type_id = RentalType._id_counter
        self.unit_of_measure = unit_of_measure
        self.price = price
        RentalType._id_counter += 1
        RentalType.rental_types_list.append(self)
        logger.debug('Rental type created.')

    def __str__(self):
        return '{}: ${}'.format(self.unit_of_measure, self.price)


class BikeRental:
    """
    A class to represent the bike rental operation.

    Attributes
    ----------
    rental_type : RentalType
        the client's bike rental operation.
    bike : Bike
        the bike that the client chose to rent
    amount_of_units : int
        the amount of hours, days or weeks that the bike is rented for
    total : float
        the price to pay for the rental operation

    Methods
    -------
    None
    """

    _id_counter = 0

    def __init__(self, rental_type, bike, amount_of_units):
        """
        Parameters
        ----------
        rental_type : RentalType
            the client's bike rental operation of choice.
        bike : Bike
            the bike that the client chose to rent
        amount_of_units : int
            the amount of hours, days or weeks that the bike is rented for
        """

        self.cli_rent_id = BikeRental._id_counter
        self.rental_type = rental_type
        self.bike = bike
        self.amount_of_units = amount_of_units
        self.total = rental_type.price * amount_of_units
        BikeRental._id_counter += 1
        logger.debug('Bike rental created.')

        def __str__(self):
            return '{} - {}: {}'.format(
                self.rental_type, self.bike, self.total
                )
