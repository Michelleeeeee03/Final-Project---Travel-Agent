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



def create_travel_plan():
    client = input("client name: ")
    countries = []

    num = int(input("how many countries will you going to visit: "))

    for i in range(num):
        country = input("Country name")
        days = int(input("days straying there:"))
        countries.append((country,days))
    
    dates = input("travel days: ")
    notes = input("notes or special requirements: ")

    plan = {"client": client, "countries": countries, "dates": dates, "notes": notes}

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

def view_plans():
    if not travel_plans:
        print("No plans saved")
        return
    
    for plan in travel_plans:
        print("Client: ", plan ["client"])
        print("Countries: ")

        for country, days in plan["countries"]:
            print(country, days, "days")

        print("Dates: ", plan["dates"])
        print("Notes: ", plan["notes"])

def main():
    while True:
        print("Welcome to New Horizons travel, plan your travel:")
        print("1. Search country")
        print("2. Create travel plan")
        print("3. Estimate cost")
        print("4. View travel plans")
        print("5. Exit")

        choice = input("Type the number of your choice: ")

        if choice == "1":
            search_country()
    
        elif choice == "2":
            create_travel_plan()

        elif choice == "3":
            estimate_cost()

        elif choice == "4":
            view_plans()

        elif choice == "5":
            print("Byee!")
            break

        else:
            print("Incorrect")

main()