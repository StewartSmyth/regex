#Need to do:
#change firstSecondMatch to indivudual so no copying and makes it actually work
#implement backtracking tree to allow for if there is multiple true options such as if both split return true can do both





#implement backtracking tree
backtrackingTree = []



def firstSecondMatch(i, text, regex) -> tuple[bool, bool]:
    #first child
    first,second = False,False
    if isinstance(regex[1], str):
        first = matchStr(i, text, regex[1])
        i+=1
    else:
        first = matchRegex(i, text, regex[1])
    #second child
    if isinstance(regex[2], str):
        second = matchStr(i, text, regex[2])
        i+=1
    else:
        second = matchRegex(i, text, regex[2])
    return first,second




def matchRegex(i:int , text: str, regex: tuple) -> bool | tuple[bool, int]:
    # in instance that original call is a character node
    if isinstance(regex, str):
        return matchStr(i, text, regex)
    if i == len(text):
        return True
    

    firstElement = regex[0]
    

    #concatinate simple as there is only one case so no backtracking required
    if firstElement == "concatinate":
        first, second = firstSecondMatch(i, text, regex)
        if first and second:
            return True

    #split requires to create multiple solutions 
    if firstElement == "split":
        first, second = firstSecondMatch(i, text, regex)
        if first and second:
            pass #figure it out include backtracking tree
        elif first:
            return True
        elif second:
            return True
        



    # if len(firstElement) != 1 and firstElement != "wild":
    #     #check whether each child regex is a character or a node
    #     #go into either match depending on what it is
    #     #store whether it is true or false
    #     first = False
    #     second = False
    #     #first child
    #     print(i, text, regex)
    #     if isinstance(regex[1], str):
    #         first = matchStr(i, text, regex[1])
    #     else:
    #         first = matchRegex(i, text, regex[1])

    #     i+=1
    #     #if first child of split is true then we can ignore second child

    #     if firstElement == "split" and first:
    #         return True

        
    #     #second child
    #     if isinstance(regex[2], str):
    #         second = matchStr(i, text, regex[2])
    #     else:
    #         second = matchRegex(i, text, regex[2])

    #     i+=1
    #     #already checked first child in occasion of split so only need to check second child
    #     if firstElement == "split" and second:
    #         return True
        

        
    print("HELLO HERE :", regex)
           
        


def matchStr(i:int, text:str, char: str) -> bool:
    print(i, char)
    if text[i] == char:
        return True
    else:
        return False



def regexMatch(text: str, regex:tuple):
    acceptable = matchRegex(0, text, regex)
    if acceptable:
        print("Regex matches text")
        return True
    else:
        print("Regex does not match text")
        return False



if __name__ == "__main__":
    
    regexMatch("ABCDE", ('concatinate', ('concatinate', ('split', ('concatinate', 'A', 'B'), ('concatinate', ('concatinate', 'A', 'B'), 'C')), 'D'), ("split", 'A', 'E')))
