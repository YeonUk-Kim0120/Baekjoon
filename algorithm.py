n = int(input())
for i in range(n):
    ans = "YES"
    VPS = input()
    stack = []
    for k in VPS:
        if k == '(':
            stack.append(k)
        else:
            try:
                stack.pop()
            except:
                ans = "NO"
                break
    if len(stack) != 0:
        ans = "NO"
    print(ans)