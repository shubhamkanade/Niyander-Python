
fo=open("fun.txt","r+")

str=fo.read(10)

print str;

print "file position"

iCnt=fo.tell();

print iCnt;

iCnt=fo.seek(0,0)

str=fo.read()

print "After seek \n",str;


