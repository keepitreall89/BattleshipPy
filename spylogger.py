class spylog:
	def __init__(self, path, buffer=0):
		self.path = path
		self.file = open(path, 'w')
		self.bufferlength = buffer
		self.buffer = []
		self.separator = ', '
		
	def add2dList(self, list):
		for r in list:
			line = ''
			for i in r:
				line += str(i) + self.separator
			line += '/n'
			line = line.replace(self.separator+'/n', '/n')
			self.buffer.append(line)
	
	def addLine(self, line):
		self.buffer.append(str(line)+'/n')
	
	def write(self):
		for l in self.buffer:
			self.file.write(str(l))
		self.buffer = []
	
	def close(self):
		self.write()
		self.file.close()
	