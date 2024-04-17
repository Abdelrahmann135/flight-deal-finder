import requests
from mange_data import MangeData
from _datetime import datetime, timedelta
END_POINT ="https://api.tequila.kiwi.com/v2/search"
KEY = "xxxxxxxxxxxxxxxxxxxxxxY3fjG09"


class FlightData:
    def __init__(self):
        self.mange_data = MangeData()
        self.data = self.mange_data.get_data()
        self.price = ""
        self.city = ""

    def get_flight_data(self, fly_to):
        date = datetime.now()
        date_from = date.strftime("%d/%m/%Y")
        six_month_from_today = date + timedelta(6 * 30)
        date_to = six_month_from_today.strftime("%d/%m/%Y")
        headers = {
            "apikey": KEY
        }

        par = {
            "fly_from": "FRA",
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        get_response = requests.get(
            url=END_POINT,
            params=par,
            headers=headers,
        )
        data = get_response.json()["data"]
        try:
            self.city = data[0]["cityTo"]
            self.price = data[0]["price"]
        except IndexError:
            return None
