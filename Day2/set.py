unique_tags = {"python", "code", "programming", "python"}
print(f"Original set: {unique_tags}") 


unique_tags.add("developer")
print(f"After adding 'developer': {unique_tags}")


unique_tags.remove("code") 
unique_tags.discard("nonexistent") 
print(f"After removing 'code': {unique_tags}")

 
set_a = {1,2,3,4}
print(set_a)
set_b = {3, 4, 5, 6}

print(f"Union (A | B): {set_a | set_b}")   
print(f"Union : {set_b .union (set_a)}")      
print(f"Intersection (A & B): {set_a & set_b}") 
print(f"Difference (A - B): {set_a - set_b}")  
print(f"Difference (A - B): {set_b - set_a}") 
