import sys
import numpy
import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox
from geoplotlib.colors import ColorMap

data = read_csv('data/out_FL.csv')
#TODO: apply filtering here rather than when making the csv
bb = BoundingBox.from_points(lons=data['lon'], lats=data['lat'])

#TODO: utilize layers
#mark the station locations
geoplotlib.dot(data,color=[0,0,0,255])

#TODO: show based on zoom level
#geoplotlib.labels(data,'Station Name (LEA)', color=[150,150,190,255], font_size=9, anchor_x='center')

#geoplotlib.voronoi(data, cmap='Blues_r', max_area=8e3, alpha=200, f_tooltip=lambda d:d['Station Name (LEA)'] )

geoplotlib.kde(data, cmap='Blues_r', bw=10, cut_below=1e-4, scaling='lin')

#geoplotlib.delaunay(data,cmap='hot_r')

##post
geoplotlib.set_bbox(bb)
geoplotlib.set_smoothing(True)
geoplotlib.show()