import logging
from .exceptions import (
    DuplicateMakeSerialNumberException,
    BikeNotAvailableException
)
import config

logger = logging.getLogger(config.LOGGER_NAME)


class Bike:
    """ A class to represent a bike.

    Attributes
    ----------
    bike_id : int
        the bike unique internal identifier
    make : str
        the make of the bike
    model : str
        the model of the bike
    serial_number : str
        the serial number of the bike
    _is_available : boolean
        it indicates whether the bike is available to rent or not

    Methods
    -------
    register_rent()
        it configures the application logger
    is_make_serial_number_duplicate()
        it marks the bike as unavailable to rent (is_available=False)
    """

    # Keeps the last id
    _id_counter = 0
    # Keeps the list of bikes
    bikes_list = []

    def __init__(self, make, model, serial_number):
        """
        Parameters
        ----------
        make : str
            the make of the bike
        model : str
            the model of the bike
        serial_number : str
            the serial number of the bike
        """

        self.bike_id = Bike._id_counter
        self.make = make
        self.model = model
        self.serial_number = serial_number
        self._is_available = True

        if self.is_make_serial_number_duplicate():
            logger.error('Make/Serial Nummber duplicate.')
            raise DuplicateMakeSerialNumberException

        Bike._id_counter += 1
        Bike.bikes_list.append(self)
        logger.debug('Bike created.')

    @property
    def is_available(self):
        return self._is_available

    def register_rent(self):
        """ When a client rents a bike, it becomes unavailable.

        Parameters
        ----------
        None

        Raises
        ------
        BikeNotAvailableException
        """

        if not self._is_available:
            logger.error('Bike is not available.')
            raise BikeNotAvailableException

        self._is_available = False
        logger.debug('Bike rented.')

    def is_make_serial_number_duplicate(self):
        """ Validate duplicity of make + serial_number.

        Parameters
        ----------
        None
        """

        for bike in Bike.bikes_list:
            if (bike.make == self.make and
               bike.serial_number == self.serial_number):
                return True
        return False

    def __str__(self):
        return '{} {}'.format(self.make, self.model)
