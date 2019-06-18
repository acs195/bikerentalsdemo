import factory
from factory import fuzzy
from bikes.models import Bike
from rentals.models import RentalType, BikeRental
from promotions.models import Promotion, PromotionRental
from clients.models import Client


class BikeFactory(factory.Factory):
    """
        Define Bike Factory
    """
    class Meta:
        model = Bike

    make = fuzzy.FuzzyChoice(['Trek', 'Vairo', 'Pinarello', 'Gimson'])
    model = fuzzy.FuzzyChoice(['Competition', 'Street', 'Racing', 'Family'])
    serial_number = fuzzy.FuzzyInteger(1, 999999)


class RentalTypeFactory(factory.Factory):
    """
        Define RentalType Factory
    """
    class Meta:
        model = RentalType

    unit_of_measure = 'hour'
    price = 5.0


class PromotionFactory(factory.Factory):
    """
        Define Promotion Factory
    """
    class Meta:
        model = Promotion

    discount_pct = 0.30
    min_rentals_to_apply = 3
    max_rentals_to_apply = 5


class ClientFactory(factory.Factory):
    """
        Define Client Factory
    """
    class Meta:
        model = Client

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BikeRentalFactory(factory.Factory):
    """
        Define BikeRental Factory
    """
    class Meta:
        model = BikeRental

    rental_type = RentalTypeFactory()
    bike = BikeFactory()
    amount_of_units = fuzzy.FuzzyInteger(1, 6)


class PromotionRentalFactory(factory.Factory):
    """
        Define PromotionRental Factory
    """
    class Meta:
        model = PromotionRental

    promotion = PromotionFactory()
    rental_bikes = [
        BikeRentalFactory.create(
            rental_type=RentalTypeFactory(
                unit_of_measure='hour',
                price=5.0
            ),
            bike=BikeFactory(),
            amount_of_units=fuzzy.FuzzyInteger(1, 6)
        ),
        BikeRentalFactory.create(
            rental_type=RentalTypeFactory(
                unit_of_measure='day',
                price=20.0
            ),
            bike=BikeFactory(),
            amount_of_units=fuzzy.FuzzyInteger(1, 6)
        ),
        BikeRentalFactory.create(
            rental_type=RentalTypeFactory(
                unit_of_measure='week',
                price=60.0
            ),
            bike=BikeFactory(),
            amount_of_units=fuzzy.FuzzyInteger(1, 6)
        )
    ]
