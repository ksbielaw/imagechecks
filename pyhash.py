import hashlib
import random
import urllib

extList = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generateUrl():
	imageUrl = "http://i.imgur.com/"
	for i in range(0,7):
		letter = extList[random.randint(0,61)]
		imageUrl = imageUrl + letter

	imageUrl = imageUrl + ".jpg"
	return imageUrl

imageExists = 0
blankUrls = 0

removedImage = 'd835884373f4d6c8f24742ceabe74946'

def checkUrl(f):
	myUrl = generateUrl()
#	imageUrl = "http://i.imgur.com/abcdefg.jpg"
	image_file = urllib.urlopen(myUrl).read()
	if hashlib.md5(image_file).hexdigest() == removedImage:
		global blankUrls
		blankUrls = blankUrls + 1
	else:
		global imageExists
		imageExists = imageExists + 1
		f.write('url : '+ myUrl + '\n hash : '+str(hashlib.md5(image_file).hexdigest()) + '\n \n')
	return blankUrls, imageExists

def runUrls(max):
	f = open('urllist','w')
	for i in range(0,max):
		checkUrl(f)
	blankUrls, imageExists = checkUrl(f)
	f.write('blanks: ' + str(blankUrls)+'\n exists: '+str(imageExists))
	f.close()

runUrls(10000)