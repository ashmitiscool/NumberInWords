def nameout(s):
    # Names out the 3 number word (s) eg s = '123'
    first = s[0]
    # print(first)
    outl = list()
    if s == '1':
        outl.append(' One')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '2':
        outl.append(' Two')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '3':
        outl.append(' Three')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '4':
        outl.append(' Four')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '5':
        outl.append(' Five')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '6':
        outl.append(' Six')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '7':
        outl.append(' Seven')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '8':
        outl.append(' Eight')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)
    elif s == '9':
        outl.append(' Nine')
        outp = ''.join(outl)
        outp = outp.title()
        return(outp)

    ## First digit
    elif first == '1':
        outl.append(' One hundred')
    elif first == '2':
        outl.append(' Two hundred')
    elif first == '3':
        outl.append(' Three hundred')
    elif first == '4':
        outl.append(' Four hundred')
    elif first == '5':
        outl.append(' Five hundred')
    elif first == '6':
        outl.append(' Six hundred')
    elif first == '7':
        outl.append(' Seven hundred')
    elif first == '8':
        outl.append(' Eight hundred')
    elif first == '9':
        outl.append(' Nine hundred')

    sec2 = s[1:] # Second two numbers in the group of 3 numbers
    # print(sec2)
    if sec2 == '01':
        outl.append(' One')
    elif sec2 == '02':
        outl.append(' Two')
    elif sec2 == '03':
        outl.append(' Three')
    elif sec2 == '04':
        outl.append(' Four')
    elif sec2 == '05':
        outl.append(' Five')
    elif sec2 == '06':
        outl.append(' Six')
    elif sec2 == '07':
        outl.append(' Seven')
    elif sec2 == '08':
        outl.append(' Eight')
    elif sec2 == '09':
        outl.append(' Nine')


    ## Unique two digit names
    elif sec2 == '10':
        outl.append(' Ten')
    elif sec2 == '11':
        outl.append(' Eleven')
    elif sec2 == '12':
        outl.append(' Twelve')
    elif sec2 == '13':
        outl.append(' Thirteen')
    elif sec2 == '14':
        outl.append(' Fourteen')
    elif sec2 == '15':
        outl.append(' Fifteen')
    elif sec2 == '16':
        outl.append(' Sixteen')
    elif sec2 == '17':
        outl.append(' Seventeen')
    elif sec2 == '18':
        outl.append(' Eighteen')
    elif sec2 == '19':
        outl.append(' Nineteen')

    ## Non unique two digit names
    elif sec2[0] == '2': # sec2[0] - 2nd digit in the group of 3 digits
        outl.append(' Twenty')
        singledig(sec2[1], outl)
    elif sec2[0] == '3':
        outl.append(' Thirty')
        singledig(sec2[1], outl)
    elif sec2[0] == '4':
        outl.append(' Forty')
        singledig(sec2[1], outl)
    elif sec2[0] == '5':
        outl.append(' Fifty')
        singledig(sec2[1], outl)
    elif sec2[0] == '6':
        outl.append(' Sixty')
        singledig(sec2[1], outl)
    elif sec2[0] == '7':
        outl.append(' Seventy')
        singledig(sec2[1], outl)
    elif sec2[0] == '8':
        outl.append(' Eighty')
        singledig(sec2[1], outl)
    elif sec2[0] == '9':
        outl.append(' Ninety')
        singledig(sec2[1], outl)



    outp = ''.join(outl)
    outp = outp.title()
    return(outp)

def singledig(d,l): # after printing the 2nd digit's word, to print the last digit's word
    if d == '1':
        l.append(' One')
    elif d == '2':
        l.append(' Two')
    elif d == '3':
        l.append(' Three')
    elif d == '4':
        l.append(' Four')
    elif d == '5':
        l.append(' Five')
    elif d == '6':
        l.append(' Six')
    elif d == '7':
        l.append(' Seven')
    elif d == '8':
        l.append(' Eight')
    elif d == '9':
        l.append(' Nine')




if __name__ == '__main__': # Inside this block the code which can run only when directly executed, not from import
    inp = int(input('Enter a number (3 digit)'))
    x = str(inp)
    print(x)
    print(nameout(x))