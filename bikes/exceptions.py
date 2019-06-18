class DuplicateMakeSerialNumberException(Exception):
    """Raised when the serial_number already exists for same make"""
    pass


class BikeNotAvailableException(Exception):
    """Raised when the bike is already rented to someone else"""
    pass
