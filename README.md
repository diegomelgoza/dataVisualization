# dataVisualization
Using Python to work with data.

# Dice
- dice_visual asks the user two questions. How many sides their dice should have and how many rolls they want analyzed. Since we are 
  taking user input I stored them into two variables which we will use throughtout the program. We have the class Die() written in its
  file called 'die.py'. We initialize num_sides and then the roll() method uses the randint() function to return a random number bewteen 
  1 and the number of sides. We come back to the data_visual file and make the rolls annd store the results in a list. Then we analyze 
  the frequency of the rolls and make a visual chart using pygal. We can't fix the x-axis to a set list since we ask the user for the
  number of sides. So we create a new list that will contain and display the correct amount of x values. Finally we render the chart to 
  an SVG file which can then be viewed.
  
# Random Walk
- Python generates data for a random walk and uses matplotlib to create a representation of the gennerated data. The green dot represents 
  the starting point and the red dot represents the end point. The path goes from light blue to dark blue which shows the path that was 
  made.
  
  
