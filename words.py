
def num_letters(n_rows, n_cols):
    return n_rows*n_cols-((n_rows-2)*(n_cols-2))

assert num_letters(3,4) == 10
assert num_letters(4, 13) == 30
assert num_letters(4, 4) == 12
assert num_letters(6,4) == 16
print("Checking assertions")
