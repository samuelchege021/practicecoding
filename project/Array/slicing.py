# Elements from beginning to a range use [:Index]
# Elements from end use [:-Index]
# Elements from specific Index till the end use [Index:]
# Elements within a range, use [Start Index:End Index]
# Print complete List, use [:].
# For Reverse list, use [::-1].



import array as arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



a=arr.array("i",l)


sliced_array=a[3:8]

print(sliced_array)



Sliced_array = a[:5]
print(Sliced_array)

Sliced_array = a[:]
print(Sliced_array)