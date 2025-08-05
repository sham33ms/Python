#list
fruits = ["apple", "banana", "cherry", "apple"]
print(f"Original list: {fruits}")


print(f"First item: {fruits[0]}") 
print(f"Last item: {fruits[-1]}") 


fruits[1] = "blackberry"
print(f"After changing 'banana': {fruits}")


fruits.append("orange")
print(f"After appending 'orange': {fruits}")

fruits.insert(1, "mango") 
print(f"After inserting 'mango' at index 1: {fruits}")


fruits.pop()
print(f"After pop(): {fruits}")

fruits.pop(3)
print(f"After pop(3): {fruits}")

fruits.remove("apple") 
print(f"After removing 'apple': {fruits}")

fruits.sort()
print(f"After sorting  : {fruits}")

fruits.reverse()
print(f"After reversing  : {fruits}")

fruits.extend(["jackfruit" , "strawberry" , "apple"])
print(f"After extending  : {fruits}")

num =[5,5,5,6,6]
print(f"Count of num: {num.count(5)}")

print(f"Length of the list: {len(fruits)}")