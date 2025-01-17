# By Using this technique we can calsulate sum 

a = [1,2,3,4,5,6,7]

currSum = 0
for x in range(len(a)):
    currSum = currSum + a[x]
    a[x] = currSum
print(a)


