import smtplib
import datetime as dt
import pandas
import random

my_email = "danielbaylon2885@gmail.com"
password = "bcyo cygf qejb uuxq"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
dates_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
persons_mail = dates_dict[today_tuple]["email"]

if today_tuple in dates_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace("[NAME]", dates_dict[today_tuple]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=persons_mail,
            msg=f"Subject: Happy Birthday!!!\n\n{new_letter}"
        )





