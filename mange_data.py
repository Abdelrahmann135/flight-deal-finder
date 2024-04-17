import requests
END_POINT = "https://api.sheety.co/74309613c4dc3df5403d2123508a9ce2/flightDeals/prices"


class MangeData:
    def __init__(self):
        self.data = {}

    def get_data(self):
        get_response = requests.get(url=END_POINT)
        self.data = get_response.json()["prices"]
        return self.data

    def put_data(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": "test"
                }
            }
            requests.put(
                f"{END_POINT}/{city["id"]}",
                json=new_data
            )
