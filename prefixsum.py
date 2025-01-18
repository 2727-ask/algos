# By Using this technique we can calulate sum between two indexes in O(1) time complexity

a = [1,2,3,4,5,6,7]

currSum = 0
for x in range(len(a)):
    currSum = currSum + a[x]
    a[x] = currSum
print(a)


