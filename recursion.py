def multiply_list(l):
    total = 1 
    if l == []: 
        return 1 
    else: 
      total = l.pop() * multiply_list(l)
    return total

# Return the factorial of n
def factorial(n):
    total = 1
    if n == 1:
        return 1
    else:
        total = factorial(n-1) * n
    return total

# Count the number of elements in the list l
def count_list(l):
    total = 0
    if l == []:
        return 0
    else:
        l.pop()
        total = count_list(l) + 1 
    return total

# Sum all of the elements in a list
def sum_list(l):
    total = 0
    if l == []:
        return 0
    else:
        total = l.pop() + sum_list(l)
        
    return total


# Reverse a list without slicing or loops
def reverse(l):
    # l.reverse() is what one would do if they were NOT insane. Insane people
    # write recursive ridiculousness here:

    if len(l) == 1:
        return l
    else:
        temp = l.pop()

    return [temp] + reverse(l)

# l = [1,2,3,4,5]
# print reverse(l)

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return None
    elif l[0] == i:
        return i
    rest = l[1:]
    return find(rest,i)

# n = [1,2,3,4,5,6]

# print find(n,3)


# Determines if a string is a palindrome
def palindrome(some_string):
    some_string = list(some_string)
    if len(some_string) == 1:
        return True
    else:
        first = some_string.pop(0)
        last = some_string.pop(len(some_string) - 1)
        if first == last:
            return palindrome(some_string)
        else:
            return False
        

# s = 'arrow'
# print palindrome(s)

# Given the width and height of a sheet of paper, and the number of times to fold it,
# return the final dimensions of the sheet as a tuple.
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):

    if folds == 0:
        return (width, height)
    else:

        # start with 8 x 12 paper: width is 8, height is 12
        # height is greater. new height is 6, width is 8.
        # width is greater. height is 6. width is 4.
        # height is greater. height is 3. width is 4.
        # width is great. height is 3. width is 2. 

        if width > height:
            # fold the width
            return fold_paper(width/2.0, height, folds-1)
        elif width < height:
            return fold_paper(width, height/2.0, folds-1)

# print fold_paper(12, 8, 4)
            

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == target:
        return n
    else:
        print n
        return count_up(target, n + 1)
        

count_up(100, 0)
 