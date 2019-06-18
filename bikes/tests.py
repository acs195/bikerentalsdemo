from factories import (
    BikeFactory,
    RentalTypeFactory,
    ClientFactory
)
from .exceptions import (
    DuplicateMakeSerialNumberException,
    BikeNotAvailableException
)


def test_bike_create_new():
    """
    Test case: create a valid bike.
    Expected Result: the bike is created with the appropiate attributes.
    """

    test_make = 'Testing Make'
    test_model = 'Testing Model'
    test_serial_number = 'TestingSerialNumber'

    bike = BikeFactory.create(
        make=test_make,
        model=test_model,
        serial_number=test_serial_number
    )

    assert bike.make == test_make,\
        'The make is not proprely saved.'
    assert bike.model == test_model,\
        'The model is not proprely saved.'
    assert bike.serial_number == test_serial_number,\
        'The serial_number is not proprely saved.'


def test_bike_register_rent():
    """
    Test case: a client rents a bike.
    Expected Result: the bike becomes unavailable.
    """

    bike = BikeFactory()
    assert bike.is_available,\
        'The bike should be available.'

    bike.register_rent()

    assert not bike.is_available,\
        'The bike should be unavailable.'


def test_bike_make_serial_number_duplicate():
    """
    Test case: create a bike when already exists the same make + serial_number.
    Expected Result: the application triggers an exception.
    """

    test_make = 'Testing Dup Make'
    test_serial_number = 'DupSerialNumber'

    BikeFactory.create(
        make=test_make,
        serial_number=test_serial_number
    )

    exception_occurred = False
    try:
        BikeFactory.create(
            make=test_make,
            serial_number=test_serial_number
        )
    except DuplicateMakeSerialNumberException:
        exception_occurred = True

    assert exception_occurred, ('DuplicateMakeSerialNumberException '
                                'exception did not occur')


def test_bike_not_available():
    """
    Test case: the clients rents a bike that is not available.
    Expected Result: the application triggers an exception.
    """

    bike = BikeFactory.create()
    rental_type = RentalTypeFactory()
    client = ClientFactory()
    amount_of_units = 3
    client.rent_bike(rental_type, bike, amount_of_units)

    exception_occurred = False
    try:
        client.rent_bike(rental_type, bike, amount_of_units)
    except BikeNotAvailableException:
        exception_occurred = True

    assert exception_occurred, ('BikeNotAvailableException '
                                'exception did not occur')
