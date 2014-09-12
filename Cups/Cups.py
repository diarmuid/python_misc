class Cups():
    def __init__(self):
        self.colour = None
        
    def paint(self,colour):
        self.colour = colour
        
    def describe(self):
        return "I am a {} cup".format(self.colour)
        
blue_cup = Cups()
blue_cup.paint("blue")

red_cup = Cups()
red_cup.paint("red")

print blue_cup.describe()
print red_cup.describe()