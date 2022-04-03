

####### INHERITANCE ################

class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "this is {} and its flavor is {}".format(self.color,self.flavor)

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass


"""Here we defined two classes Apple and Grape we can see both classes inherit from the Fruit class above as they have the name of the parent class in declaration"""

apple = Apple("green","KY")
grap = Grape("purple","sweet")

