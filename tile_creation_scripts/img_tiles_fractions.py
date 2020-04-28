import rsgislib, glob, subprocess
import rsgislib.imageutils

'''
use this script to convert a three band raster 
(in this instance fractions of water, veg and sand)
into tiles. Need to add colour table first. Note that
hashed out code is available for band selection if you
have a raster with more than three bands (e.g. landsat image).
Function is also added to apply a stretch if needed (typical
if you are using satellite imagery)

'''


listFiles=glob.glob('Fractions*.tif')

for input_img in listFiles:
	
	print('Processing: '  + input_img)


	#need to create new img if it is not already 3 band (ie. if doing a landsat composite)
	band_sel_img = input_img
#	band_sel_img = '/Users/Andy/Documents/Rwanda/Data/TropWet_Outputs/TW_v7.2/stretched/' + input_img.replace('.tif','_select.tif') 

#	rsgislib.imageutils.selectImageBands(input_img, band_sel_img, 'GTIFF', rsgislib.TYPE_16INT, [5,6,4])

	#output stretched img
	stch_img = './stretched/' + input_img.replace('.tif','_stretch.tif') 

	#function to stretch img
#	rsgislib.imageutils.stretchImage(input_img, stch_img, False, '', True, False, 'GTIFF', rsgislib.TYPE_8INT, rsgislib.imageutils.STRETCH_LINEARMINMAX)


	#use this to generate tiles after on command line
	outFolder = './stretched/tiles_'+input_img.split('.')[0]

	cmd="gdal2tiles.py -z 1-14 -w none  '%s' '%s'" %(stch_img, outFolder)
	subprocess.call(cmd, shell=True)