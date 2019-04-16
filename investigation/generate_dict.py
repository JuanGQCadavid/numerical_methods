import mido
import sys
from mido import MidiFile


def get_nota(msg):
    texto = str(msg)
    pos_nota = texto.find('note', 10)
    if texto[pos_nota + 7] != ' ':
        nota = texto[pos_nota+5] + texto[pos_nota+6] + texto[pos_nota+7]
    else:
        nota = texto[pos_nota+5] + texto[pos_nota+6]

    return nota

def get_vel(msg):
    vel = 0
    texto = str(msg)
    pos_vel = texto.find('velocity', 10)
    vel = texto[pos_vel+9]
    return vel

def control(msg):
    texto = str(msg)
    if 'key_signature' in texto:
        return True
    elif 'program_change' in texto:
        return True
    elif 'control_change' in texto:
        return True
    elif 'end_of_track' in texto:
        return True
    elif 'time_signature' in texto:
        return True
    else:
        return False



def main():

    song = sys.argv[1]
    print('Transformando canción: ', song)
    
    puntos = {}
    def agregar_a_arreglo(x, y):
        puntos[x] = y

    tiempo_acumulado = 0
    mid = MidiFile(song)
    for i, track in enumerate(mid.tracks):
        last_time = -1
        for msg in track:
            if(not control(msg)):
                tiempo_acumulado += msg.time

                if get_vel(msg) != '0':
                    nota = get_nota(msg)
                    if tiempo_acumulado != last_time:
                        agregar_a_arreglo(tiempo_acumulado, nota)
                        last_time = tiempo_acumulado

    print(puntos)
    return puntos
    
if __name__ == '__main__':
    main()