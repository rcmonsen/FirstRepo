#This code returns the percent similarity between two user-entered strings

def percentDiff(string1, string2):
    import difflib

    set1=[]
    set2=[]

    for i in string1:
        set1.append(i)
    #print(set1)

    for l in string2:
        set2.append(l)
    #print(set2)
        
    ratio = round(difflib.SequenceMatcher(None, set1, set2).ratio()*100, 2)
    #print("The strings are %",ratio," similar.")
    return ratio

