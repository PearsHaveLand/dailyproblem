# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array
# except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
#
# Follow-up: what if you can't use division?

input_list = [1, 2, 3, 4, 5]

def products(num_list):

    product_list = []
    length = len(num_list)

    for i in range(length):
        
        # Unintuitively, lists in Python are passed by reference, which
        # necessitates the .copy() function
        multiplicand_list = num_list.copy()

        # Remove the i'th index from the list to follow the problem instructions
        multiplicand_list.pop(i)

        # Initialize product to be first number in the list
        product = multiplicand_list[0]

        # Iterate through the list of multiplicands, not including current
        # product
        for j in range(1, len(multiplicand_list)):
            product = product * multiplicand_list[j]
        
        product_list.append(product)

    return product_list

if __name__ == "__main__":
    print(products(input_list))