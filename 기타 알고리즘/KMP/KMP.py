def KMPSearch(pattern, text):
    m = len(pattern)
    n = len(text)

    j = 0 # pattern[] 인덱스
    i = 0 # text[] 인덱스
    
    pi = [0] * m
    getPi(pattern, m, pi)

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
  
        if j == m:
            print("Found pattern at index " + str(i - j))
            j = pi[j - 1]
  
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = pi[j - 1]
            else:
                i += 1
  
def getPi(pattern, m, pi):
    l = 0
    i = 1
  
    while i < m:
        if pattern[i] == pattern[l]:
            l += 1
            pi[i] = l
            i += 1
        else:
            if l != 0:
                l = pi[l - 1]
            else:
                pi[i] = 0
                i += 1
  
t1 = "ABABDABACDABABCABAB"
p1 = "ABABCABAB"
KMPSearch(p1, t1)
# index 10

t2 =  "AABAACAADAABAABA"
p2 =  "AABA"
KMPSearch(p2, t2)
# index 0
# index 9
# index 12
