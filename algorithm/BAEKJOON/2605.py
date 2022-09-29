n = int(input())
number = list(map(int,input().split()))
order  = []
for i in range(len(number)):
    order.insert(i-number[i],i+1)
print(*order)