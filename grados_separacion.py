##gets file with movie information

f=open("actores.txt")
actedWith={}
ActorList=[]
movies={}
actedIn=[]
dos=1


def getDegrees(original,target,base,dos=0,seen=[]):
	dos=dos+1
	print "---> checking %s against %s" %(target,base)
	for actor in actedWith[base]:
		print "\t" + actor
		if target == actor:
			print original, "has ", dos, "degree(s) of separation from", target
			return True
	for actor in actedWith[base]:
		if actor in seen: continue
		seen= seen+[actor]
		if getDegrees(original,target,actor,dos,seen):
			return False
	return True
	
for l in f:
    ##strip of whitespace
    l = l.strip()
    ##split by where forward-slashes are
    l = l.split("/")
    ##add the first "word" on the line to the database of movie names
    movies = {l[0] : l[1:]}
    for e in l[1:]:
        if e in actedWith:
            actedWith[e] = actedWith[e]+movies[l[0]]
        else:
            actedWith[e] = movies[l[0]]

original = raw_input("Enter Actor Name (Last, First): ")
target = raw_input("Enter Second Actor Name (Last, First): ")
getDegrees(original, target, original)
