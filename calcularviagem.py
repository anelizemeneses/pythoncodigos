distancia = float(input("Qual a distância em km:"))
velocidade_media = float(input("Qaul a velocidade média em km/h:"))
tempo = distancia / velocidade_media
print("O tempo estimado é da viagem é de %5.2f horas" % tempo)
tempo_segundos = int(tempo * 3600)  #horas p/segundos
horas = int(tempo / 3600)
tempo_segundos = int(tempo % 3600)
minutos = int(tempo / 60)
segundos = int(tempo % 60)
