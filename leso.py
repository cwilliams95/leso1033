import sys
import numpy
import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox

data = read_csv('data/out_FL.csv')
bb = BoundingBox.from_points(lons=data['lon'], lats=data['lat'])
geoplotlib.dot(data)
geoplotlib.show()