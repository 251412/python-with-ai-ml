#Create a list with 2 integers,2 float ,2 string data

list_values = [24, 14, 2.5, 2.6, "array", "list"]
print("List with mixed data:", list_values)
#Create an Empty list 
empty_list = []
print("Empty list:", empty_list)
#Data =[12,45,46,36,10.5,9.6] 
#Replace 10.5 to 100
Data = [12, 45, 46, 36, 10.5, 9.6]
print("Before replace:", Data)
Data[4] = 100
print("After replace:", Data)
#VData=[10,12.5,’python’] 
#Output: python Programming
# 1.extract and remove python text from list
# 2.add ‘programming’ word with extracted word 
# 3.Finaly print the output 
Data = [10, 12.5, 'python']
print("Original Data:", Data)
word = Data.pop(2)  #remove python
print("Extracted word:", word)
output = word + " Programming"
print("Final Output:", output)
#Data=[12,45,2,78,36,92,101,9] 
#1.Print ascending order  
#2.print descending order   
Data = [12, 45, 2, 78, 36, 92, 101, 9]
print("Original:", Data)
Data.sort()
print("Ascending:", Data)
Data.sort(reverse=True)
print("Descending:", Data)
#Data=[12,45,63,78,95] 
#1. Find and print the index value of 95 value
Data = [12, 45, 63, 78, 95]
index_val = Data.index(95)
print("Index of 95:", index_val)
# Create Dictionary with two key 
dict1 = {'book': ['a', 'b', 'c'],
         'age': [16, 54, 10]}
print("Dictionary:", dict1)
#Add new key with this dict 
 
 
 #       dict1 = {'book': ['a', 'b', 'c'], 
  #               'age': [16,54,10]} 
 
#Add new key: 
 #  Gender =[‘m’,’f’,’m’]
dict1['Gender'] = ['m', 'f', 'm']
print("After adding Gender:", dict1)
#Delete gender key from above dictionary 
dict1.pop('Gender')
print("After deleting Gender:", dict1)
#merge two dictionary 
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print("Merged dictionary:", dict1)
