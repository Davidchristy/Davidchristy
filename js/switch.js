/**
 * Created by david on 4/25/15.
 */

$('body').click(function () {
    $("#mainArticle").load("./home.html");
    console.log("hi")
});

$('#navWrapProject').click(function () {
    $("#mainArticle").load("./project.html");
    console.log("hi")
});

$('#navWrapThoughts').click(function () {
    $("#mainArticle").load("./thoughts.html");
});

$('#navWrapProgramming').click(function () {
    $("#mainArticle").load("./programming.html");
});

$('#navWrapAbout').click(function () {
    $("#mainArticle").load("./about.html");
});
