from ColoTrackingAndTx import readFrameAndSend

camera = 0
hsv_min = (0, 142, 187)
hsv_max = (179, 192, 192)
ip_address = "201.174.122.202"
port = 5001
id = "19212386"

readFrameAndSend(camera, hsv_min, hsv_max, ip_address, port, id)