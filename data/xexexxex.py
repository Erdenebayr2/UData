with open("urls.txt", "r") as file:
    content = file.read().split("\n")
    s = []
    l = len(content)
for i in range(l):
    s.append(content)
for ii in s:
    print(ii)