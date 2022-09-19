s = 'spam'
for i in range(len(s)):
    print(s[1:])
    print(s[:1])
    s = s[1:] + s[:1]

    print(s)