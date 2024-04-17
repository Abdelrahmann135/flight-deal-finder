from flight_data import FlightData
from mange_data import MangeData
from send_mail import SendMail

flight_data = FlightData()
mange_data = MangeData()
send_mail = SendMail()

sheet_data = mange_data.get_data()
for destination in sheet_data:
    flight = flight_data.get_flight_data(destination["iataCode"])
    if flight.price < destination["lowestPrice"]:
        send_mail.send_mail(f"Low price alert! Only £{flight.price} to fly from {flight.city}")
