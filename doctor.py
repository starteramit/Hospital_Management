#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
	<title>Dr. Registration Page</title>
	<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css"  type="text/css" rel="stylesheet"/>
<link href="css/bootstrap-theme.min.css" type="text/css" rel="stylesheet"/>
<link href="css/font-awesome.min.css" type="text/css" rel="stylesheet"/>
<link href="csscode/code.css" type="text/css" rel="stylesheet"/>
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</head>
<body>
<div class="container-fluid">
<div class="row roa"style="background-color:#fbfbfb">
		<div class="col-sm-1"></div>
		<div class="col-sm-1"><img src="images/l.png"/></div>
		<div class="col-sm-3"><br/><span class="cola">Sanjay Gandhi Post Graduate</span><br/><h4>Institute Of Medical Science</h4></div>
		<div class="col-sm-1"></div>
		<div class="col-sm-6">
		<div class="row">
		<div class="navbar navbar-default" style="background-color:white;border:none">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="index.html" style="line-height:25px;font-size:15px;font-family:Javanese Text;font-weight:bold;">HOME</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse menu" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
		<li><i class="fa fa-phone" style="color:green;font-size:30px;line-height:40px;"></i><b style="font-size:20px;font-family:Javanese Text;font-weight:bold;"><font color="red">Emergency</font> 102</b></li>
        <li><a href="about.py">ABOUT US</a></li>
        <li><a href="doctor.py">DOCTOR</a></li>
		<li><a href="patient.py">PATIENT</a></li>
       <li><a href="login.py">LOGIN</a></li>
       <li><a href="contact.py">CONTACT US</a></li>
          </ul>
        </li>
        </ul>
    </div><!-- /.navbar-collapse -->
</div>
</div>
		<div class="row menu2">
			<ul>
		<li><a href="#"><img class="img1"src="images/appointment.png"/>APPOINTMENT</a></li>
		<li><a href="#"><img class="img1"src="images/find-a-doctor.png"/>FIND A DOCTOR</a></li>
		<li><a href="#"><img class="img1"src="images/health-packages(1).png"/>HEALTH/LAB PACKAGES</a></li>
		<li><a href="#"><img class="img1"src="images/lab-report(1).png"/>LAB REPORTS</a></li>
        </ul>
		</div>
	</div>
	</div>    <br/>
  <div class="row" style="background-image:url('images/b12.jpg')">
    <div class="col-sm-4"> </div>
<div class="col-md-4">
<h1 class="text-center" style="color:black;font-family:Javanese Text">Doctor Registration</h1>
<br/>

<form action="doctorcode.py" method="post">
<b style="color:black;font-family:Gabriola;font-size:20px;">Name</b>
<input type="text" name="name" class="form-control" placeholder="Enter Your Name!!"/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">F'Name</b>
<input type="text" name="fname" class="form-control" placeholder="Enter Father's Name!!"/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Email</b>
<input type="email" name="email" class="form-control" placeholder="Enter Your Email!!"/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Password</b>
<input type="password" name="password" class="form-control" placeholder="Enter Your Password!!"/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Gender</b>
<input type="radio" name="a" value="male"/><b style="color:black;font-family:Gabriola;font-size:20px;">Male</b>
<input type="radio" name="a" value="female"/><b style="color:black;font-family:Gabriola;font-size:20px;">Female</b>
<br/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Specialization</b>
<select name="special" class="form-control">
<option>---SELECT SPECIALIZATION---</option>
<option>Surgion</option>
<option>Eye Specialist</option>
<option>Physician</option>
<option>Orthopediation</option>
<option>Cardiologist</option>
</select>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Experience</b>
<input type="text" name="experience" class="form-control" placeholder="Enter Experience!!"/>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Fees</b>
<input type="text" name="fee" class="form-control" placeholder="Enter Fees!!"/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Address</b>
<textarea name="address" class="form-control"></textarea>
<b style="color:black;font-family:Gabriola;font-size:20px;">Availibility Timing</b>
<select name="at" class="form-control">
<option>---SELECT TIMING---</option>
<option>7:00 A.M To 10:00 A.M</option>
<option>12:00 P.M To 2:00 P.M</option>
<option>4:00 P.M To 6:00 P.M</option>
</select>
<br/>
<b style="color:black;font-family:Gabriola;font-size:20px;">Captcha Confirmation</b>
<br/>
"""
import random
a=[0,1,2,3,4,5,6,7,8,9]
n1=random.choice(a)
n2=random.choice(a)
sum=n1+n2
print "<input type='hidden' value='"+str(sum)+"' name='sum'/>"
print "<input type='text' value='"+str(n1)+"' style='width:180px;border-radius:10px'readonly/> + "
print "<input type='text' value='"+str(n2)+"' style='width:180px;border-radius:10px'readonly/>"
print " = <input type='number' name='t' style='width:140px;border-radius:10px ' required/> "
print """
<br/>
<br/>
<button class="btn btn-danger form-control">Submit</button>
<br/>
</form>
</div>
</div>
<br/>
<div class="row footer">SGPGI Institute Of Medical Science<i class="fa fa-twitter" style="margin-left:1%;"></i><i class="fa fa-facebook" style="margin-left:1%;"></i><i class="fa fa-youtube" style="margin-left:1%;"></i><br/>&copy;2019 SGPGI Institute Of Medical Science - Lucknow,Uttar Pradesh,226004<br/>Developed By:- AMIT JAISWAL<br/>SOFTPRO INDIA PVT. LTD.</div>
</div>
</div>
</body>
</html>
"""