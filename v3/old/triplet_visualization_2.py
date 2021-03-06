import matplotlib.pyplot as plt
import numpy as np


def remove_values_along_axes():
    from matplotlib import pylab
    frame = pylab.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])


def get_coordinates_from_cosine_similarity(cos_sim):
    cosine_similarities = np.linspace(1, -1, 100)
    i = np.argmin(np.square(cosine_similarities - cos_sim))
    x, y = find_all_x_y_along_circle()
    return x[i], y[i]


def find_all_x_y_along_circle():
    theta = np.linspace(0, 2 * np.pi, 100)

    # the radius of the circle
    r = np.sqrt(1)

    # compute x1 and x2
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)
    return x1, x2


def newline(p1, p2, color):
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines
    ax = plt.gca()
    x_min = p1[0]
    x_max = p1[1]
    y_min = p2[0]
    y_max = p2[1]
    print([x_min, x_max], [y_min, y_max])
    l = mlines.Line2D([x_min, x_max], [y_min, y_max], color=color, linestyle='dashdot', linewidth=3)
    ax.add_line(l)
    return l


plt.ion()
plt.xlim(-1, 1)
plt.ylim(-1, 1)
xs, ys = find_all_x_y_along_circle()
plt.scatter(xs, ys)
for cos_sim in np.linspace(1, -1, 100):
    x_i, y_i = get_coordinates_from_cosine_similarity(cos_sim)
    newline([0, x_i], [0, y_i], color='green')
    plt.draw()
    plt.pause(0.0001)

# xs, ys = find_all_x_y_along_circle()
# plt.scatter(xs, ys)
#
# plt.ion()
# for i in range(len(xs)):
#     x_i = xs[i]
#     y_i = ys[i]
#     newline([0, x_i], [0, y_i], color='green' if i % 2 ==0 else 'red')
#     plt.draw()
#     plt.pause(0.0001)

# plt.scatter([1], [1], s=10000, facecolors='none', color=['black'], linewidth=3)
newline([0, 0], [1, 1], color='green')
newline([0, 0.5], [1, 0.5], color='blue')
newline([0.5, 0], [0.5, 1], color='red')
newline([0, 1], [1, 0], color='yellow')

remove_values_along_axes()
# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
plt.show()
