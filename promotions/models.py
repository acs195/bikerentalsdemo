import logging
from .exceptions import (
    MinGreaterThanMaxException,
    PromotionNotApplicableException
)
import config

logger = logging.getLogger(config.LOGGER_NAME)


class Promotion:
    """
    A class to represent a promotion.

    Attributes
    ----------
    promotion_id : int
        the promotion unique internal identifier
    discount_pct : float
        the discount percentage offered
    min_rentals_to_apply : int
        the minimum amount of rentals to be considered within the promotion
    max_rentals_to_apply : int
        the maximum amount of rentals to be considered within the promotion

    Methods
    -------
    None
    """

    # Keeps the last id
    _id_counter = 0
    # Keeps the list of promotions
    promotions_list = []

    def __init__(self, discount_pct, min_rentals_to_apply,
                 max_rentals_to_apply):
        """
        Parameters
        ----------
        discount_pct : float
            the discount percentage offered
        min_rentals_to_apply : int
            the minimum amount of rentals to be considered within the promotion
        max_rentals_to_apply : int
            the maximum amount of rentals to be considered within the promotion

        Methods
        -------
        None
        """

        self.promotion_id = Promotion._id_counter
        self.discount_pct = discount_pct
        self.min_rentals_to_apply = min_rentals_to_apply
        self.max_rentals_to_apply = max_rentals_to_apply
        if self.is_min_greater_than_max():
            logger.error('Min value is greater than Max value.')
            raise MinGreaterThanMaxException

        Promotion._id_counter += 1
        Promotion.promotions_list.append(self)
        logger.debug('Promotion created.')

    def is_min_greater_than_max(self):
        """ Validate whether the min value is greater than the max value.
        Parameters
        ----------
        None
        """

        if self.min_rentals_to_apply > self.max_rentals_to_apply:
            return True
        return False

    def __str__(self):
        return '{}% when {} to {} rentals'.format(
            self.discount_pct,
            self.min_rentals_to_apply,
            self.max_rentals_to_apply
        )


class PromotionRental:
    """
    A class to represent the bike rental operation under a promotion.

    Attributes
    ----------
    promotion : Promotion
        the client's promotion of choice
    rental_bikes : list
        the list of the rental_bikes included in the promotion
    total : float
        the price to pay for the promotion

    Methods
    -------
    None
    """

    _id_counter = 0

    def __init__(self, promotion, rental_bikes):
        """
        Parameters
        ----------
        promotion : Promotion
            the client's promotion of choice
        rental_bikes : list
            the list of the BikeRental included in the promotion
        """

        self.promo_rental_id = PromotionRental._id_counter
        self.promotion = promotion
        self.rental_bikes = rental_bikes
        self.total = (sum(rb.total for rb in rental_bikes)
                      * (100 - promotion.discount_pct) / 100)

        if not self.is_promotion_applicable():
            logger.error('Promotion is not applicable.')
            raise PromotionNotApplicableException

        PromotionRental._id_counter += 1
        logger.debug('Promotion/rentals created.')

    def is_promotion_applicable(self):
        """Validate whether the promotions is applicable or not.

        Parameters
        ----------
        None
        """

        if (self.promotion.min_rentals_to_apply <= len(self.rental_bikes) <=
           self.promotion.max_rentals_to_apply):
            return True

        return False

    def __str__(self):
        return '{}: {}'.format(self.promotion, self.total)
