L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:",L)

count = 0

for i in L:
    count += i
    
average = count/len(L)
print("sum = ", count)
print("average =", average)

L.sort()
print("The smallest element is:", L[0])
print("The largest element is: ", L[-1])
    