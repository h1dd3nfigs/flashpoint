# -*- encoding: utf-8 -*-

html_doc = '''

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html dir="ltr">
<head>

<meta name="description" content="Classic car, van and pickup forum">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Content-Style-Type" content="text/css">

<link rel="top" href="./index.php" title="Classic cars forum & vehicle restoration. Forum Index" />
<link rel="search" href="./search.php" title="Search" />
<link rel="help" href="./faq.php" title="FAQ" />
<link rel="author" href="./memberlist.php" title="Memberlist" />
<link rel="prev" href="viewtopic.php?t=12591&amp;view=previous" title="View previous topic" />
<link rel="next" href="viewtopic.php?t=12591&amp;view=next" title="View next topic" />
<link rel="up" href="viewforum.php?f=1" title="Classic & Vintage Cars - General Chat" />
<link rel="chapter forum" href="viewforum.php?f=38" title="Welcome To The OldClassicCar Forum" />
<link rel="chapter forum" href="viewforum.php?f=23" title="Find Old Car Parts & Books on Ebay" />
<link rel="chapter forum" href="viewforum.php?f=1" title="Classic & Vintage Cars - General Chat" />
<link rel="chapter forum" href="viewforum.php?f=13" title="Classic Lorries, Steam, Vans, Pickup Trucks, Tractors, & Plant" />
<link rel="chapter forum" href="viewforum.php?f=36" title="Classic Motorcycles & Bicycles" />
<link rel="chapter forum" href="viewforum.php?f=41" title="Bodywork & Paint Restoration" />
<link rel="chapter forum" href="viewforum.php?f=40" title="Electrical Restoration" />
<link rel="chapter forum" href="viewforum.php?f=42" title="Mechanical Restoration" />
<link rel="chapter forum" href="viewforum.php?f=24" title="General Restoration Advice" />
<link rel="chapter forum" href="viewforum.php?f=31" title="Vintage Motoring-Related Toys, Tools & Accessories" />
<link rel="chapter forum" href="viewforum.php?f=25" title="Interesting Links" />
<link rel="chapter forum" href="viewforum.php?f=43" title="All Other Cars & Vehicles." />
<link rel="chapter forum" href="viewforum.php?f=44" title="Austin" />
<link rel="chapter forum" href="viewforum.php?f=45" title="Ford" />
<link rel="chapter forum" href="viewforum.php?f=52" title="Jaguar, Daimler & SS" />
<link rel="chapter forum" href="viewforum.php?f=46" title="Morris" />
<link rel="chapter forum" href="viewforum.php?f=49" title="Rootes Group & Original Companies (Hillman, Humber, Singer, Sunbeam, Commer etc)" />
<link rel="chapter forum" href="viewforum.php?f=48" title="Triumph" />
<link rel="chapter forum" href="viewforum.php?f=26" title="Classic Caravans" />
<link rel="chapter forum" href="viewforum.php?f=54" title="Historic Aviation" />
<link rel="chapter forum" href="viewforum.php?f=29" title="Your Adverts & Ebay 'finds'" />
<link rel="chapter forum" href="viewforum.php?f=34" title="Show News, Reports, Press Releases & Photographs" />
<link rel="chapter forum" href="viewforum.php?f=39" title="General Motoring & Collectables" />

<title>Classic Car Rescue - C5</title>
<!-- link rel="stylesheet" href="templates/subSilver/subSilver.css" type="text/css" -->
<style type="text/css">
<!--
/*
  The original subSilver Theme for phpBB version 2+
  Created by subBlue design
  http://www.subBlue.com

  NOTE: These CSS definitions are stored within the main page body so that you can use the phpBB2
  theme administration centre. When you have finalised your style you could cut the final CSS code
  and place it in an external file, deleting this section to save bandwidth.
*/

/* General page style. The scroll bar colours only visible in IE5.5+ */
body {
	background-color: #F1FBF3;
	scrollbar-face-color: #ffffff;
	scrollbar-highlight-color: #FFFFFF;
	scrollbar-shadow-color: #ffffff;
	scrollbar-3dlight-color: #D1D7DC;
	scrollbar-arrow-color:  #0534FD;
	scrollbar-track-color: #ffffff;
	scrollbar-darkshadow-color: #98AAB1;
}

/* General font families for common tags */
font,th,td,p { font-family: Verdana, Arial, Helvetica, sans-serif }
a:link,a:active,a:visited { color : #0534FD; }
a:hover		{ text-decoration: underline; color : #DD6900; }
hr	{ height: 0px; border: solid #D1D7DC 0px; border-top-width: 1px;}

/* This is the border line & background colour round the entire page */
.bodyline	{ background-color: #FFFFFF; border: 1px #98AAB1 solid; }

/* This is the outline round the main forum tables */
.forumline	{ background-color: #FFFFFF; border: 2px #006699 solid; }

/* Main table cell colours and backgrounds */
td.row1	{ background-color: #ffffff; }
td.row2	{ background-color: #ffffff; }
td.row3	{ background-color: #D1D7DC; }

/*
  This is for the table cell above the Topics, Post & Last posts on the index.php page
  By default this is the fading out gradiated silver background.
  However, you could replace this with a bitmap specific for each forum
*/
td.rowpic {
		background-color: #FFFFFF;
		background-image: url(templates/subSilver/images/cellpic2a.gif);
		background-repeat: repeat-y;
}

/* Header cells - the blue and silver gradient backgrounds */
th	{
	color: #000000; font-size: 11px; font-weight : bold;
	background-color: #0534FD; height: 25px;
	background-image: url(templates/subSilver/images/cellpic3a.gif);
}

td.cat,td.catHead,td.catSides,td.catLeft,td.catRight,td.catBottom {
			background-image: url(templates/subSilver/images/cellpic1a.gif);
			background-color:#D1D7DC; border: #FFFFFF; border-style: solid; height: 28px;
}

/*
  Setting additional nice inner borders for the main table cells.
  The names indicate which sides the border will be on.
  Don't worry if you don't understand this, just ignore it :-)
*/
td.cat,td.catHead,td.catBottom {
	height: 29px;
	border-width: 0px 0px 0px 0px;
}
th.thHead,th.thSides,th.thTop,th.thLeft,th.thRight,th.thBottom,th.thCornerL,th.thCornerR {
	font-weight: bold; border: #FFFFFF; border-style: solid; height: 28px;
}
td.row3Right,td.spaceRow {
	background-color: #D1D7DC; border: #FFFFFF; border-style: solid;
}

th.thHead,td.catHead { font-size: 12px; border-width: 1px 1px 0px 1px; }
th.thSides,td.catSides,td.spaceRow	 { border-width: 0px 1px 0px 1px; }
th.thRight,td.catRight,td.row3Right	 { border-width: 0px 1px 0px 0px; }
th.thLeft,td.catLeft	  { border-width: 0px 0px 0px 1px; }
th.thBottom,td.catBottom  { border-width: 0px 1px 1px 1px; }
th.thTop	 { border-width: 1px 0px 0px 0px; }
th.thCornerL { border-width: 1px 0px 0px 1px; }
th.thCornerR { border-width: 1px 1px 0px 0px; }

/* The largest text used in the index page title and toptic title etc. */
.maintitle	{
	font-weight: bold; font-size: 22px; font-family: "Trebuchet MS",Verdana, Arial, Helvetica, sans-serif;
	text-decoration: none; line-height : 120%; color : #000000;
}

/* General text */
.gen { font-size : 12px; }
.genmed { font-size : 11px; }
.gensmall { font-size : 10px; }
.gen,.genmed,.gensmall { color : #000000; }
a.gen,a.genmed,a.gensmall { color: #0534FD; text-decoration: none; }
a.gen:hover,a.genmed:hover,a.gensmall:hover	{ color: #DD6900; text-decoration: underline; }

/* The register, login, search etc links at the top of the page */
.mainmenu		{ font-size : 11px; color : #000000 }
a.mainmenu		{ text-decoration: none; color : #0534FD;  }
a.mainmenu:hover{ text-decoration: underline; color : #DD6900; }

/* Forum category titles */
.cattitle		{ font-weight: bold; font-size: 12px ; letter-spacing: 1px; color : #0534FD}
a.cattitle		{ text-decoration: none; color : #0534FD; }
a.cattitle:hover{ text-decoration: underline; }

/* Forum title: Text and link to the forums used in: index.php */
.forumlink		{ font-weight: bold; font-size: 12px; color : #0534FD; }
a.forumlink 	{ text-decoration: none; color : #0534FD; }
a.forumlink:hover{ text-decoration: underline; color : #DD6900; }

/* Used for the navigation text, (Page 1,2,3 etc) and the navigation bar when in a forum */
.nav			{ font-weight: bold; font-size: 11px; color : #000000;}
a.nav			{ text-decoration: none; color : #0534FD; }
a.nav:hover		{ text-decoration: underline; }

/* titles for the topics: could specify viewed link colour too */
.topictitle,h1,h2	{ font-weight: bold; font-size: 11px; color : #000000; }
a.topictitle:link   { text-decoration: none; color : #0534FD; }
a.topictitle:visited { text-decoration: none; color : #5493B4; }
a.topictitle:hover	{ text-decoration: underline; color : #DD6900; }

/* Name of poster in viewmsg.php and viewtopic.php and other places */
.name			{ font-size : 11px; color : #000000;}

/* Location, number of posts, post date etc */
.postdetails		{ font-size : 10px; color : #000000; }

/* The content of the posts (body of text) */
.postbody { font-size : 12px; line-height: 18px}
a.postlink:link	{ text-decoration: none; color : #0534FD }
a.postlink:visited { text-decoration: none; color : #5493B4; }
a.postlink:hover { text-decoration: underline; color : #DD6900}

/* Quote & Code blocks */
.code {
	font-family: Courier, 'Courier New', sans-serif; font-size: 11px; color: #006600;
	background-color: #FAFAFA; border: #D1D7DC; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}

.quote {
	font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 11px; color: #444444; line-height: 125%;
	background-color: #FAFAFA; border: #D1D7DC; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}

/* Copyright and bottom info */
.copyright		{ font-size: 10px; font-family: Verdana, Arial, Helvetica, sans-serif; color: #444444; letter-spacing: -1px;}
a.copyright		{ color: #444444; text-decoration: none;}
a.copyright:hover { color: #000000; text-decoration: underline;}

/* Form elements */
input,textarea, select {
	color : #000000;
	font: normal 11px Verdana, Arial, Helvetica, sans-serif;
	border-color : #000000;
}

/* The text input fields background colour */
input.post, textarea.post, select {
	background-color : #FFFFFF;
}

input { text-indent : 2px; }

/* The buttons used for bbCode styling in message post */
input.button {
	background-color : #ffffff;
	color : #000000;
	font-size: 11px; font-family: Verdana, Arial, Helvetica, sans-serif;
}

/* The main submit button option */
input.mainoption {
	background-color : #FAFAFA;
	font-weight : bold;
}

/* None-bold submit button */
input.liteoption {
	background-color : #FAFAFA;
	font-weight : normal;
}

/* This is the line in the posting page which shows the rollover
  help line. This is actually a text box, but if set to be the same
  colour as the background no one will know ;)
*/
.helpline { background-color: #ffffff; border-style: none; }

/* Import the fancy styles for IE only (NS4.x doesn't use the @import function) */
@import url("templates/subSilver/formIE.css");
-->
</style>
</head>
<body bgcolor="#F1FBF3" text="#000000" link="#0534FD" vlink="#5493B4">

<a name="top"></a>

<table width="100%" cellspacing="0" cellpadding="10" border="0" align="center">
	<tr>
		<td class="bodyline"><table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tr>
				<td align="center" width="100%" valign="middle">

</span>

<a href="http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/">
<img border="0" title="Return to the forum homepage" alt="classic car forum header" src="http://www.oldclassiccar.co.uk/images/OCC/1.jpg" width="950" height="112">
</a>

<br />

<! **** 22/1/16 RJ added variables for category and keywords -->

<script type="text/javascript" src='http://adn.ebay.com/files/js/min/jquery-1.6.2-min.js'></script>
<script type="text/javascript" src='http://adn.ebay.com/files/js/min/ebay_activeContent-min.js'></script>
<script charset="utf-8" type="text/javascript">
document.write('\x3Cscript type="text/javascript" charset="utf-8" src="http://adn.ebay.com/cb?programId=15&campId=5336732204&toolId=10026&keyword=%28%281930%2C%2C1931%2C1932%2C1933%2C1934%2C1935%2C1936%2C1937%2C1938%2C1939%29%2C%281940%2C1941%2C1942%2C1943%2C1944%2C1945%2C1946%2C1947%2C1948%2C1949%29%2C%281950%2C1951%2C1952%2C1953%2C1954%2C1955%2C1956%2C1957%2C1958%2C1959%29%2C%281960%2C1961%2C1962%2C1963%2C1964%2C1965%2C1966%2C1967%2C1968%2C1969%29%2C%28vintage%2C1920%2C1921%2C1922%2C1923%2C1924%2C1925%2C1926%2C1927%2C1928%2C1929%29%29&showItems=1&sortBy=2&minPrice=150&maxPrice=20000&width=950&height=95&font=2&textColor=000000&linkColor=0000AA&arrowColor=ffffff&color1=ffffff&color2=[COLORTWO]&format=html&contentType=TEXT_AND_IMAGE&enableSearch=n&usePopularSearches=n&freeShipping=n&topRatedSeller=n&itemsWithPayPal=n&descriptionSearch=y&showKwCatLink=n&excludeCatId=&excludeKeyword=&catId=29751&disWithin=300&ctx=n&autoscroll=n&flashEnabled=' + isFlashEnabled + '&pageTitle=' + _epn__pageTitle + '&cachebuster=' + (Math.floor(Math.random() * 10000000 )) + '">\x3C/script>' );
</script>



<br />


<span class="maintitle">Classic cars forum & vehicle restoration.</span><br />

<table cellpadding="0" cellspacing="0" style="background-color: transparent;"  cellpadding="0">
  <tr>
    <td align="center">


				<table cellspacing="0" cellpadding="2" border="0">
					<tr>
						<td align="center" valign="top" nowrap="nowrap"><span class="mainmenu">&nbsp;<a href="faq.php" class="mainmenu"><img src="templates/subSilver/images/icon_mini_faq.gif" width="12" height="13" border="0" alt="FAQ" hspace="3" />FAQ</a>&nbsp; &nbsp;<a href="search.php" class="mainmenu"><img src="templates/subSilver/images/icon_mini_search.gif" width="12" height="13" border="0" alt="Search" hspace="3" />Search</a>&nbsp; &nbsp;<a href="memberlist.php" class="mainmenu"><img src="templates/subSilver/images/icon_mini_members.gif" width="12" height="13" border="0" alt="Memberlist" hspace="3" />Memberlist</a>&nbsp; &nbsp;<a href="groupcp.php" class="mainmenu"><img src="templates/subSilver/images/icon_mini_groups.gif" width="12" height="13" border="0" alt="Usergroups" hspace="3" />Usergroups</a>&nbsp;

						</span></td>
					</tr>
					<tr>
						<td height="25" align="center" valign="top" nowrap="nowrap"><span class="mainmenu">&nbsp;<a href="profile.php?mode=editprofile" class="mainmenu"><img src="templates/subSilver/images/icon_mini_profile.gif" width="12" height="13" border="0" alt="Profile" hspace="3" />Profile</a>&nbsp; &nbsp;<a href="privmsg.php?folder=inbox" class="mainmenu"><img src="templates/subSilver/images/icon_mini_message.gif" width="12" height="13" border="0" alt="Log in to check your private messages" hspace="3" />Log in to check your private messages</a>&nbsp; &nbsp;<a href="login.php" class="mainmenu"><img src="templates/subSilver/images/icon_mini_login.gif" width="12" height="13" border="0" alt="Log in" hspace="3" />Log in</a>&nbsp;</span></td>
					</tr>
				</table>

<span class="mainmenu">
<a rel="nofollow" href="http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=2311">How To Register</a>   &nbsp; &nbsp;
<a rel="nofollow" href="http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=2454">Posting Photographs</a>   &nbsp; &nbsp;
<a rel="nofollow" href="http://www.ableweb.co.uk/priv.htm?url=oldclassiccar" target="_blank">Privacy Policy</a> &nbsp; &nbsp;
<img src="http://www.oldclassiccar.co.uk/classic-car-images/fb.gif" width="16" height="16" border="0" alt="F/book">
<a href="http://www.facebook.com/oldclassiccar" target="_blank" rel="nofollow">facebook.com/oldclassiccar</a>
</span>


</td>
			</tr>
		</table>

		<br />


<table width="100%" cellspacing="2" cellpadding="2" border="0">
  <tr>
	<td align="left" valign="bottom" colspan="2"><a class="maintitle" href="viewtopic.php?t=12591&amp;start=75&amp;postdays=0&amp;postorder=asc&amp;highlight=">Classic Car Rescue - C5</a><br />

	  <span class="gensmall"><b>Goto page  <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=60">Previous</a>&nbsp;&nbsp;<a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=0">1</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=15">2</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=30">3</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=45">4</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=60">5</a>, <b>6</b>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=90">7</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=105">8</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=120">9</a>&nbsp;&nbsp;<a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=90">Next</a></b>  </span></td>

  </tr>
</table>

<table width="100%" cellspacing="2" cellpadding="2" border="0">
  <tr>
	<td align="left" valign="bottom" nowrap="nowrap"><span class="nav"><a href="posting.php?mode=newtopic&amp;f=1"><img src="templates/subSilver/images/lang_english/post.gif" border="0" alt="Post new topic" align="middle" /></a>&nbsp;&nbsp;&nbsp;<a href="posting.php?mode=reply&amp;t=12591"><img src="templates/subSilver/images/lang_english/reply.gif" border="0" alt="Reply to topic" align="middle" /></a></span></td>
	<td align="left" valign="middle" width="100%"><span class="nav">&nbsp;&nbsp;&nbsp;<a href="http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/" class="nav">Classic cars forum & vehicle restoration. Forum Index</a>
	  -> <a href="viewforum.php?f=1" class="nav">Classic & Vintage Cars - General Chat</a></span></td>
  </tr>
</table>

<table class="forumline" width="100%" cellspacing="1" cellpadding="3" border="0">
	<tr align="right">
		<td class="catHead" colspan="2" height="28"><span class="nav">





                                           </span></td>
	</tr>
	
	<tr>
		<th class="thLeft" width="150" height="26" nowrap="nowrap">Author</th>
		<th class="thRight" nowrap="nowrap">Message</th>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87755"></a><b>Churchill Johnson</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 11 Jan 2011<br />Posts: 302<br />Location: Rayleigh Essex</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87755#87755"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Tue Oct 09, 2012 10:12 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87755"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote">Make your opinion known - I have-
<br />

<br />
<a href="mailto:customerservices@channel5.com">customerservices@channel5.com</a></td>	</tr></table><span class="postbody"> Not wishing to knock anyone who make's a comment on the rubbish that is shown on TV but when do the producer's take any notice, i myself have written several time's not e-m's but proper letter's to two different TV station's in the past and all i got was a reply to the effect that &quot;they were sorry i did not enjoy the programme and in the future they would take on board my complaint's'' of course they carried on as before, it's a captive audience, i am so happy that TV's are made with an on and off button.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=1877"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=1877"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87761"></a><b>riley541</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 18 Jun 2008<br />Posts: 1360<br />Location: Derbyshire</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87761#87761"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Wed Oct 10, 2012 7:51 am<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87761"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>Churchill Johnson wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote">Make your opinion known - I have-
<br />

<br />
<a href="mailto:customerservices@channel5.com">customerservices@channel5.com</a></td>	</tr></table><span class="postbody"> Not wishing to knock anyone who make's a comment on the rubbish that is shown on TV but when do the producer's take any notice... </td>	</tr></table><span class="postbody">
<br />

<br />
If only one or two complaints are received, they won't but if the number of complaints is in the thousands, they will.
<br />

<br />
From what I've read in this forum and elsewhere, hundreds of people think the series is absolute rubbish yet they're all still watching it and writing about in forum threads rather than complaining to Channel 5 - who must be delighting in all the free publicity!</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=560"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=560"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87768"></a><b>Journer</b></span><br /><span class="postdetails"><br /><img src="images/avatars/21379932464ff6eb2b48f20.jpg" alt="" border="0" /><br /><br />Joined: 28 May 2012<br />Posts: 111<br />Location: Glasgow</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87768#87768"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Wed Oct 10, 2012 3:39 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87768"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">For such a **** programme it certainly gets a lot of attention. Personally, I cant stand the amatuer dramatics and the forced anger but to each his own. I prefer Mike Brewer and big Ed, in my opinion they can do no wrong...lol<br />_________________<br />'Iron sharpens iron, so one man sharpens another'</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=2478"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=2478"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87780"></a><b>ukdave2002</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 23 Nov 2007<br />Posts: 2931<br />Location: South Cheshire</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87780#87780"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Thu Oct 11, 2012 7:21 am<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87780"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>Churchill Johnson wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote">Make your opinion known - I have-
<br />

<br />
<a href="mailto:customerservices@channel5.com">customerservices@channel5.com</a></td>	</tr></table><span class="postbody"> Not wishing to knock anyone who make's a comment on the rubbish that is shown on TV but when do the producer's take any notice... </td>	</tr></table><span class="postbody">
<br />

<br />
If only one or two complaints are received, they won't but if the number of complaints is in the thousands, they will.
<br />

<br />
From what I've read in this forum and elsewhere, hundreds of people think the series is absolute rubbish yet they're all still watching it and writing about in forum threads rather than complaining to Channel 5 - who must be delighting in all the free publicity!</td>	</tr></table><span class="postbody">
<br />

<br />
Viewing figures will be the only thing C5 will be interested in, as this directly dictates revenue from  advertisers  .  Making a  controversial  program that maintains the viewing numbers certainly wont bother them.
<br />

<br />
Dave</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=17"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=17"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87781"></a><b>riley541</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 18 Jun 2008<br />Posts: 1360<br />Location: Derbyshire</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87781#87781"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Thu Oct 11, 2012 7:59 am<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87781"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>ukdave2002 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>Churchill Johnson wrote:</b></span></td>	</tr>	<tr>	  <td class="quote"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>riley541 wrote:</b></span></td>	</tr>	<tr>	  <td class="quote">Make your opinion known - I have-
<br />

<br />
<a href="mailto:customerservices@channel5.com">customerservices@channel5.com</a></td>	</tr></table><span class="postbody"> Not wishing to knock anyone who make's a comment on the rubbish that is shown on TV but when do the producer's take any notice... </td>	</tr></table><span class="postbody">
<br />

<br />
If only one or two complaints are received, they won't but if the number of complaints is in the thousands, they will.
<br />

<br />
From what I've read in this forum and elsewhere, hundreds of people think the series is absolute rubbish yet they're all still watching it and writing about in forum threads rather than complaining to Channel 5 - who must be delighting in all the free publicity!</td>	</tr></table><span class="postbody">
<br />

<br />
Viewing figures will be the only thing C5 will be interested in, as this directly dictates revenue from  advertisers  .  Making a  controversial  program that maintains the viewing numbers certainly wont bother them.
<br />

<br />
Dave</td>	</tr></table><span class="postbody">
<br />

<br />
Which is why, having watched the first programme, I am not watching the rest. Unfortunately others seem to be continuing to watch it and boosting viewing figures.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=560"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=560"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87824"></a><b>peterwpg</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 10 Apr 2008<br />Posts: 1487<br />Location: New Brunswick Canada.  55 Years UK  14 Years Canada</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87824#87824"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Fri Oct 12, 2012 2:48 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87824"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">For all those who are blocked from viewing Channel  5,  The Discovery Channel will be airing the series staring on Monday 15th November.
<br />

<br />
Following up on Riley's comment,  I promise not to buy anything that is advertised during the show.   <img src="images/smiles/icon_smile.gif" alt="Smile" border="0" /></span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=440"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=440"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a> <a href="mailto:peterhlawford@gmail.com"><img src="templates/subSilver/images/lang_english/icon_email.gif" alt="Send e-mail" title="Send e-mail" border="0" /></a>    <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87831"></a><b>D4B</b></span><br /><span class="postdetails"><br /><img src="images/avatars/177567476555340a6bca317.jpg" alt="" border="0" /><br /><br />Joined: 28 Dec 2010<br />Posts: 1837<br />Location: Hampshire UK</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87831#87831"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Fri Oct 12, 2012 4:52 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87831"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">I did stumble accross this again just as Bernie was spraying 
<br />
the MG with the rag left on the roof ~ by the time he was in the 
<br />
pub begging the painter to come back I switched over.....
<br />

<br />
I promise never to stumble accross it again ~ simply dreadful <img src="images/smiles/icon_evil.gif" alt="Evil or Very Mad" border="0" /></span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=1858"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=1858"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87841"></a><b>47p2</b></span><br /><span class="postdetails"><br /><img src="images/avatars/186751655484a80c1adb38.gif" alt="" border="0" /><br /><br />Joined: 24 Nov 2007<br />Posts: 1911<br />Location: Glasgow</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87841#87841"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Fri Oct 12, 2012 9:21 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87841"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">Just read this on another forum where someone wrote to Chanel 5 asking about the MGBGT...
<br />

<br />

<br />
</span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>Quote:</b></span></td>	</tr>	<tr>	  <td class="quote"><span style="font-style: italic">Update on the MBG being 2 or even 3 different cars, I sent channel 5 questions which I don't have a copy of but along the lines of confirming if indeed the car was the same as the wreck &quot;rescued &quot; from the barn and about the validity of the 2 week restoration claim. This was the reply I recieved:</span>
<br />

<br />

<br />

<br />
Dear David 
<br />

<br />
Thank you for your recent enquiry regarding Classic Car Rescue. 
<br />

<br />
While the production team were filming in Canada, the mechanics in London discovered some serious problems with the MGB, midway through the restoration, which meant they felt it might not be entirely safe to drive. Their original plan was to buy a new chassis, which is a common way that people restore MGBs (you can buy an entire new monocoque chassis for just £1000) and build on top of that. But wanting to stick with used parts, they bought another car and used the chassis from that, transferring much of the first MGB, right down to door-handles, and windows. The cost of the second car was included in the figures mentioned and the end result was a combination of the two. 
<br />

<br />
The programme aims to show how Bernie Fineman and Mario Pacione cope with restoration jobs with a “tight deadline and an even tighter budget” in an entertaining fashion while also giving some background into why each selected model is held in the high regard that it is. It is not intended to, and does not claim to, demonstrate the detailed effort and finance that can go into the high end restoration of classic cars. 
<br />

<br />
Nevertheless, this does not diminish the validity of your opinions and we are grateful to you for taking the time to make us aware of your concerns. Your comments have been logged in our Viewer Enquiries Report. This is circulated throughout the company and seen by all relevant personnel. 
<br />

<br />
Thank you for your interest in Channel 5. 
<br />

<br />
Yours sincerely 
<br />

<br />

<br />
Ian 
<br />
VIEWER ADVISOR </td>	</tr></table><span class="postbody"><br />_________________<br /><span style="font-weight: bold"><span style="color: red">ROVER</span>
<br />
<span style="font-style: italic">One of Britain's Fine Cars</span></span>
<br />

<br />
<img src="http://i117.photobucket.com/albums/o69/47p2/Signature800.png" border="0" />
<br />

<br />
<a href="http://www.1947rover.co.uk/" target="_blank" rel="nofollow" class="postlink">1947 16hp Sports Saloon</a></span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=47"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=47"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>  <a href="http://www.1947rover.co.uk" target="_userwww" rel="nofollow"><img src="templates/subSilver/images/lang_english/icon_www.gif" alt="Visit poster's website" title="Visit poster's website" border="0" /></a>   <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87843"></a><b>Rick</b></span><br /><span class="postdetails">Site Admin<br /><img src="images/avatars/1622729613519b33bc3e86c.jpg" alt="" border="0" /><br /><br />Joined: 27 Apr 2005<br />Posts: 16070<br />Location: S. Cheshire</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87843#87843"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Fri Oct 12, 2012 10:31 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87843"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">Interesting stuff, I read elsewhere that there were certain differences between the car shown at the beginning, and the finished car. Who says the camera cannot tell fibs eh!? <img src="images/smiles/icon_smile.gif" alt="Smile" border="0" />
<br />

<br />
R<br />_________________<br />Rick (Admin. oldclassiccar.co.uk)
<br />
Various 1930s-1960s relics - Austin, Morris, Bedford, Dodge etc.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=15"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=15"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87847"></a><b>scott_budds</b></span><br /><span class="postdetails"><br /><img src="images/avatars/16853189074929bfa8685b4.jpg" alt="" border="0" /><br /><br />Joined: 20 Nov 2008<br />Posts: 174<br />Location: Norwich</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87847#87847"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Fri Oct 12, 2012 11:53 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87847"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">Saw my first one tonight the MGBGT one. It was giving me heart palpitations watching it! The rear wheels fell off when the car was lifted on the lift. How come the transition wasn't connected?  But then the welded new brackets back on but it the underside was that rusty what were they welding too!
<br />

<br />
Good news you could win this car...Im that unlucky if I entered I would probably end up wining it! arghhhh
<br />

<br />
I just cant watch programmes like this.
<br />

<br />
Buddsy<br />_________________<br />Im looking for an Elan plus 2 for my next resto project...if you see one think of me please!!</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=792"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=792"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a> <a href="mailto:scott_budds@hotmail.com"><img src="templates/subSilver/images/lang_english/icon_email.gif" alt="Send e-mail" title="Send e-mail" border="0" /></a> <a href="http://www.rsbudds.co.uk" target="_userwww" rel="nofollow"><img src="templates/subSilver/images/lang_english/icon_www.gif" alt="Visit poster's website" title="Visit poster's website" border="0" /></a>   <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87854"></a><b>Churchill Johnson</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 11 Jan 2011<br />Posts: 302<br />Location: Rayleigh Essex</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87854#87854"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Sat Oct 13, 2012 9:53 am<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87854"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">surely one cannot change a chassis from one car to another without using that car's registration number as this is what a reg is based on.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=1877"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=1877"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87869"></a><b>MikeEdwards</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 25 May 2011<br />Posts: 885<br />Location: South Cheshire</span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87869#87869"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Sat Oct 13, 2012 5:58 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87869"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">Never mind that, since when did an MGB GT have a separate chassis? It has a monocoque bodyshell, and I am pretty sure a new Heritage shell is a little bit more than £1000.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=2060"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=2060"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>  <a href="http://www.firenza.net" target="_userwww" rel="nofollow"><img src="templates/subSilver/images/lang_english/icon_www.gif" alt="Visit poster's website" title="Visit poster's website" border="0" /></a>   <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87876"></a><b>Rick</b></span><br /><span class="postdetails">Site Admin<br /><img src="images/avatars/1622729613519b33bc3e86c.jpg" alt="" border="0" /><br /><br />Joined: 27 Apr 2005<br />Posts: 16070<br />Location: S. Cheshire</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87876#87876"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Sat Oct 13, 2012 8:16 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87876"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody"></span><table width="90%" cellspacing="1" cellpadding="3" border="0" align="center"><tr> 	  <td><span class="genmed"><b>MikeEdwards wrote:</b></span></td>	</tr>	<tr>	  <td class="quote">Never mind that, since when did an MGB GT have a separate chassis? It has a monocoque bodyshell, and I am pretty sure a new Heritage shell is a little bit more than £1000.</td>	</tr></table><span class="postbody">
<br />

<br />
<img src="images/smiles/icon_smile.gif" alt="Smile" border="0" /> it justs get better the whole &quot;story&quot; doesn't it <img src="images/smiles/icon_smile.gif" alt="Smile" border="0" />
<br />

<br />
RJ<br />_________________<br />Rick (Admin. oldclassiccar.co.uk)
<br />
Various 1930s-1960s relics - Austin, Morris, Bedford, Dodge etc.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=15"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=15"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row2"><span class="name"><a name="87878"></a><b>gresham flyer</b></span><br /><span class="postdetails"><br /><img src="images/avatars/870375934f2ee4e383c00.jpg" alt="" border="0" /><br /><br />Joined: 06 Sep 2008<br />Posts: 1424<br /></span><br /></td>
		<td class="row2" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87878#87878"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Sat Oct 13, 2012 9:33 pm<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87878"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">If classic car programmes are not correct in detail and how to carry out a proper restoration,how many other types of TV programmes are incorrect.
<br />
Cookery,Financial,Gardening,Antique etc etc.
<br />
 Even radio 4 has its incorrect descriptions and detail when i have heard programmes about the motor car or the motorcycle,or another topic I am passionate about.
<br />
I am sure these production companies can find better presenters.
<br />

<br />
Even our old flower Ed China has a helping hand you know.....John Simpson from Practical Classics magazine was behind the scenes at last years NEC show.
<br />
If we cannot produce a proper programme about old cars here in the UK then it is a sad old world.
<br />

<br />
                                     Gresham Flyer</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row2" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row2" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=681"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=681"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td width="150" align="left" valign="top" class="row1"><span class="name"><a name="87886"></a><b>victor 101</b></span><br /><span class="postdetails"><br /><br /><br />Joined: 03 Apr 2009<br />Posts: 399<br />Location: East Yorkshire</span><br /></td>
		<td class="row1" width="100%" height="28" valign="top"><table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td width="100%"><a href="viewtopic.php?p=87886#87886"><img src="templates/subSilver/images/icon_minipost.gif" width="12" height="9" alt="Post" title="Post" border="0" /></a><span class="postdetails">Posted: Sun Oct 14, 2012 8:10 am<span class="gen">&nbsp;</span>&nbsp; &nbsp;Post subject: </span></td>
				<td valign="top" nowrap="nowrap"><a href="posting.php?mode=quote&amp;p=87886"><img src="templates/subSilver/images/lang_english/icon_quote.gif" alt="Reply with quote" title="Reply with quote" border="0" /></a>   </td>
			</tr>
			<tr>
				<td colspan="2"><hr /></td>
			</tr>
			<tr>
				<td colspan="2"><span class="postbody">I thought this guy Bernie was supposed to be a knowledgeable chap with 35 years in the trade, if his idea of checking a car for rust is jabbing a screwdriver in the inner wing or yanking a wing off so it hits the floor, its a wonder he hasn't had a smack in the mouth. Now that would make interesting viewing.</span><span class="gensmall"></span></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="row1" width="150" align="left" valign="middle"><span class="nav"><a href="#top" class="nav">Back to top</a></span></td>
		<td class="row1" width="100%" height="28" valign="bottom" nowrap="nowrap"><table cellspacing="0" cellpadding="0" border="0" height="18" width="18">
			<tr>
				<td valign="middle" nowrap="nowrap"><a href="profile.php?mode=viewprofile&amp;u=990"><img src="templates/subSilver/images/lang_english/icon_profile.gif" alt="View user's profile" title="View user's profile" border="0" /></a> <a href="privmsg.php?mode=post&amp;u=990"><img src="templates/subSilver/images/lang_english/icon_pm.gif" alt="Send private message" title="Send private message" border="0" /></a>     <script language="JavaScript" type="text/javascript"><!--

	if ( navigator.userAgent.toLowerCase().indexOf('mozilla') != -1 && navigator.userAgent.indexOf('5.') == -1 && navigator.userAgent.indexOf('6.') == -1 )
		document.write(' ');
	else
		document.write('</td><td>&nbsp;</td><td valign="top" nowrap="nowrap"><div style="position:relative"><div style="position:absolute"></div><div style="position:absolute;left:3px;top:-1px"></div></div>');

				//--></script><noscript></noscript></td>
			</tr>
		</table></td>
	</tr>
	<tr>
		<td class="spaceRow" colspan="2" height="1"><img src="templates/subSilver/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr align="center">
		<td class="catBottom" colspan="2" height="28"><table cellspacing="0" cellpadding="0" border="0">
			<tr><form method="post" action="viewtopic.php?t=12591&amp;start=75">
				<td align="center"><span class="gensmall">Display posts from previous: <select name="postdays"><option value="0" selected="selected">All Posts</option><option value="1">1 Day</option><option value="7">7 Days</option><option value="14">2 Weeks</option><option value="30">1 Month</option><option value="90">3 Months</option><option value="180">6 Months</option><option value="364">1 Year</option></select>&nbsp;<select name="postorder"><option value="asc" selected="selected">Oldest First</option><option value="desc">Newest First</option></select>&nbsp;<input type="submit" value="Go" class="liteoption" name="submit" /></span></td>
			</form></tr>
		</table></td>
	</tr>
</table>

<table width="100%" cellspacing="2" cellpadding="2" border="0" align="center">

  <tr>
	<td align="center" colspan="3">

<script type="text/javascript"><!--
google_ad_client = "ca-pub-2512916887581639";
/* OCC Forum 728x90 */
google_ad_slot = "3306618733";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="//pagead2.googlesyndication.com/pagead/show_ads.js">
</script>

            </td>
  </tr>

  <tr>
	<td align="left" valign="middle" nowrap="nowrap"><span class="nav"><a href="posting.php?mode=newtopic&amp;f=1"><img src="templates/subSilver/images/lang_english/post.gif" border="0" alt="Post new topic" align="middle" /></a>&nbsp;&nbsp;&nbsp;<a href="posting.php?mode=reply&amp;t=12591"><img src="templates/subSilver/images/lang_english/reply.gif" border="0" alt="Reply to topic" align="middle" /></a></span></td>
	<td align="left" valign="middle" width="100%"><span class="nav">&nbsp;&nbsp;&nbsp;<a href="http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/" class="nav">Classic cars forum & vehicle restoration. Forum Index</a>
	  -> <a href="viewforum.php?f=1" class="nav">Classic & Vintage Cars - General Chat</a></span></td>
	<td align="right" valign="top" nowrap="nowrap"><span class="gensmall">All times are GMT + 1 Hour</span><br /><span class="nav">Goto page  <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=60">Previous</a>&nbsp;&nbsp;<a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=0">1</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=15">2</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=30">3</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=45">4</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=60">5</a>, <b>6</b>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=90">7</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=105">8</a>, <a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=120">9</a>&nbsp;&nbsp;<a href="viewtopic.php?t=12591&amp;postdays=0&amp;postorder=asc&amp;start=90">Next</a></span>
	  </td>
  </tr>
  <tr>
	<td align="left" colspan="3"><span class="nav">Page <b>6</b> of <b>9</b></span></td>
  </tr>


</table>

<table width="100%" cellspacing="2" border="0" align="center">
  <tr>
	<td width="40%" valign="top" nowrap="nowrap" align="center"><span class="gensmall">




                              </span><br />
	  &nbsp;<br />
	  </td>
	<td align="right" valign="top" nowrap="nowrap">
<form method="get" name="jumpbox" action="viewforum.php" onSubmit="if(document.jumpbox.f.value == -1){return false;}"><table cellspacing="0" cellpadding="0" border="0">
	<tr>
		<td nowrap="nowrap"><span class="gensmall">Jump to:&nbsp;<select name="f" onchange="if(this.options[this.selectedIndex].value != -1){ forms['jumpbox'].submit() }"><option value="-1">Select a forum</option><option value="-1">&nbsp;</option><option value="-1">Welcome</option><option value="-1">----------------</option><option value="38">Welcome To The OldClassicCar Forum</option><option value="-1">&nbsp;</option><option value="-1">Classic Cars, Lorries & Motorcycles</option><option value="-1">----------------</option><option value="23">Find Old Car Parts & Books on Ebay</option><option value="1"selected="selected">Classic & Vintage Cars - General Chat</option><option value="13">Classic Lorries, Steam, Vans, Pickup Trucks, Tractors, & Plant</option><option value="36">Classic Motorcycles & Bicycles</option><option value="41">Bodywork & Paint Restoration</option><option value="40">Electrical Restoration</option><option value="42">Mechanical Restoration</option><option value="24">General Restoration Advice</option><option value="31">Vintage Motoring-Related Toys, Tools & Accessories</option><option value="25">Interesting Links</option><option value="-1">&nbsp;</option><option value="-1">Ownership - Your Cars, Lorries & Restoration Projects (1900-1985)</option><option value="-1">----------------</option><option value="43">All Other Cars & Vehicles.</option><option value="44">Austin</option><option value="45">Ford</option><option value="52">Jaguar, Daimler & SS</option><option value="46">Morris</option><option value="49">Rootes Group & Original Companies (Hillman, Humber, Singer, Sunbeam, Commer etc)</option><option value="48">Triumph</option><option value="-1">&nbsp;</option><option value="-1">Vintage & Classic Caravans</option><option value="-1">----------------</option><option value="26">Classic Caravans</option><option value="-1">&nbsp;</option><option value="-1">Aircraft</option><option value="-1">----------------</option><option value="54">Historic Aviation</option><option value="-1">&nbsp;</option><option value="-1">For Sale & Wanted</option><option value="-1">----------------</option><option value="29">Your Adverts & Ebay 'finds'</option><option value="-1">&nbsp;</option><option value="-1">'Ye Olde Ventilated Crankcase' Public House</option><option value="-1">----------------</option><option value="34">Show News, Reports, Press Releases & Photographs</option><option value="39">General Motoring & Collectables</option></select><input type="hidden" name="sid" value="8616877ffa58d2fec112b34d94d82058" />&nbsp;<input type="submit" value="Go" class="liteoption" /></span></td>
	</tr>
</table></form>

<span class="gensmall">You <b>cannot</b> post new topics in this forum<br />You <b>cannot</b> reply to topics in this forum<br />You <b>cannot</b> edit your posts in this forum<br />You <b>cannot</b> delete your posts in this forum<br />You <b>cannot</b> vote in polls in this forum<br /></span></td>
  </tr>
</table>



<table width="100%" align="center">
<tr><td align="center">

</td></tr>
</table>



<div align="center"><span class="copyright"><br /><br />
<!--
	We request you retain the full copyright notice below including the link to www.phpbb.com.
	This not only gives respect to the large amount of time given freely by the developers
	but also helps build interest, traffic and use of phpBB 2.0. If you cannot (for good
	reason) retain the full copyright we request you at least leave in place the
	Powered by phpBB line, with phpBB linked to www.phpbb.com. If you refuse
	to include even this then support on our forums may be affected.

	The phpBB Group
// -->
php BB powered &copy; php BB Grp.<br /></span></div>
		</td>
	</tr>
</table>

<!-- Start of StatCounter Code -->
<script type="text/javascript">
var sc_project=3354223;
var sc_invisible=0;
var sc_partition=36;
var sc_security="540d7256";
</script>

<script type="text/javascript" src="http://www.statcounter.com/counter/counter_xhtml.js"></script><noscript><div class="statcounter"><a rel="nofollow" class="statcounter" href="http://www.statcounter.com/"><img class="statcounter" src="http://c37.statcounter.com/3354223/0/540d7256/0/" alt=" " /></a></div></noscript>
<!-- End of StatCounter Code -->





</body>
</html>

'''