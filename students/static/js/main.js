/**
 * Created by dgaievskyi on 14.07.2015.
 */


$(document).ready(function () {
    // Посилання з id="test" буде тригером події
    $("#load_more").click(function () {
        // AJAX-запит на потрібну адресу
        $.ajax({
            url: 'ajax/test.html',
            success: function () {
                alert('Load was performed.');
            },
            error: function () {
                alert('Load was NOT performed.');
            }
        });
    });
});

