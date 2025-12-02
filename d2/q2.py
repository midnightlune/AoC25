def invalid(n):
    length=len(str(n))
    if length%2!=0:
        return False
    first = str(n)[:length//2]
    sec = str(n)[length//2:]
    return first==sec

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
