import datetime
import io
import select
import time
import Image

import cv2
import numpy as np
import v4l2capture
import zbar

while True:
    # Open the video device.
    video = v4l2capture.Video_device("/dev/video0")

    # Suggest an image size to the device. The device may choose and
    # return another size if it doesn't support the suggested one.
    size_x, size_y = video.set_format(1280, 1024)

    # Create a buffer to store image data in. This must be done before
    # calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
    # raises IOError.
    video.create_buffers(1)

    # Send the buffer to the device. Some devices require this to be done
    # before calling 'start'.
    video.queue_all_buffers()

    # Start the device. This lights the LED if it's a camera that has one.
    video.start()

    # Wait for the device to fill the buffer.
    select.select((video,), (), ())

    # The rest is easy :-)
    image_data = video.read()
    video.close()
    pil = Image.frombuffer("RGB", (size_x, size_y), image_data)

    imgGauss = cv2.GaussianBlur(np.asarray(pil), (3, 3), 0)
    gray = cv2.cvtColor(imgGauss, cv2.COLOR_RGB2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
#  print "%d" % fm
#  if fm < 100:
#    continue

#
#########################################
#
# create a reader
    scanner = zbar.ImageScanner()

# configure the reader
    scanner.parse_config('enable')

    pil = pil.convert('L')
    width, height = pil.size
    print pil, width, height
    raw = pil.tobytes()

# wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

# scan the image for barcodes
    scanner.scan(image)

# extract results
    for symbol in image:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

# clean up
    del(image)
    pass
