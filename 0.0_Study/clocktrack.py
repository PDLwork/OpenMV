# 颜色追踪学习

import sensor, image, time

#颜色阈值 LAB形式
thresholds = (30, 80, 15, 40, 40, 65) #ST-link颜色
#thresholds = (0, 15, -10, 10, -10, 10) #黑色

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(False) #关闭自动增益
sensor.set_auto_whitebal(False) #关闭白平衡
sensor.skip_frames(time = 2000)

ROI = [80,60,160,120]       #设置感兴趣区域

while(True):
    img = sensor.snapshot()

    img.draw_rectangle(ROI)

    for blob in img.find_blobs([thresholds], roi = ROI, pixels_threshold=200, area_threshold=200, merge=True):
        #if blob.elongation() > 0.5:
            #img.draw_edges(blob.min_corners(), color=(255,0,0))
            #img.draw_line(blob.major_axis_line(), color=(0,255,0))
            #img.draw_line(blob.minor_axis_line(), color=(0,0,255))

        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())

        #img.draw_keypoints([(blob.cx(), blob.cy(), int(math.degrees(blob.rotation())))], size=20)
