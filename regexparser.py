#Precidence: (), repeat chars, concatinate, split


def parseSplit(r,i):
    #parse left side of split first
    i, left = parseConcatination(r,i)
    
    while i<len(r): #if length at the end of left side of split is less than 
        
        if r[i] == ')':
            #must be end of regex or of this subrexex in regex
            break
        
        assert r[i] == '|', f"Bug: {r[i]}, This character should be |" #bug if char inbetween left and right of split is not | 
        i, right = parseConcatination(r,i+1) #parse the right side of the 
        left = ("split", left, right)
    return i,left

def parseConcatination(r,i):
    concatExp = None
    while i<len(r):
        if r[i] in "|)":
            break #break back to split as it is no longer concatinated
        i, node = parseNode(r,i)
        if concatExp is None:
            concatExp = node
        else:
            concatExp = ("concatinate", concatExp, node)
    return i, concatExp

def parseNode(r,i):

    #currentChar
    ch = r[i]

    i+=1

    #create subexpression when come across a bracket so could go back to lowest precidence Split
    if ch == '(':
        i, node = parseSplit(r,i)
        #if there is no more chars or the next char is not a ) then there is unbalenced brackets
        if i<len(r) and r[i] == ')':
            i+=1
        else:
            
            raise Exception("Unbalenced brackets")


    #dot is wildcard char
    elif ch == '.':
        node = "wild"

    elif ch in "+*":
        raise Exception("Nothing to repeat")

    else:
        node = ch
    
    i, node = parsePostfix(r,i,node)
    return i, node


def parsePostfix(r,i, node):
    #if its not a postfix letter then return
    if i == len(r) or r[i] not in "*+":
        return i, node
    
    #ch is the postfix letter
    ch = r[i]
    i+=1

    #min, max are minimum and maximum amount of times can be repeated
    if ch == '*':
        min, max = 0, float("inf")
    elif ch == '+':
        min, max = 1, float("inf")
    
    node = ("Repeat", node, min, max)
    return i, node
    

#entry point
def regexParse(r):
    #split lowest precidence so start there and deal with other possibilies ontop of that
    i, node = parseSplit(r,0)
    return node

if __name__ == "__main__":
    print("Run via tests or userInput")