def hotel_cost(nights):
    return nights * 140
def plane_ride_cost(city):
    if city == "Los Angeles":
        return 200
    elif city == "Mumbai":
        return 150
    elif city == "Toronto":
        return 300
    elif city == "Melbourne":
        return 350
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print("Cost of a car rental:", rental_car_cost(5))
print("Cost of plane ride to Toronto:", plane_ride_cost("Toronto"))
print("Cost of hotel for 3 nights:", hotel_cost(3))
print("Total trip cost:", trip_cost("Toronto", 10, 500))












