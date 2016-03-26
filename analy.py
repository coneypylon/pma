goodwords = ['good','great','awesome','loved','love','go','blew me away']
badwords = ['sucked','been better',"didn't like",'boring','awful','dull','dumb','lame','disappointed','pedestrian','nauseating','out of tune','flat']
contwords = ['not','both',"can't","hard",'decide']

keywords = ['Academy', 'The Academy', 'Blue Devils', '#dci', '@dci', '@DCI', 'Blue Knights', 'Knights', 'Blue Stars', 'Stars', 'Bluecoats', 'Bloo', 'Boston Crusaders', 'Boston', 'The Cadets', 'Cadets', 'cadets', 'the cadets', 'Carolina Crown', 'Carolina', 'Crown', 'Cascades', 'The Cavaliers', 'Cavaliers', 'Colts', 'Crossmen', 'Jersey Surf', 'Surf', 'Madison Scouts', 'The Scouts', 'Mandarins', 'Oregon Crusaders', 'Pacific Crest', 'Crest', 'Phantom Regiment', 'Phantom', 'Pioneer', 'Santa Clara Vanguard', 'SCV', 'Spirit of Atlanta', 'Troopers']

acs = 0
bds = 0
bks = 0
bss = 0
bloos = 0
bcs = 0
tcs = 0
ccs = 0
cas = 0
tcs = 0
cos = 0
crs = 0
jss = 0
mss = 0
mas = 0
ocs = 0
pcs = 0
prs = 0
pis = 0
scvs =0
sas = 0
trs = 0



# check for opinion
def goodeval(text):
	if any(y in text for y in contwords):
		return 'cont'
	elif any(y in text for y in (goodwords + badwords)):
		return 'cont'
	elif any(y in text for y in badwords):
		return 'bad'
	elif any(y in text for y in goodwords):
		return 'good'
	else: return 'cont'

def analysis(tweetfile):
	tweets = []
	tweets2 = []
	tweets3 = []
	tweetscont = []
	with open(tweetfile, "r") as f:
		curline = f.readline()	
		while curline != '':
			tweets.append(curline)
			curline = f.readline()
	print("made it")
	for x in tweets:
		tweets2.append(x.split("|"))
	
	for x in range(0,len(tweets2) - 1):
		try:
			if tweets2[x][1] != tweets2[x-1][1]: # attempt to remove multiple votes
				tweet = str(tweets2[x][0]).lower()
				tweets3.append(tweet)
		except:
			tweets3.append(str(tweets2[x][0]).lower()) # accounting for the first tweet
	
	ac = []
	bd = []
	bdb = []
	bk = []
	bs = []
	bloo = []
	bc = []
	tc = []
	cc = []
	ca = []
	cav = []
	co = []
	cr = []
	js = []
	ms = []
	ma = []
	oc = []
	pc = []
	pr = []
	pi = []
	scv =[]
	vc = []
	sa = []
	tr = []
	
	# loc == list of corps
	loc = [ac,bd,bdb,bk,bs,bloo,bc,tc,cc,ca,cav,co,co,cr,js,ms,ma,oc,pc,pr,pi,scv,vc,sa,tr]
	
	# cors == corps score
	corsg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	corsb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	# separating by corps
	for x in tweets3:
			if any(y in x for y in ['academy', 'the academy']):
				ac.append(x)
			elif any(y in x for y in ['blue devils b', 'devils b']):
				bdb.append(x)
			elif any(y in x for y in ['blue devils','devils']):
				bd.append(x)
			elif any(y in x for y in ['blue knights','knights']):
				bk.append(x)
			elif any(y in x for y in ['blue stars','stars']):
				bs.append(x)
			elif any(y in x for y in ['bluecoats', 'bloo']):
				bloo.append(x)
			elif any(y in x for y in ['boston crusaders', 'boston']):
				bc.append(x)
			elif any(y in x for y in ['the cadets','cadets']):
				tc.append(x)
			elif any(y in x for y in ['carolina crown','crown','carolina']):
				cc.append(x)
			elif any(y in x for y in ['cascades']):
				ca.append(x)
			elif any(y in x for y in ['the cavaliers','cavaliers']):
				cav.append(x)
			elif any(y in x for y in ['colts']):
				co.append(x)
			elif any(y in x for y in ['crossmen','cross']):
				cr.append(x)
			elif any(y in x for y in ['jersey','surf','jersey surf']):
				js.append(x)
			elif any(y in x for y in ['madison scouts','madison','scouts']):
				ms.append(x)
			elif any(y in x for y in ['mandarin']):
				ma.append(x)
			elif any(y in x for y in ['oregon crusaders','oregon']):
				oc.append(x)
			elif any(y in x for y in ['pacific crest','crest']):
				pc.append(x)
			elif any(y in x for y in ['phantom regiment','phantom','regiment']):
				pr.append(x)
			elif any(y in x for y in ['pioneer']):
				pi.append(x)
			elif any(y in x for y in ['vanguard cadet']):
				vc.append(x)
			elif any(y in x for y in ['santa clara', 'vanguard', 'scv']):
				scv.append(x)
			elif any(y in x for y in ['spirit','atlanta']):
				sa.append(x)
			elif any(y in x for y in ['troopers']):
				tr.append(x)
	
	contro = []
	
	for x in range(0,len(loc)):
		for y in loc[x]:
			temp = goodeval(y)
			if temp == 'cont':
				contro.append(y)
			elif temp == 'good':
				corsg[x] += 1
			else: corsb[x] += 1
	
	while len(contro) > 1:
		print("There are undetermined tweets")
		print(contro[0])
		decision = input("Is this good or bad?")
		corps = int(input("Enter corps number \n 0 ac, 1 bd, 2 bdb, 3 bk, 4 bs, 5 bloo, 6 bc, 7 tc \n 8 cc, 9 ca, 10 cav, 11 co, 12 co, 13 cr, 14 js, 15 ms, 16 ma, 17 oc,18 pc, 19 pr, 20 pi, 21 scv, 22 vc, 23 sa, 24 tr]"))
		if decision == 'g':
			corsg[corps] += 1
			contro = contro[1:]
		elif decision == 'b':
			corsb[corps] += 1
			contro = contro[1:]
		else: contro = contro[1:]
	
	if contro != []:
		print("There are undetermined tweets")
		print(contro[0])
		decision = input("Is this good or bad?")
		corps = int(input("Enter corps number \n 0 ac, 1 bd, 2 bdb, 3 bk, 4 bs, 5 bloo, 6 bc, 7 tc \n 8 cc, 9 ca, 10 cav, 11 co, 12 co, 13 cr, 14 js, 15 ms, 16 ma, 17 oc,18 pc, 19 pr, 20 pi, 21 scv, 22 vc, 23 sa, 24 tr]"))
		if decision == 'g':
			corsg[corps] += 1
			contro = []
		elif decision == 'b':
			corsb[corps] += 1
			contro = []
		else: contro = []
	
	percors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	
	for x in range(0, len(percors)):
		try:
			percors[x] = corsg[x]/(corsg[x]+corsb[x])
		except:
			percors[x] = "NaN"
	
	totalefftweets = sum(corsg) + sum(corsb)
	
	
	# writing to file
	with (open(tweetfile[0:4] + "report.txt","w")) as f:
		f.write("This is a report for " + tweetfile[0:4] + "\n")
		f.write("\n The number of responses was culled from " + str(len(tweets) - 1) + " tweets to " + str(totalefftweets) + " effective tweets.\n")
		f.write("Key for corps:\n 0 ac, 1 bd, 2 bdb, 3 bk, 4 bs, 5 bloo, 6 bc, 7 tc \n 8 cc, 9 ca, 10 cav, 11 co, 12 co, 13 cr, 14 js, 15 ms, 16 ma, 17 oc,18 pc, 19 pr, 20 pi, 21 scv, 22 vc, 23 sa, 24 tr \n")
		f.write("Raw results: \n Good scores: " + str(corsg) + "\n Bad scores: " + str(corsb) + "\n Percentages of votes: " + str(percors) + "\n")
		f.write("Raw tweets follow: \n" + str(tweets) + "\n END OF FILE " + tweetfile)

