# YOLOV5-UA-DETRAC 智能红绿灯

在运行程序之前，首先安装requirments.txt中的依赖项

进入终端，打开程序文件夹

输入`pip -r install ./requirements,txt`来安装依赖项

安装完成后，重启电脑

进入终端，cd至文件夹目录

输入`python ./detect.py --weights ./best.pt --source ./vid.mp4 --view-img`

以检测依赖项是否安装成功

![detect](https://i.loli.net/2021/11/21/RMZA4VTgCrcLDho.png)

![run.png](https://i.loli.net/2021/11/21/aEmSjDJvfOdwzkp.png)

程序运行图

在运行mainserver程序时，首先修改程序中的host，改为本机IP地址，先启动mainserver，再启动detect_client

启动方法：`python mainserver.py`

启动detect_client程序前，修改host为mainserver的host地址，port根据摄像头以此递进

启动方法：`python detect_client.py --weights best.pt --source 0 --img 320`

`--source`后的参数，0为摄像头，可以是0、1、2、3、4等等，根据摄像头位置决定

detect_client的host与port可以直接在启动时加上`--host + 地址`的方法和`--port + 端口`的方法传入

## **注意！mainserver需要4个client全部启动才会运行**

mainserver输出数据格式为：纵向车流量；横向车流量；纵向红灯时间；横向红灯时间
