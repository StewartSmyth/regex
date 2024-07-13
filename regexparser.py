#### r is regex and i is the current position

def parseSplit(r,i):
    i, left = parseConcat(r,i)
    while i<len(r):
        if r[i] == ')':
            break
        assert r[i] == '|', 'BUG'
        i, right = parseConcat(r,i+1)
        left = ('split', left, right)
    return i,left

def parseConcat(r,i):
    left = None
    while i<len(r):
        if r[i] in "|)":
            break
        i, node = parseNode(r,i)
        if left is None:
            left = node
        else:
            left = ('cat', left, node)
    return i, left

def parseNode(r,i):
    ch = r[i]
    i+=1
    if ch == '(':
        i, node = parseSplit(r,i)
        if i<len(r) and r[i] == ')':
            i+=1
        else:
            raise Exception("Unbalenced brackets")
        
    elif ch in "+*":
        raise Exception("Nothing to repeat")

    else:
        node = ch
    
    i, node = parsePostfix(r,i,node)
    return i, node


def parsePostfix(r,i, node):
    if i == len(r) or r[i] not in "*+":
        return i, node
    
    ch = r[i]
    i+=1

    #rmin, rmax are minimum and maximum amount of times can be repeated
    if ch == "*":
        rmin, rmax = 0,float("inf")
    elif ch == "+":
        rmin, rmax == 1, float("inf")
    else:
        raise Exception("Shouldn't be here")
    
    node = ("Repeat", node, rmin, rmax)
    return i, node
    

def regexParse(r):
    i, node = parseSplit(r,0)
    return node

if __name__ == "__Main__":
    print("Hi")