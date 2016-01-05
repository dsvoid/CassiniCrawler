import urllib
import urllib2
import sys
import linecache

class CassiniCrawler:
	def __init__(self,dest):
		self.dest = str(dest)
		self.browseUrl = 'http://saturn.jpl.nasa.gov/photos/raw/rawimagedetails/index.cfm'
		self.rawUrl = 'http://saturn.jpl.nasa.gov/multimedia/images/raw/'
		self.rawUrlArg = ''
	
	def downloadImage(self, imageID):	
		postArgument = { 'imageID' : imageID }
		data = urllib.urlencode(postArgument)
		browseReq = urllib2.Request(self.browseUrl, data)
		response = urllib2.urlopen(browseReq)
		doc = response.readlines()
		for i in range(3600,4100):
			argumentIndex = doc[i].find('casJPGFull')
			if(argumentIndex != -1):
				self.rawUrlArg = doc[i][argumentIndex:argumentIndex+27]
				break
		image = urllib2.urlopen(self.rawUrl + self.rawUrlArg)
		imageDest = self.dest + "/" + ("%06d" % (imageID,)) + "_" + self.rawUrlArg[14:]
		with open(imageDest, "wb") as downloader:
			downloader.write(image.read())
		print("downloaded " + imageDest)
	
	def batchDownload(self,start,count):
		for i in range(count):
			self.downloadImage(start+i)
			
if __name__ == '__main__':
	args = sys.argv
	cc = CassiniCrawler(str(args[3]))
	cc.batchDownload(int(args[1]),int(args[2]))
