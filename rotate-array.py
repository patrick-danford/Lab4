"""
Patrick Danford 
Lab 4, Rotate array

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

"""

array1 = input("Enter a number: ")
array2 = input("Enter another number: ")
array3 = input("Enter yet another number: ")
array4 = input("Enter one more number: ")
array5 = input("Enter a final number: ")

array = [array1,array2,array3,array4,array5]
print "The list is: "
print array

amount = input("Enter a number to rotate the array by: ")

def rotate (n,k):
    return n[k:] + n[:k]

print rotate(array,amount)

