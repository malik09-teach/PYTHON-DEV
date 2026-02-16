import os 

class home:
    def __init__(self,room_no,per_R_L,per_fan,use_t):
        self.room_no=room_no
        self.per_R_L=per_R_L
        self.per_fan=per_fan
        self.use_t=use_t 

    def __power_use (self):
            return (self.per_R_L*self.use_t)+(self.per_fan*self.use_t)


    def _totcost (self):
        return (self.__power_use()*15.4 )*self.room_no 



def main():
    print("************************************")

    room_no=int(input("Enter the number of rooms in your home: "))
    fans=int(input("Enter the number of fans in your home: "))
    lights=int(input("Enter the number of lights in your home: "))
    hours=int(input("Enter the number of hourss in your home: "))



    os.system('cls')


    home1=home(room_no,lights,fans,hours)
    print("************************************")
    print("ROOMS:",room_no)
    print("FANS:",fans)
    print("LIGHTS:",lights)
    print("HOURS:",hours)
    print('\n')
    print("Total cost :",home1._totcost(),"Rs")
    print("************************************") 


main()