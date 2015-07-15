/**
 * Created by dgaievskyi on 14.07.2015.
 */


$(document).ready(function () {
    // Посилання з id="test" буде тригером події
    $("#load_more").click(function () {
        // AJAX-запит на потрібну адресу
        $.get("/ajax_test/", function (data) {
            // Замінюємо текст тегу з id="target" на отримані дані
            $("#load_more").html(data.param1 + ' ' + data.param2);
        });
    });
});

