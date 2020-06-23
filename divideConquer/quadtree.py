def solution(tree):
    return reverse(iter(tree))

def reverse(it):
    current = next(it)
    if current == 'w' or current == 'b':
        return current

    upperLeft = reverse(it)
    upperRight = reverse(it)
    lowerLeft = reverse(it)
    lowerRight = reverse(it)

    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight



def check(result, answer):
    if result == answer:
        return True
    return False

case = ['w', 'xbwwb', 'xbwxwbbwb', 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb']
answer = ['w', 'xwbbw', 'xxbwwbbbw', 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb']

for i in range(4):
    print(check(solution(case[i]), answer[i]))