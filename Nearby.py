import math
T,Q,N  = [int(x) for x in raw_input().split(" ")]

class Topic:
    def __init__ (self, ID, xloc=0, yloc=0):
        self.ID = int(ID)
        self.x = float(xloc)
        self.y = float(yloc)
     #   self.assocQueries = []

    def __repr__(self):
        return str(self.ID) + ": (" + str(self.x) + ", " + str(self.y) + ") "

    def __eq__(self, other):
        if not isinstance(other, Topic): raise NotImplementedError
        return self.ID == other.ID

topicList = []

while T:
    T = T-1
    [idd,x,y] = raw_input().split(" ")
    topicList.append(Topic(idd, x, y))


class Query:
    def __init__(self, input_string):
        rQ = input_string.split(" ",2)
        self.ID = int(rQ[0])
        self.Qn = int(rQ[1])
        self.topics = []
        if self.Qn:
            self.topics.extend(int(x) for x in rQ[2].split(" "))

        #for x in self.topics:
        #    indX = topicList.index(Topic(x))
        #    if not topicList[indX].assocQueries.count(self.ID): topicList[indX].assocQueries.append(self.ID)



    def __repr__(self):
        return str(self.ID) + ": " + str(self.topics)

class Result:
    def __init__(self, ID):
        self.ID = ID


queryList = []

while Q:
    Q = Q-1
    queryList.append(Query(raw_input()))

nonZeroQL = []
for x in queryList:
    if x.Qn: nonZeroQL.append(x)

class topicDist:
    def __init__(self, ID, dist=0):
        self.ID = ID
        self.dist = dist

    def __repr__(self):
        return str(self.ID) + ": " + str(self.dist)

    def __eq__(self, other):
        if not isinstance(other, topicDist): raise NotImplementedError
        return self.ID == other.ID

def distComp(a,b):
    if abs(a-b) < 0.01: return 0
    if a>b: return 1
    return -1

def topicSearch(xloc, yloc, limit, tList=topicList):
    tDistList = []
    for x in tList:
        tDistList.append(topicDist(x.ID,math.sqrt(math.pow(x.x-xloc,2.0)+math.pow(x.y-yloc,2.0))))
    tDistList.sort(key=lambda k: k.ID, reverse=True)
    tDistList.sort(cmp=distComp,key=lambda k: k.dist)
    return tDistList[0:limit]

class queryDist:
    def __init__(self,query,xloc=0,yloc=0):
        self.ID = query.ID
        topics = []
        for record in query.topics:
           idx = topicList.index(Topic(record))
           topics.append(topicList[idx])
        self.dist = topicSearch(xloc,yloc,1,topics)[0].dist

    def __repr__(self):
        return str(self.ID) + ": " + str(self.dist)

    def __eq__(self, other):
        if not isinstance(other, queryDist): raise NotImplementedError
        return self.ID == other.ID

def querySearch(xloc, yloc, limit):
    if not limit: return;
    #topicsByDist = topicSearch(xloc,yloc,len(topicList))
    if limit > len(nonZeroQL): limit = len(nonZeroQL)
    qDistList = []
    for record in nonZeroQL:
        qDistList.append(queryDist(record,xloc,yloc))

    qDistList.sort(key=lambda k: k.ID, reverse=True)
    qDistList.sort(key=lambda k: k.dist)

    return qDistList[0:limit]

while N:
    N -= 1
    queryType,limit,xloc,yloc = raw_input().split(" ")
    if queryType == 't': print ' '.join(str(y) for y in [x.ID for x in topicSearch(float(xloc),float(yloc),int(limit))])
    elif queryType == 'q' : print ' '.join(str(y) for y in [x.ID for x in querySearch(float(xloc),float(yloc),int(limit))])
    else: print ("Can't process search. Search type must be 'q' or 't'.")

