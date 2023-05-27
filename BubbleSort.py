l = [1234567,12345543,4312345,234321,1234563,1234565,12345675]
n = len(l)

for i in range(0,n-1):
    for j in range(0,n-i-1):
        if l[j] > l[j+1]:
            t = l[j]
            l[j] = l[j+1]
            l[j+1] = t
            
print(l)
print(l[::-1])
print("Below codes are done using shortcuts :)")
L = sorted(l)
print("Assending Order: ",L)
print("Deccending Order: ",L[::-1])
