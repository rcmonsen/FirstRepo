#This code returns the percent similarity between two user-entered strings

def percentDiff(string1, string2):
    import difflib

    set1=[]
    set2=[]

    for i in string1:
        set1.append(i)
    for l in string2:
        set2.append(l)
    ratio = round(difflib.SequenceMatcher(None, set1, set2).ratio()*100, 2)
    
    return ratio

