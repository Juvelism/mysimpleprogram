def get_temperature():
    weather = int(input("Enter the temperature in Celsius(°C): "))
    return weather

def check_weather(temp):
    if temp < 0:
        return 'Freezing'
    elif 0 >= temp <= 20:
        return 'Cold'
    elif 21 >= temp <= 30:
        return 'Warm'
    else:
        return 'Hot'

def display_weather(temp, category):
    print(f"It's {temp}°C - {category} weather.")

def main():
    temp = get_temperature()
    weather = check_weather(temp)
    display_weather(temp,weather)

main()