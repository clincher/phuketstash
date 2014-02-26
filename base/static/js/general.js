//Google maps initialize function

//function initialize() {
//	//---- Code for a small maps located in footer ----
//	var myOptions = {
//		//Coordinates of the map's center
//		center: new google.maps.LatLng(7.836750, 98.334666),
//		//Zoom level
//		zoom: 15,
//		//Type of the map (posible values .HYBRID, .SATELLITE, .ROADMAP, .TERRAIN)
//		mapTypeId: google.maps.MapTypeId.HYBRID
//	};
//	//Define the map and select the element in which it will be displayed
//	var map = new google.maps.Map(document.getElementById("gmaps"),myOptions);
//	var marker = new google.maps.Marker({
//		//Coordinate of the map marker's location
//		position: new google.maps.LatLng(7.836750, 98.334666),
//		map: map,
//		//Text that will be displayed when the mouse hover on the marker
//		title:"Phuket STASH"
//	});
//	//---- Code for a big maps located in contact section ----
//	if (document.getElementById("contact-gmaps")) {
//		var myOptions1 = {
//			//Coordinates of the map's center
//			center: new google.maps.LatLng(7.836750, 98.334666),
//			//Zoom level
//			zoom: 15,
//			//Type of map (possible values .ROADMAP, .HYBRID, .SATELLITE, .TERRAIN)
//			mapTypeId: google.maps.MapTypeId.ROADMAP
//		};
//		//Define the map and select the element in which it will be displayed
//		var map1 = new google.maps.Map(document.getElementById("contact-gmaps"),myOptions1);
//		var marker1 = new google.maps.Marker({
//			//Coordinate of the marker's location
//			position: new google.maps.LatLng(7.836750, 98.334666),
//			map: map1,
//			//Text that will be displayed when the mouse hover on the marker
//			title:"Phuket STASH"
//		});
//	}
//}
			
$(window).load(function() {
//	initialize();
	
	//Main Sliders
	$('#slider').nivoSlider({
		effect:'fade',
		pauseOnHover:true,
		captionOpacity:0.9,
		pauseTime:17000
	});
	
	//Illustration Slider (used in "Our Story" on Main Page)
	$('#slider1').nivoSlider({
		effect:'fade',
		pauseOnHover:true,
		captionOpacity:0.7,
		pauseTime:5000
	});
	$('#slider2').nivoSlider({
		effect:'fade',
		pauseOnHover:true,
		captionOpacity:0.7,
		pauseTime:5000
	});
	
	if (!($.browser.msie)  && !(parseInt($.browser.version, 10) === 8)) {
		//Social button animation 
		$('#social-button img').mouseout(function(){
			$(this).css('opacity','0.6');
		}).mouseover(function(){
			$(this).css('opacity','1');
		});
		//Form submit button animation 
		$('#send-button, #contact-send-button').mouseout(function(){
			$(this).css('opacity','0.9');
		}).mouseover(function(){
			$(this).css('opacity','1');
		});
	}

	//Drop-down menu
	$("#menu-header-menu li").mouseenter(function(){
		$(this).children(".sub-menu").fadeIn(300);
	}).mouseleave(function(){
		$(this).children(".sub-menu").fadeOut(300);
	});
	//Add arrow icon to dropdown menu
	$(".drop-triangle").appendTo($(".sub-menu")).css('display','block');
	
	//Smooth scrolling
	$(".scroll").click(function(event){		
		event.preventDefault();
		$('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);
	});
	
	//Lightbox plugin for menu page
	$(".menu-image-wrap a").lightBox();
	
	//Lightbox plugin for gallery page
	$(".gallery .image-bg a").lightBox();
	
	//FancyCaption plugin for menu page
	$(".fancycaption-fade").fancyCaption({
		slideTopBar:false, 
		slideBottomBar:false, 
		slideLeftBar:false, 
		slideRightBar:false, 
		fadeFrom:1, 
		fadeTo:0.2
	});
	
	//FancyCaption plugin for gallery page
	$(".fancycaption-full").fancyCaption({
		slideLeftBar:false, 
		slideRightBar:false, 
		fadeFrom:1, 
		fadeTo:0.2
	});
	
	//Twitter feed initialize
//	var displaylimit = 3;
//	var showdirecttweets = true;
//	var showretweets = true;
//	var showtweetlinks = true;
//	var showprofilepic = true;
//
//	$.getJSON('get-tweets.php',{"twitterusername": "envato", "displaylimit": 3},
//	function(feeds) {
//		var feedHTML = '';
//		var displayCounter = 1;
//		for (var i=0; i<feeds.length; i++) {
//			var tweetscreenname = feeds[i].user.name;
//			var tweetusername = feeds[i].user.screen_name;
//			var profileimage = feeds[i].user.profile_image_url_https;
//			var status = feeds[i].text;
//			var isaretweet = false;
//			var isdirect = false;
//			var tweetid = feeds[i].id_str;
//
//			//If the tweet has been retweeted, get the profile pic of the tweeter
//			if(typeof feeds[i].retweeted_status != 'undefined'){
//				profileimage = feeds[i].retweeted_status.user.profile_image_url_https;
//				tweetscreenname = feeds[i].retweeted_status.user.name;
//				tweetusername = feeds[i].retweeted_status.user.screen_name;
//				tweetid = feeds[i].retweeted_status.id_str
//				isaretweet = true;
//			};
//
//			//Check to see if the tweet is a direct message
//			if (feeds[i].text.substr(0,1) == "@") {
//				isdirect = true;
//			}
//
//			if (((showretweets == true) || ((isaretweet == false) && (showretweets == false))) && ((showdirecttweets == true) || ((showdirecttweets == false) && (isdirect == false)))) {
//				if ((feeds[i].text.length > 1) && (displayCounter <= displaylimit)) {
//					if (showtweetlinks == true) {
//						status = addlinks(status);
//					}
//					feedHTML += '<div class="twitterRow">';
//					feedHTML += '<div class="twitter-pic"><a href="https://twitter.com/'+tweetusername+'" ><img src="'+profileimage+'"images/twitter-feed-icon.png" width="42" height="42" alt="twitter icon" /></a></div>';
//					feedHTML += '<div class="twitter-text"><p><span class="tweetprofilelink"><strong><a href="https://twitter.com/'+tweetusername+'" >'+tweetscreenname+'</a></strong> <a href="https://twitter.com/'+tweetusername+'" >@'+tweetusername+'</a></span><br/>'+status+'</p></div>';
//					feedHTML += '</div>';
//					displayCounter++;
//				}
//			}
//		}
//
//		$('#tweet-feed-main,.tweet').html(feedHTML);
//	});
	
	//Function modified from Stack Overflow
//	function addlinks(data) {
//		//Add link to all http:// links within tweets
//		data = data.replace(/((https?|s?ftp|ssh)\:\/\/[^"\s\<\>]*[^.,;'">\:\s\<\>\)\]\!])/g, function(url) {
//			return '<a href="'+url+'" >'+url+'</a>';
//		});
//
//		//Add link to @usernames used within tweets
//		data = data.replace(/\B@([_a-z0-9]+)/ig, function(reply) {
//			return '<a href="http://twitter.com/'+reply.substring(1)+'" style="font-weight:lighter;" >'+reply.charAt(0)+reply.substring(1)+'</a>';
//		});
//		return data;
//	}
	
	//Delete last delimiter
	$("#hours_list li:last").css('border-bottom','none');
	$("#footer-misc li:last").html($("#footer-misc li:last").html().replace("|"," "));
	$("#site-section-wrap .three-columns:last").css('border-bottom','none');
	//Form submit and button animation 
	$('#submit, #contact-send-button').mouseout(function(){
		$(this).css('opacity','0.9');
	}).mouseover(function(){
		$(this).css('opacity','1');
	});
	$("#respond").mouseenter(function(){
		$(this).css('opacity','1')
	}).mouseleave(function(){
		$(this).css('opacity','0.9')
	});
	//Mobile menu
	$('#header-mobile-menu').change(function() {
		// set the window's location property to the value of the option the user has selected
		window.location = $(this).val();
	});	
	//Make current option in mobile menu selected
	$("#header-mobile-menu option").each(function() {
		var path = window.location.pathname;
		var pageName = path.substring(path.lastIndexOf('/') + 1);
		if ($(this).attr('value') == pageName) {
			$(this).attr('selected','selected');
		}
	});
	
	
	//Customer review on main page
	$('#customer-review').bxSlider({mode:'vertical',speed:1000,controls:false,auto:true});	
	//Accordion widget initializing
	$(".accordion").accordion({
		icons: {
			'header':'accordionplus', 
			'headerSelected':'accordionminus'
		}
	});
	//Tabs widget initializing
	$(".tabs").tabs();

});