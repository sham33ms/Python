user_profile = {
    "username": "coder_xyz",
    "age": 25,
    "is_active": True
}
print(f"Original dictionary: {user_profile}")


print(f"Username: {user_profile['username']}")

print(f"Location: {user_profile.get('location')}") 
print(f"Location with default: {user_profile.get('location', 'Not specified')}")

user_profile["location"] = "India"  
user_profile["age"] = 26            

print(f"Updated dictionary: {user_profile}")


del user_profile["is_active"]
print(f"After deleting 'is_active': {user_profile}")


print(f"Keys: {user_profile.keys()}")
print(f"Values: {user_profile.values()}")
print(f"Items (key-value pairs): {user_profile.items()}")
