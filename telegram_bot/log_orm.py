import logging

logger = logging.getLogger('orm_logger')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s: %(message)s')

fh = logging.FileHandler('advanced.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)