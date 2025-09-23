class Complexs:
    def __init__(self,real,img):
          self.real=real
          self.img=img

    def show(self):
        print(self.real ,"i +",self.img,"j")

    def __add__(self,other):
         new_real=self.real + other.real
         new_img=self.img+other.img
         return Complexs(new_real,new_img)
    
    def __sub__(self,other):
         new_real=self.real - other.real
         new_img=self.img - other.img
         return Complexs(new_real,new_img)

    def __mul__(self,other):
         new_real=self.real *other.real
         new_img=self.img * other.img
         return Complexs(new_real,new_img)
    
    def __truediv__(self,other):
         new_real=self.real /other.real
         new_img=self.img / other.img
         return Complexs(new_real,new_img)


    

n1=Complexs(87,88)
n1.show()

n2=Complexs(98,67)
n2.show()

n3=n1+n2
n3.show()

n4= n1-n2
n4.show()

n5=n1*n2
n5.show()

n6=n1/n2
n6.show()
     

    
     

    