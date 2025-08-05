
coordinates = (10.0, 20.0,10.0, "north")
print(f"Original tuple: {coordinates}")


print(f"First item: {coordinates[0]}") 
print(f"Last item: {coordinates[-1]}") 

#  You CANNOT change a tuple
# coordinates[0] = 5.0  

print(f"Count of 10.0: {coordinates.count(10.0)}")
print(f"Index of 'north': {coordinates.index('north')}")

print(f"slicing : {coordinates[3:]}")
print(f"slicing : {coordinates[:3]}")


print(f"Length of the tuple: {len(coordinates)}")