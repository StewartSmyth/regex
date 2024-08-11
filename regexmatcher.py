#at each new node: 


def matchRegex(i:int , text: str, regex: tuple) -> bool:
    # in instance that origional call is a character node
    if isinstance(regex, str):
        return matchStr(i, text, regex)
    if i == len(text):
        return True
    firstElement = regex[0]
    # check that the regex is a tuple
    if len(firstElement) != 1 and firstElement != "wild":
        #check whether each child regex is a character or a node
        #go into either match depending on what it is
        #store whether it is true or false
        first = False
        second = False
        #first child
        
        if isinstance(regex[1], str):
            first = matchStr(i, text, regex[1])
        else:
            first = matchRegex(i, text, regex[1])

        #if first child of split is true then we can ignore second child
        if firstElement == "split" and first:
            return True
        if firstElement == "concatinate":
            i+=1
        
        #second child
        if isinstance(regex[2], str):
            second = matchStr(i, text, regex[2])
            i+=1
        else:
            second = matchRegex(i, text, regex[2])
        
        #already checked first child in occasion of split so only need to check second child
        if firstElement == "split" and second:
            return True
        
        #for concatinate both children need to be true
        print("here")
        if firstElement == "concatinate" and first and second:

            return True


def matchStr(i:int, text:str, char: str) -> bool:
    print(i, text)
    if text[i] == char:
        
        return True
    else:
        return False

    






def regexMatch(text, regex):
    acceptable = matchRegex(0,text, regex)
    if acceptable:
        print("Regex matches text")
        return True
    else:
        print("Regex does not match text")
        return False



if __name__ == "__main__":
    
    regexMatch("B",("split", 'A', 'B'))
