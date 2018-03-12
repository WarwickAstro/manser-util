Requires: Numpy, astropy.io.fits

This program converts the output of the X-shooter reflext
reduction pipeline into ascii files.

It will read the directory the files are in, e.g.

somedirectory/reflex_end_products/2017-10-23T13:02:11/

and create a folder called complete_data

After this, it will read the README file and find the science
data and convert it into ascii files with columns:

wavelength, flux, flux_err

