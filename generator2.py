import board
import boardlogger
import spylogger
import time

def boardFromList(l):
	if len(l)!=17:
		return False
	bo = board.board(l[0], l[1])
	ships = []
	ships.append(board.ship('p', l[2], l[3], l[4]))
	ships.append(board.ship('s', l[5], l[6], l[7]))
	ships.append(board.ship('d', l[8], l[9], l[10]))
	ships.append(board.ship('b', l[11], l[12], l[13]))
	ships.append(board.ship('c', l[14], l[15], l[16]))
	for s in ships:
		success = bo.placeShip(s)
		if not success:
			return False
	return bo

def generatePossibilities(x, y, 
                           startingPos=[1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True]
                           ,logger=False, blog=False):
	validCount = 0
	valids = []
	count = 0
	index=16
	pointer=16
	pos = [x, y]
	for i in startingPos:
		pos.append(i)
	start = [x, y, 1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True]
	end = [x, y, x, y, False, x, y, False, x, y, False, x, y, False, x, y, False]
	while pointer>=2:
		b = boardFromList(pos)
		if b!=False:
			validCount+=1
			if blog==False:
				valids.append(b)
			else:
				blog.addLine(pos)
			#print(validCount)
		count+=1
		pointer=findRightPointer(pos, end)
		if pointer==16 or pointer==13 or pointer==10 or pointer==7 or pointer==4:
			pos[pointer]=not pos[pointer]
		else:
			pos[pointer]=pos[pointer]+1
		if pointer<16:
			index=pointer+1
			while index<=16:
				pos[index]=start[index]
				index+=1
		if count%20000000==0:
			print(count)
			print(pos)
	print(count)
	print(validCount)
	if logger!=False:
		logger.addLine('Count: '+str(count))
		logger.addLine('Valid Count: '+str(validCount))
	return valids


def findRightPointer(current, maxValues):
	if len(current)!=len(maxValues):
		return 0
	i = len(current)-1
	while i>=0:
		if current[i]!=maxValues[i]:
			return i

		i = i - 1
	return i

def writeToCSV(l):
	f=open('f:/PythonOutput/battleship10x10valid.csv', 'w')
	for line in l:
		f.write(line)
	f.close()

def generateBoards():
	start = time.perf_counter()
	log = spylogger.spylog('f:/PythonOutput/battleshipGen2Log.txt')
	log.addLine('Started at: '+str(start))
	log.write()
	boardLogger = boardlogger.boardLog('g:/BattleshipValidlogs/ValidBoards_2_2.csv', 577)
	start = [2, 1, True, 6, 4, True, 8, 5, True, 6, 9, False, 4, 8, False]
	validList = generatePossibilities(10, 10, start, log, boardLogger)
	end = time.perf_counter()
	log.addLine('Ended at: '+str(end))
	log.addLine('Time taken: '+str(end-start))
	log.close()
	boardLogger.close()
