from sys import stdin

INF = float('inf')


def isWord(string):
    words = set()
    word=""
    original=[]
    flag=False
    for i in string:
        letter = ord(i)
        if  97 <= letter <= 122:
            word+=i
        
        elif word != "":
            flag = True
        
        if flag:
            words.add(word)
            original.append(word)
            word=""
            flag=False

    if word != "":
        original.append(word)
        words.add(word)

    return words,original

def words(comment):
   word=s.lower()
    words,original=isWord(word)
    cant = len(original)
    i=0
    check = {}
    flag = False
    start = i
    save = (0,INF)
    while i < cant:  
        if original[i] in words:
            if check.get(original[i]) == None:
                check[original[i]] = True
        
        if len(check) == len(words):        
            actual = (start,i)
            if save[1] == INF:
                x = actual[0]
                y = actual[1]+1
                save = (x,y)

            if save[1]-save[0] >= actual[1]-actual[0]:
                x = actual[0]
                y = actual[1]+1
                if save[1]-save[0] == actual[1]-actual[0] and save[0] > actual[0]:
                    save = (x,y)
                else:
                    save = (x,y)

            flag = True

        if flag:
            i=start+1
            start=i
            check = {}
            flag = False
        else:
            i+=1
    return save
            
    
    
