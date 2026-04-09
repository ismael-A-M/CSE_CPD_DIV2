t=int(input())
s=input()
s=s.upper()
if len(set(s))==26:
    print("YES")
else:
    print("NO")