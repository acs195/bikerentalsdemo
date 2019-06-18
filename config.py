# Logging Setup
LOG_LEVEL = 'DEBUG'
LOG_FILENAME = '/home/nothing/warehouse/dev/rental/app/rental.log'
LOG_FORMAT = '[%(asctime)s] %(name)s %(levelname)s in %(module)s: %(message)s'
LOGGER_NAME = 'rental_log'

# Override some values in config.py with config_prod.py if exists
try:
    from config_prod import *
except ImportError:
    pass
