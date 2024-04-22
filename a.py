from cubo import Cubo, Lector_txt

lector = Lector_txt()
capas_desarmado = lector.cargar_txt("armado.txt")
if capas_desarmado:
    cubo_desarmado = Cubo(*capas_desarmado)

cubo_desarmado.U()
cubo_desarmado.Rp()
cubo_desarmado.F()
cubo_desarmado.Dp()


lector.guardar_txt(cubo_desarmado, "desarmado.txt")