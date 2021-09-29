#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('did')
#print id
print """
<form action="appointcode.py" method="post">
Patient Name
<input type="text" name="patname"/><br/>
Appointment Date
<input type="date" name="date"/>
"""
print '<input type="hidden" name="id" value="'+id+'"/>'
print  """
<input type="submit" value="submit"/>
</form>
"""