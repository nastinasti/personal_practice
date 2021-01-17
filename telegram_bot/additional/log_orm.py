import logging


class DuckLogger:
    def __init__(self):
        self.logger = logging.getLogger('orm_logger')
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(levelname)s: %(message)s')
        self.fh = logging.FileHandler('advanced.log')
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(self.formatter)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)