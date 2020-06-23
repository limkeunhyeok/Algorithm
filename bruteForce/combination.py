def comb1(arr, k):
    answer = []
    if k > len(arr):
        return answer
    
    if k == 1:
        for i in arr:
            answer.append([i])
    else:
        for i in range(len(arr) - k + 1):
            for temp in comb1(arr[i + 1:], k - 1):
                answer.append([arr[i]] + temp)
    return answer

def comb2(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield arr[i]
        else:
            for j in comb2(arr[i + 1:len(arr)], k - 1):
                yield arr[i] + j



print(comb1([1, 2, 3, 4, 5], 3))
print(list(comb2(['1', '2', '3', '4', '5'], 3)))
