from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

class Tree:
  def __init__(self, comment_id="", body="", author="", ups=0, downs=0, date="", parent=None, lvl=0):
    self.__comment_id = comment_id
    self.__body = body
    self.__author = author
    self.__ups = ups
    self.__downs = downs
    self.__date = date
    self.__comments = []
    self.__parent = parent
    self.__lvl = lvl

  def preorder(self):
    ans = "{}".format(self.__comment_id)
    for comment in self.__comments:
      ans += " {}".format(comment.preorder())
    return ans

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

  def setUps(self, ups):
    self.__ups = ups

  def getDowns(self):
    return self.__downs

  def setDowns(self, downs):
    self.__downs = downs

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
  print(foro.preorder())

build()
