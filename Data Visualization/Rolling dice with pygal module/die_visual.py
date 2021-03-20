from die import Die
import pygal

#Create a D6 amd D10
die_1 = Die()
die_2 = Die(10)

#Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


#Analize the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#Visualize the results
hist = pygal.Bar()

hist.title = 'Result of rolling a D6 and D10 50000 times'
hist.xlabels = ['1''2', '3','4','5','6','7''8', '9','10','11','12','13','14','15','16']
hist.xtitle = 'Result'
hist.ytitle = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

