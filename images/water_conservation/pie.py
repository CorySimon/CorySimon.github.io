import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
import matplotlib
matplotlib.rc('font', size=15)
matplotlib.rc('axes', facecolor='w')

# The slices will be ordered and plotted counter-clockwise.
labels = ['Domestic consumption', 'Industrial products', 'Agriculture']
 # sizes = [80., 242., 1735.]
sizes = [324, 400, 7404+913+46] # pnas water foot print of humanity
colors = ['yellowgreen', 'gold', 'lightskyblue']
explode = (0.00, 0.0, 0.0) # only "explode" the 2nd slice (i.e. 'Hogs')
fig = plt.figure(facecolor='w')
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%d%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.savefig("wateruse.png", format="png", dpi=300, facecolor=fig.get_facecolor())

plt.show()
