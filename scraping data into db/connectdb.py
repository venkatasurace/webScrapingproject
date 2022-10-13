import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='scrapinguser',
    password ='pass123',
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for 

# # mycursor.execute("Show ")






# import json


# def get_quotes_json_file():
#   with open("quotes.json","r") as f:
#     quotes_file = f.read()
#     quotes_file = json.loads(quotes_file)
#   print("Quotes File Fetched")
#   print(quotes_file)

