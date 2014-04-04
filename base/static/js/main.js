VK.init({apiId: 4202342, onlyWidgets: true});
//VK.Widgets.Recommended("vk_recommended", {limit: 3, period: 'month', verb: 1, width: "450"});
if ($("#vk_comments").size()) {
    VK.Widgets.Comments("vk_comments", {limit: 10, width: "604", attach: "*"});
};

VK.Widgets.Like("vk_like", {type: "full", height: 24});
if ($("#vk_groups")) {
    VK.Widgets.Group("vk_groups", {
        mode: 0,
        width: "260",
        height: "350",
        color1: 'ffffff',
        color2: '2B587A',
        color3: '333333'},
        58968036);
};


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


// reformal
var reformalOptions = {
    project_id: 549995,
    project_host: "phuketstash.reformal.ru",
    tab_orientation: "right",
    tab_indent: "50%",
    tab_bg_color: "#F05A00",
    tab_border_color: "#FFFFFF",
    tab_image_url: "http://tab.reformal.ru/T9GC0LfRi9Cy0Ysg0Lgg0L%252FRgNC10LTQu9C%252B0LbQtdC90LjRjw==/FFFFFF/a08a7c60392f68cb33f77d4f56cf8c6f/right/1/tab.png",
    tab_border_width: 2
};

(function() {
    var script = document.createElement('script');
    script.type = 'text/javascript'; script.async = true;
    script.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'media.reformal.ru/widgets/v3/reformal.js';
    document.getElementsByTagName('head')[0].appendChild(script);
})();
