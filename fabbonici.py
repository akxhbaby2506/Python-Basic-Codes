n = int(input("Enter the number of elements: "))
print("Number of elements: ",n)


first = 0;
second = 1;

i = 0;
while (i <= n):
    
    print(first)
    
    next = first + second
    first = second
    second = next
    
    i = i+1;