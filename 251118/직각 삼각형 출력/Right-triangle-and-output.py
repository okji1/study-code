N=int(input())

for i in range(1,2*N):
    if i%2==1:
        for j in range(i):
            print("*", end="")
        print()