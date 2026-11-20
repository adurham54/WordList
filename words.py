import numpy as np
data = np.loadtxt("loop4.csv", delimiter = ",", dtype=str, encoding ="utf8")
words = []
rows, columns = data.shape

def num_letters(n_rows, n_cols):
    return n_rows*n_cols-((n_rows-2)*(n_cols-2))

# top
for c in range(columns):
    words.append(str(data[0,c]))
# right
for r in range(1, rows-1):
    words.append(str(data[r,-1]))
# bottom
for c in range(1, columns+1):
    words.append(str(data[-1,-c]))
# left
for r in range(2, rows):
    words.append(str(data[-r, 0]))
# check
print(words)
assert len(words) == num_letters(rows,columns)
print("Checking assertions")
