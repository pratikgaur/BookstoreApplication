import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def defination(word):
    if word in data:
        return data[word]
    elif word.title() in data:            #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]         #if user entered "usa" this will check for "USA" as well.
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
        userResponse = input("Y or N ?")
        if userResponse.upper() =="Y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Word doesn't exist! Please double check."
    else:
        return "Word doesn't exists! Please double check."

inputWord = input("Search Word:")
output = defination(inputWord.lower())
if isinstance(output,list):
    print("\n".join(output))
else:
    print(output)