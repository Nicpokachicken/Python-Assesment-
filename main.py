# In this game users choose a car (numbered 1 to 6).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# A simulated die is rolled and if the car’s number comes up, the car moves forward one space.
# The winning car is the one which completes the race distance the first.
import random
import time

print("Welcome to TURBO TITANS")
time.sleep(0.5)  # The sleep function makes the code print with a 0.5 sec gap between the prints
# This are the variables that link the car to the car's number
Lamborghini = 1
Bugatti = 2
Ferrari = 3
Ford = 4
Toyota = 5
Nissan_Juke = 6

track_dist = 0

# These variables are the cars score
Lamborghini_score = 0
Bugatti_score = 0
Ferrari_score = 0
Ford_score = 0
Toyota_score = 0
Nissan_Juke_score = 0

Dice_Rolled = 0

def car_input_validated(Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan_Juke):
    car = 0
    while True:

        print(f"Your choices are Lamborghini, Bugatti, Ferrari, Ford, Toyota, Nissan Juke")
        time.sleep(0.5)
        car = (input("Please choose your car : "))#this askes for user input
        time.sleep(0.5)
        car = car.lower()
        if car == "lamborghini":
            return Lamborghini #this links the cars name back to the varible that links the car to its number
        elif car == "bugatti":
            return Bugatti
        elif car == "ferrari":
            return Ferrari
        elif car == "ford":
            return Ford
        elif car == "toyota":
            return Toyota
        elif car == "nissanjuke":
            return Nissan_Juke

        else:

            print("Invalid input. Try again.")

print(f"Your car is car {car_input_validated(1, 2, 3, 4, 5, 6)}") #This tells you the number of your car
time.sleep(0.5)


print("You have chosen well!")
time.sleep(0.5)
def track_dist_validated():
    track_dist = 0
    while True:
        try:
            track_dist = int(input("Choose how long you want your road (5-15:) "))
            if 5<= track_dist <=15:
                return track_dist
            else:
                print("Invalid input.")
                continue
        except ValueError:
            print("Invalid input.")
        else:
            break
def car_score_validated(Lamborghini_score, Bugatti_score, Ferrari_score, Ford_score, Toyota_score, Nissan_Juke_score, length):
    car_score = 0
    Dice_Rolled = 0
    print("You will win by praying that your cars number is rolled " + str(length) + " times before any other car.")
    time.sleep(1.5)
    print("Racing starts now!")
    time.sleep(1)
    while True:
        dice = random.randint(1, 6) #This is why the dice roll is random as it chooses a number between 1-6
        print("The dice roll is: " + str(dice))#This prints the dice roll
        time.sleep(1)
        if dice == 1:
            Lamborghini_score +=1 #When a dice is rolled its number correlates to a car and increases that cars score
        elif dice == 2:
            Bugatti_score +=1
        elif dice == 3:
            Ferrari_score +=1
        elif dice == 4:
            Ford_score +=1
        elif dice == 5:
            Toyota_score +=1
        elif dice == 6:
            Nissan_Juke_score += 1

        else:
            print("roll again")
        Dice_Rolled += 1
        print("Lamborghini score is:" + str(Lamborghini_score)) #This prints the recorded car's score
        time.sleep(0.5)
        print("Bugatti score is now:" + str(Bugatti_score))
        time.sleep(0.5)
        print("Ferrari score is now:" + str(Ferrari_score))
        time.sleep(0.5)
        print("Ford score is now:" + str(Ford_score))
        time.sleep(0.5)
        print("Toyota score is now:" + str(Toyota_score))
        time.sleep(0.5)
        print("Nissan Juke score is now:" + str(Nissan_Juke_score))
        time.sleep(0.5)
        print("The dice has been rolled: " + str(Dice_Rolled) + " times")
        time.sleep(3)
        if Lamborghini_score == length:
            return "The Lambrghini won"
        elif Ferrari_score == length:
            return "The Ferarri won"
        elif Bugatti_score == length:
            return "The Bugatti won"
        elif Ford_score == length:
            return "The Ford won"
        elif Toyota_score == length:
            return "The Toyota won"
        elif Nissan_Juke_score == length:
            return "The Nissan Juke has crushed the competition as usual!"
print(car_score_validated(0, 0, 0, 0, 0, 0, track_dist_validated()))