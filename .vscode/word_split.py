def wordBreak(s, dic):
    # write your code here
    # dic = set(dic)

    if not s:
        return True
    if not dic:
        return False

    arr = [False] * (len(s) + 1)
    arr[0] = True
    maxlen = max([len(d) for d in dic])
    for i in range(1, len(s) + 1):
        for word in dic:
            if i - len(word) >= 0 and arr[
                    i - len(word)] and word == s[i - len(word):i]:
                arr[i] = True
                break
    return arr[-1]


s = "github"
dict = ["git", "gi", "hu", "h", "b"]
print(wordBreak(s, dict))
