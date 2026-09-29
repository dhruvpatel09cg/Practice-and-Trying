import random
import string

pass_len = int(input("Length of Password will be:"))
chr_val = string.printable

# List Comprehension [function for i in range(n)]
res = "".join([random.choice(chr_val) for i in range (pass_len)])
print(res)  # "".join() will join all element of list and give as string separated by value in between ""

# Alternate

# password = ""
# for i in range(pass_len):
#     password += random.choice(chr_val)

# print("Your random password is:",password)