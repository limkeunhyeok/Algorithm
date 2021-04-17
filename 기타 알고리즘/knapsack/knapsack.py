def knapsack(items, k):
    answer = [0] * (k + 1)
    for i in range(len(items)):
        for j in range(k, 1, -1):
            if items[i][0] <= j:
                answer[j] = max(answer[j], answer[j - items[i][0]] + items[i][1])
    return answer[-1]

items = [[6, 13], [4, 8], [3, 6], [5, 12]] # 각 물건의 무게 및 가치
k = 7 # 배낭이 버틸 수 있는 무게
print(knapsack(items, k))