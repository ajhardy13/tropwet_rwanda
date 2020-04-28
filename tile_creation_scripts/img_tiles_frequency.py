import rsgislib, glob, subprocess
import rsgislib.imageutils
'''
use this script to convert a single band raster 
(continuous data for instance % frequency inundation)
into tiles. Need to add colour table first

'''


												 
											


listFiles=glob.glob('Percent*_byte.tif')

for input_img in listFiles:
	
	print('Processing: '  + input_img)

	band_sel_img = input_img

	#output stretched img
	stch_img = './stretched/' + input_img.replace('.tif','_stretch.tif') 
	
	cmd="gdal_translate -of GTIFF -ot Byte -expand rgb '%s' '%s'" %(input_img, stch_img)
	subprocess.call(cmd, shell=True)
	

	outFolder = './stretched/tiles_'+input_img.split('.')[0]

	cmd="gdal2tiles.py -z 1-14 -w none  '%s' '%s'" %(stch_img, outFolder)
	subprocess.call(cmd, shell=True)