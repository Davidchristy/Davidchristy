/*
* This is to cover mousing over an item on the menu
* on the main screen.
*
* */

$(document).ready(function() {
    $('.home .homeLink').hover(function () {
        $('.home .homeLink').addClass('active');
        $('.home .projectLink').addClass('inactive');
        $('.home .contentLink').addClass('inactive');
        $('.home .aboutLink').addClass('inactive');

    }, function () {
        $('.home .homeLink').removeClass('active');
        $('.home .projectLink').removeClass('inactive');
        $('.home .contentLink').removeClass('inactive');
        $('.home .aboutLink').removeClass('inactive');
    });

    $('.home .projectLink').hover(function () {
        $('.home .projectLink').addClass('active');
        $('.home .homeLink').addClass('inactive');
        $('.home .contentLink').addClass('inactive');
        $('.home .aboutLink').addClass('inactive');

    }, function () {
        $('.home .projectLink').removeClass('active');
        $('.home .homeLink').removeClass('inactive');
        $('.home .contentLink').removeClass('inactive');
        $('.home .aboutLink').removeClass('inactive');

    });

    $('.home .contentLink').hover(function () {
        $('.home .contentLink').addClass('active');
        $('.home .projectLink').addClass('inactive');
        $('.home .homeLink').addClass('inactive');
        $('.home .aboutLink').addClass('inactive');

    }, function () {
        $('.home .contentLink').removeClass('active');
        $('.home .projectLink').removeClass('inactive');
        $('.home .homeLink').removeClass('inactive');
        $('.home .aboutLink').removeClass('inactive');
    });
    $('.home .aboutLink').hover(function () {
        $('.home .aboutLink').addClass('active');
        $('.home .contentLink').addClass('inactive');
        $('.home .projectLink').addClass('inactive');
        $('.home .homeLink').addClass('inactive');

    }, function () {
        $('.home .aboutLink').removeClass('active');
        $('.home .contentLink').removeClass('inactive');
        $('.home .projectLink').removeClass('inactive');
        $('.home .homeLink').removeClass('inactive');
    });



/*
* This will be to cover when a menu item is clicked on
* it will move the menu up and display the section clicked
* */

    $(".homeLink").click(function(){
        //Change the header
        $('header').removeClass('detailed');
        $('header').addClass('home');

        //Reset the menu
        $(".projectLink").removeClass("active");
        $(".contentLink").removeClass("active");
        $(".aboutLink").removeClass("active");

        //Hide the section
        $("projects").addClass("hidden");
        $("contact").addClass("hidden");
        $("about").addClass("hidden");
    })

    $(".aboutLink").click(function(){
        /*If the project link is clicked,
         * This check to see if the details page
         * is active, and makes it so if not*/
        if(! $( "header" ).hasClass( "detailed" )){
            $('header').addClass('detailed');
            $('header').removeClass('home');
        }
        //Remove hidden from yourself
        $("about").removeClass("hidden");

        //Add class hidden to everything else
        $("contact").addClass("hidden");
        $("projects").addClass("hidden");

        //Change the menu active or not
        $(".aboutLink").addClass("active");
        $(".contentLink").removeClass("active");
        $(".projectLink").removeClass("active");

        /*Here I will load the rest of the info*/
        $('about').load('about.html #detailed_about_info');
    });


    $(".projectLink").click(function(){
        /*If the project link is clicked,
        * This check to see if the details page
        * is active, and makes it so if not*/
        if(! $( "header" ).hasClass( "detailed" )){
            $('header').addClass('detailed');
            $('header').removeClass('home');
        }

        //Add class hidden to everything else
        $("contact").addClass("hidden");
        $("about").addClass("hidden");

        //Remove hidden from yourself
        $("projects").removeClass("hidden");

        //Change the menu active or not
        $(".projectLink").addClass("active");
        $(".contentLink").removeClass("active");
        $(".aboutLink").removeClass("active");

    /*Here I will load the rest of the info*/
        $('projects').load('projects.html #detailed_project_info');
    })

    $(".contentLink").click(function(){
        /*If the project link is clicked,
         * This check to see if the details page
         * is active, and makes it so if not*/
        if(! $( "header" ).hasClass( "detailed" )){
            $('header').addClass('detailed');
            $('header').removeClass('home');
        }

        //Add class hidden to everything else
        $("projects").addClass("hidden");
        $("about").addClass("hidden");

        //Removve hidden from yourself
        $("contact").removeClass("hidden");

        //Change the menu active or not
        $(".contentLink").addClass("active");
        $(".projectLink").removeClass("active");
        $(".aboutLink").removeClass("active");

        /*Here I will load the rest of the info*/
        $('contact').load('contact.html #detailed_contact');
    })

});
