$(".hh").blur(function () {
    if ($(this).val() >= 24)
        $(this).val($(this).val() % 24);

    if ($(this).val() === "")
        $(this).val("");
    else if ($(this).val() < 10)
        $(this).val("0" + parseInt($(this).val()));
});
$(".mm").blur(function () {
    if ($(this).val() >= 60)
        $(this).val($(this).val() % 60);

    if ($(this).val() === "")
        $(this).val("00");
    else if ($(this).val() < 10)
        $(this).val("0" + parseInt($(this).val()));

});


function checked(id) {
    var checked_green = document.getElementById("check" + id);
    checked_green.classList.toggle('green');
    var strike_unstrike = document.getElementById("strike" + id);
    strike_unstrike.classList.toggle('strike_none');
}