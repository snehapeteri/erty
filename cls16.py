#files

fileobject=open('log.txt','w')
fileobject.write('iam in digital lync')
print(fileobject.read(4))
print(fileobject.readline(1))
fileobject.close() 