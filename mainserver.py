import socket
import time
import threading

skt1 = socket.socket()
skt2 = socket.socket()
skt3 = socket.socket()
skt4 = socket.socket()
# 创建 socket 对象

host = socket.gethostname()
port_one = 43420
port_two = 43421
port_three = 43422
port_four = 43423
client_port1 = 25572
client_port2 = 25573
client_port3 = 25574
client_port4 = 25575
#主机名，端口号定义

skt1.bind((host , port_one))
skt2.bind((host , port_two))
skt1.listen(5)
skt2.listen(5)
skt3.bind((host , port_three))
skt4.bind((host , port_four))
skt3.listen(5)
skt4.listen(5)
#绑定端口号，开始监听

car_rcv1 = 0 #纵向1
car_rcv2 = 0 #纵向2
cnt2_addr = ''
cnt1_addr = ''
car_rcv3 = 0 #横向1
car_rcv4 = 0 #横向2
cnt3_addr = ''
cnt4_addr = ''

total_time = int(input('Please enter total passing time(UNIT:Second):'))

green_light_time_1 = 0.1
green_light_time_2 = 0.1
red_light_time_1 = 0.1
red_light_time_2 = 0.1
yellow_light_time_1 = 3
yellow_light_time_2 = 3
#时间定义
total_car_amount = 0

#weights defination
cow_weight = 0.1
row_weight = 0.1

print('Waiting For Conection...')
cnt1 , cnt1_addr = skt1.accept()
cnt2 , cnt2_addr = skt2.accept()
cnt3 , cnt3_addr = skt3.accept()
cnt4 , cnt4_addr = skt4.accept()

#被动式连接
print('All Four Connected!')
start = 0
end = 0
used = 0
def recieve_data():
    global car_rcv1 , car_rcv2 , cnt1_addr , cnt2_addr , car_rcv3 , car_rcv4 , cnt3_addr, cnt4_addr
    global total_car_amount , total_time , green_light_time_1 , green_light_time_2
    global yellow_light_time_1 , yellow_light_time_2 , red_light_time_1 , red_light_time_2 , start , end , used
#    start = time.time()
    green_light_time_1 = 0.1
    green_light_time_2 = 0.1
    red_light_time_1 = 0.1
    red_light_time_2 = 0.1
    yellow_light_time_1 = 3
    yellow_light_time_2 = 3

    total_car_amount = 0
    car_rcv1 = 0
    car_rcv2 = 0
    cnt2_addr = ''
    cnt1_addr = ''
    car_rcv3 = 0
    car_rcv4 = 0
    cnt3_addr = ''
    cnt4_addr = ''

    rcv1 = cnt1.recv(16)
    rcv1 = str(rcv1[0:2])[2:-1]
    if rcv1.strip() == '':
        pass
    else:
        car_rcv1 = int(rcv1[0:2])
    rcv2 = cnt2.recv(16)
    rcv2 = str(rcv2)[2:-1]
    if rcv2.strip() == '':
        pass
    else:
        car_rcv2 = int(rcv2)
    rcv3 = cnt3.recv(16)
    rcv3 = str(rcv3[0:2])[2:-1]
    if rcv3.strip() == '':
        pass
    else:
        car_rcv3 = int(rcv1[0:2])
    rcv4 = cnt4.recv(16)
    rcv4 = str(rcv4)[2:-1]
    if rcv4.strip() == '':
        pass
    else:
        car_rcv2 = int(rcv2)

def process_data():
    global car_rcv1 , car_rcv2 , cnt1_addr , cnt2_addr , car_rcv3 , car_rcv4 , cnt3_addr, cnt4_addr
    global total_car_amount , total_time , green_light_time_1 , green_light_time_2
    global yellow_light_time_1 , yellow_light_time_2 , red_light_time_1 , red_light_time_2 , start
    recieve_data()
    car_rcv1 = car_rcv1 + car_rcv2
    car_rcv3 = car_rcv3 + car_rcv4
    if car_rcv2 <= 10 and car_rcv1 <= 10:
        red_light_time_1 = total_time / 2
        red_light_time_2 = red_light_time_1
        green_light_time_1 = red_light_time_1 - 3
        green_light_time_2 = green_light_time_1
    elif car_rcv3 > 10 or car_rcv1 > 10:
        if car_rcv1 > car_rcv3:
            red_light_time_1 = total_time * 

#    end = time.time()
#    used = end - start
#    print(used)
    print(car_rcv1)#摄像头1车辆
    print(car_rcv2)#摄像头2车辆
    print(red_light_time_1)#时间1
    print(red_light_time_2)#时间2
    #        cnt1.sendall(bytes(red_light_time_1 , encoding='utf8'))
    #        cnt2.sendall(bytes(red_light_time_2 , encoding='utf8'))
#    time.sleep(total_time - used)
def light_control_1():
    global car_rcv1 , car_rcv2 , cnt1_addr , cnt2_addr
    global total_car_amount , total_time , green_light_time_1 , green_light_time_2
    global yellow_light_time_1 , yellow_light_time_2 , red_light_time_1 , red_light_time_2 , start
    print('Light One,Three Green!')
    print('Time: ' + str(green_light_time_1))
    time.sleep(green_light_time_1)
    print('Light One.Three Yellow')
    print('Time: ' + str(yellow_light_time_1))
    time.sleep(yellow_light_time_1)
    print('Light One,Three Red')
    print('Time: ' + str(red_light_time_1))
    time.sleep(red_light_time_1)
def light_control_2():
    global car_rcv1 , car_rcv2 , cnt1_addr , cnt2_addr
    global total_car_amount , total_time , green_light_time_1 , green_light_time_2
    global yellow_light_time_1 , yellow_light_time_2 , red_light_time_1 , red_light_time_2 , start
    print('Light Two,Four Green!')
    print('Time: ' + str(green_light_time_2))
    time.sleep(green_light_time_2)
    print('Light Two,Four Yellow')
    print('Time: ' + str(yellow_light_time_2))
    time.sleep(yellow_light_time_2)
    print('Light Two,Four Red')
    print('Time: ' + str(red_light_time_2))
    time.sleep(red_light_time_2)

if __name__ =='__main__':
    while True:
        process_data()
#        t1 = threading.Thread(target=light_control_1)
#        t2 = threading.Thread(target=light_control_2)
#        t1.start()
#        t2.start()