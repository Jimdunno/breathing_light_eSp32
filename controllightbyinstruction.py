import time
import network
import machine

# Set the Pin to the LED light
led2 = machine.PWM(machine.Pin(2))
led2.freq(1000)

while True: # Control the repetition of the light pulse

    # From off gradually to on
    for i in range(0, 1024):
        led2.duty(i)
        time.sleep_ms(2)

    # From on gradually to off
    for i in range(1023, -1, -1):
        led2.duty(i)
        time.sleep_ms(2)

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('121Lab-2G', 'Lab2024!@Zte')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def create_UDP_socket():
    import socket
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定一个固定的窗口
    udp_socket.bind(("0.0.0.0", 7788))
    return udp_socket



def main():
    
    # Connect ESP32 to WIFI
    do_connect()
    # Create UDP socket 
    udp_socket = create_UDP_socket()
    
    # create GPIO controller
    led = machine.Pin(2, machine.Pin.OUT)
    
    # Receive udp data
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        print('{} sent the data: {}'.format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        print('data after decoding: {}'.format(recv_data_str))
        
        # 根据UDP数据控制灯的亮灭
        if recv_data_str == 'light on':
            led.value(1)
        elif recv_data_str == 'light off':
            led.value(0)

if __name__ == "__main__":
    main()
