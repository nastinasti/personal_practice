from api_processor.api_processor import APIProcessor


class DOGAPIProcessor(APIProcessor):
    def __init__(self):
        super().__init__()
        self.url = "https://dog.ceo/api/"
        self.api_breeds_url = "https://dog.ceo/api/breeds/list/all"


if __name__ == '__main__':
    dogs = DOGAPIProcessor()
    dogs.refresh_data()

