
try:
    flights = {}
    all_flights = {}
    with open("C:/Python/Python_Bootcamp/Exception_Handling/flights.txt","r") as f:
        for line in f:
            flight_num, available_seat, price = line.strip().split()
            flights[flight_num] = {"seats":available_seat, "price":price}
            all_flights[flights]
        print(all_flights)

except:
    print('error')        


