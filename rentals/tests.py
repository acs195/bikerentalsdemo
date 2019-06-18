from factories import RentalTypeFactory


def test_rental_type_create_new():
    """
    Test case: create a valid rental type.
    Expected Result: the rental type is created with the proper attributes.
    """
    test_unit_of_measure = 40.0
    test_price = 2

    rental_type = RentalTypeFactory.create(
        unit_of_measure=test_unit_of_measure,
        price=test_price
    )

    assert rental_type.unit_of_measure == test_unit_of_measure,\
        'The unit_of_measure is not proprely saved.'
    assert rental_type.price == test_price,\
        'The price is not proprely saved.'
