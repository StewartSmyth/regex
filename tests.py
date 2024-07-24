from regexparser import regexParse

Tests = [["A","A"], ["A|B",('split', 'A', 'B')],["(A(B|DE)|B)C",('cat', ('split', ('cat', 'A', ('split', 'B', ('cat', 'D', 'E'))), 'B'), 'C')]]


flag = True

for test in Tests:
    parsedRegex = regexParse(test[0])

    if(parsedRegex != test[1]):
        print(f"Test failed, does not match, parsed regex: {parsedRegex} and test regex: {test[1]}")
        flag = False

    else:
        print(f"Test passed, does match, parsed regex: {parsedRegex} and test regex: {test[1]}")

if flag == True:
    print("---ALL PASSED---")
else:
    print("---TESTS FAILED---")

