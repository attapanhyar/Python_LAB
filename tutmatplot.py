import matplotlib.pyplot as plt
import numpy as np
### Simple Plot
# Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.cos(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()

#########################################################
####STEM PLOT
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0.1, 2 * np.pi, 41)
# y = np.exp(np.sin(x))

# plt.stem(x, y)
# plt.show()


###############################################
### Pie Chart
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Aqib', 'Ali', 'Shahbaz', 'Saad'
sizes = [1500, 3000, 4500, 1000]
explode = (0, 0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



###############################################################################################
#### Plot a bar chat
# N = 5
# menMeans = (20, 35, 30, 35, -27)
# womenMeans = (25, 32, 34, 20, -25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)    # the x locations for the groups
# width = 0.35       # the width of the bars: can also be len(x) sequence
# fig, ax = plt.subplots()

# p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
# p2 = ax.bar(ind, womenMeans, width,
#             bottom=menMeans, yerr=womenStd, label='Women')
# ax.axhline(0, color='grey', linewidth=0.8)
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
# ax.legend()
# # Label with label_type 'center' instead of the default 'edge'
# ax.bar_label(p1, label_type='center')
# ax.bar_label(p2, label_type='center')
# ax.bar_label(p2)
# plt.show()
###########################################################
##### Line Plot###########
# x = np.linspace(0, 10, 500)
# y = np.cos(x)

# fig, ax = plt.subplots()

# # Using set_dashes() to modify dashing of an existing line
# line1, = ax.plot(x, y, label='Using set_dashes()')
# line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
# # Using plot(..., dashes=...) to set the dashing when creating a line
# line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')
# ax.legend()
# plt.show()

######################################################
##  stream Plot
# import matplotlib.gridspec as gridspec

# w = 3
# Y, X = np.mgrid[-w:w:100j, -w:w:100j]
# U = -1 - X**2 + Y
# V = 1 + X - Y**2
# speed = np.sqrt(U**2 + V**2)

# fig = plt.figure(figsize=(7, 9))
# gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

# #  Varying density along a streamline
# ax0 = fig.add_subplot(gs[0, 0])
# ax0.streamplot(X, Y, U, V, density=[0.5, 1])
# ax0.set_title('Varying Density')

# # Varying color along a streamline
# ax1 = fig.add_subplot(gs[0, 1])
# strm = ax1.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
# fig.colorbar(strm.lines)
# ax1.set_title('Varying Color')

# #  Varying line width along a streamline
# ax2 = fig.add_subplot(gs[1, 0])
# lw = 5*speed / speed.max()
# ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
# ax2.set_title('Varying Line Width')

# # Controlling the starting points of the streamlines
# seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1,  0, 1, 2, 2]])

# ax3 = fig.add_subplot(gs[1, 1])
# strm = ax3.streamplot(X, Y, U, V, color=U, linewidth=2,
#                       cmap='autumn', start_points=seed_points.T)
# fig.colorbar(strm.lines)
# ax3.set_title('Controlling Starting Points')

# # Displaying the starting points with blue symbols.
# ax3.plot(seed_points[0], seed_points[1], 'bo')
# ax3.set(xlim=(-w, w), ylim=(-w, w))

# # Create a mask
# mask = np.zeros(U.shape, dtype=bool)
# mask[40:60, 40:60] = True
# U[:20, :20] = np.nan
# U = np.ma.array(U, mask=mask)

# ax4 = fig.add_subplot(gs[2:, :])
# ax4.streamplot(X, Y, U, V, color='r')
# ax4.set_title('Streamplot with Masking')

# ax4.imshow(~mask, extent=(-w, w, -w, w), alpha=0.5, cmap='gray', aspect='auto')
# ax4.set_aspect('equal')

# plt.tight_layout()
# plt.show()

############################################
### Dipole Pattern

from matplotlib.tri import (
    Triangulation, UniformTriRefiner, CubicTriInterpolator)



# ----------------------------------------------------------------------------
# Electrical potential of a dipole
# ----------------------------------------------------------------------------
# def dipole_potential(x, y):
#     """The electric dipole potential V, at position *x*, *y*."""
#     r_sq = x**2 + y**2
#     theta = np.arctan2(y, x)
#     z = np.cos(theta)/r_sq
#     return (np.max(z) - z) / (np.max(z) - np.min(z))


# ----------------------------------------------------------------------------
# Creating a Triangulation
# ----------------------------------------------------------------------------
# First create the x and y coordinates of the points.
# n_angles = 30
# n_radii = 10
# min_radius = 0.2
# radii = np.linspace(min_radius, 0.95, n_radii)

# angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
# angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
# angles[:, 1::2] += np.pi / n_angles

# x = (radii*np.cos(angles)).flatten()
# y = (radii*np.sin(angles)).flatten()
# V = dipole_potential(x, y)

# # Create the Triangulation; no triangles specified so Delaunay triangulation
# # created.
# triang = Triangulation(x, y)

# # Mask off unwanted triangles.
# triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
#                          y[triang.triangles].mean(axis=1))
#                 < min_radius)

# # ----------------------------------------------------------------------------
# # Refine data - interpolates the electrical potential V
# # ----------------------------------------------------------------------------
# refiner = UniformTriRefiner(triang)
# tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)

# # ----------------------------------------------------------------------------
# # Computes the electrical field (Ex, Ey) as gradient of electrical potential
# # ----------------------------------------------------------------------------
# tci = CubicTriInterpolator(triang, -V)
# # Gradient requested here at the mesh nodes but could be anywhere else:
# (Ex, Ey) = tci.gradient(triang.x, triang.y)
# E_norm = np.sqrt(Ex**2 + Ey**2)

# # ----------------------------------------------------------------------------
# # Plot the triangulation, the potential iso-contours and the vector field
# # ----------------------------------------------------------------------------
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# # Enforce the margins, and enlarge them to give room for the vectors.
# ax.use_sticky_edges = False
# ax.margins(0.07)

# ax.triplot(triang, color='0.8')

# levels = np.arange(0., 1., 0.01)
# ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
#               linewidths=[2.0, 1.0, 1.0, 1.0])
# # Plots direction of the electrical vector field
# ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
#           units='xy', scale=10., zorder=3, color='blue',
#           width=0.007, headwidth=3., headlength=4.)

# ax.set_title('Gradient plot: an electrical dipole')
# plt.show()

