import nltk

intr = open("intr.txt").readlines()

code = []

curindex = 0
while intr[curindex] != "end of code\n":
    code.append(intr[curindex])
    curindex += 1

curindex += 1
litTab = nltk.word_tokenize(intr[curindex])
print(litTab)

curindex += 1
litAdr = nltk.word_tokenize(intr[curindex])
print(litAdr)

curindex += 1
symTab = nltk.word_tokenize(intr[curindex])
print(symTab)

curindex += 1
symAdr = nltk.word_tokenize(intr[curindex])
print(symAdr)

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

reg = ["R1","R2","R3","R4","R5"]
tokens = []
for line in code:
    linetoken = nltk.word_tokenize(line)
    linetoken.append("\n")
    tokens.extend(linetoken)

print(tokens)

macFile = open("machine.txt","w")
previous = tokens[0]
comand = ""
for token in tokens:
    if comand == "" and is_integer(token):
        comand += token + ") " 

    if "_" in token:
        comand += "_ "

    if previous == "_" and is_integer(token):
        comand += token + " "
    
    if "AD" in token or "IS" in token or "C" in token:
        temp = ""
        for i in token:
            temp += i
            if i == ",":
                temp = ""
        
        temp += " "
        comand += temp

    if token in reg:
        index = reg.index(token) + 1
        comand += str(index) + " "

    if "L" in token: 
        temp = ""
        for i in token:
            temp += i
            if i == ",":
                temp = ""
        
        # print("temp ", temp)
        index = int(temp) - 1
        comand += litAdr[index] + " "

    if "S" in token and "IS" not in token: 
        temp = ""
        for i in token:
            temp += i
            if i == ",":
                temp = ""
        
        # print("token ",token)
        index = int(temp) - 1
        # print("S ",index)
        comand += symAdr[index] + " "

    if "\n" in token:
        print(comand)
        comand += "\n"
        macFile.write(comand)
        comand = ""

    previous = token