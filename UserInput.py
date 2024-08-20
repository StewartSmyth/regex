from regexparser import regexParse
from regexmatcher import regexMatch


inpRegex = input("Input regex: ")

print(f"Regex: {regexParse(inpRegex)}")

inpTextToMatch = input("Input text: ")

regexMatch(inpTextToMatch, inpRegex)

