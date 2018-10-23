from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

class Tree:
  def __init__(self, comment_id="", body="", author="", ups=0, downs=0, date="", parent=None, lvl=0, totUp=0, totDown=0):
    self.__comment_id = comment_id
    self.__body = body
    self.__author = author
    self.__ups = ups
    self.__downs = downs
    self.__date = date
    self.__comments = []
    self.__parent = parent
    self.__lvl = lvl
    self.__totUp = totUp
    self.__totDown = totDown


  def preorder(self):
    ans = "{}".format(self.__comment_id)
    for comment in self.__comments:
      ans += " {}".format(comment.preorder())
    return ans

  
  def dfs(self):
    stack = [self]
    path=[]
    x=0
    while stack: 
      vertex = stack.pop()
      path.append(vertex)
      x=0
      for i in range(len(vertex.__comments)):
        #path[x].__totUp += vertex.__comments[i].__ups
        stack.append(vertex.__comments[i])
        x=i
      if len(stack) > 0:
        flag = False
        while vertex.getLvl() + 2 != stack[x].getLvl():
          flag=True
          past = vertex
          vertex = vertex.getParent()
          vertex.setSubUp(past.getSubUp())
      else:
        while vertex.getLvl() != 0:
          flag=True
          past = vertex
          vertex = vertex.getParent()
          print("parent",vertex, past.getUps())
          vertex.setSubUp(past.getSubUp())

      x+=1
    #print(path)
    for i in path:
      print(i.__totUp)
  
  def getParent(self):
    return self.__parent

  def setParent(self, parent):
    self.__parent = parent

  def getLvl(self):
    return self.__lvl

  def setLvl(self, lvl):
    self.__lvl = lvl

  def addComment(self, comment):
    self.__comments.append(comment)
    comment.setParent(self)

  def getBody(self):
    return self.__body

  def setBody(self, text):
    self.__body = text

  def getId(self):
    return self.__comment_id

  def setId(self, comment_id):
    self.__comment_id = comment_id

  def getAuthor(self):
    return self.__author

  def setAuthor(self, author):
    self.__author = author

  def getUps(self):
    return self.__ups


   #agregue upVotes
  def setUps(self, ups):
    self.__ups = ups
    self.__totUp = ups
  
  def getDowns(self):
    return self.__downs

    #agregue upVotes
  def setDowns(self, downs):
    self.__downs = downs
    self.__totDown = downs
    
  def setSubUp(self, votes):
    self.__totUp += votes

  def getSubUp(self):
    return self.__totUp

  def setSubDown(self, votes):
    self.__totDown += votes

  def getSubDown(self):
    return self.__totDown

  def getDate(self):
    return self.__date

  def setDate(self, date):
    self.__date = date

def build():
  line = stdin.readline().strip()
  foro = Tree()
  index = foro
  while len(line):
    I = 0

    temp = Tree()
    while line[I] != '>':
      I += 1
    temp.setLvl(I)
    d = I+1
    while line[d] != '[':
      d += 1
    temp.setBody(line[I+1:d])
    j = d+1
    while line[j] != '|':
      j += 1
    temp.setAuthor(line[d+1:j])
    z = j+1
    while line[z] != '|':
      z += 1
    temp.setUps(int(line[j+1:z]))
    x = z+1
    while line[x] != '|':
      x += 1
    temp.setDowns(int(line[z+1:x]))
    y = x+1
    while line[y] != '|':
      y += 1  
    temp.setId(line[x+1:y])
    w = y+1
    while line[w] != ']':
      w += 1
    temp.setDate(line[w+1:w])
    
    if temp.getLvl() > index.getLvl():
      index.addComment(temp)
     
    else:
      if temp.getLvl() != 0:
        while index.getLvl() + 2 != temp.getLvl():
          index = index.getParent()
        index.addComment(temp)
      else:
        foro = temp
    index = temp

    line = stdin.readline().strip()
  
  #foro.printF()
  foro.dfs()
  #print(foro.preorder())
  #print(foro.comments)

build()
