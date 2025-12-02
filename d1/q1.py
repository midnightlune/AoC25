#q1
start=50
ans=0
with open('q1input.txt','r') as f:
    lines=f.readlines()
    for l in lines:
        l=l.strip()
        if l=='':
            continue
        move=l[0]
        val=int(l[1:])
        if move=='L':
            start=(start-val)%100
        elif move=='R':
            start=(start+val)%100
        
        if start==0:
            ans+=1
print(ans)

#q2
start = 50
ans = 0

with open("q1input.txt", "r") as f:
	lines = f.readlines()

for l in lines:
	l = l.strip()
	if l=='':
		continue
	
	val=int(l[1:])
	if l[0]=='R':
		ans+=(start+val)//100
		start=(start+val)%100
		
	elif l[0]=='L':
		if start == 0:
			ans+= val//100
		else:
			if val>=start:
				ans += 1 + ((val-start)//100)
		start = (start-val) % 100
print(ans)


        