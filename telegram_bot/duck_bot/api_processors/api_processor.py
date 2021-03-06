'''
API configuration tunning
'''

from duck_bot.additional.log_orm import DuckLogger
import requests



class APIProcessor:
    def __init__(self):
        self.url = ""
        self.log = DuckLogger(self)
        self.breeds = list()

    def refresh_data(self):
        try:
            new_data = self._get_data()
        except Exception as e:
            self.log.error(f'refresh_data -'
                           f'failed to get data from API: '
                           f'{e}')
            return False

        try:
            clean_data = self._clean_data(raw_data=new_data)
        except Exception as e:
            self.log.error(f'refresh_data - '
                           f'failed to clean data: '
                           f'{e}')
            return False

        try:
            self._save_data(data_to_save=clean_data)
        except Exception as e:
            self.log.error(f'refresh_data - '
                           f'failed to save data: '
                           f'{e}')
            return False
        self.log.info(f'refresh_data - '
                      f'Done')
        return True

    def _get_data(self):
        try:
            response = requests.get(self.url)
        except Exception as e:
            self.log.error(f'get data - '
                           f'received {response.status_code}')
            raise RuntimeError(f'{response.status_code}: {response.text}')

        return response.json()

    def clean_data(self):
        raise NotImplementedError

    def _save_data(self, data_to_save):
        pass


if __name__ == '__main__':
    t = APIProcessor()
    t.refresh_data()
