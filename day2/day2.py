safe = 0
lines = open("input2.txt", 'r').readlines()

for line in lines:
    nlist = line.split(" ")
    nlist = [int(x) for x in nlist]
    
    inc = all(i < j for i, j in zip(nlist, nlist[1:]))
    dec = all(i > j for i, j in zip(nlist, nlist[1:]))
    
    valid_diffs = all(1 <= abs(j - i) <= 3 for i, j in zip(nlist, nlist[1:]))
    
    if (inc or dec) and valid_diffs:
        safe += 1
    else:
        for i in range(len(nlist)):
            test = nlist[:i] + nlist[i+1:]
            inc = all(i < j for i, j in zip(test, test[1:]))
            dec = all(i > j for i, j in zip(test, test[1:]))
            valid_diffs = all(1 <= abs(j - i) <= 3 for i, j in zip(test, test[1:]))
            if (inc or dec) and valid_diffs:
                safe += 1
                break


print(safe)
