import pymcprotocol

#Definindo parâmetros para a comunicação com o PLC
pymc3e = pymcprotocol.Type3E() #Instanciando o FX5
pymc3e.setaccessopt(commtype="binary")
pymc3e.connect("192.168.100.22", 3456) #IP e porta 

#Lendo parâmetros do loader da router

while True:
    wordunits_values = pymc3e.batchread_wordunits(headdevice="D1121", readsize=1)
    print(wordunits_values)