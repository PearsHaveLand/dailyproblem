# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not
# allowed.

def count(msg):
    variations = 1

    if (len(msg) >= 2):

        if (int(msg[:2:]) <= 26 and int(msg[:2:]) >= 10):

            # There are at least two variations of the message:
            #   1st: interprets as two-digit number
            #   2nd: interprets as one-digit number
            variations = count(msg[2::]) + count(msg[1::])

        # Continue counting as normal
        else:
            variations = count(msg[1::])
    
    return variations

print(count('131'))