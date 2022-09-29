T = int(input())
for testcase in range(1,T+1):
    K,N,M = map(int,input().split())
    stops = list(map(int,input().split())) 
    current = 0 #현재 위치
    cnt = 0   # 개수
    next = current+K # 다음 위치
    while next != N:  #다음 위치가 마지막 종점이 되기 전까지
        if next in stops:  #다음 위치가 정류장 번호 안에 있다면
            current=next   #현재 위치를 바꿔주고
            next = current+K  #다시 한번 위치 이동
            cnt+=1
        else:   # 정류장 번호안에 위치하지 못한 경우
            next-=1  #다음 위치를 한칸 전으로 옮겨주기
        if next == current:  #다음 위치와 현재위치가 같게 된다(즉,이동불가능한 거리)
            cnt =0   #0으로 반환 시켜주고 끝
            break
    print(f'#{testcase} {cnt}')

'''
3
3 10 5
1 3 5 7 9
'''