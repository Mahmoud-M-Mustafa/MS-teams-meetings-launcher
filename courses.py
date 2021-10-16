class course():

	def __init__(self, name,start_hour,start_minute,days,end_hour,end_minute=59):
		self.name=name
		self.start_minute=start_minute
		self.start_hour=start_hour
		self.days=days # 0 --> MON , 2-->WED , 5 --> SAT
		self.end_hour=end_hour
		self.end_minute = end_minute

#-------------End of class--------------


# ToDo:
# 	  add your courses 
courses = [['CSE448 (UG2013) - Embedded Operating Systems  (20847)', 17, 30, ['3'], 19,30], # team 1
           ['RTOS', 14, 50, ['0', '2', '5'], 16] # team 2
		   ]


