
def invalid(n):
    ch=str(n)
    for patternlen in range(1, (len(ch)//2)+1):
        if len(ch)%patternlen == 0:
            pattern=ch[:patternlen]
            if pattern*(len(ch)//patternlen)==ch:
                return True
    return False

def find(start, end):
    invalids = []
    for i in range(start, end + 1):
        if invalid(i):
            invalids.append(i)
    return invalids

total=0
allinvalids=[]
with open('q2input.txt','r') as f:
    line=f.readline()
    ranges=line.split(',')
    for i in ranges:
        temp=i.split('-')
        start,end=int(temp[0]),int(temp[1])
        invalids=find(start,end)
        allinvalids.extend(invalids)
        total+=sum(invalids)

print(total)