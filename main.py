import smtplib, random, os, pandas
import datetime as dt

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv("./birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (_, data_row) in data.iterrows()}
# ^^^ “Go through every row in the CSV file, and create a dictionary where:
# -the KEY is (month, day)
# -the VALUE is the entire row of data.”
# what this looks like ^^
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

if today in birthdays_dict:
    print('Birthday Match!')

    random_letter_file = random.choice(os.listdir("./letter_templates"))

    birthday_person_name = birthdays_dict[today]["name"]
    birthday_person_email = birthdays_dict[today]["email"]
    with open(f"./letter_templates/{random_letter_file}", mode="r") as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person_name)

    print("sending email...")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  #encrypt message
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person_email, 
            msg=f"Subject:Happy Birthday!\n\n{content}")
    print("email sent!")
else:
    print('NOT a birthday Match')