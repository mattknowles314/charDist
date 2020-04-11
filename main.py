import matplotlib.pyplot as plt
import numpy as np
import scipy
ct = str(input(">> ")).lower() #Get the ciphertext
letters = []
letters_count = []
i = 0
while i <= (len(ct)-1):
    if ct[i] in letters:
        i+=1
    else:
        letters.append(ct[i])
        i+=1

for i in letters:
    count = ct.count(i)
    letters_count.append(count)

plt.bar(letters,letters_count, align='center',alpha=0.5)
plt.show()
