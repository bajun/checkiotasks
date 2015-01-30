import re
def checkio(text):
    new = re.sub(r'[^a-zA-Z]', '', text.lower())
    result = {}
    for l in sorted(new):
        if l in result:
            result[str(l)] += 1
        else:
            result[str(l)] = 1
    if(sum(result.values()) == len(result)):
        return sorted(new)[0]
    else:
        return max(result,key=result.get)
    