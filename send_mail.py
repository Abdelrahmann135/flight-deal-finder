import smtplib
DEMO_MAIL = "mail@gmail.com"
PASSWORD = "password"


class SendMail:

    def send_mail(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=DEMO_MAIL, password=PASSWORD)
            connection.sendmail(
                to_addrs="your email",
                from_addr=DEMO_MAIL,
                msg=f"Subject:new flight\n\n"
                    f"{message}"
            )
