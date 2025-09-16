class Car:
    @staticmethod
    def start():
        print("starting.....")

    @staticmethod
    def stop():
        print("stoping.....")
    
class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyota):
    def __init__(self,brand,engine):
        super().__init__(brand)
        self.engine=engine

c1=Fortuner("prius","Petrol")
print("brand_name",c1.brand)
print("Engine",c1.engine)
c1.start()
