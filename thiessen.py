from heapq import heappush, heappop
INF = float('inf')



def build_graph(tree, G):
  if tree.getAuthor() not in G:
    G[tree.getAuthor()] = {}
  ocurrencias = []
  for subcomment in tree.getComments():
    delta = subcomment.getDate() - tree.getDate()
    delta = delta.seconds
    aux = build_graph(subcomment, G)
    aux.append([subcomment.getAuthor(), 0])

    for k in range(len(aux)):
      aux[k][1] += delta
      if not aux[k][0] in G:
        G[aux[k][0]] = {}

      if aux[k][0] != tree.getAuthor():
        if aux[k][0] in G[tree.getAuthor()]:
          G[tree.getAuthor()][aux[k][0]][0] += aux[k][1]
          G[tree.getAuthor()][aux[k][0]][1] += 1
        else:
          G[tree.getAuthor()][aux[k][0]] = [aux[k][1], 1]

        if tree.getAuthor() in G[aux[k][0]]:
          G[aux[k][0]][tree.getAuthor()][0] += aux[k][1]
          G[aux[k][0]][tree.getAuthor()][1] += 1
        else:
          G[aux[k][0]][tree.getAuthor()] = [aux[k][1], 1]

    ocurrencias += aux

  return ocurrencias

def thiessen(tree):
  G = {}
  build_graph(tree, G)
  distribucion = {}
  for node in G:
    if len(G[node]) in distribucion: distribucion[len(G[node])] += 1
    else: distribucion[len(G[node])] = 1
  
  k = INF
  maxima_frecuencia = -INF
  for grado in distribucion:
    if distribucion[grado] > maxima_frecuencia:
      k = min(grado, k)
      maxima_frecuencia = distribucion[grado]
  participacion = tree.getUserByCommentsList()
  centros = {}
  distance = {}
  heap = []
  k = k if k > 2 else 2
  for i in range(len(participacion)):
    if i < k:
      centros[participacion[i][0]] = set()
      heappush(heap, (participacion[i][0], 0))
    distance[participacion[i][0]] = INF

  source = last = ""
  while len(heap):
    u, wi = heappop(heap)
    if wi == 0:
      last, source = source, u
    for v in G[u]:
      acumulado, n = G[u][v]
      promedio = acumulado//n
      if wi + promedio < distance[v]:
        distance[v] = wi + promedio
        heappush(heap, (v, wi + promedio))
        if u not in centros:
          if last != "":
            if u in centros[last]: centros[last].remove(u)
          centros[source].add(u)
  
  for centro in centros:
    print(centro, end=" ")
    print(*centros[centro], end=" ")
    stop = len(centros[centro])
    for vertice in centros[centro]:
      print(distance[vertice], end=" ")
    print()
