import os
import time
import spylogger
import boardlogger

class board:
    def __init__(self, height=10, width=10):
        self.height=height
        self.width=width
        self.rows=[]
        self.ships=[]
        #pt boat, sub, destroyer, battleship, carrier
        self.shipsBool=[False, False, False, False, False]
        i=0
        while i<self.height:
            j=0
            row = []
            while j<self.width:
                row.append(space())
                j+=1
            self.rows.append(row)
            i+=1
    
    def __str__(self):
        value = ''
        for r in self.rows:
            for c in r:
                value+=str(c)+', \t'
            value+='\n'
        value = value.replace(', \t\n', '\n')
        value = value.rstrip()
        return value
    
    def shipExists(self, ship):
        for s in self.ships:
            if s.symbol==ship.symbol:
                return True
        return False
    
    
    #Return True if valid placement and mark on board, else return False
    def placeShip(self, ship):
        try:
            if not ship.valid:
                print("ship not valid")
                return False
        except:
            print("Was not passed a Ship class")
            return False
        if self.shipExists(ship):
            print("Same ship already on board")
            return False
        if ship.x>self.width or ship.y>self.height or (ship.vertical and (ship.y+ship.size-1)>self.height) or \
        (not ship.vertical and (ship.x+ship.size-1)>self.height):
            #print("ship coordinates off board")
            return False
        blank = space()
        if ship.vertical:
            y=ship.y
            while y<ship.y+ship.size:
                if str(self.rows[y-1][ship.x-1])!=str(blank):
                    #print("ship collides")
                    return False
                y+=1      
            y=ship.y
            while y<ship.y+ship.size:
                self.rows[y-1][ship.x-1]=ship.shortname
                y+=1
            self.ships.append(ship)
            return True
        if not ship.vertical:
            x=ship.x
            while x<ship.x+ship.size:
                if str(self.rows[ship.y-1][x-1])!=str(blank):
                    #print("ship collides")
                    return False
                x+=1
            x=ship.x
            while x<ship.x+ship.size:
                self.rows[ship.y-1][x-1]=ship.shortname
                x+=1
            self.ships.append(ship)
            return True
        
        

class space:
    def __init__(self):
        self.value = 'Blank'
        self.symbol = '_'
        
    def __str__(self):
        return self.value
    
    def setValue(self, value):
        self.value=str(value)
    

class ship:
    def __init__(self, symbol, x, y, vertical=True):
        self.symbol=symbol
        self.x=x
        self.y=y
        self.vertical=vertical
        if self.symbol=='s':
            self.size=3
            self.longname='Submarine'
            self.shortname='sub'
        elif self.symbol=='p':
            self.size=2
            self.longname='PT Boat'
            self.shortname='pt'
        elif self.symbol=='d':
            self.size=3
            self.longname='Destroyer'
            self.shortname='dest'
        elif self.symbol=='b':
            self.size=4
            self.longname='Battleship'
            self.shortname='batt'
        elif self.symbol=='c':
            self.size=5
            self.longname='Carrier'
            self.shortname='car'
        else:
            self.valid=False
        self.valid=True
    def rotate(self):
        self.vertical=not self.vertical
        return self
    
#Format 'h, w, ptx, pty, ptr, sx, sy, sr, dx, dy, dr, bx, by, br, cx, cy, cr'
def boardFromCSV(string):
    listValues = string.split(', ')

def boardFromList(l):
    if len(l)!=17:
        return False
    bo = board(l[0], l[1])
    ships = []
    ships.append(ship('p', l[2], l[3], l[4]))
    ships.append(ship('s', l[5], l[6], l[7]))
    ships.append(ship('d', l[8], l[9], l[10]))
    ships.append(ship('b', l[11], l[12], l[13]))
    ships.append(ship('c', l[14], l[15], l[16]))
    for s in ships:
        success = bo.placeShip(s)
        if not success:
            return False
    return bo

    
def testBoard():
    b = board()
    print(b)
    b.placeShip(ship('s', 3, 8))
    print()
    print(b)
    b.placeShip(ship('s', 2, 8, False))
    print()
    b=board(15, 20)
    print(b)
    b = board()
    print(b)
    b.placeShip(ship('s', 3, 8, False))
    print()
    l = [10, 10, 1, 1, True, 2, 1, False, 5,2, True, 1, 8, False, 2, 9, False]
    b = boardFromList(l)
    print(b)
    
    
def generatePossibilities(x, y):
    xi=1
    yi=1
    ships = ['p', 's', 'd', 'b', 'c']
    rotation = [False, True]
    validBoards=[]
    #for s in ships:
        #for r in rotation:
            #while xi<=x:
                #while yi<=y:
                    #b = board(x, y)
                    ##won't work this way. Unless....
                    #yi+=1
                #xi+=1
    
def generatePossibilities2(x, y):
    validCount = 0
    valids = []
    count = 0
    index=16
    pos = [x, y, 1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True, 1, 1, True]
    end = [x, y, 10, 10, False, 10, 10, False, 10, 10, False, 10, 10, False, 10, 10, False]
    while not pos == end:
        print(pos)
        b = boardFromList(pos)
        if b!=False:
            validCount+=1
            valids.append(b)
            print(validsCount)
        if index==16 or index==13 or index==10 or index==7 or index==4:
            pos[index]=not pos[index]
        else:
            pos[index]=pos[index]+1
            if pos[index]>10:
                pos[index]=10
            if pos[index]<1:
                pos[index]=1
        if index<=2:
            index=16
        else:
            index-=1
        count+=1
    print(count)
    print(validCount)
    
def generatePossibilities3(x, y, logger=False, blog=False):
    validCount = 0
    valids = []
    count = 0
    index=16
    pointer=16
    pos = [x, y, 1, 1, False, 2, 2, True, 4, 10, False, 1, 5, True, 5, 1, True]
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
    log = spylogger.spylog('f:/PythonOutput/battleshipGen3Log.txt')
    log.addLine('Started at: '+str(start))
    log.write()
    boardLogger = boardlogger.boardLog('g:/BattleshipValidlogs/ValidBoards.csv', 577)
    validList = generatePossibilities3(10, 10, log, boardLogger)
    end = time.perf_counter()
    log.addLine('Ended at: '+str(end))
    log.addLine('Time taken: '+str(end-start))
    log.close()
    boardLogger.close()
    
    
#generateBoards()
#writeToCSV(generatePossibilities3(10, 10))
#testBoard()
    
    
