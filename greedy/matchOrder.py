def matchOrder(length, russian, korean):
    answer = 0
    russian = sorted(russian, reverse = True)
    korean = sorted(korean)
    
    for i in range(length):
        if russian[i] > korean  [-1]:
            continue
        else:
            korean.pop()
            answer += 1
    return answer