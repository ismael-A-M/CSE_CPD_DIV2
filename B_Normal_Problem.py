t=int(input())
for i in range(t):
    s=input().replace("q","P").replace("p","q")
    s=s.lower()
    s=s[::-1]
    print(s)