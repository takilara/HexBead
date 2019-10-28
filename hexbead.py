import argparse
parser = argparse.ArgumentParser(description='Convert an image to a "hexbinplot" so that it can be used for Perler patterns.')
parser.add_argument('inputfile',
                    help='The file to process.')
parser.add_argument('outputfile',
                    help='The filename for the outputfile.')
                    
parser.add_argument('--colors', dest='colorcount', default=16, type=int, 
                    help='Number of colors to use.')
parser.add_argument('--size', dest='size', default=20, type=int,
                    help='Number of "rows and columns" to use.')
parser.add_argument('--mode', dest='interpolationmode', default="mode",
                    help='Commaseparated list of averaging modes to use. Options include [mode,median,all]. \
                    (Note that if more than one, or "all" is chosen, then the mode will be appended to the outputfilename.')
                    


args = parser.parse_args()

avgmodes = []
if "all" in args.interpolationmode or "mode" in args.interpolationmode:
    avgmodes.append("mode")
if "all" in args.interpolationmode or "median" in args.interpolationmode:
    avgmodes.append("median")

#print(args)
#exit()

#do heavy imports later
import pandas as pd
import numpy as np
from scipy import stats
import cv2

import matplotlib.pyplot as plt

from PIL import Image
from matplotlib.colors import LinearSegmentedColormap,ListedColormap

def mode(a):
    return stats.mode(a)[0][0]

def meanInt(a):
    return round(np.mean(a))





colorcount=args.colorcount
size=args.size
inFile = args.inputfile
im = Image.open(inFile)
#im = Image.open("pikachu.jpg")
#im = Image.open("pokeball.png")
#im = im.resize((20,20), resample=0)
#im3 = im.quantize(colorcount)
im3= im.convert('P', palette=Image.ADAPTIVE, colors=16)

#fig, ax = plt.subplots(num="MRI_demo")
#ax.imshow(im3, cmap="gray")
#ax.axis('off')

#plt.show()
im2 = np.array(im3)
p = np.array(im3.getpalette()).reshape(256,3)
colorsUsed = []
for thecol in range(0,colorcount):
    red = p[thecol][0]/255.0
    green = p[thecol][1]/255.0
    blue = p[thecol][2]/255.0
    colorsUsed.append((red,green,blue))
    
    
# pull out X,Y and Color
x = []
y = []
c = []
c2 = []
c3 = []
for row in range(0,im2.shape[0]):
    for col in range(0,im2.shape[1]):
        y.append(row)
        x.append(col)
        c.append(im2[row,col])
y.reverse()


# setup Colormap

bins = colorcount
cm = LinearSegmentedColormap.from_list('rgb', colorsUsed, N=bins)


# Plot the figure
df = pd.DataFrame({'x':x, 'y':y, 'c':c})

outFileA = args.outputfile.split(".")
#print(outFileA)
extension = outFileA[-1]
outFile = ".".join(outFileA[0:-1])
#print(outFile,extension)

#print(avgmodes)

if "median" in avgmodes:
    medPlot = df.plot.hexbin(x='x', y='y',C='c',gridsize=size, figsize=(13,13), colorbar=False, cmap=cm ,reduce_C_function=np.median,vmin=0,vmax=colorcount,linewidths=0.5, edgecolor="white")
    figMed = medPlot.get_figure()
    if len(avgmodes)>1:
        figMed.savefig("{}_median.{}".format(outFile,extension))
    else:
        figMed.savefig("{}.{}".format(outFile,extension))
if "mode" in avgmodes:        
    modePlot = df.plot.hexbin(x='x', y='y',C='c',gridsize=size, figsize=(13,13), cmap=cm ,colorbar=False, reduce_C_function=mode,vmin=0,vmax=colorcount,linewidths=0.5, edgecolor="white")
    figMode = modePlot.get_figure()

    if len(avgmodes)>1:
        figMode.savefig("{}_mode.{}".format(outFile,extension))
    else:
        figMode.savefig("{}.{}".format(outFile,extension))
