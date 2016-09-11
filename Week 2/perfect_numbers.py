n = 1
count = 0;
while True:
    if sum([i for i in range(1,n+1) if n%i == 0]) == 2*n:
        print(n)
        count = count + 1;
        if count >= 4:
            break;
    n += 1

print("done");