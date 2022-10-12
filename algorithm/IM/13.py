T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    bucket = [0] * 1001
    for _ in range(N):
        bus,A,B = map(int,input().split())
        if bus == 1:
            for i in range(A,B+1):
                bucket[i] += 1
 
        elif bus == 2:
            if A % 2 == 1:
                for j in range(A,B+1):
                    if j % 2 == 1:
                        bucket[j] +=1
            elif A % 2 == 0:
                for j in range(A,B+1):
                    if j % 2 == 0:
                        bucket[j] += 1

        else:
            if A % 2 == 0:
                for j in range(A,B+1):
                    if j % 4 == 0:
                        bucket[j] += 1
            if A % 2 == 1:
                for j in range(A,B+1):
                    if j % 3 == 0 and j % 10 != 0:
                        bucket[j] += 1

    print(f'#{testcase} {max(bucket)}')

