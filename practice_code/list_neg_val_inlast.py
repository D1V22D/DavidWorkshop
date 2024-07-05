s = []
n = int(input("ENTER THE RANGE ="))
for i in range(n):
    l =int(input(f"ENTER THE ELEMENT{i} ="))
    s.append(l)
print(s)
for j in range(len(s)):
    if s[j]<0:
        b = s.pop(j+5)
        s.append(b)
print(s)
