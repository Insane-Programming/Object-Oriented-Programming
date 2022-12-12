# Unlike other programming languages, file name need not to match the class name

# According to Python, it is good to start the class name with a capital letter.

class Item: # Class name contains no parantheses or any kind of argument

    # variables that are declared outside of any kind of function but in the class are global, 
    # they can even be used outside the class by ClassName.variableName

    # DECLARING THE CLASS ATTRIBUTES

    pay_rate = 0.8 # this variable can be accessed anywhere by, Class.variableName Item.pay_rate
    all = [] # save our instances

    # Arguments of the init file should be the basic requirement of the class
    # init runs automatically whenever an instance of class is created

    def __init__(self, name, price : float, quantity = 0):
        
        # I wanted to give name argument a default value of '' 
        # but it says non - default argument cannot follow a default argument 
        # means all the default arguments must be wriiten after the non defaults

        # Here price is taken as a floating point value even if passes as int
        
        # RUNNING VALIDATIONS

        # assert - if False show error, opposite of if statement

        assert price >= 0, f'Price cannot be {price}'
        assert quantity >= 0, f'Quantity cannot be {quantity}'

        # DECLARING THE INSTACE ATTRIBUTES

        self.name = name 
        self.price = price
        self.quantity = quantity

        # These above declarations helps to get these variables not in just init function but in the whole calss
        
        # self.display_instance_details()

        # SAVING INSTANCE DETAILS

        Item.all.append(self)
       
    def calculate_price(self):

        return self.price * self.quantity

    def apply_discount(self):
                
        self.discounted_price = self.price * self.quantity * self.pay_rate
        return self.price * self.pay_rate * self.quantity # Here we did self.pay_rate instead of Item.pay_rate 

    def display_instance_details(self):
        
        # print(f'\nAn Instance created - {name} ')
        print(f'\nProduct: {self.name}')
        print(f'Final Price: {self.price}')
        print(f'Quantity: {self.quantity}')

        # for i in Item.all:
        #     print(i)

    def __repr__(self):
        return f'Item("{self.name}","{self.price}","{self.quantity}")' # Returls a list, automatically apends 
        

# TRAINING CODE

# # item1 = Item() # if name = ''
# item1 = Item("Phone",100)

# item2 = Item("Laptop",200,2)

# # Checking the Functionalities

# print(item1.name)
# print(item2.price)

# print(Item.pay_rate)
# print(item2.pay_rate) # Here it wil first find the pay rate at instace level, but if not found then go for class level

# print(item2.calculate_price())

# # Here the pay rate is 0.8 as defualt for every product, but for exception, you can define seprate pay rates for each instance
# item2.pay_rate = 0.6

# print(item2.apply_discount())
# print(item2.discounted_price)

# -----------------------------------------

# Creating some insatances

item1 = Item('Phone',100,1) # variable name - phone
item2 = Item('Laptop',1000,3)
item3 = Item('Cable',10,5)
item4 = Item('Mouse',50,5)
item5 = Item('Keyboard',75,5)

# Getting Insatace details

# print(Item.all) # This will return the object address of instances which is not so helpful, 
# so we can use magic method called repr stands for represtation of objects

# for instance in Item.all:
#     print(f'Instance Name: {instance.name}')

for i in Item.all:
    print(i)

# CSV - Comma Seprated Values



