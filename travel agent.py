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

def estimate_cost():
    if not travel_plans:
        print("no travel plans available.")
        return
    
    plan = travel_plans[-1]

    daily_cost = 150
    transport = 200
    agency_cost = 100

    total_days = sum(days for country, days in plan["countries"])
    accommodation =  total_days + daily_cost

    total_cost = accommodation + transport + agency_cost

    print("Cost estimate:")
    print("Accommodation:", accommodation)
    print("Transport:", transport)
    print("Agency cost:", agency_cost)
    print("Total cost:", total_cost)