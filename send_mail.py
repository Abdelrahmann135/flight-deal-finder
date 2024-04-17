import smtplib
DEMO_MAIL = "mail@gmail.com"
PASSWORD = "password"


class SendMail:

    @staticmethod
    def send_mail(message, emails):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=DEMO_MAIL, password=PASSWORD)
            for email in emails:
                connection.sendmail(
                    to_addrs=email,
                    from_addr=DEMO_MAIL,
                    msg=f"Subject:new flight\n\n"
                        f"{message}"
                )
