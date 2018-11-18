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
    s = comment
    word=s.lower() 
    words,original=isWord(word)
    cant = len(original)
    i=0
    check = {}
    #actual = (i,j)
    start = i
    save = (0,INF)
    while i < cant:  
        if original[i] in words:
            if check.get(original[i]) == None:
                check[original[i]] = True
        
        if i > save[1]:
            i=start+1
            start=i
        
        if len(check) == len(words):
            #update
            actual = (start,i)
            if save[1] == INF:
                x = actual[0]
                y = actual[1]+1
                save = (x,y)
            if save[1]-save[0] > actual[1]-actual[0] and save[0]>=actual[0]:
                x = actual[0]
                y = actual[1]+1
                save = (x,y)
            
            i=start+1
            start=i
            check = {}
            #arreglo
        i+=1
    return save
            
    
    
