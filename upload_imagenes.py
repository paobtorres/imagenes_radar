import time
import os


current_timestamp = time.time()


# Ajusta el intervalo de subida en segundos
intervalo = 850 

while True:
    try:
        print ('copiando imagenes')
        os.system ('cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/ultima_tormenta_entrenamiento.png . ')
        os.system ('cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/pred_nowcast_005.png . ')
        os.system ('cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/pred_nowcast_010.png . ')
        print ('subiendo a git')
        os.system('git add *png')
        os.system(f'git commit -m "auto update {current_timestamp}" ')
        os.system('git push')
        print(f"Imagen actualizada. Esperando {intervalo} segundos...")
    except Exception as e:
        print("Error:", e)
    
    time.sleep(intervalo)
