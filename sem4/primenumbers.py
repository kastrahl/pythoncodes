num = int(input("Enter N"))
count = 0
for i in range (1, num + 1):
    for j in range (2, i):
        if i%j == 0 :
            count = count + 1
    if count == 0 :
        print(i)
    else:
        count = 0
