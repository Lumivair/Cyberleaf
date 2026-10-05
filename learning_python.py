import math
import random
import pygame, time
from sys import exit
import datetime

from pathlib import Path

from learning_python_module import divide2
from learning_python_module import swap_ab

from learning_packages import package

# #BEGINNER COURSE 1:

# print("Hello World") # print the string hello world

# age = 6 # set variable age to 6
# age = 42 # change variable to 42
# print(age) # print variable age

# price = 14.6 # float variable
# first_name = "Michael" # string variable
# is_online = True  # boolean variable

# something = input("Input something: ") # set variable something to input
# print("this is something: " + something) # print variable something

# number = input("Enter a number: ") # set number to input !will be a string!
# opposite_number = 0 - int(number) # convert variable number to int and subtract it from 0 -> set opposite_number to this value
# print("This is the opposite of the number: " + str(opposite_number)) # convert opposite_number back to string to be able to print it with another string

# string = "this is a string" # set a string
# # print(string.capitalize()) # the string is an object with which we can capitalize the first letter using a function for an object by just writing the function after a dot. function is actually a method
# print(string.find("string")) # this will print where in the string we will find the word string. specifically it will start with 0 and count until it finds the first character of the word string so 10 int this case
# print("this" in string) # this is similar but will only say if it found it and output as boolean. whereas the one above will say where and when nowwhere is found will say -1

# print(10 + 3 - 2 * 5, 2 ** 8) # math as usual
# print(11 / 2) # division to float
# print(11 % 2) # division but only what is left so 0 when works and otherwise whats left
# print(11 // 2) # division to integer rounded down, so the rest can always be gotten from operator above

# x = 10 # set var to 10
# x = x + 3 # add 3
# x += 3 # add 3 but more simple

# x = (10 + 3) * 2 # more normal math
# print(x) # print x

# x = 3 > 2 # boolean expressian of true
# x = 3 == 2 # boolean expressian of false
# #some operators: >, <, ==, !=, <=, >=
# print(x) # print x again

# price = 25
# print(price > 10 and price < 30) # both things must be true
# print(price > 50 or price < 20) # 1 or more needs to be true
# print(not price > 50) # not just reverses so false becomes true

# temp = 35 # set temps to 35
# if temp > 10: # if temp higher then 10 run code block
#     print("temp higher than 10") # print
# elif temp > 0: # will not run even though true because it is elif(else if) and not (and if/ or if)
#     print("higher than 0")
# print("done") # will always run

# number = 1
# while number < 16: # repeat until number is not smaller than 16
#     print(number * "*") # will print * however many times as number is in the itteration
#     number += 1 # add 1

# names = ["michi", "malik", "fritzli"]
# print(names[0]) # prints first name in list
# print(names[-1]) # prints last name in list
# print(names[-2]) # prints second last name in list

# names[0] = "michael" # change first element in list to michael
# print(names[0:2]) # prints first 2 names

# num = [1, 3, 5, 7, 88, 10] # make list
# num.append(6) # add 6 as last item in list
# num.insert(1, "hello this isnt a number") # use ctrl + shift + space for help, adds string as second item moving rest forward
# num.remove(88) # removes number 88 from list
# num.pop(1) # removes the second item !not number 2 or 1 as in .remove!
# #num.clear() # clears list
# print(1 in num) # checks if 1 is in num and outputs boolean True
# print(len(num)) # prints number of elements

# nnum = [1, 4, 7, 10, 13, 304]
# for item in nnum: # for loop using item variable and repeating for every item in list
#     print(item) # same is possible with while but is worse

# rng= range(5)
# print(rng) # prints range(0, 5) instead of how one would expect 12345

# for i in rng: # repeat for every item in rnf so 5 times
#     print(i) # how to properly do it

# for i in range(5, 10, 2): # range from 5 to 9 but only every second item
#     print(i)

# num = (1, 2, 3, 6, 6) # this creates a tuple. tuple = immutable(not modifiable) list
# print(num.count(6)) # will print amount of 6 in tuple
# print(num.index(6)) # will print index of first occurence of this number. print(num.__class__) with underscore its called a magic method(complicated shit)




# #TUTORIAL 2

# first = "michi"
# last = "meier"
# message = first + " [" + last + "] is a coder" # more complex
# print(message)

# msg = f"{first} [{last}] is a coder" # formated string with f infront makes it easier to read in code
# print(msg)

# x = 2.50
# y = -23.4
# print(round(x)) # will round down when exactly in middle ?weird?
# print(abs(y)) # will turn number positive

# print(math.floor(2.7)) # floor of 2.7 is 2 (basically just rounding down)

# answer = input("enter a password, it must have between 3 and 12 character: ") # password validity check excersize
# if len(answer) < 4 or len(answer) > 11:
#     print("please enter a name between 3 and 12 character")
# else:
#     print("answer looks good")

# secret_number = 3
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("you won")
#         break # break will exit while loop
# else: # else can also be used for while statements when loop isnt exited with break
#     print("you lost")

# command = ""
# car_started = False
# print("help - help menu")
# while True: #while true is basically a forever loop
#     command = input("> ").lower() # .lower can be used on inputs directly
#     if command == "start":
#         if car_started == False:
#             print("car started...")
#             car_started = True
#         else:
#             print("car is already started")
#     elif command == "stop":
#         if car_started == True:
#             print("car stopped")
#             car_started = False
#         else:
#             print("car hasnt started yet")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit programm
# """) # triple quotes will print exactly as is in code to terminal(useful for multiline)
#     elif command == "quit":
#         break # exit loop so it doesnt repeat forever
#     else:
#         print("I dont understand.")

# for item in "Python": #item = loop variable, this will run for item = P,y,t,h,o,n so it will run 6 times each with item being a different letter
#     print(item)

# for x in range(4):
#     for y in range(3): # nested loop for coordinates
#         print(f"({x}, {y})")

# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print(item * "*") # print f shape easily with lists

# number = [1, 4, 2, 14, 756, 3]
# print(max(number)) # get maximum from list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] # 2d list (matrix)
# print(matrix)
# print(matrix[1][2]) # print second row, 3rd column
# for row in matrix: # prints all items after each other
#     for item in row:
#         print(item)

# num = [3, 1, 46, 12, 4, 4, 89]
# num2 = num.copy() # creates num copy
# num.sort() # sorts list and updates it. (persistent)
# num.reverse() # reverses the list
# print(num)
# print(num2) # prints old list because of copy

# num = [3, 1, 46, 12, 4, 4, 89, 89, 3, 3, 2, 7, 65, 33]
# unique_num = []
# for item in num: # official way to do it
#     if item not in unique_num:
#         unique_num.append(item)

# print(num)
# for item in num: # my way to check for duplicates
#     if num.count(item) > 1:
#         num.remove(item)
# num.sort()
# print(num)
# print(unique_num)

# coordinates = (13, 54, 12)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# # both of these do the same thing one is way more efficient
# x, y, z = coordinates # can extract data from lists or tuples into multiple variables at once
# print(x, y, z)

# person = {
#     "name": "michi meier",
#     "age": 23,
#     "is_male": True
# } # add dictionary like this
# print(person["name"]) # name must exist otherwise will result in error
# print(person.get("birthdate", "march 3rd")) # birthday doesnt exist and will just say none or value provided instead of error
# person["birthdate"] = "june 4th" # change value or add value to dictionary
# print(person["birthdate"])

# spelled_numbers = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero"
# } # make dictionary for number
#
# numbers_output = ""
# numbers_input = input("Phone: ")
# for item in numbers_input:
#     numbers_output += spelled_numbers.get(item, "!") + " "
# print(numbers_output) # print out spelled numbers


# message = input("> ") # add input to message
# words = message.split(" ") # split message at spaces into a list called words

# emoji_dict = { 
#     ":)": "😀",
#     ":(": "☹️"
# } # define emoji dictionary
# output = ""
# for word in words:
#     output += emoji_dict.get(word, word) + " " # add either just the word or if in emoji dict add emoji to output with a space between
# print(output)

# def greet_user(): # define function
#     print("hi")
#     print("hello")


# print("start")
# greet_user() # run function
# print("finish")

# def hoch2(num): # add variable input for function. num = parameters
#     print(num ** 2)


# hoch2(4) # prints 16. 4 = argument

# def multiplier(num1, num2): # 2 parameter
#     print(num1 * num2)


# multiplier(3, 5) # needs 2 positional arguments

# def hello_user(first, last):
#     print(f"Hi {first} {last}!")


# hello_user(last="smith", first="john") # using parameter name makes it usable in whatever orientation

# def adder(num1, num2):
#     return num1 + num2 # return a value

# result = adder(6,7) # set result to returned value
# print(result) # print result

# def emoji_translate(input):
#     words = input.split(" ") # split message at spaces into a list called words
#     emoji_dict = { 
#     ":)": "😀",
#     ":(": "☹️"
#     } # define emoji dictionary
#     output = ""
#     for word in words:
#         output += emoji_dict.get(word, word) + " " # add either just the word or if in emoji dict add emoji to output with a space between
#     return output
    

# terminal_input = input("> ")
# print(emoji_translate(terminal_input))

# try: # Exceptions can be used if you want errors to not crash programm, try will just try
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError: # if error is one of these exceptions it will run the code in the code block and continue as normal
#     print("Invalid Value")
# except ZeroDivisionError:
#     print("Age cannot be 0")


# #comments can be used to communicate with developers, reminders to fix/clean, or explain why the code is needed
# """
# This is also a comment, but can be used on multiple lines
# Also try to avoid stating the obvious or adding to many comments
# good comments are why and how
# """

# class Point: #pascal naming convention for classes by capitalizing first letter of every word, used to define new types
#     def move(self): # define methods
#         print("move")
#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10 # define attributes
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 3
# print(point2.x)

# class Point: #pascal naming convention for classes by capitalizing first letter of every word, used to define new types
#     def __init__(self, x, y): # self is a reference to the current object, so Point in this case. This is a constructor used to create an object
#         self.x = x
#         self.y = y
#     def move(self): # define methods
#         print("move")
#     def draw(self):
#         print("draw")

    
# point = Point(10, 20) # x any y are defined directly
# point.x = 11 # change x to 11
# print(point.x)
# print(point.y)

# class Person: 
#     def __init__(self, name): # Dont understand this shit, edit:still don't understand btw
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")


# michi = Person("Michi")
# michi.talk()
# print(michi.name)

# bob = Person("Bob")
# bob.talk() # Same with all this



# class Mammal: # Define class Mammal
#     def walk(self):
#         print("walk")

         
# class Dog(Mammal): # Make Dog inherit methods from Mammal so no repetitions
#     pass # pass needed because empty class is not good


# class Cat(Mammal): # same with cat
#     def miau(self):
#         print("miau") # cat specific method so pass isnt needed


# dog1 = Dog()
# dog1.walk()
# cat1 = Cat()
# cat1.miau()

# print(divide2(16)) # imported from module

# print(swap_ab(input("Say something: "))) # runs swapping letter a and b function from module

# package.calc_shipping() # run calc_shipping from package

# for i in range(5):
#     print(random.random()) # random number between 0 and 1

# for i in range(2):
#     print(random.randint(5, 245)) # random integer between set numbers

# members = ["Michi", "Marcel", "Max", "Hanspeter"]

# print(random.choice(members)) # prints random element from list


# class Dice:
#     def roll():
#         output = []
#         for i in range(2):
#             output.append(random.randint(1, 6))
#         return tuple(output)
    

# print(Dice.roll()) # my solution


# class DiceOfficial:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second # in class when no [] automataically a tuple so () not needed


# dice = DiceOfficial()
# print(dice.roll()) # official way

# path = Path("/home/felix")
# file = Path("/home/felix/Desktop/commands.txt")
# # print(path.exists()) # checks if path exists, and returns as boolean
# # print(file.read_text()) # reads text from path
# for file in (path.glob("*.*")):
#     print(file) # prints all files/dirs containing a dot anywhere

# # other methods: mkdir, rmdir


##OWN PYGAME TEST
# pygame.init() # initialize pygame components like sound, graphics, fonts, joystick, etc

# screen_x, screen_y = 1200, 600 # define width and height to independent variables

# screen = pygame.display.set_mode((screen_x, screen_y), pygame.RESIZABLE) # create window from variables
# screen.fill((0, 255, 0))


# run = True
# #print(pygame.display.Info())

# while run:
    
#     # if pygame.key.get_pressed()[pygame.K_F11]:
#     #     pygame.display.set_mode((screen_x, screen_y), pygame.FULLSCREEN)


#     #Window.from_display_module().maximize()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
        
#         screen.fill((0, 255, 0))
#         pygame.display.update()
        
# pygame.quit()



##PYGAME TUTORIAL

pygame.init() # initialize pygame components like sound, graphics, fonts, joystick, etc
info = pygame.display.Info() # get display info and put it in info variable00
screen_width,screen_height = info.current_w, info.current_h # pull screen size
screen = pygame.display.set_mode((800, 400)) # create display surface, this is what the player sees, only 1 possible, always visable
run = True # initialize run variable needed for game loop
now = datetime.datetime.now() # set variable now to time

pygame.display.set_caption("learning_python") # set windows title to learning_python
clock = pygame.time.Clock() # set clock variable to pygame Clock object

ground = pygame.Surface((800, 50)) # create regular surface, isnt visable unless drawn on display surface, multiple possible
human = pygame.Surface((400, 100)) # create regular surface, isnt visable unless drawn on display surface, multiple possible
sky = pygame.Surface((800, 400)) # create regular surface, isnt visable unless drawn on display surface, multiple possible
test_obstical = pygame.Surface((50, 50)) # create regular surface, isnt visable unless drawn on display surface, multiple possible

jersey10 = pygame.font.Font("graphics/font/Jersey10-Regular.ttf", 25)



test_obstical.fill((0, 255, 0)) # fill ground with colour
ground = pygame.image.load("graphics/grass.png")
human = pygame.image.load("graphics/person.png")
sky = pygame.image.load("graphics/sky.png")

human_x = 100
human_y = 100

sky = pygame.transform.scale(sky, (800, 400))
human = pygame.transform.scale_by(human, ((800 / 800 + 400/ 400) / 2))
ground = pygame.transform.scale(ground, (800, 50))



ground_y = 350
fullscreen = False
prev_time = time.time()
dt = 0
vertical_velocity = 0
human_direction = "right"
fps = 0
resolution_scale = 1
resolution_scale_y = 1
resolution_scale_x = 1


while run: # run loop while run == True
    for event in pygame.event.get(): # event loop, checking for all events every game loop
        if event.type == pygame.QUIT: # if it finds and event of type QUIT it sets run to False which finishes the loop but doesnt start a new one
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11 and fullscreen == False:
                resolution_scale = (screen_width / 800 + screen_height / 400) / 2
                resolution_scale_y = (screen_height / 400)
                resolution_scale_x = (screen_width / 800)
                pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                fullscreen = True
                sky = pygame.transform.scale(sky, (screen_width, screen_height))
                human = pygame.transform.scale_by(human, (resolution_scale))
                test_obstical = pygame.transform.scale_by(test_obstical, (resolution_scale))
                ground = pygame.transform.scale(ground, (screen_width, screen_height / 8))
                ground_y = screen_height - screen_height / 8
                human_y = human_y * resolution_scale_y
                human_x = human_x * resolution_scale_x
                jersey10 = pygame.font.Font("graphics/font/Jersey10-Regular.ttf", 25 * int(resolution_scale))
            
            elif event.key == pygame.K_F11 and fullscreen:

                human_y = human_y / resolution_scale_y
                human_x = human_x / resolution_scale_x
                pygame.display.set_mode((800, 400))
                fullscreen = False
                sky = pygame.transform.scale(sky, (800, 400))
                human = pygame.transform.scale_by(human, (1 / (resolution_scale)))
                test_obstical = pygame.transform.scale_by(test_obstical, (1 / resolution_scale))
                ground_y = 350
                ground = pygame.transform.scale(ground, (800, 50))
                resolution_scale = 1
                resolution_scale_y = 1
                resolution_scale_x = 1
                jersey10 = pygame.font.Font("graphics/font/Jersey10-Regular.ttf", 25 * int(resolution_scale))
                
            elif event.key == pygame.K_q:
                run = False



    test_obstical_x = 30 * resolution_scale_x
    test_obstical_y = 300 * resolution_scale_y
    def colision(coliding_object):
            if coliding_object.colliderect(obsticle):
                print("colision")
                return(True)
    test_rect = test_obstical.get_rect(topleft=(test_obstical_x, test_obstical_y))
    obsticle = (test_rect)
    human_rect = human.get_rect(topleft=(human_x, human_y))

    time_now = time.time()
    dt = time_now - prev_time # dt = time it takes to run 1 frame
    prev_time = time_now
    
    print(colision(human_rect))
    

    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if colision(human_rect) == None:
            human_direction = "left"
            human_x -= 300 * dt * resolution_scale
            pygame.transform.flip(human, 1, 1)
        elif colision(human_rect) == True:
            human_direction = "left"
            human_x += 1000 * dt * resolution_scale
            pygame.transform.flip(human, 1, 1)
    if key[pygame.K_RIGHT]:
        if colision(human_rect) == None:
            human_direction = "right"
            human_x += 300 * dt * resolution_scale
        elif colision(human_rect) == True:
            human_direction = "right"
            human_x -= 1000 * dt * resolution_scale
    if key[pygame.K_UP]:
        if human_y > 249 * resolution_scale_y:
            vertical_velocity = 75 * resolution_scale_y


    test_obstical_x = 30 * resolution_scale_x
    test_obstical_y = 300 * resolution_scale_y

    human_y -= 9.81 * dt * vertical_velocity
    
    if vertical_velocity > -300:
        vertical_velocity -= 255 * dt * resolution_scale_y

    if human_y > 249 * resolution_scale_y or colision(human_rect):
        vertical_velocity = 0


    fps = int(1 / dt)
    text_surface = jersey10.render(f"FPS: {fps}", True, (0, 0, 0))
    screen.blit(sky, (0, 0)) # blit = BLock Image Transfer, put one surface on another, () = coords       
    screen.blit(ground, (0, ground_y)) # blit = BLock Image Transfer, put one surface on another, () = coords
    screen.blit(text_surface, (0,0))
    screen.blit(test_obstical, (test_obstical_x, test_obstical_y)) # blit = BLock Image Transfer, put one surface on another, () = coords  
    if human_direction == "left":
        screen.blit(pygame.transform.flip(human, 1, 0), (human_x, human_y)) # blit = BLock Image Transfer, put one surface on another, () = coords
    else:
        screen.blit(human, (human_x, human_y)) # blit = BLock Image Transfer, put one surface on another, () = coords


    pygame.display.update()
    clock.tick() # set fps cap using the method tick
    

    
    
pygame.quit() # quit pygame, opposite of pygame.init, so uninitializing everything


exit(print(now.strftime("%y-%m-%d %H:%M:%S:"),"Game successfully closed")) # exit with success message
