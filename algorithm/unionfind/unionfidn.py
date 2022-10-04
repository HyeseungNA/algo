# def findboss(member):
#     if arr[member] == member:
#         return member
#     ret = findboss(arr[member])
#     return ret

# def union(a,b):
#     aboss = findboss(a)
#     bboss = findboss(b)
#     if aboss == bboss:
#         return
#     else:
#         arr[bboss] = aboss
# N = int(input())
# arr = list(range(6))
# #[0,1,2,3,4,5]
# for _ in range(N):
#     a,b = map(int,input().split())
#     union(a,b)

# print(findboss(1))
# print(findboss(2))


def findboss(member):
    if arr[member] == 0:
        return member
    ret = findboss(arr[member])
    arr[member]=ret
    return ret

def union(a,b):
    aboss = findboss(a)
    bboss = findboss(b)

    if aboss == bboss:
        return
    else:
        arr[bboss] = aboss

N = int(input())
arr = [0] * 6
for _ in range(N):
    a,b = map(int,input().split())
    if a>b:
        a,b = b,a
    union(a,b)