import logging


class DuckLogger(logging.Logger):
    def __init__(self, parent):
        super().__init__(parent.__class__.__name__)
        self.setLevel(logging.DEBUG)

        formatter = logging.Formatter(f'%(asktime)s - %(name)s - %(message)s',
                                      "%Y-%m-%d %H:%M:%S")
        fh = logging.FileHandler('advanced.log')
        fh.setLevel(logging.ERROR)
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        self.addHandler(fh)
        self.addHandler(ch)
