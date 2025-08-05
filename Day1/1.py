
#varialbles & datatypes------------------
name='shameem'
age=21
pass1=True
print(name,age,pass1)

#loop------------------------
#while-------------
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1
#for--------
i=1
for i in range(i,3):
    print(i)

#CONDITION--------
#if-----------------
age=21
if age>=18:
    print('you are eligible', age , 'from if')

#if else------------------
age=17
if age>=18:
    print('you are eligible')
else:
    print('you are not eligible', age , 'form iflese')


#indexing--------------------
text = 'Shameem'
for i in range (len(text)):
    print(text[i])
print(text[i]) 

#slicing----------------------
text = 'ShameemMohamedShameem'
print(text[1:4])
print(text[1:5])
print(text[1:15:2]) #hmeMhmd

#list-----------------------------
list1=[1,2,3,4,5]
print(list1[0]) #1
# print(list1[1]) #2
list1.append(6)
list1.pop(4)
list1.insert(2,5)
# list1.remove(3)
list1.sort()
list1.reverse()
# list1.clear()
list1.extend([7,8,9])
list1.sort()
list1.reverse()
# print(list1)
print(list1[0:5]) 
print(list1[0:5:2])
# print(list1[0:5:3])
print(list1) 
