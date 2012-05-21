#My submission to interviewstreet.com 'Liars' problem.
#Currently passes 4 of 12 test cases.
__author__ = 'laura'
import itertools, sys

binomial = {}
liars = set()

def countcombos(n,r):
    if not 0<=r<=n : return 0
    if r == n or r == 0: return 1
    if r == 1 or r == n-1: return n
    if n < 2*r: return countcombos(n,n-r)
    key = n,r
    if key in binomial: return binomial[key]
    binomial[key] = countcombos(n-1,r)+countcombos(n-1,r-1)
    return binomial[key]

def updateliars(info, l):
    temp = set()
    global liars
    for x in liars:
        cert = tuple(itertools.ifilter(lambda y: y in info,x[0]))
        if l - len(cert)>=0:
            combos = itertools.combinations(filter(lambda y: y in info,x[1]),l - len(cert))
            for y in combos:
                theseliars = frozenset(tuple(x[0]) + y)
                temp.add((theseliars,x[1]-info))
            liars=temp

input=sys.stdin.readlines()
N,M = [int(x) for x in input.pop(0).strip().split()]

liars = {(frozenset(), frozenset(range(1, N + 1)))}
readme = M
info = []
while len(input):
    A,B,C = input.pop().strip().split()
    info.append((frozenset(range(int(A),int(B)+1)),int(C)))

while len(info):
#pick a test case with no subsets
    readme = len(info)
    notsupersets = []
    while readme:
        readme -= 1
        isnt = 1
        for x in info:
            if info[readme][0] > x[0]:
                isnt = 0
                break
        if isnt:
            notsupersets.append(readme)

    dothese = []
    for x in notsupersets:
        dothese.append(info.pop(x))

    dothese.sort(key=lambda x: countcombos(len(x[0]),x[1]))

    for x in dothese:
        updateliars(x[0],x[1])


print min(itertools.imap(lambda x: len(x[0]),liars)), max(itertools.imap(lambda x: len(x[0])+len(x[1]),liars))