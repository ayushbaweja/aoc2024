lines = open("input1.txt", 'r').readlines()
#print(lines)
col1, col2 = [], []
for line in lines:
    col1.append(line.strip().split()[0])
    col2.append(line.strip().split()[1])
col1.sort()
col2.sort()
sum = 0
for i in range(len(col1)):
    sum += abs(int(col1[i]) - int(col2[i]))
print(sum)

sim = 0
col1int = [int(x) for x in col1]
col2int = [int(x) for x in col2]
for n in col1int:
    print(col2int.count(int(n)))
    sim += n*col2int.count(n)
print(sim)