"""
Patrick Danford 
Lab 4, Returns duplicates

Given an array of integers, find all integers if the array contains any duplicates. 
Your function should return all the duplicates uniquely and should return -1 
if every element is distinct.

In [124]: find_duplicate([1,1,2,2,3])
 {1: 2, 2: 2}

Out[124]: dict_keys([1, 2])

In [102]: assert(find_duplicate([3, 4, 5, 6, 2, 3, 3, 4, 5, 6, 2, 3]))
 {2: 2, 3: 4, 4: 2, 5: 2, 6: 2}
 dict_keys([2, 3, 4, 5, 6])

Return Dups
In [40]: assert(dups([1,2,3]) == -1)
{1: 1, 2: 1, 3: 1}
In [41]: assert(dups([1,2,3,3]) == [3])
{1: 1, 2: 1, 3: 2}
In [42]: assert(dups([1,2,3,3,4,4]) == [3,4])
{1: 1, 2: 1, 3: 2, 4: 2}

"""

l = [1,1,2,2,3,4,5,6,6,7,7,8,9]

d = {}
for elem in l:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

print [x for x, y in d.items() if y > 1]