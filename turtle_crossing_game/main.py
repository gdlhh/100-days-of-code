from turtle import Turtle, Screen
from user import User
from car import Car
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Turtle crossing")
screen.setup(width=600,height=600)
screen.tracer(0)

difficulty = screen.textinput("Welcome to the Turtle crossing game!", "Please select your difficulty (1,2,3)")



if difficulty == '1':
    number_of_cars = 25
elif difficulty == '2':
    number_of_cars = 50
elif difficulty == '3':
    number_of_cars = 75

user = User()

car_list = []

for cars in range(number_of_cars):
    car = Car()
    car_list.append(car)

screen.listen()
screen.onkey(user.up, "Up")
screen.onkey(user.left, "Left")
screen.onkey(user.right, "Right")
screen.onkey(user.down, "Down")

car_list

game_is_on = True

while game_is_on:
    screen.update()

    time.sleep(0.01)

    for cars in car_list:
        cars.move()

        # restart cars that have reached the end
        if cars.xcor() < -300:
            cars.restart()
        
        # detect collision
        if user.distance(cars) < 20:
            game_is_on=False
    

screen.exitonclick()

 