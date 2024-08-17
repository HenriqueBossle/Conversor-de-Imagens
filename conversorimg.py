from PIL import Image
import os

lista_arquivos = os.listdir("imagens")

for arquivos in lista_arquivos:
   imagem = Image.open(f"imagens/{arquivos}")

   imagem.save(f'convertidas/{arquivos.replace("webp", "jpeg")}')