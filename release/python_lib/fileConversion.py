HORIZON = 26
VIRTICAL = 10

def fileConvert(file_add, braille_file):
    file = open(file_add, "r")
    braille = file.read()
    file.close()

    braille_l = braille.split()
    line1 = ''
    line2 = ''
    line3 = ''
    cell_line = []
    page = []
    line_counter = 0
    for word in braille_l:
        if (line_counter + len(word)//6+1) >= HORIZON:
            while (len(line1) < HORIZON*2):
                line1 += "00"
                line2 += "00"
                line3 += "00"
			    
            cell_line.append(line1[::-1])
            cell_line.append(line2[::-1])
            cell_line.append(line3[::-1])
            page.append(cell_line)
            line_counter = 0
            cell_line = []
            line1 = ''
            line2 = ''
            line3 = ''
        L1, L2, L3 = consLine(word)
        line1 = line1 + L1 + '00'
        line2 = line2 + L2 + '00'
        line3 = line3 + L3 + '00'
        line_counter += (len(word)//6 + 1)
    while (len(line1) < HORIZON*2):
        line1 += "00"
        line2 += "00"
        line3 += "00"
    cell_line.append(line1[::-1])
    cell_line.append(line2[::-1])
    cell_line.append(line3[::-1])
    print(cell_line)
    page.append(cell_line)
    
    return writeFile(page, braille_file)
    # return page

def consLine(word):
    L1 = []
    L2 = []
    L3 = []
    for i in range(0, len(word), 6):
        cell = word[i:i+6]
        L1.append(cell[0:2])
        L2.append(cell[2:4])
        L3.append(cell[4:6])
    L1 = ''.join(L1)
    L2 = ''.join(L2)
    L3 = ''.join(L3)
    return L1, L2, L3

def writeFile(page, braille_file):
    braille = ""
    for cell_line in page:
        for line in cell_line:
            braille = braille + line + "\n"
    try:
        file = open(braille_file, "w")
        file.write(braille)
        file.close()
        return True
    except:
        return False