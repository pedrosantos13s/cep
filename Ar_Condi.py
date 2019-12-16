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

    temp_Set = temp_Ext * 3
    while temp_Set > 2.2*temp_Ext or temp_Set < 0.3*temp_Ext:
        temp_Set = numpy.random.normal(temp_Ext,0.4*temp_Ext,1)

    visc_Flu = numpy.random.normal(0.001002,0.0001002,1)  

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
    print(type(str_dic))
    print(str_dic)
    msg = str_dic.encode()
    skt.sendto(msg,(ip,porta))

def ar_cond():

    ar_msg()
    Timer(5, ar_cond).start()

    
IPV4 = AF_INET
UDP = SOCK_DGRAM
TCP = SOCK_STREAM

skt = socket (IPV4, UDP)

ip = input("insira o IP de destino: ")
porta = int(input("Insira a porta de destino: "))

ar_cond()