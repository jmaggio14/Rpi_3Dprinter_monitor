import imagepypelines as ip
import cv2
import time
from getpass import getpass

cam = ip.blocks.CameraBlock(device="/dev/video0", mode='count')
data2stream = ip.blocks.Img2Stream()
ftp = ip.blocks.FTP(host="ftp.jeffmagg.io",
                    user="aplab@jeffmagg.io",
                    passwd=getpass() )

pipeline = ip.Pipeline([cam, data2stream, ftp])

while True:
    pipeline.process( [1] ) # capture 1 image every 5 seconds
    time.sleep(5)
