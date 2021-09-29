#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<script>
function logout()
{
window.history.forward();
window.setTimeout("window.location.href='login.py'",2000);
}
</script>
</head>
<body onload="logout()" bgcolor="black">
</body>
</html>
"""