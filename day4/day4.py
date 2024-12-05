import re
with open("input4.txt", 'r') as f:
    lines = f.readlines()
    count = 0

    # left to right
    pat1 = r"XMAS"
    for line in lines:
        matches = re.findall(pat1, line)
        count += len(matches)
    # right to left
    pat2 = r"SAMX"
    for line in lines:
        matches = re.findall(pat2, line)
        count += len(matches)


    # top to bottom
    rows = len(lines)
    cols = len(lines[0])
    word_len = 4

    for col in range(cols):
        for row in range(rows-word_len+1):
            #extract vertical word
            word = "".join(lines[row+i][col] for i in range(word_len))
            if word == "XMAS":
                count+=1
    # bottom to top
            if word == "SAMX":
                count+=1
    # diagonal left to right
    for col in range(cols-word_len+1):
        for row in range(rows-word_len+1):
            word = "".join(lines[row+i][col+i] for i in range(word_len))
            if word == "XMAS":
                count+=1
            if word == "SAMX":
                count+=1
    # diagonal right to left
    for col in range(cols - word_len + 1):
        for row in range(word_len - 1, rows):
            word = "".join(lines[row-i][col+i] for i in range(word_len))
            if word == "XMAS" or word=="SAMX":
                count += 1
    # overlap? should just double count reuses
    
    # diagonal mas or sam on same a
    # check for left to right mas/sam then check top right and top left
    xmascount = 0
    for col in range(cols-2):
        for row in range(rows-2):
            diag1 = "".join(lines[row+i][col+i] for i in range(3))
            if diag1 in ["MAS", "SAM"]:
                diag2 = "".join([lines[row][col+2], lines[row+1][col+1], lines[row+2][col]])
                if diag2 in ["MAS", "SAM"]:
                    xmascount += 1
    print(count)
    print(xmascount)