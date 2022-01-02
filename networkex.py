from socket import *
import os

def parsing(host):
    #raw socket 생성 및 bind
    if os.name=="nt":      # nt는 윈도우 체제이면 os.name으로 나오는 단어이다.
        sock_protocol=IPPROTO_IP
    else:
        sock_protocol=IPPROTO_ICMP
    sock=socket(AF_INET, SOCK_RAW, sock_protocol)    # AF_INET = IPv4 / SOCK_RAW = 소켓의 형태(SOCK_STREAM=TCP SOCK_DGRAM=UDP) / 지정하거나 하지않아도됨
    sock.bind((host,0))    #아이피 주소와 포트를 연결하는 것 튜플 형태로 연결 / 포트 0으로 지정시 자동 연결
    
    
    #socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)  #대상 지정 / 옵션 / 옵션 값
    
    #promiscuous mode
    if os.name=="nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)
        
    data=sock.recvfrom(65535) #버퍼 크기 설정
    print(data[0])
    
    #promiscuous mode 끄기
    if os.name =="nt":
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)
        
    #소켓 종료
    sock.close()
    
    
if __name__ == "__main__":
    host = "192.168.219.102"
    print(f"Listening at [{host}]")
    parsing(host)