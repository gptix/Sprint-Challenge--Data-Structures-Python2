import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# The code below is O(n^2) because it has two nested for loops.

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# The code below is O(n) because it has two for loops, but they are in series.
# The dictionary has an average worst case of O(1)
# ref: https://wiki.python.org/moin/TimeComplexity - section "dict"

# names_dict = {}
# for name_1 in names_1:
#     names_dict.update({name_1:True})

# for name_2 in names_2:
#     if name_2 in names_dict:
#         duplicates.append(name_2)


names_1.sort()
names_2.sort()



index_n1 = 0
index_n1_OOR = len(names_1) # OOR means Out of Range
index_n2 = 0
index_n2_OOR = len(names_2)

# stop when we get to the end of either list
while (index_n1 < index_n1_OOR) and (index_n2 < index_n2_OOR):
    left = names_1[index_n1]
    right = names_2[index_n2]



    if left == right:
        duplicates.append(left)
        names_1 = names_1[1:] # shorten lists to save memory
        names_2 = names_2[1:]
        index_n1_OOR -= 1 # update OOR markers
        index_n2_OOR -= 1


    elif left < right:
        names_1 = names_1[1:]
        index_n1_OOR -= 1


    else:
        names_2 = names_2[1:]
        index_n2_OOR -= 1


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# Python dicts are appropriate. Average worst time for insert or retrieve of O(1).
# Best time on a lenovo X230 running Ubuntu 18.04 and Python 3.7: 



# SSTTRREETTCCHH


# with limited memory, I would:
# sort both lists
# chop extraneous head off of the one with 'earlier' unmatched names
# crawl pointers down both lists
  # if a match, add to 'duplicates' and delete both.
  # if not a match, delete the 'less' one
  # stop when either input list is empty