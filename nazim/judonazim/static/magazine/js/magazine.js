$('.menuItem').click(function(){$(this).children('div').css('visibility', 'visible');});
$('.menuItem>div').mouseleave(function(){$(this).css('visibility', 'hidden');});
$('.more-posts-link').mouseover(function(){
  $(this).find('.bi-chevron-double-left').css('fill', 'yellow');
});
$('.more-posts-link').mouseleave(function(){
  $(this).find('.bi-chevron-double-left').css('fill', 'orange');
});

$(document).ready(function(){
  setTimeout(function(){$('a').attr('target' , '_blank');}, 100);

});
