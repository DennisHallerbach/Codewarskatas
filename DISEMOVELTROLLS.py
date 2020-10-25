def disemvowel(string):
    tmp = ""
    for ch in string :
        if (ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A'
       and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U'):

              tmp += ch      
    return tmp

print(disemvowel("TAest"))