from api_processor import APIProcessor


class DOGAPIProcessor(APIProcessor):
    def __init__(self):
        super().__init__()
        # self.url = "https://dog.ceo/api/"
        self.url = "https://dog.ceo/api/breeds/list/all"

    def _clean_data(self, raw_data):

        raw_data = raw_data['message']
        for breed in raw_data:
            self.breeds.append(breed)
        return self.breeds

    def get_dogbreed_pic(self):
        print(self.breeds)


if __name__ == '__main__':
    dogs = DOGAPIProcessor()
    dogs.refresh_data()
    dogs.get_dogbreed_pic()

