def solution(N, M, arr):
    s = 0
    start, end = 0, 0
    cnt = 0

    while True:
        if s >= M:
            s -= arr[start]
            start += 1
        else:
            if end == N:
                break
            s += arr[end]
            end += 1
        if s == M:
            cnt += 1
    return cnt

N, M = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
print(solution(N, M, arr))