# In this game users choose a car (numbered 1 to 6).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# A simulated die is rolled and if the car’s number comes up, the car moves forward one space.
# The winning car is the one which completes the race distance the first.
import random
import time

print("Welcome to TURBO TITANS")
time.sleep(0.5)
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
Nissan_juke_score = 0

def car_input_validated(Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan_juke):
    car = 0
    while True:

        print(f"Your choices are Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan_juke")
        time.sleep(0.5)
        car = (input("Please choose your car : "))#this askes for user input
        time.sleep(0.5)
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
time.sleep(0.5)

print("You have chosen well!")
time.sleep(0.5)
print("You will win by praying that your cars number is rolled 5 times before any other car.")
time.sleep(0.5)
print("Racing starts now!")
time.sleep(3)

def car_score_validated(Lamborghini_score, Bugatti_score, Ferrari_score, Ford_score, Toyota_score, Nissan_juke_score):
    car_score = 0
    while True:
        dice = random.randint(1, 6)
        print("The dice roll is: " + str(dice))
        time.sleep(1)
        if dice == 1:
            Lamborghini_score +=1
        elif dice == 2:
            Bugatti_score +=1
        elif dice == 3:
            Ferrari_score +=1
        elif dice == 4:
             Ford_score +=1
        elif dice == 5:
            Toyota_score +=1
        elif dice == 6:
            Nissan_juke_score += 1
        else:
            print("roll again")
        print("Lamborghini score is:" + str(Lamborghini_score))
        time.sleep(0.5)
        print("Bugatti score is now:" + str(Bugatti_score))
        time.sleep(0.5)
        print("Ferrari score is now:" + str(Ferrari_score))
        time.sleep(0.5)
        print("Ford score is now:" + str(Ford_score))
        time.sleep(0.5)
        print("Toyota score is now:" + str(Toyota_score))
        time.sleep(0.5)
        print("Nissan juke score is now:" + str(Nissan_juke_score))
        time.sleep(4)
        if Lamborghini_score == 5:
            return "The Lambrghini won"
        elif Ferrari_score == 5:
            return "The Ferarri won"
        elif Bugatti_score == 5:
            return "The Bugatti won"
        elif Ford_score == 5:
            return "The Ford won"
        elif Toyota_score == 5:
            return "The Toyota won"
        elif Nissan_juke_score == 5:
            return "The Nissan Juke won"
print(car_score_validated(0, 0, 0, 0, 0, 0))



