import requests

myPrice = 5.3

response = requests.get("https://api.bitpin.ir/v1/mkt/markets/")
results = response.json()["results"]

for i in results:
    if i['title_fa'] == "پاری سن ژرمن/تتر":
        if float(i['price']) < myPrice - 0.3 :
            print("Hey Mopano    buy thattttt 😍 !")
        elif float(i['price']) > myPrice + 0.3 :
            print("Hey Mopano    sell thattttt 😍 !")
        print("Do nothing 😒")
