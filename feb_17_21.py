# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

my_k = 17
my_num_list = [10, 15, 3, 7]

# For each item in the list, adds it to each of the _next_ items on the list,
# checking if that sum is k
#
# Note: only attempts two-number summations 
#
# Returns a list containing each of the combinations of elements that add to k
def find_sums(k, num_list):

    sums_list = []

    # Iterating by indices for proper list slicing
    for i in range(len(num_list)):

        # Get all items after i in the list
        remainder_list = num_list[i::]

        # Check the sum of num_list[i] with all of the remaining elements
        for j in range(i, len(remainder_list)):
            if num_list[i] + num_list[j] == k:
                sums_list.append((num_list[i], num_list[j]))
            
    return sums_list

if __name__ == "__main__":
    print(find_sums(my_k, my_num_list))