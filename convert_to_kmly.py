import csv

nem_csvf=r'NEM_DUIDs_with_geo.csv'
nem_kml=r'nem.kml'

with open(nem_csvf) as csvfile, open(nem_kml,'w') as kml:
  print >>kml, """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>SA Generators</name>
    <open>1</open>
    <description>Location of AEMO generators in SA https://www.aemo.com.au/Electricity/National-Electricity-Market-NEM/Participant-information/Current-participants/Current-registration-and-exemption-lists</description>
  """
  csvreader = csv.reader(csvfile)
  for row in csvreader:
        if 'SA1' not in row: continue
        print ', '.join([ row[x] for x in (14,18,19,21)])
        (duid,lat,lon)=(row[14],row[18],row[19])
        print >>kml,"""<Placemark>
        <name>%s</name>
        <Point>
        <coordinates>%s,%s,0</coordinates>
        </Point>
        </Placemark>""" % (duid,lon,lat)
  print >>kml, '''
 </Document>
</kml>
  '''
