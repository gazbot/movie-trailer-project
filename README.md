Overview
--------
Fresh Tomatoes provides a way for users to store their favourite
movies in one spot and can be used to show movie trailers to other
people who may not have seen your favourite movie.


Requirements
------------
movies.json is populated with movie details and associated information 
you want displayed on the fresh tomatoes website in valid JSON format. 
Adhere to the format in the default movies.json file provided.


Instructions
============
Load the Fresh Tomatoes website by executing the following command

$ python entertainment_centre.py

This will load your current default web browser and point it to the
Fresh Tomatoes website that is built with the data provided in the
movies.json file.


Files provided
--------------
entertainment_center.py - Loads in the JSON data and provides it to
                          the fresh_tomatoes.py HTML generator.
media.py - Class definition of media and movie objects.
person.py - Class definition of person and director objects.
fresh_tomatoes.py - Creates the html page for display.
movies.json - Contains movie data to be displayed on the website.
