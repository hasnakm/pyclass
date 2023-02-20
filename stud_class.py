class student:
    def __init__(self,name:str,place:str,age:int):
        self.name=name
        self.place=place
        self.age=age
    def set_age(self,a: int):
        self.age=a
    def get_age(self):
        print()
        print("Age of the student : ",self.age)
    def display_student_details(self):
        print()
        print("Details of the Student")
        print("Name : "+self.name)
        print("Place : "+self.place)
        print("Age : ",self.age)