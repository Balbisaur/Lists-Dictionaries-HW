#Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time complexity of this operation.
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

merged_dict = {**dict_1, **dict_2} # unpacking the key/value pairs and merging them into one dictionary, while keeping the values of the second dict.

print(merged_dict)


# Time complexity: O(n) because the key/value pairs need to be copied from both dictionaries and then merged into one new dictionary.


