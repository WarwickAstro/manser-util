import numpy as np
import astropy.io.fits as fits
import os
# CHANGE THIS TO THE PATH FOR THE REDUCED DATA
path = '/Volumes/Storage/PhD_files/gas_disc_work/SDSS0738+1835/reflex_end_products/2017-10-23T13:02:11/'
if not os.path.exists(path + 'complete_data'):
  os.makedirs(path + 'complete_data')
# Selects all filenames from README
f=open(path + 'README')
lines=f.readlines()
for i in range(len(lines)):
  if (lines[i][0] == '/'): #Checks line in README is a filepath.
    file_name = lines[i].split()[0]
    if (file_name.find('IDP') != -1 ): # Selects science data files.
      hdulist = fits.open(file_name)
      data = hdulist[1].data[0] 
      vel = hdulist[0].header['HIERARCH ESO QC VRAD HELICOR'] #Heliocentric cor
      obj = hdulist[0].header['OBJECT'] # Object name for final file name
      wav, flux, err = data[0]*(1.0 + (vel/3.0E5)), data[1], data[2]  
      date = hdulist[0].header['DATE-OBS'] # t_o_o = time of obs, used in fname
      t_o_o = date[:4] + date[5:7] + date[8:10] + date[10:13] + date[14:16] + date[17:19]
      colour = file_name[-8:-5] # UVB, VIS or NIR
      sav_dat = np.transpose(np.vstack((wav, flux, err)))
      name = obj + '-Xshoo-' + t_o_o + '-' + colour + '.dat'
      save_path = path + 'complete_data/'  # Change to location of output files
      np.savetxt( save_path + name, sav_dat)
      #exptime = hdulist[0].header['EXPTIME']
      #texptime = hdulist[0].header['TEXPTIME']
      #print name + ' saved.' , 'exptime = ', exptime, 'totalexptime = ', texptime 
      #print 'RESOLUTION =', hdulist[0].header['SPEC_RES']
