import numpy as np
data = np.loadtxt("loop4.csv", delimiter = ",", dtype=str, encoding ="utf8")
words = []
rows, columns = data.shape

def num_letters(n_rows, n_cols):
    return n_rows*n_cols-((n_rows-2)*(n_cols-2))
#loop 1
for c in range(columns):
    words.append(data[rows, columns])
        
print(words)
assert len(words) == num_letters(rows,columns)


