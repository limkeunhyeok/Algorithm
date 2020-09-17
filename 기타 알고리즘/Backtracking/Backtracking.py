"""
좋은 수열
숫자 1, 2, 3으로만 이루어지는 수열이 있다.
임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다.
그렇지 않은 수열은 좋은 수열이다.
길이가 N인 좋은 수열들을 N자리의 정수로 보아 그중 가장 작은 수를 나타내는 수열을 구하는 프로그램을 작성하라.
출처: https://www.acmicpc.net/problem/2661
      https://sungmin-joo.tistory.com/66
"""

def back_tracking(idx):
    # print(s)
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2*i:-i]: return -1

    if idx == n:
        
        for i in range(n): print(s[i], end = '')
        return 0

    for i in range(1, 4):
        s.append(i)
        if back_tracking(idx + 1) == 0:
            return 0
        s.pop()

if __name__ == "__main__":
    n = int(input())
    s = []
    back_tracking(0)