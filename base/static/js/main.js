VK.init({apiId: 4202342, onlyWidgets: true});
VK.Widgets.Recommended("vk_recommended", {limit: 3, period: 'month', verb: 1, width: "450"});
VK.Widgets.Comments("vk_comments", {limit: 5, width: "450", attach: "*"});
VK.Widgets.Like("vk_like", {type: "full", height: 24});
VK.Widgets.Group("vk_groups", {mode: 0, width: "285", height: "350", color1: 'ffffff', color2: '2B587A', color3: '333333'}, 58968036);

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=605738149495900";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

$("a.submit").click(function(){
    $(this).parents('form').submit();
});