import requests
import datetime

travel_plans = []

def search_country():
    country = input("enter a country name: ")

    link = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(link)
    if response.status_code == 200:
        data = response.json()[0]

        name = data["name"]["official"]
        capital = data.get("capital", ["not valid"])[0]
        region = data["region"]
        population = data["population"]
        timezones = data["timezones"]
        code = data.get("cca2")

        currency_dictionary = data.get("currencies", {})
        currency_name = list(currency_dictionary.values())[0]["name"]

        languages_dictionary = data.get("languages", {})
        languages = ", ".join(languages_dictionary.values())
                    
                           
        print("\ncountry information")
        print("Official Name:", name)
        print("Capital:", capital)
        print("Region:", region)
        print("Population:", population)
        print("Timezones:", ", ".join(timezones))
        print("Country code:", code)
        print("Currency:", currency_name)
        print("Local time:", datetime.datetime.now().strftime("%H:%M"))
        print("Languages:", languages)

    else: print("\ncountry not found")

def create_travel_plan():
    client = input("\nclient name: ")
    countries = []

    while True:
        try:
            num = int(input("\nhow many countries are you going to visit: "))
            if num >= 1:
                break
            print("You must visit at least 1 country.")
            
        except:
            print("Invalid number.")

    for i in range(num):
        country = input("Country name: ")
        while True:
            try:
                days = int(input("days staying there:"))
                if days >= 1:
                    countries.append((country,days))
                    break
                print("Stay must be at least 1 day.")
            except:
                print("Invalid input.")
    
    while True:
        date1 = input("What date are you arriving at your destination? (YYYY-MM-DD)")
        date2 = input("What date are you leaving your destination? (YYYY-MM-DD)")

        try:
            arrival = datetime.datetime.strptime(date1, "%Y-%m-%d")
            departure = datetime.datetime.strptime(date2, "%Y-%m-%d")

            if departure <= arrival:
                print("You can't leave before or on the day you arrive")
            else:
                dates = f"{date1} to {date2}"
                break

        except ValueError:
            print("Use the format YYYY-MM-DD")

    notes = input("notes or special requirements: ")
    plan = {"client": client, "countries": countries, "dates": dates, "notes": notes}
    travel_plans.append(plan)
    print("\ntravel plan created!")

def estimate_cost():
    if not travel_plans:
        print("\no travel plans available.")
        return
    
    plan = travel_plans[-1]

    daily_cost = 150
    transport = 200
    agency_cost = 100

    total_days = sum(days for country, days in plan["countries"])
    accommodation =  total_days * daily_cost

    total_cost = accommodation + transport + agency_cost

    print("\nCost estimate:")
    print("Accommodation:", accommodation)
    print("Transport:", transport)
    print("Agency cost:", agency_cost)
    print("Total cost:", total_cost)

def view_plans():
    if not travel_plans:
        print("No plans saved")
        return
    
    for plan in travel_plans:
        print("Client: ", plan["client"])
        print("Countries: ")

        for country, days in plan["countries"]:
            print(country, ":", days, "days")
       
        print("Dates: ", plan["dates"])
        print("Notes: ", plan["notes"])

def main():
    while True:
        print("\nWelcome to New Horizons travel, plan your travel: ")
        print("1. Search country")
        print("2. Create travel plan")
        print("3. Estimate cost")
        print("4. View travel plans")
        print("5. Exit")

        choice = input("\nType the number of your choice: ")

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