import pygal
from die import Die

# Create dice
num_sides = int(input("How many sides do you want your die? "))
num_rolls = int(input("How many rolls do you want analyzed? "))

die = Die(num_sides)

# Make some rolls, and store results in a list
results = []
for roll_num in range(num_rolls):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = f"Results of rolling choice of die {num_rolls} times."

# Get the correct x-axis
xaxis = []
for i in range(1, num_sides + 1):
    xaxis.append(i)
    
hist.x_labels = xaxis
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(f'D{die.num_sides}', frequencies)
hist.render_to_file('dice_visual.svg')
