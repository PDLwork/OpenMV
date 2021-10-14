# 矩形追踪

import sensor, image

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

while(True):
    img = sensor.snapshot()

    r = 0

    for r in img.find_rects(threshold = 10000):
        img.draw_rectangle(r.rect(), color = (255, 0, 0))
        for p in r.corners():
            img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
    #print(type(r))

    if(r == 0):
        print(0)
    else:
        print(1)

        #print(1)
    #print(0)
