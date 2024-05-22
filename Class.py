#!/usr/bin/env python
# coding: utf-8

# In[10]:


class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get_age(self):
        print(self.age)
    def set_age(self, newage):
        if newage>100:
            print('age can not be greater then 60')
        else:
            self.age = newage


# In[14]:


p1 = person(50, 'hamza')


# In[15]:


p1.age


# In[23]:


p1.get_age()


# In[19]:


p1.set_age(59)


# In[20]:


p1.get_age()


# In[37]:


class Items:
    def __init__(self, washing, kitchen):
        self.washing = washing
        self.kitchen = kitchen
        
    def get_kitchen(self):
        print(self.kitchen)
        
    def set_kitchen(self, new_item):
        if len(self.kitchen) > 5:
            print('ITEMS LIST IS FULL, PLEASE TRY AGAIN NEXT TIME')
        else:
            self.kitchen.append(new_item)


# In[54]:


items = Items(washing='Washing Machine', kitchen=['Microwave', 'Toaster'])


# In[56]:


items.get_kitchen()


# In[66]:


class Car():
    def __init__(self,make,model,engine,color,year):
        self.make = make
        self.model = model
        self.engine = engine
        self.color = color
        self.year = year
    def start_car(self):
        print("Car Starting")
    def apply_breaks(self):
        print("Car Stopped")
    def fill_tank(self):
        print("Car tank is being filled")


# In[80]:


car1 = Car('Honda','City','1300CC','Black',2022)


# In[85]:


car1.fill_tank()


# In[102]:


class ElectricCar(Car):
    def __init__(self,make,model,engine,color,year,battery):
        super().__init__(make,model,engine,color,year)
        self.battery = battery
        
    def charger(self):
        print('Battery charging in progress')


# In[105]:


ec1 = ElectricCar('Honda','City','1300CC','Black',2022,'200Amp')


# In[106]:


ec1.charger()


# In[115]:


class Animal():
    def __init__(self,color,height,weight):
        self.color = color
        self.height = height
        self.weight = weight


# In[116]:


class Cat(Animal):
    def __init__(self,color,height,weight,name):
        super().__init__(color,height,weight)
        self.name = name
    
    def name(Cat):
        print("This is cat")


# In[118]:


c1 = Cat('orange','3inch','10kg','cat')


# In[120]:


c1.name


# In[121]:


c1.weight


# In[130]:


class Students:
    def __init__(self, name, clas, roll_number, fees):
        self.name = name
        self.clas = clas
        self.roll_number = roll_number
        self.fees = fees
        
    def check_fees(self):
        if self.fees > 4000:
            print("You can go now inside the class")

class Sections(Students):
    def __init__(self, name, clas, roll_number, fees, section):
        super().__init__(name, clas, roll_number, fees)
        self.section = section

    def check_section(self):
        if self.section == 'A':
            print("You can go now inside the class in section A")
        elif self.section == 'B':
            print("You can go now inside the class in section B")
        else:
            print("Please stand there")


