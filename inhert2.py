# class Grandfather:
#     def behaviour(self):
#         print("i have big house")

# class father(Grandfather):
#     def behaviour(self):
#         super().behaviour()
#         print("i have a house and bike")

# class Son(father):
#     def behaviour(self):
#         super().behaviour()
#         print("i am rich now")

    
        
# son_jr=Son()
# son_jr.behaviour()

class Grandfather:
    def __init__(self,house):
        self.house=house
    
    def behaviour(self):
        print("i have big house")

class father(Grandfather):
     def __init__(self,house,bike):
          super().__init__(house)
          self.bike=bike

     def behaviour(self):
        super().behaviour()
        print("i have both house and bike")

class Son(father):
     def __init__(self,house,bike,car):
          super().__init__(house,bike)
          self.car=car
     def behaviour(self):
        super().behaviour()
        print("i am rich now .i have house bike and car")

    
        
son_jr=Son("one_house","one_bike","two_car")
print(son_jr.house)
print(son_jr.bike)
print(son_jr.car)
son_jr.behaviour()