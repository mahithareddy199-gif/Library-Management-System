class User:
    def __init__(self,user_id,name,Roll_no,department,phone):
        self.user_id=user_id
        self.name=name
        self.Roll_no=Roll_no
        self.department=department
        self.phone=phone

    def  display(self):
        print(f"user ID   :{self.user_id}")   
        print(f"Name      :{self.name}")   
        print(f"ROll no   :{self.Roll_no}")   
        print(f"department:{self.department}")   
        print(f"phone     :{self.phone}")   
 
    def update_phone(self,new_phone):
        self.phone=new_phone
        print("phone number updated successfully")
d1=User(101,"Mahitha","244CA05167","CSE",9876543210)
d1.display()
d1.update_phone(9988484300)
d1.display()        