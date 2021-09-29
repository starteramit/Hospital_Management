#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('id')
s=data.getvalue('s')
print s	
#print id
if s=='Confirm':
	s='Cancel'
else:
	s='Confirm'
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
q="update tbl_appointment set status='"+s+"' where appointid='"+id+"'"
cur=con.cursor()
a=cur.execute(q)
if a==1:
	print "<script>alert('Status Updated!!!');window.location.href='dprofile.py';</script>"
else:
	print "<script>alert('Status Not Updated!!!');window.location.href='cancelappoint.py';</script>"