#class

'''
def : function

class : source
instance : result



class Cat:

    def _init_(self):

        self.c = 3
        self.b = 1
        print("first")

    def say(self):
        print("hi")

    def bye(self):
        print("bye")

a_Cat = Cat()

a_Cat.say()

a_Cat.bye()

#inherit information

class Tiger(Cat):

    def say(self):

        print("Aaaaaargh")

tiger = Tiger()

tiger.say()

tiger.bye()

cat = Cat()



class Cat:

    def __init__(self, a, b):

        self.c = a
        self.b = b
        print("first")

    def say(self, c, b):
        print(c + b)

    def bye(self):
        print("bye")

class Tiger(Cat):

    def say(self):

        print("Aaaaaargh")

cat = Cat(3,4)

cat.say(3,4)

tiger = Tiger(5,6)

tiger.bye()

tiger.say()

'''


'''
class Cal():

    def add(self, a, b):
        print(a+b)
    def minus(self, a, b):
        print(a-b)
    def multiply(self, a, b):
        print(a*b)
    def divide(self, a, b):
        print(a/b)
    def left(self, a, b):
        print(a%b)

cal = Cal()

cal.add(3,4)
cal.minus(24,25)
cal.multiply(9,9)
cal.divide(20,2)
cal.left(3838,234)

'''

#Github.com


#Github.com

#dovelet.com - prime number

a = int(input())

flag = True

for i in range(2,a):

    if(a%i == 0):
        flag = False
        break

if(flag == False):
    print('not prime')
else :
    print('prime')



a = float(input())

F = ((9.0/5) * a) + 32

print(F)

