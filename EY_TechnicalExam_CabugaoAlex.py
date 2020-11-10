# 1.BracketValidator
def validateBracket (bracketString):
    # bracketString = "{ [ ] ( ) }"
    # bracketString = "{ [ ( ] ) }"
    # bracketString = "{ [ }"
    
    openersList = ('{', '[', '(',)
    closerList = ('}', ']', ')')
    pairList = (('{','}'),
                ('[',']'),
                ('(',')'),)
    
    # Remove spaces
    bracketStringNoSpaces = bracketString.replace(" ","")
    # Convert to list
    bracketList = []
    bracketList = bracketStringNoSpaces
    
    # Utilize stack
    bracketStack = []
    for b in bracketList:
        if b in closerList:
            top = bracketStack.pop()
            bracketIdx = closerList.index(b)
            # Check if pairing is correct
            if b in pairList[bracketIdx] and top in pairList[bracketIdx]:
                continue
            else:
                print(top + b)
                return False
        else:
            bracketStack.append(b)
    
    if len(bracketStack) == 0: 
        return True
    else:
        return False

# 2. Reverse Words 
def reverse_words (message):
    # message = ['c','a','k','e',' ',
    #             'p','o','u','n','d', ' ',
    #             's', 't', 'e', 'a', 'l']
    
    outString = ""

    # Make string from characters then split to words
    outString = outString.join(message)
    outString = outString.split()

    # Reverse list
    outString.reverse()
    
    return outString

# 3. Camel to Snake Case
import re

def convert_to_snake_case (message):
    # message = "ThisIsAwesome"

    # Utilize sub function
    messageSnakeCase = re.sub(r'(?<!^)(?=[A-Z])', '_', message).lower()
    
    return messageSnakeCase
