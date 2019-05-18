import imagepypelines as ip
import cv2
import time
import os

cam = ip.blocks.CameraBlock(device="/dev/video0", mode='count')
img2png = ip.blocks.PngCompress()
data2stream = ip.blocks.Array2Stream()
ftp = ip.blocks.FTP(host="ftp.jeffmagg.io",
                    user="aplab@jeffmagg.io",
                    passwd=os.environ["FTP_PASS"],)

pipeline = ip.Pipeline([cam, img2png, data2stream, ftp])

while True:
    pipeline.process( [1] ) # capture and upload 1 image every 5 seconds
    time.sleep(5)
