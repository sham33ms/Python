import pandas as pd

# list1=[1,2,3,4,5,6]
# l1=pd.Series(list1)
# print(l1)

s1=[98,77,88,87,86,89]
student_scores = {
    'Alice': 95,
    'Bob': 88,
    'Charlie': 92,
    'David': 78
}
s2=["Rishi", "Shameem","Raj","Raaja","Britto", "Dervin"]
s3=pd.Series(s1,index=s2)
print(s3)
print(s3.index)
print(s3.values)    

s4= pd.Series([85, 92, 78, 65, 100], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print(s4)

print(s4['Bob'])

print(s4[['Alice', 'Eve']])

# add=s4+5
print(s4+5)

print(s4/100)

# passing_mask = s4 > 80
# print("This is the boolean mask:")
print(s4 > 80)


# #dict


scores_series = pd.Series(student_scores)

print(scores_series)