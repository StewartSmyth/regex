#need to: implement repeat chars

def firstSecondMatch(i, text, regex) -> tuple[bool, bool, int, int]:
    #first child
    first,second = False,False
    firstIncrement, secondIncrement = 0, 0
    if isinstance(regex[1], str):
        first = matchStr(i, text, regex[1])
        firstIncrement+=1
    else:
        first, firstIncrement = matchRegex(i, text, regex[1])
    i+=firstIncrement
    #second child
    if i >= len(text):
        return first, False, firstIncrement, 0
    if isinstance(regex[2], str):
        second = matchStr(i, text, regex[2])
        secondIncrement+=1
        i+=1
    else:
        second, secondIncrement = matchRegex(i, text, regex[2])
    i += secondIncrement
    return first,second,firstIncrement,secondIncrement




def matchRegex(i:int , text: str, regex: tuple) -> bool | tuple[bool, int]:
    # in instance that original call is a character node
    if isinstance(regex, str):
        return matchStr(i, text, regex), 0
    if i == len(text):
        return True, 0
    

    firstElement = regex[0]
    

    if firstElement == "concatinate":
        first, second, firstIncrement, secondIncrement = firstSecondMatch(i, text, regex)
        if first and second:
            return True, firstIncrement+secondIncrement
        else:
            return False, 0

    #split requires to create multiple solutions 
    if firstElement == "split":
        first, second, firstIncrement, secondIncrement = firstSecondMatch(i, text, regex)
        if first:
            return True, firstIncrement
        elif second:
            return True, secondIncrement
        else:
            return False, 0

    return False,0
        


def matchStr(i:int, text:str, char: str) -> bool:
    if text[i] == char:
        return True
    else:
        return False



def regexMatch(text: str, regex:tuple):
    acceptable, integer = matchRegex(0, text, regex)
    if acceptable:
        print("Regex matches text")
        return True
    else:
        print("Regex does not match text")
        return False



if __name__ == "__main__":
    regexMatch("a", "ab|acd")
