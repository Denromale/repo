clients= {
    "name": [],
    "age": [],
    "sex": []
    }
clients_loop=0
while clients_loop<3:
    
    print(f"Hello, my name is Bella, Please write your name") 
    first_name=input()
    clients["name"].append(first_name)
    print(f"Please write your age")
    your_age=input()
    clients["age"].append(your_age)
    print(f"Please write your sex")
    your_sex=input()
    clients["sex"].append(your_sex)

    client = {"name":str(first_name),"age":int(your_age),"sex":str(your_sex)}


    class Human():
        def __init__(self, name, age, sex):
            self.name=name
            self.age=age
            self.sex=sex

        def display_info(self):
            print(f"name: {self.name},\n age: {self.age}, \n sex: {self.sex}")

        def age_control(self):
            if self.age>=21:
                print("Entrance except!")
            else:
                print(f"Sorry {self.name},You are {self.age} years old and you are too young for this shit!")

        def sex_control(self):
            if self.sex=="male":
                print("Yeah boy!")
            elif self.sex=="female":
                print("this is the man's world!")
            else:
                print("What are you?")


    client= Human(client.get("name"),client.get("age"),client.get("sex"))
    client.display_info()
    client.age_control()
    client.sex_control()
    clients_loop+=1
    
else:
    print("list is full")
print(clients)