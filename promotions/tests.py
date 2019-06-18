from factories import (
    PromotionFactory,
    BikeRentalFactory,
    BikeFactory,
    RentalTypeFactory,
    PromotionRentalFactory
    )
from .exceptions import (
    MinGreaterThanMaxException,
    PromotionNotApplicableException
)


def test_promotion_create_new():
    """
    Test case: create a valid promotion.
    Expected Result: the promotion is created with the proper attributes.
    """

    test_discount_pct = 40.0
    test_min_rentals_to_apply = 2
    test_max_rentals_to_apply = 4

    promotion = PromotionFactory.create(
        discount_pct=test_discount_pct,
        min_rentals_to_apply=test_min_rentals_to_apply,
        max_rentals_to_apply=test_max_rentals_to_apply
    )

    assert promotion.discount_pct == test_discount_pct,\
        'The discount_pct is not proprely saved.'
    assert promotion.min_rentals_to_apply == test_min_rentals_to_apply,\
        'The min_rentals_to_apply is not proprely saved.'
    assert promotion.max_rentals_to_apply == test_max_rentals_to_apply,\
        'The max_rentals_to_apply is not proprely saved.'


def test_promotion_min_greater_than_max():
    """
    Test case: save a new promotion with a min value greater than the max.
    Expected Result: the application triggers an exception.
    """

    test_discount_pct = 40.0
    test_min_rentals_to_apply = 4
    test_max_rentals_to_apply = 3
    exception_occurred = False
    try:
        PromotionFactory.create(
            discount_pct=test_discount_pct,
            min_rentals_to_apply=test_min_rentals_to_apply,
            max_rentals_to_apply=test_max_rentals_to_apply
        )
    except MinGreaterThanMaxException:
        exception_occurred = True

    assert exception_occurred, ('MinGreaterThanMaxException '
                                'exception did not occur')


def test_promotion_not_applicable():
    """
    Test case: the client takes a promotion but does not meet the criteria.
    Expected Result: the application triggers an exception.
    """

    promotion = PromotionFactory()
    rental_bikes = [
        BikeRentalFactory.create(
            rental_type=RentalTypeFactory(),
            bike=BikeFactory(),
            amount_of_units=1
        )]

    exception_occurred = False
    try:
        PromotionRentalFactory.create(
            promotion=promotion,
            rental_bikes=rental_bikes
        )
    except PromotionNotApplicableException:
        exception_occurred = True

    assert exception_occurred, ('PromotionNotApplicableException '
                                'exception did not occur')
