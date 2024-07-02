import numpy as np # I pip installed numpy so I can use 'concatenate' to combine two arrays into a single array then turn it back into a list.

##################Task 2#################
#Implement a function to merge two pre-sorted lists into a single sorted list. Analyze the time complexity of this operation.

list1 = [1, 2, 3, 4]

list2 = [5, 6, 7, 8]

array1 = np.array(list1)

array2 = np.array(list2)

sorted_array = np.concatenate((array1, array2)).tolist()

print(sorted_array)
 # this is my first attempt to merge two lists, it works when the number of lists are in order. besides that if it was pre-sorted,
 # it would just add the second list to the end of the first list.

# Time Complexity: O(n) because we are iterating over each element in both lists.


first_list1 = [1,3,5,7]

sec_list2 = [2,4,6,8]

sorted_test_list = sorted(first_list1 + sec_list2)

print(sorted_test_list)
#this is my seccond attempt. works great, combining both lists with the numbers in their correct spots!
