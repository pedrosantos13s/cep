import numpy
import json 
from socket import *
from threading import Timer

def ar_val():

    temp_Ext = 31
    while temp_Ext > 30 or temp_Ext < 0: 
        temp_Ext = numpy.random.normal(20,6.66,1)

    temp_Int = numpy.random.normal(35,11.66,1)  

    vcc = 26
    while vcc > 25 or vcc < 8:
        vcc = numpy.random.normal(12,4.33,1)  

    temp_Mult = 3
    while temp_Mult > 2.2 or temp_Mult < 0.3:
        temp_Mult = numpy.random.normal(1,0.4,1)
    
    temp_Set = temp_Ext * temp_Mult

    visc_Flu = numpy.random.normal(0.001002,0.0001002/3,1)

    dic = {}
    dic["temperatura_externa"] = temp_Ext[0]
    dic["temperatura_interna"] = temp_Int[0]
    dic["vcc"] = vcc[0]
    dic["temperatura_setada"] = temp_Set[0]
    dic["viscosidade_fluido"] = visc_Flu[0]

    return dic

def ar_msg():

    dic = ar_val()
    encoder = json.JSONEncoder()
    str_dic = encoder.encode(dic)
    # print(type(str_dic))
    print(str_dic)
    msg = str_dic.encode()
    return msg
    # skt.sendto(msg,(ip,porta))

def ar_cond():
    t = 5
    msg = ar_msg()
    skt.sendto(msg,(ip,porta))
    Timer(t, ar_cond).start()

    
IPV4 = AF_INET
UDP = SOCK_DGRAM
# TCP = SOCK_STREAM

skt = socket (IPV4, UDP)

ip = input("insira o IP de destino: ")
porta = int(input("Insira a porta de destino: "))

ar_cond()