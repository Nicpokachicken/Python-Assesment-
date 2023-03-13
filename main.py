# In this game users choose a car (numbered 1 to 6).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# A simulated die is rolled and if the car’s number comes up, the car moves forward one space.
# The winning car is the one which completes the race distance the first.
import random
print("Welcome to TURBO TITANS")
Lamborghini = 1
Bugatti = 2
Ferrari = 3
Ford = 4
Toyota = 5
Nissan_juke = 6

Lamborghini_score = 0
Bugatti_score = 0
Ferrari_score = 0
Ford_score = 0
Toyota_score = 0
Susuki_score = 0

def car_input_validated(Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan_juke):
    car = 0
    while True:

        print(f"Your choices are Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan_juke")
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
        elif car == "Nissan_juke":
            return Nissan_juke

        else:

            print("Invalid input. try again.")

print(f"Your car is car {car_input_validated(1, 2, 3, 4, 5, 6)}")

print("You have chosen well!")
print("You will win by praying that your cars number is rolled 3 times before any other car.")
print("Racing starts now!")
dice = random.randint(1, 6)
print("The first car to move is Car: " + str(dice))

def car_score_validated(Lamborghini_score, Bugatti_score, Ferrari_score, Ford_score, Toyota_score, Nissan_juke_score):
    car_score = 0

    if dice == 1:
        return Lamborghini_score +1
    elif dice == 2:
        return Bugatti_score +1
    elif dice == 3:
        return Ferrari_score +1
    elif dice == 4:
        return Ford_score +1
    elif dice == 5:
        return Toyota_score +1
    elif dice == 6:
        return Nissan_juke_score +1


