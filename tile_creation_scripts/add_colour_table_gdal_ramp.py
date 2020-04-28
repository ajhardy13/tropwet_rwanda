import gdal, glob, subprocess

'''
use this script to add a colour table to a raster, 
necessary before extracxting tiles. In this instance
this is a single band raster with a colour ramp for
% frequency indundation. Note that image needed to be 
converted to a byte first

'''

listFiles=glob.glob('/Users/Andy/Documents/Rwanda/Data/TropWet_Outputs/TW_v7.2/Percentage*')

for fn in listFiles:

#fn = '/Users/Andy/Documents/Rwanda/Data/TropWet_Outputs/TW_v7.2/Classified_Output_April_to_June_2016_to_2020.tif'
	print('processing: ' + fn)
	
	fn_byte = fn.replace('.tif','_byte.tif') 
	
	# convert to byte first
	cmd="gdal_translate -of GTIFF -ot Byte '%s' '%s'" %(fn, fn_byte)
	subprocess.call(cmd, shell=True)
	
	ds = gdal.Open(fn_byte, 1)
	band = ds.GetRasterBand(1)

	# create color table
	colors = gdal.ColorTable()

	# set color for each value
	colors.CreateColorRamp(0, (255, 255, 204), 25, (161, 218, 180))
	colors.CreateColorRamp( 25, (161, 218, 180), 50, (65, 182, 196))
	colors.CreateColorRamp(50, (65, 182, 196), 75, (44, 127, 184))
	colors.CreateColorRamp(75, (44, 127, 184), 100, (37, 52, 148))


	# set color table and color interpretation
	band.SetRasterColorTable(colors)
	band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)

	# close and save file
	del band, ds