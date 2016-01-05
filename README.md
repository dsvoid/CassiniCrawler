# CassiniCrawler
Cassini image crawler written in python.

Downloads NASA photos from the Cassini satellite orbiting Saturn.
This program iteratively downloads these photos by imageID (example: http://saturn.jpl.nasa.gov/photos/raw/rawimagedetails/index.cfm?imageID=360), which starts from 1 on NASA's website.

## Use
```
python CassiniCrawler.py [starting imageID][number of images to download][destination folder for images]
```

For example, ```python CassiniCrawler.py 1 1000 ~/Downloads/cassini``` will download images corresponding to imageIDs 1 to 1000 to the folder ~/Downloads/cassini.
