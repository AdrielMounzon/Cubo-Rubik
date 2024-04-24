from clases.cubo import Cubo
from clases.lectortxt import Lector_txt

lector = Lector_txt()
capas = lector.cargar_txt("textos/armado.txt")
if capas:
    cubo = Cubo(*capas)

comandos = lector.cargar_comandos("textos/comandos.txt")
if comandos:
    for comando in comandos:
        if hasattr(cubo, comando):
            getattr(cubo, comando)()

lector.guardar_txt(cubo, "textos/desarmado.txt")

# Carga manual directamente de "textos/desarmado.txt"
# lector = Lector_txt()
# capas = lector.cargar_txt("textos/desarmado.txt")
# if capas:
#     cubo = Cubo(*capas)           