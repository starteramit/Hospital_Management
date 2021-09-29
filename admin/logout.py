#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<script>
function logout()
{
window.history.forward();
window.setTimeout("window.location.href='index.html'",2000);
}
</script>
</head>
<body onload="logout()" style="background-image:url('../images/about.jpg')">
</body>
</html>
"""