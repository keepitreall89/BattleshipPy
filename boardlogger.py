class boardLog:
	def __init__(self, path, bufferSize=0):
		self.path = path
		self.file = open(self.path, 'w')
		self.buffer = []
		self.bufferSize = bufferSize
		
	def addLine(self, line):
		string = ''
		for i in line:
			string += str(i)+', '
		string += '\n'
		string = string.replace(', \n', '\n')
		self.buffer.append(string)
		if self.bufferSize!=0 and len(self.buffer)>=self.bufferSize:
			self.write()
	def write(self):
		for i in self.buffer:
			self.file.write(str(i))
		self.buffer = []
	def close(self):
		self.write()
		self.file.close()
	
def testBuffer():
	path = 'F:/PythonOutput/boardLogger.txt'
	log = boardLog(path)
	log.addLine(["test", "testing", True, 8, "Test"])
	log.close()
	
#testBuffer()