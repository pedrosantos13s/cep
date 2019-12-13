import numpy
import json 
from socket import *
from threading import Timer
n=1
##Gerar numeros aleatorios##
def ar_cond():
    ## Gera aleatorios distribuição normal centrado em 20 vai até 10~30, 50 valores##
    temp_Ext = numpy.random.normal(20,3.33,n)  
    #print (temp_Ext)


    ## Gera aleatorios distribuição normal centrado em 35 vai até 0~70, 50 valores##

    temp_Int = numpy.random.normal(35,11.66,n)  
    #print (temp_Int)


    ## Gera aleatorios distribuição normal centrado em 12 vai até 8~16, 50 valores##

    vcc = numpy.random.normal(12,1.33,n)  
    #print (vcc)

    ## Gera aleatorios distribuição normal centrado em temp_Ext vai até (temp_Ext * 0.3~1.7), 50 valores##
    ## Temp Ext * normal
    temp_Set = numpy.random.normal(temp_Ext,0.23*temp_Ext,n)  
    #print (temp_Set)


    ## Gera aleatorios distribuição normal centrado em 0.001002 vai até ~, 50 valores##

    visc_Flu = numpy.random.normal(0.001002,0.0001002,n)  
    #print (visc_Flu)

    dic = {}
    dic["temperatura_externa"] = temp_Ext[0]
    dic["temperatura_interna"] = temp_Int[0]
    dic["vcc"] = vcc[0]
    dic["temperatura_setada"] = temp_Set[0]
    dic["viscosidade_fluido"] = visc_Flu[0]

    encoder = json.JSONEncoder()
    str_dic = encoder.encode(dic)   # Isso é um STR
    print(type(str_dic))
    print(str_dic)

    ##Enviar para o outro programa

    msg = str_dic.encode()
    skt.sendto(msg,(ip,porta))

    

    ##Contagem para cada 5 segundos
    Timer(5, ar_cond).start()



IPV4 = AF_INET
UDP = SOCK_DGRAM
TCP = SOCK_STREAM

skt = socket (IPV4, UDP)

ip = input("insira o IP de destino: ")
porta = int(input("Insira a porta de destino: "))

ar_cond()


