import re

email = "v.j.-_85j@v.v.ghv.jhv"
pattern = r'^[\w.-]+@[\w.-]+.\w+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


pattern = r'^[6-9]\d{9}$'  # Indian mobile numbers start with 6-9

number = "9876543210"
if re.match(pattern, number):
    print("Valid")
else:
    print("Invalid")
    

