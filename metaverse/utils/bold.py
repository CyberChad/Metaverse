import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
from PIL import Image


#2D Gaussian function
def twoD_Gaussian(x, y, xo, yo, sigma_x, sigma_y):
    a = 1./(2*sigma_x**2) + 1./(2*sigma_y**2)
    c = 1./(2*sigma_x**2) + 1./(2*sigma_y**2)
    g = np.exp( - (a*((x-xo)**2) + c*((y-yo)**2)))
    return g.ravel()


def transparent_cmap(cmap, N=255):
    "Copy colormap and set alpha values"

    mycmap = cmap
    mycmap._init()
    mycmap._lut[:,-1] = np.linspace(0, 0.8, N+4)
    return mycmap


#Use base cmap to create transparent
DM_cmap = transparent_cmap(plt.cm.Reds) #Red
PM_cmap = transparent_cmap(plt.cm.Blues) #Blue
WM_cmap = transparent_cmap(plt.cm.Oranges) #Brownish

# create yellow colormaps
N = 256
yellow = np.ones((N, 4))
yellow[:, 0] = np.linspace(255/256, 1, N) # R = 255
yellow[:, 1] = np.linspace(232/256, 1, N) # G = 232
yellow[:, 2] = np.linspace(11/256, 1, N)  # B = 11

yellow_cmp = ListedColormap(yellow)
yellow_cmp2 = ListedColormap(yellow)

Visual_cmap = transparent_cmap(yellow_cmp) #Yellow

Motor_cmap = transparent_cmap(plt.cm.Greens) #Green


# Import image and get x and y extents
brain_top = Image.open('./brain.jpg')
#brain_side = Image.open('./brain_side.jpg')
p = np.asarray(brain_top).astype('float')
w, h = brain_top.size
y, x = np.mgrid[0:h, 0:w]

#Plot image and overlay colormap
fig, ax = plt.subplots(1, 1)
ax.imshow(brain_top)

DMGaussL = twoD_Gaussian(x, y, .3*x.max(), .3*y.max(), .05*x.max(), .05*y.max())
DMGaussR = twoD_Gaussian(x, y, .7*x.max(), .3*y.max(), .05*x.max(), .05*y.max())

PMGaussL = twoD_Gaussian(x, y, .4*x.max(), .4*y.max(), .05*x.max(), .05*y.max())
PMGaussR = twoD_Gaussian(x, y, .6*x.max(), .4*y.max(), .05*x.max(), .05*y.max())

WMGaussL = twoD_Gaussian(x, y, .45*x.max(), .5*y.max(), .05*x.max(), .05*y.max())
WMGaussR = twoD_Gaussian(x, y, .55*x.max(), .5*y.max(), .05*x.max(), .05*y.max())

MotorGaussL = twoD_Gaussian(x, y, .4*x.max(), .7*y.max(), .05*x.max(), .05*y.max())
MotorGaussR = twoD_Gaussian(x, y, .6*x.max(), .7*y.max(), .05*x.max(), .05*y.max())

VisualGaussL = twoD_Gaussian(x, y, .45*x.max(), .9*y.max(), .05*x.max(), .05*y.max())
VisualGaussR = twoD_Gaussian(x, y, .55*x.max(), .9*y.max(), .05*x.max(), .05*y.max())

DM_cbL = ax.contourf(x, y, DMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=DM_cmap)
DM_cbR = ax.contourf(x, y, DMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=DM_cmap)

PM_cbL = ax.contourf(x, y, PMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=PM_cmap)
PM_cbR = ax.contourf(x, y, PMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=PM_cmap)

WM_cbL = ax.contourf(x, y, WMGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=WM_cmap)
WM_cbR = ax.contourf(x, y, WMGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=WM_cmap)

Motor_cbL = ax.contourf(x, y, MotorGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=Motor_cmap)
Motor_cbR = ax.contourf(x, y, MotorGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=Motor_cmap)

Vis_cbL = ax.contourf(x, y, VisualGaussL.reshape(x.shape[0], y.shape[1]), 15, cmap=Visual_cmap)
Vis_cbR = ax.contourf(x, y, VisualGaussR.reshape(x.shape[0], y.shape[1]), 15, cmap=Visual_cmap)

# plt.colorbar(DM_cb)
# plt.colorbar(PM_cb)
# plt.colorbar(WM_cb)
# plt.colorbar(Vis_cb)
# plt.colorbar(Motor_cb)

plt.show()





