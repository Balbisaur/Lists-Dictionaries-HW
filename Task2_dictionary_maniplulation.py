#implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time complexity of this operation.
dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

merged_dict = {**dict_1, **dict_2} # unpacking the key/value pairs and merging them into one dictionary

print(merged_dict)

def intersection(dict_1, dict_2):
    return {k: dict_1[k] for k in dict_1 if k in dict_2 and dict_1[k] == dict_2[k]} # using a dictionary comprehension to create a new dictionary with the values of the dict_1 and the values of the dict_2

intersection_dict = intersection(dict_1, dict_2)

print(intersection_dict)

# Time complexity: O(n), where n is the total number of key-value pairs in both dictionaries. 
# The function iterates over the keys in dict_1 once and performs a dictionary lookup in dict_2, resulting in a constant time complexity for each key-value pair. 
# The overall time complexity is therefore O(n).
    