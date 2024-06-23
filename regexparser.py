#### r is regex and i is the current position
#### 

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

    elif ch == '.':
        node = "dot"
    else:
        node = ch
    
    return i, node


def parsePostfix(r,i):
    pass
    #TODO

def regexParse(r):
    i, node = parseSplit(r,0)
    return node



print(regexParse("(A(B|DE)|B)C"))






