# 1. Sum of all numbers in a list using for loop
List = [45, 12, 32, 65, 98, 12]
sum_val = 0
for num in List:
    sum_val += num
print("Sum of list:", sum_val)

# 2.Find the number is odd or even using for loop.
  #   1.Print ‘odd number’ if value is odd number.
   #  2.Print ‘even number’ if value is even number 

for num in List:
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")

# 3. write a code below conditions: 

#1.Generate a List with 20 random numbers between 10 and 50 
#2. find second largest number in a list and second smallest number in a list

import random
rand_list = [random.randint(10, 50) for _ in range(20)]
print("Random List:", rand_list)

# Find second largest and second smallest
sorted_list = sorted(rand_list)
second_smallest = sorted_list[1]
second_largest = sorted_list[-2]
print("Second smallest:", second_smallest)
print("Second largest:", second_largest)

# 4. Print negative numbers in a list
#Input: list1 = [12, -7, 5, 64, -14] 
#Output: -7, -14
list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num < 0:
        print("Negative number:", num)

# 5. Print all negative numbers in given range
#Input: start = -4, end = 5 
#Output: -4, -3, -2, -1
start, end = -4, 5
for i in range(start, end):
    if i < 0:
        print("Negative number in range:", i)

# 6. Count occurrences of an element in a list
#Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10] 
#x = 10 
#Output: 3 
#10 appears three times in given list
list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
count = list.count(x)
print(x, "appears", count, "times in given list")

# 7. Remove empty list from list
#The original list is: [5, 6, [], 3, [], [], 9] -->input 
#List after empty list removal: [5, 6, 3, 9] -->output
original = [5, 6, [], 3, [], [], 9]
cleaned = [ele for ele in original if ele != []]
print("List after empty list removal:", cleaned)

# 8. Add two lists using for loop
#A=[10,12,15,45,30]
#B=[18,38,16,82,20]
#
   # 1.add a two list and if result value is match to 50 then store 5 instead of 50.


A = [10, 12, 15, 45, 30]
B = [18, 38, 16, 82, 20]
result = []
for i in range(len(A)):
    val = A[i] + B[i]
    if val == 50:
        result.append(5)
    else:
        result.append(val)
print("Result after adding two lists:", result)