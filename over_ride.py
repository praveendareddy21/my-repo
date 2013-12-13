class Base():
    def __init__(self):
        print 'Base initilized'
    def say_hi(self):
        print('Hello, World from Base.')

class Man(object):
    def __init__(self):
        print 'Man initilized'
    def say_hi(self):
        print('Hello, World.')

class ExcitingMan(Base ,Man):
    def say_hi(self): 
        super(ExcitingMan)       
        print('Wow!')
        return super(ExcitingMan, self).say_hi()  # Returning the value of the cal
e=ExcitingMan()
e.say_hi()
