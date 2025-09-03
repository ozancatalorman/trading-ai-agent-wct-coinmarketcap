from dotenv import load_dotenv

class coinmarketcapClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.connection = self.__create_connection(api_key, api_secret)


    @staticmethod
    def __create_connection(api_key: str, api_secret: str):
        pass







