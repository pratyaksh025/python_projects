import random

def dummy_report(city):
    conditions=["Sunny", "Rainy", "Cloudy", "Stormy", "Snowy"]
    condition=random.choice(conditions)
    temprature=random.randint(-5,49)
    humidity= random.randint(20,95)
    emoji_map={
        'Sunny': '☀️',
        'Rainy': '⛈️',
        'Cloudy': '☁️',
        'Stormy': '🍃',
        'Snowy': '❄️'
    }
    print(f"Weather Report For:  {city}")
    print(f"Condition: {condition}{emoji_map[condition]}")
    print(f"Temprature: {temprature}°C")
    print(f"Humidity: {humidity}%")


def main():
    text="Weather Information"
    thanks="Thanks for using program"
    Warning_msg="this program is just for understanding doesn't fetch real world reports"
    print(f"{'-'*(len(text)+2)}")
    print(text)
    print(f"{'-'*(len(text)+2)}")

    while True:
        city=input("Enter 'exit' to quit the program or City Name to check weather: ")
        if city == 'exit':
            print(f"{'-'*(len(thanks)+2)}")
            print(thanks)
            print(f"{'-'*(len(thanks)+2)}")
            break
        else:
            dummy_report(city)
            print(f"{'-'*(len(Warning_msg)+2)}")
            print(Warning_msg)
            print(f"{'-'*(len(Warning_msg)+2)}")

main()

