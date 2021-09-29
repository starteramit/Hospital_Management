#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
	<title>Patient Registration Page</title>
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
		<div class="navbar navbar-default" style="background-color:black;border:none">
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
  <h1 class="text-center" style="color:black;font-family:Javanese Text">Contact Information</h1>
<br/>
  <div class="col-sm-6" style="border-right:2px solid black;">
  
	<div class="col-sm-1"></div>
	<div class="col-sm-4">
	<form action="contactcode.py">
		<b style="color:black;font-family:Gabriola;font-size:25px;">Name</b>
		<input type="text" name="name" class="form-control"style="width:400px;" placeholder="Enter Your Name!!!"/>
		<br/>
		<b style="color:black;font-family:Gabriola;font-size:25px;">Email</b>
		<input type="email" name="email" class="form-control" style="width:400px;"placeholder="Enter Your Email!!!"/>
		<br/>
		<b style="color:black;font-family:Gabriola;font-size:25px;">Mobile Number</b>
		<input type="text" name="number" class="form-control" style="width:400px;"placeholder="Enter Your Number!!!"/>
		<br/>
		<b style="color:black;font-family:Gabriola;font-size:25px;">Message</b>
		<textarea name="msg" class="form-control" style="width:400px;"placeholder="Enter Your Message!!!"></textarea>
		<br/>
		<button class="btn btn-danger form-control"style="width:400px;">Send</button>
		</form>
	</div>
	<div class="col-sm-1"></div>
  </div>
  <div class="col-sm-6">
  <div class="row">
  <h1 class="text-center" style="color:black;font-family:Javanese Text">Address</h1>
  </div>
  <div class="row">
  <div class="col-sm-3"></div>
  <div class="col-sm-6">
  <center>
	<span style="font-family:Gabriola;font-size:30px;color:black;">SGPGI Institute Of Medical Science -<br/> Charbagh,Lucknow,Uttar Pradesh,226004</span><br/>
	<span style="font-family:Gabriola;font-size:30px;color:black;">SGPGI Institute Of Medical Science -<br/> Alambagh,Lucknow,Uttar Pradesh,226004</span>
	</center>
</div>
<div class="col-sm-3"></div>
  </div>
  </div>
    </div>
	<div class="row" style="height:500px">
	<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14234.67795370525!2d80.94821!3d26.88224!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x730fe46201abc68a!2sSoftpro+India!5e0!3m2!1sen!2sin!4v1411887056855" width="100%" height="100%"></iframe>
	</div>
<br/>
<div class="row footer">SGPGI Institute Of Medical Science<i class="fa fa-twitter" style="margin-left:1%;"></i><i class="fa fa-facebook" style="margin-left:1%;"></i><i class="fa fa-youtube" style="margin-left:1%;"></i><br/>&copy;2019 SGPGI Institute Of Medical Science - Lucknow,Uttar Pradesh,226004<br/>Developed By:- AMIT JAISWAL<br/>SOFTPRO INDIA PVT. LTD.</div>
</div>
</div>
</body>
</html>
"""