start, end = map(int, input().split())

# Please write your code here.
knock = [] #약수의 갯수가 3개인 정수들을 받아놓음

for i in range(start, end + 1):
    
    knocK_knock = [] #특정 정수의 약수를 받아높음
    
    for j in range(1, i + 1):
        if i % j == 0:
            knocK_knock.append(j)
            
        if len(knocK_knock) > 3:
            break
            
    if len(knocK_knock) == 3:
        knock.append(i)

print(len(knock))