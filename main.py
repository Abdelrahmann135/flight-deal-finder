from dealing_with_users import Users
from flight_data import FlightData
from mange_data import MangeData
from send_mail import SendMail

users = Users()
flight_data = FlightData()
mange_data = MangeData()
send_mail = SendMail()

sheet_data = mange_data.get_data()
for destination in sheet_data:
    users_data = users.ger_info()
    emails = [row["email"] for row in users_data]
    names = [row["firstName"] for row in users_data]
    flight = flight_data.get_flight_data(destination["iataCode"])
    if flight_data.price < destination["lowestPrice"]:
        send_mail.send_mail(f"Low price alert! Only £{flight_data.price} to fly from {flight_data.city}", emails)
