# Problem:
# There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb
# the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1 2, 1, 1 1, 2, 1 1, 1, 2 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if X = {1, 3,
# 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to
# take in X.

num_stairs = 10
step_types = [3, 4, 5, 6]

def climb_stairs(p_num_steps, available_step_types):
    
    steps_taken = []

    # remove step lengths that are greater than remaining stairs
    available_step_types = [ i for i in available_step_types if not i > p_num_steps]

    # handle empty list
    if available_step_types == []:
       return []

    # attempt every possible step
    for curr_step in available_step_types:
        
        # climb steps of the remainder of the stairs
        steps_remainder = climb_stairs(p_num_steps - curr_step, available_step_types)
        
        journey = [curr_step]

        # check if remainder is actually climbable
        if (steps_remainder == []):
            steps_taken.append(journey)
            
        # parse lists of recursive climbs
        else:

            for step_list in steps_remainder:
                
                # track each individual journey
                for step in step_list:
                    journey.append(step)
                steps_taken.append(journey)

                # reset after each journey
                journey = [curr_step]

    # remove any journeys that exceed the number of steps
    steps_taken = [i for i in steps_taken if sum(i) == p_num_steps ]
    
    return steps_taken


available = step_types
available = climb_stairs(num_stairs, available)

for i in available:
    print(i, "\n")