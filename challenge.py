import tsp
import json
import matplotlib.pyplot as plt



# Load the data
with open('data/att48.json') as f:
    data = json.load(f)['points']

# Get the greedy and the 2opt routes
g = tsp.greedy(data)
a = tsp.multi_opt2_anne(100000, data) # 100k=12s on 2,6 GHz Intel Core i5

# Print distances to see diference
print tsp.total_distance(g), '<-- Total distance of greedy function.'
print tsp.total_distance(a), '<-- Total distance of 2opt + sanneling function.'

# Plot the 2opt + simulated anneling
a = tsp.to_xy(a)
plt.plot(a[0], a[1], '.b-')
plt.axis([0, 8000, 0, 6000])
plt.show()