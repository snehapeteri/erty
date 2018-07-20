#def details(*names):
  #  print(names)
   # for i in names:
   	   # print('welcome {} to the digital lync'.format(i))
#details('batsman','superman','ironman')
def details(**info):
	print(info)
	for i in info:
		print("welcome %s from %s" %(i,info[i]))
details(batsman="india",superman="pakistan")


		