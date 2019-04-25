// js search

$(document).ready(function () {
    $('select').formSelect();
    $('select > option').css('font-size', '18px');
    $('#hero_submit').click(function () {
        var path = $('select').val();

        var search = $("input").val()
        if (search === null || search === "") {
            M.toast({
                html: "Please enter a superhero name"
            });
            return false;
        } else {
            window.location.href = "/heroes/" + search
        }
    })
});