import time
import os


current_timestamp = time.time()


# Ajusta el intervalo de subida en segundos
intervalo = 850 

upload_dir = '/home/paola/Fabricio/Radar/upload_imagenes_radar_'

#while True:
try:
    print ('copiando imagenes')
        
    os.system (f'cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/ultima_tormenta_entrenamiento.png {upload_dir}')
    os.system (f'cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/pred_nowcast_005.png {upload_dir}')
    os.system (f'cp /home/paola/Fabricio/Radar/Pipeline/Pipeline_ultimos_10_modelo_Mini_UNET/Output_Nowcast/pred_nowcast_010.png {upload_dir}')
    
    os.chdir (upload_dir)


    print ('subiendo a git')
    
    os.system(f'git add *png')
    os.system(f'git commit -m "auto update {current_timestamp}" ')
    os.system('git push')
    print(f"Imagen actualizada.")
except Exception as e:
    print("Error:", e)
    
    #time.sleep(intervalo)
