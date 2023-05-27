n = [123,321,453,272,193,495]
add = sum(n)
d = len(n)
avg = float(add/d)
print(avg)

#print("The below one is done using for loop: ")

print(n)
sum = 0
for i in range(len(n)):
    sum = sum + n[i]
print("Average is: ",sum/d)
