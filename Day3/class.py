#without class
user1_name = "Alice"
user1_email = "alice@example.com"
user1_posts = ["Hello World!"]

user2_name = "Bob"
user2_email = "bob@example.com"
user2_posts = ["My first post."]

def login_user(name):
    print(f"{name} has logged in.")

def post_message(name, message):
    # a real function would need to find the right post list
    print(f"{name} posted: {message}")

login_user(user1_name) # Alice has logged in.
post_message(user2_name, "My first post.")




class MainClass1:
    def _init_(self,name,age):
        self.name=name
        self.age=age
obj=MainClass1("John",30)
print("Name is:",obj.name)
print("Age is:",obj.age)



class MainClass2:
    def _init_(self,city,country):
        self.city=city
        self.country=country
    def display(self):
        print(f"City:{self.city} and Country:{self.country}")
obj2=MainClass2("New York","USA")
obj2.display()



class MainClass3():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
obj3=MainClass3()
print("Addition of 10 and 5 is:",obj3.add(10,5))
print("Subtraction of 10 and 5 is:",obj3.sub(10,5))