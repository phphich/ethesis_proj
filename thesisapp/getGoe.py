from django.contrib.gis.geoip2 import GeoIP2

g = GeoIP2()
print("Latitude: ", g.lat_lon())
print("Longitude: ", g.lon_lat())
