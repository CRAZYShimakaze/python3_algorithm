def wordSplit(s, dic):
    # write your code here
    # dic = set(dic)
    if s == '':
        return True
    if dic == None:
        return False
    answer = [False] * (len(s) + 1)
    answer[0] = True
    for i in range(1, len(s)+1):
        for item in dict:
            if i - len(item) >= 0 and answer[i - len(item)] and item == s[i-len(item):i]:
                answer[i] = True
                break
    return answer[-1]


s = "github"
dict = ["git", "gi", "hu", "h", "b"]
print(wordSplit(s, dict))
