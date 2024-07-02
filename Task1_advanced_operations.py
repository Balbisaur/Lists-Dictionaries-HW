
##################Task 1#################
#implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter.
# Analyze the time and space complexity of this operation.
def double_odds(n):
    output = []

    for num in n:
        if num % 2 == 1:
            output.append(num * 2)
    
    return output

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(double_odds(num))


def squared_odds(n):
    result = []

    for num in n:
        if num % 2 == 1:
            result.append(num ** 2)
    
    return result

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(squared_odds(num))

# Time Complexity: O(n) because the function iterates over the numbers in the list once to see which are odd numbers first.
    