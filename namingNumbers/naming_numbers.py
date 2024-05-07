''' Program to name the number inputted '''

from namingNumbers.nameout_f import nameout


n = int(input('Enter a number')) # 123456789
# n = 123456789
ns = str(n) # '123456789'
fs = format(n,',d') # '123,456,789'
rev = ns[::-1] # '987654321'
commac = fs.count(',')
# print(commac)
spl = fs.split(',') # split list
# print(spl)
print(fs)
spl = [x.zfill(3) for x in spl]
print(spl)

if commac == 0:
    for no in spl:
        print(nameout(no))
if commac == 1:
    for no in spl:
        if commac == 1:
            outp = nameout(no)+' Thousand'
            print(outp,end='')
            commac -= 1
        else:
            print(nameout(no))
if commac == 2:
    for no in spl:
        if commac == 2:
            outp = nameout(no)+' Million'
            print(outp,end='')
            commac -= 1
        elif commac == 1:
            outp = nameout(no) + ' Thousand'
            print(outp, end='')
            commac -= 1
        else:
            print(nameout(no))
if commac == 3:
    for no in spl:
        if commac == 3:
            outp = nameout(no)+' Billion'
            print(outp,end='')
            commac -= 1
        elif commac == 2:
            outp = nameout(no)+' Million'
            print(outp,end='')
            commac -= 1
        elif commac == 1:
            outp = nameout(no) + ' Thousand'
            print(outp, end='')
            commac -= 1
        else:
            print(nameout(no))
