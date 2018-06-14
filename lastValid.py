def main():
	path = 'G:/BattleshipValidlogs/ValidBoards_2_1.csv'
	f = open(path, 'r')
	last = ''
	for l in f:
		if len(l)>10:
			last = l
	f.close()
	print(last)
	ar = last.rstrip().split(', ')
	print(len(ar))
	if len(ar)==17:
		ar2 = []
		ar2.append(int(ar[0]))
		ar2.append(int(ar[1]))
		ar2.append(int(ar[2]))
		ar2.append(int(ar[3]))
		if ar[4]=='False':
			ar2.append(False)
		else:
			ar2.append(True)
		ar2.append(int(ar[5]))
		ar2.append(int(ar[6]))
		if ar[7]=='False':
			ar2.append(False)
		else:
			ar2.append(True)
		ar2.append(int(ar[8]))
		ar2.append(int(ar[9]))
		if ar[10]=='False':
			ar2.append(False)
		else:
			ar2.append(True)
		ar2.append(int(ar[11]))
		ar2.append(int(ar[12]))
		if ar[13]=='False':
			ar2.append(False)
		else:
			ar2.append(True)
		ar2.append(int(ar[14]))
		ar2.append(int(ar[15]))
		if ar[16]=='False':
			ar2.append(False)
		else:
			ar2.append(True)
		for i in ar2:
			print(str(i)+', '+str(type(i)))
main()