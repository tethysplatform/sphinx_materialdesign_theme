$(document).ready(function () {
    $('.mx-card').each(function(){
        $(this).addClass('mdl-card mdl-shadow--2dp');
    });
    $('.mx-card .mx-card-title').each(function(){
        $(this).addClass('mdl-card__title');
    });
    $('.mx-card .mx-card-text').each(function(){
        $(this).addClass('mdl-card__supporting-text');
    });
    $('.mx-card-link').each(function(){
        $(this).hide();
    });
    $('h1').hide();
    $('.mdl-card').each(function(){
        $(this).click(function() {
            url = $(this).find('.mx-card-link').text();
            if (url) {
                window.location = url;
            }
            return true;
        });
    });
});
