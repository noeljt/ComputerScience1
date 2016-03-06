from copy import deepcopy

def open_file(f):
    f1 = open(f).read().strip()
    fl = f1.split('\n')
    letters = {}
    del fl[0]
    i = 0
    for line in fl:
        if i%8 == 0:
            temp = line.split()
            if temp[0] == '32':
                temp[1] = " "
                del temp[2]
            temp[1] = temp[1].replace("'","")
            if temp[0] == '39':
                temp[1] = "'"
            letters[temp[1]] = []
        else:
            letters[temp[1]].append(line)
        i += 1
    return letters

def display_sentence(s,letters,f,b):
    if f == '':
        f = '#'
    if b == '':
        b = '.'
    s = list(s)
    line1,line2,line3,line4,line5,line6,line7,line8 = "","","","","","","",""
    for char in s:
        i = 1
        for line in letters[char]:
            if i == 1:
                line1 += line
            elif i == 2:
                line2 += line
            elif i == 3:
                line3 += line
            elif i == 4:
                line4 += line
            elif i == 5:
                line5 += line
            elif i == 6:
                line6 += line
            elif i == 7:
                line7 += line
            elif i == 8:
                line8 += line
            i += 1
            
    line1 = line1.replace('#',f).replace('.',b)
    line2 = line2.replace('#',f).replace('.',b)
    line3 = line3.replace('#',f).replace('.',b)
    line4 = line4.replace('#',f).replace('.',b)
    line5 = line5.replace('#',f).replace('.',b)
    line6 = line6.replace('#',f).replace('.',b)
    line7 = line7.replace('#',f).replace('.',b)
    line8 = line8.replace('#',f).replace('.',b)
    
    print line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+\
          line7+'\n'+line8

def kerning(letters):
    kerned = deepcopy(letters)
    for char in kerned:
        if char == " ":
            continue
        kern_front = False
        kern_back = False
        for line in kerned[char]:
            if line[0] == "#":
                kern_front = True
            if line[-1] == "#":
                kern_back = True
                    
        if kern_front == True:
            for i in range(len(kerned[char])):
                kerned[char][i] = '.' + kerned[char][i]                    
                    
        if kern_back == True:
            for i in range(len(kerned[char])):
                kerned[char][i] += '.'
        elif kern_back == False:
            remove_end = -1000
            for line in kerned[char]:
                found = False
                for i in range(2,len(line)):
                    if line[-i] == '#':
                        found = True
                        if -i > remove_end:
                            remove_end = -i
                    if found == True:
                        break
            for i in range(len(kerned[char])):
                if remove_end != -2:
                    kerned[char][i] = kerned[char][i][0:remove_end+2]        
                
    return kerned
            
                


if __name__ == '__main__':
    letters = open_file('simple_font.txt')
    kerned = kerning(letters)
    message = raw_input('Please enter the message ==> ')
    print message
    back = raw_input('Please enter the background char (blank for .) ==> ')
    print back
    fore = raw_input('Please enter the foreground char (enter for #) ==> ')
    print fore
    print "No kerning"
    display_sentence(message,letters,fore,back)
    print "With kerning"
    display_sentence(message,kerned,fore,back)
    #when input empty replaces . and # with blanks!!!