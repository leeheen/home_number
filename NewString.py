T = int(input())
for i in range(T):
    word = input()
    re_word = word[::-1]
    answer = word+re_word
    if word == re_word:
        print(word)
        continue
    for j in range(len(word)):
        a=word[j:]
        b=re_word[:len(word)-j]
        if a == b:
            if len(answer) > len(word + re_word[len(word)-j:]):
                answer = word + re_word[len(word)-j:]
    print(answer)