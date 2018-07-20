import csv
def pen(fileobj,data):
	#print(fileobj)
	#print(data)
	#print(type(fileobj))
	#print(type(data))
    csv_writer=csv.writer(fileobj,delimiter=',')
    for a in data:
	    csv_writer.writerow(a)
if __name__=='__main__':
	
    fileobj = open('details.csv','w')
    data=['name,class,phno,address'.split(','),
         'batman,python,654344893,goa'.split(','),
         'superman,data science,986344428,vizag'.split(','),
         'ironman,big data,784446346,Arku'.split(',')]
pen(fileobj,data)