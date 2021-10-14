# 学习OpenMV函数使用
import sensor, image, time

sensor.reset()      #重置感光元件
sensor.set_pixformat(sensor.GRAYSCALE)     #设置色彩模式 黑白：GRAYSCALE 彩色：RGB565
sensor.set_framesize(sensor.QVGA)      #设置显示图像大小
#sensor.set_vflip(True)         #设置水平翻转
#sensor.set_hmirror(True)       #设置水平翻转
sensor.skip_frames(time = 2000)         #跳过一些帧  等待感光元件变稳定

clock = time.clock()        # 创建一个时钟对象来跟踪FPS帧率。并初始化

while(True):
    clock.tick()           # 更新FPS帧率时钟。

    img = sensor.snapshot()     #截取当前图像，存放于变量img中。注意python中的变量是动态类型，不需要声明定义，直接用即可。
    print(clock.fps())      # 注意: 当连接电脑后，OpenMV会变成一半的速度。当不连接电脑，帧率会增加。

    img.draw_line((20, 30, 40, 50))
    img.draw_line((80, 50, 100, 100), color=(255,0,0))
    img.draw_rectangle((20, 30, 41, 51), color=(255,0,0))
    img.draw_circle(50, 50, 30)
    img.draw_cross(90,60,size=10)
    img.draw_string(10,10, "hello world!")






#img = sensor.snapshot()     #返回一张图
#print(img.get_pixel(10,10))     #获取这张图X,Y坐标的色彩信息
#print(img.width())        #返回图像的宽度(像素)
#print(img.height())       #返回图像的高度(像素)
#print(img.format())       #灰度图会返回 sensor.GRAYSCALE（2），彩色图会返回 sensor.RGB565（3）。
#print(img.size())         #返回图像的大小(byte)

#while(True):
    #clock.tick()
#    print(clock.fps())
