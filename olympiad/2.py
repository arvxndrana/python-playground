"""
    Consider the set S = {1,2,3,...,1000}. How many arithmetic progressions can be made from the elements of S that starts with 1 and ends with 1000 and have at least 3 elements?
"""

S = [x for x in range(1,1000+1)]
required_sequences = []


def sequence_generator(n):
    """
        Returns arithmetic sequences starting from '1' having difference of 'n' until the last term is less than or equal to 1000.
    """
    k = [1]
    prev_ = k[0]
    while (prev_ < 1000): # Don't know why equals is not valid here
        next_ = prev_ + n
        k.append(next_)
        prev_ = next_
    return k


s = []
for i in S:
    s = sequence_generator(i)

    # Conditions
    first_element_is_one = (s[0] == 1)
    last_element_is_thousand = (s[-1] == 1000)
    has_at_least_3_elements = len(s) >= 3

    if (first_element_is_one and last_element_is_thousand and has_at_least_3_elements):
        required_sequences.append(s)


print(f"Ans: {len(required_sequences)}")
