class Apple():  # in python class name should start with a capital letter.
    color = "red"
    size = "m"
    flavor = ""

    def __init__(self, color, flavor):  # this function is also constructor that get input values
        """This is the constructor function it will built an Apple object"""
        self.color = color
        self.flavor = flavor


    def __str__(self): # ths str function will implement object printing when calling print function
        """this is the print implementation function called str"""
        return "this apple is {} and its falvor is {} and size is {}".format(self.color,self.flavor,self.size)

    def bigger(self):  # self This parameter represents the instance that the method is being execute on
        self.size = "L"  # to change the attribute of the object  we need to refer to  them by the self.
        return self.size



#SecondApple = Apple()
#print(SecondApple.color, SecondApple.flavor, SecondApple.size)
ThirdApple = Apple("Yellow", "Sweet")
print(ThirdApple.color, ThirdApple.size, ThirdApple.flavor)

print(ThirdApple)

help(Apple)