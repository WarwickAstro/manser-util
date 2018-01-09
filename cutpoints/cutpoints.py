"""
A program to cut points from a spectrum. The features used in matplotlib
overwrite the rectangular selection used by this script so you can zoom
in on a specific region you wish to cut. The program will cut any points
that are within the boxed area, and then replot the data. If you make a 
mistake, you can restart by pressing 'u'

###############
SETTING UP DATA
###############

The input data is read in from a directory called 'file_name' and the data
file 'name'. data output is stored as sav_dat, with the location of the 
saved file being 'sav_name = filepath + ???' where ??? is the name of the 
output file

Feel free to edit this or make the input command line arguements.

########
CONTROLS
########

If you wish to undo any changes made, press 'u' and make the same selection
over the region you want to undo, and the program will set all points in 
this region back to the original spectrum. Press 'i' to change back to 
cutting points.

You can also press q and a to stop and activate the rectangle selection
respectively.

Also, try commenting out the line 'matplotlib.use('tkagg')' as I have 
only included this to stop the program from not working on my Mac.
"""

from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib
matplotlib.use('tkagg') # try hashing out
import matplotlib.pyplot as plt
  
undo = 0

def print_help():
  print('Box areas you wish to cut out of the plot.')
  print('Press q to deactivate the rectangle selector.')
  print('Press a to reactivate the rectangle selector.')
  print('Press a to reactivate the cutting region.')
  print('Press h to redisplay this message.')

def line_select_callback(eclick, erelease):
    global undo, wav2, flux2, err2
    '''eclick and erelease are the press and release events'''
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    if x2 < x1: cutx1, cutx2 = x2, x1
    else:       cutx1, cutx2 = x1, x2
    if y2 < y1: cuty1, cuty2 = y2, y1
    else:       cuty1, cuty2 = y1, y2
    print("(%3.2f) --> (%3.2f)" % (cutx1, cutx2))
    print("(%3.2f) --> (%3.2f)" % (cuty1, cuty2))
    element1 = np.where(wav2 == min( wav2[(wav2 > cutx1) & (wav2 < cutx2)] ))
    element2 = np.where(wav2 == max( wav2[(wav2 > cutx1) & (wav2 < cutx2)] ))
    x1, x2 = wav2[element1], wav2[element2]
    y1, y2 = flux2[element1], flux2[element2]
    if undo == 0:
      condition = ((wav2 > cutx1) & (wav2 < cutx2) & (flux2 > cuty1) & (flux2 < cuty2))
      condition = np.invert(condition)
      ftmp = flux2[condition]
      wtmp = wav2[condition]
      etmp = err2[condition]
      flux2 = ftmp
      err2 = etmp
      wav2 = wtmp
    if undo == 1:
      for j in xrange(wav.size):
        if ((wav2[j] > cutx1) & (wav2[j] < cutx2)):
          flux2[j] = flux[j]
    line.set_data(wav2,flux2)
    plt.draw()

def toggle_selector(event):
    global undo, wav2, flux2, err2
    print(' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print(' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print(' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)
    if event.key in ['U', 'u']:
        tmp = wav.size
        wav2, flux2, err2 = np.zeros(tmp), np.zeros(tmp), np.zeros(tmp)
        wav2[:], flux2[:], err2[:] = wav, flux, err
        flux2 = np.zeros(flux.size)
        line.set_data(wav2,flux2)
        plt.draw()
        print('Undone changes.')
    if event.key in ['I', 'i']:
        undo = 0
        print('Cutting mode active.')
        print(undo)
    if event.key in ['H', 'h']:
        print_help() 
               
###############################################
#############        Main        ##############
###############################################

print_help()

# Data setup
file_path = '/home/astro/phukfh/'
name = 'SDSSJ122859.93+104032.9_52725-1231-0617.dat'
data = np.genfromtxt(file_path + name)
wav, flux, err = data[:,0], data[:,1], data[:,2]
tmp = wav.size
wav2, flux2, err2 = np.zeros(tmp), np.zeros(tmp), np.zeros(tmp)
wav2[:], flux2[:], err2[:] = wav, flux, err

# Runs matplotlib with interactiability
fig, current_ax = plt.subplots() 
line, = plt.plot(wav2, flux2, lw=0.5, c='k')
toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1,3],
                                       minspanx=5, minspany=5,
                                       spancoords='pixels')
plt.connect('key_press_event', toggle_selector)
plt.show()

# When the plot is closed, saves modified file.
sav_dat = np.transpose(np.vstack((wav2,flux2,err2)))
sav_name = file_path + name[:-4] + '_cutpoints.dat'
print(sav_name)
#np.savetxt(sav_name, sav_dat)
