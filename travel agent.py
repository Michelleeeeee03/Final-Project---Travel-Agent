import requests
import json

travel_plans = []

def search_country():
    country = input("enter a country name: ")

    link = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(link)
    if response.status_code == 200:
        data = response.json()[0]

        name = data["name"]["official"]
        capital = data.get("capital", ["not valid"])
        region = data["region"]
        population = data["population"]
        timezones = data["timezones"]
#idk how to put languages so scratch that                      
                           
        print("country information")
        print("Official Name:", name)
        print("Capital:", capital)
        print("Region:", region)
        print("Population:", population)
        print("Timezones:", ", ".join(timezones))

    else: print("country not found")

search_country()
