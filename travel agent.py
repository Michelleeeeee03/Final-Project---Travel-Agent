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

def create_travel_plan():
    client = input("client name:")
    countries = []

    num = int(input("how many countries will you going to visit"))

    for i in range(num):
        country = input("Country name")
        days = int(input("days straying there:"))
        countries.append((country,days))
    
    dates = input("travel days:")
    notes = input("notes or special requirements:")

    plan = {"client":client, "countries": countries, "dates": dates, "notes": notes}

    travel_plans.append(plan)

    print("travel plan created!")