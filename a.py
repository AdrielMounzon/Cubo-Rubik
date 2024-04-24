from cubo import Cubo, Lector_txt

lector = Lector_txt()
capas_desarmado = lector.cargar_txt("armado.txt")
if capas_desarmado:
    cubo_desarmado = Cubo(*capas_desarmado)

cubo_desarmado.Up()
cubo_desarmado.L()
cubo_desarmado.F()
cubo_desarmado.Rp()
cubo_desarmado.B()

# cubo_desarmado.D()
# cubo_desarmado.Rp()
# cubo_desarmado.Fp()
# cubo_desarmado.Lp()
# cubo_desarmado.Up()


lector.guardar_txt(cubo_desarmado, "desarmado.txt")