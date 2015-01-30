line = raw_input().split()

a = int(line[0])
b = int(line[1])
result = ""

c = a+b

if c<0:
    c= -c
    sign = "-"
else:
    sign = ""

while c > 999:
    result = ","+str(c%1000) + result
    c = c/1000

result = str(c) + result

print result