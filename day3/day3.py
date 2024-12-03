# thinking this will use regex
import re
with open("input3.txt", 'r') as file:
    lines = file.read()

pattern = r"mul\(([1-9]\d{0,2}),([1-9]\d{0,2})\)|(do\(\))|(don't\(\))"
matches = re.findall(pattern, lines)
#print(matches)

sum = 0
flag = True
for match in matches:
    n1, n2, do, dont = match
    if do == "do()":
        flag = True
    if dont == "don't()":
        flag = False
    if flag and n1 and n2:
        result = int(n1) * int(n2)
        sum += result
print(sum)