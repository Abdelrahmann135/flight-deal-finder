import requests
ENDPOINT = "https://api.sheety.co/74309613c4dc3df5403d2123508a9ce2/flightDeals/users"


class Users:

    @staticmethod
    def add_user():
        first_name = input("enter your first name")
        second_name = input("enter your second name")
        email = input("enter your email")
        verify_email = input("enter your email again")
        if email == verify_email:
            new_data = {
                "user": {
                    "firstName": first_name,
                    "secondName": second_name,
                    "email": email
                }
            }
            requests.post(
                url=ENDPOINT,
                json=new_data
            )

    @staticmethod
    def ger_info():
        get_response = requests.get(url=ENDPOINT)
        return get_response.json()["users"]
