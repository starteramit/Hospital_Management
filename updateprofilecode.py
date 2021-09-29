#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Edit Code Wala Page"
import cgi,MySQLdb
data=cgi.FieldStorage()
aid=data.getvalue('appid')
pn=data.getvalue('patname')
did=data.getvalue('docid')
s=data.getvalue('stat')
apd=data.getvalue('appdate')
d=data.getvalue('date')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="update tbl_appointment set appointid='"+aid+"',patname='"+pn+"',docid='"+did+"',status='"+s+"',appointdate='"+apd+"',date='"+d+"'"
cur=con.cursor()
a=cur.execute(query)
if a==1:
	print "<script>alert('Record Updated');window.location.href='pprofile.py';</script>"
else:
	print "<script>alert('Record Not Updated');window.location.href='updateprofile.py';</script>"
