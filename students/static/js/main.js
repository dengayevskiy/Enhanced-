/**
 * Created by dgaievskyi on 14.07.2015.
 */

$('#load_more').on('click', function (event) {
    event.preventDefault();
    console.log("Students are loaded!");  // sanity check
    create_post();
});

function create_post() {
    console.log("create post is working!"); // sanity check
    console.log($('#h2').val())
}