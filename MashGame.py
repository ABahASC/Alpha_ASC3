import random
a = raw_input("where do you want to live: ") 
b = raw_input("who you wanna marry: ")
c = raw_input("what car do you want to drive: ")
houses = ['You will live in '+ a ,'You will live in '+ b,'You will live in '+ c,'You will live in a mansion','You will live in the street','You will live in a subway']
car = ['You will ride a '+ a,'You will mide a  '+ b,'You will ride a '+ c,'You will ride a bugatti','You will ride nothing','You will drive on the train']
wife = ['You will marry your crush','You will marry '+ a,'You will marry '+ b,'You will marry '+ c,'You will marry nobody']
print(random.choice(houses)), print(random.choice(car)), print(random.choice(wife))