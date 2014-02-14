listtest = []
if listtest.pop() is False: #throws an error, how check
    print "yes!"
# if listtest == []:

"""
Exercise 4
"""

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    half_length = custom_len(input_list) // 2
    for i in range(half_length):
        # Swap the corresponding pair of values in place.
        input_list[i], input_list[-i-1] = input_list[-i-1], input_list[i]