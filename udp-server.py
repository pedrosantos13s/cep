import matplotlib.pyplot as plt
from _socket import *
import json


def convert_str_json(str_dic):
    return json.loads(str_dic)


IPV4 = AF_INET
UDP = SOCK_DGRAM
TCP = SOCK_STREAM

skt = socket(IPV4, UDP)
porta = int(input("Qual porta deseja bindar? "))
skt.bind(('', porta))

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
i = 0
janela = 10

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_xlim(0, janela+1)
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_xlim(0, janela+1)
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_xlim(0, janela+1)
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_xlim(0, janela+1)

fig.show()
ax1.set_xlim(0, janela+1)

while True:
    # Receber resposta
    print("> Esperando resposta...")
    msg, adr = skt.recvfrom(1024)
    json_dic = convert_str_json(msg)

    x.append(i)
    y1.append(json_dic["temperatura_externa"])
    y2.append(json_dic["temperatura_interna"])
    y3.append(json_dic["vcc"])
    y4.append(json_dic["temperatura_setada"])
    y5.append(json_dic["viscosidade_fluido"])

    ax1.plot(x, y1, color='b')
    ax2.plot(x, y2, color='b')
    ax3.plot(x, y3, color='b')
    ax4.plot(x, y4, color='b')
    
    fig.canvas.draw()

    i += 1
    if i > janela:
        ax1.set_xlim(i-janela, i+1)
        ax2.set_xlim(i-janela, i+1)
        ax3.set_xlim(i-janela, i+1)
        ax4.set_xlim(i-janela, i+1)
        