# Assignment: Checkerboard
# Objectives:
Continue to learn how to pass information from the url to the route
Practice linking static files to templates
Get comfortable passing information from the route to the template
Understand how to use for loop properly in the template
Recognize the value of creating a html/css first and then adding logic/code

Now let's practice linking static files to our template. For this project, we'll render a template that displays a checkerboard:

# Your program should have the following output

* http://localhost:5000 - should display 8 by 8 checkerboard
* http://localhost:5000/4 - should display 8 by 4 checkerboard
* http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

HINT: Remember that values from urls come in as strings by default. If you want to use the value in a loop, you should convert it to an integer before passing it to Jinja.

* Create a new Flask project
* Have the root route render a template with a checkerboard on it
* Have the css in a separate stylesheet and link this to the template
* Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
* NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
* SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2