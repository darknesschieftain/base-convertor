def menu():
    print("--------------------------------------------------------------------------")
    print("|1- convert decimal to binary and hexadecimal and octal                  |")
    print("|2- convert binary to decimal                                            |")
    print("|3- hexadecimal to decimal                                               |")
    print("|4- convert octal to decimal                                             |")
    print("|5- decimal to ascii(character)                                          |")
    print("--------------------------------------------------------------------------")
    print("|created by darkness chieftain                                           |")
    print("|convertor of hexadecimal and decimal and octal and binary and characters|")
    print("--------------------------------------------------------------------------")
menu()
select = input("please select = ")



def convert_decimal_to_others(string,string_length):
    for i in range(0,string_length):
        string = list(string)
        strchr = string[i]
        string[i] = int(string[i])
        binary = bin(string[i])
        hexadecimal = hex(string[i])
        octal = oct(string[i])
        print("--------------------------------------------------------------------------")
        print("string character is = " + strchr + " binary code is = " + binary)
        print("--------------------------------------------------------------------------")
        print("string character is = " + strchr + " hexadecimal code is = " + hexadecimal)
        print("--------------------------------------------------------------------------")
        print("string character is = " + strchr + " octal code is = " + octal)
        print("--------------------------------------------------------------------------")
def binary_to_decimal(string,string_length):
    string = list(string)
    value = 0
    for i in range(0,string_length):
        value = value + pow(2, i)
        if (i == string_length-1):
            print("The decimal value of the number is = ", value)
def hexadecimal_to_decimal(string):
    strd = string.split(":")
    strd_length = len(strd)
    for i in range(0,strd_length):
        strdp = strd[i]
        strd[i] = int(str(strd[i]), 16) 
        print("hexadecimal is = "+ str(strdp))
        print(" decimal is = " + str(strd[i]))
def octal_to_decimal(string):
    stringlst = string.split(":")
    stringlstl = len(stringlst)
    for i in range(0, stringlstl):
        octald = int(stringlst[i], 8)
        print("octal code is = " + stringlst[i] + " decimal is = " + str(octald))
def decimal_to_ascii(string):
    stringlst = str(string).split(":")
    stringlstl = len(stringlst)
    for i in range(0, stringlstl):
        asciii = chr(int(stringlst[i], 10))
        print("decimal code is = " + stringlst[i] + " character is = " + str(asciii))


if (select == '1'):
    string = input("please enter your string  = ")
    string_length = len(string)
    convert_decimal_to_other(string,string_length)
if (select == '2'):
    string = input("please enter your string  = ")
    string_length = len(string)
    binary_to_decimal(string,string_length)
if (select == '3'):
    string = input("please enter your string  = ")
    string_length = len(string)    
    hexadecimal_to_decimal(string)
if (select == '4'):
    string = input("please enter your string (example = 76:54:)  = ")
    string_length = len(string)
    octal_to_decimal(string)
    
if (select == '5'):
    string = input("please enter your string  = ")
    string_length = len(string)        
    decimal_to_ascii(string)