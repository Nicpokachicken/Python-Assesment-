# In this game users choose a car (numbered 1 to 6).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# A simulated die is rolled and if the car’s number comes up, the car moves forward one space.
# The winning car is the one which completes the race distance the first.
print("Welcome to TURBO TITANS")
Lamborghini = 1
Bugatti = 2
Ferrari = 3
Ford = 4
Toyota = 5
Susuki = 6
def car_input_validated(Lamborghini, Bugatti, Ferrari, Ford, Toyota, Susuki):
    car = 0
    while True:

        print(f"Your choices are Lamborghini, Bugatti, Ferrari, Ford, Toyota, Susuki")
        car = (input("Please choose your car : ")) #this askes for user input
        if car == "Lamborghini":
            return Lamborghini #this links the cars name to its number
        elif car == "Bugatti":
            return Bugatti
        elif car == "Ferrari":
            return Ferrari
        elif car == "Ford":
            return Ford
        elif car == "Toyota":
            return Toyota
        elif car == "Susuki":
            return Susuki

        else:

            print("Invalid input. try again.")

print(f"Your car is car {car_input_validated(1, 2, 3, 4, 5, 6)}")


