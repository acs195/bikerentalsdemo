from factories import (
    ClientFactory,
    BikeFactory,
    RentalTypeFactory,
    PromotionRentalFactory
)


def test_client_create_new():
    """
    Test case: create a valid client.
    Expected Result: the client is created with the proper attributes.
    """

    test_first_name = 'Testing First Name'
    test_last_name = 'Testing Last Name'

    client = ClientFactory.create(
        first_name=test_first_name,
        last_name=test_last_name
    )

    assert client.first_name == test_first_name,\
        'The first_name is not proprely saved.'
    assert client.last_name == test_last_name,\
        'The last_name is not proprely saved.'


def test_client_rent_bike():
    """
    Test case: the client rents a bike.
    Expected Result: the bike rental is created with the proper attributes.
    """

    bike = BikeFactory()
    rental_type = RentalTypeFactory()
    client = ClientFactory()
    amount_of_units = 3
    client.rent_bike(rental_type, bike, amount_of_units)

    assert client.rentals[0].rental_type == rental_type and\
        client.rentals[0].bike == bike and\
        client.rentals[0].amount_of_units == amount_of_units,\
        'The bike rental did not add correctly to the client.'


def test_client_rent_bikes_with_promotion():
    """
    Test case: the client takes a promotion.
    Expected Result: the promotion is added to the promotion client's list.
    """

    promotion_rental = PromotionRentalFactory()
    client = ClientFactory()
    client.rent_bikes_with_promotion(promotion_rental)

    assert client.promotions[0] == promotion_rental,\
        'The promotion rental did not add correctly to the client.'
