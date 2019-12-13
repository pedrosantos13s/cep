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

skt.bind(('',porta))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.show()



x = []
y = []
i = 0
janela = 10

while True:
    # Receber resposta
    print("> Esperando resposta...")
    msg, adr = skt.recvfrom(1024)

    json_dic = convert_str_json(msg)

    x.append(i)
    y.append(json_dic["temperatura_externa"])

    ax.plot(x, y, color='b')

    fig.canvas.draw()

    # print("Mensagem recebida de: ", str(adr))
    # print(msg.decode())

    i += 1
    if len(y) >= janela:
        x.pop(0)
        y.pop(0)

    #msg = input("O que deseja enviar?")
    #msg = msg.encode()
    # Enviar mensagem
    #skt.sendto(msg, adr)