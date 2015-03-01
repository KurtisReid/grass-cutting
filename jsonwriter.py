import webbrowser

data_file = open("Title.txt", "r")
new_file = open("jsontxttest.geojson", "w")
print('''{
  "type": "FeatureCollection",\n\t"features": [''', file = new_file)
count=num=pos=0
coordinates = []
for line in data_file:
    latitude = line[:4]
    longitude = line[4:]
    latitude = latitude.replace(" ","")
    longitude = longitude.replace(" ","")
    latitude = latitude.replace("0","")
    longitude = longitude.replace("0","")
    longitude1 = longitude.replace("\n","")
    coordinates += [float(latitude),float(longitude1)]
    print('''{
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Point",
        "coordinates": [
          ''',latitude,''',
          ''',longitude,'''
        ]
      }
    },''', file = new_file)
    count += 1
print('''{
    "type": "Feature",
    "properties": {},
    "geometry": {
    "type": "LineString",
    "coordinates": [
    ''', file = new_file)
while num < count:
    if num == count-1:
        print("[\n",coordinates[pos],",\n",coordinates[pos+1],"\n]\n", file = new_file)
    else:
        print("[\n",coordinates[pos],",\n",coordinates[pos+1],"\n],\n", file = new_file)
    pos += 2
    num += 1
print(''']
}
}''', file = new_file)
print("\t]\n}", file = new_file)
new_file.close()
data_file.close()

url = "http://geojson.io/"
webbrowser.open(url, new = 0, autoraise=True)
