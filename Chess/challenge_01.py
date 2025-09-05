import pprint as pp


class X:
    def __init__(self, coordenda: tuple, disponible: bool = True):
        self.coordenada = coordenda
        self.disponible = disponible

    def __str__(self):
        cadena = " "
        cadena += f"{self.coordenada},{self.disponible}"
        return cadena


def lista_movimientos_diagonales(
    m: int, coordenada_reina: X, coordenadas_bloqueo: X = None
) -> list:
    # Contador de posibles movimientos
    fila_reina = coordenada_reina.coordenada[0]
    columna_reina = coordenada_reina.coordenada[1]

    # Armar lista de coordenadas donde la reina puede moverse en diagonal
    coordenadas_diagonales = []
    # Diagonal superior izquierda
    apuntador_fila = fila_reina - 1
    apuntador_columna = columna_reina - 1
    while apuntador_fila >= 0 and apuntador_columna >= 0:
        if (
            coordenadas_bloqueo
            and apuntador_fila == coordenadas_bloqueo.coordenada[0]
            and apuntador_columna == coordenadas_bloqueo.coordenada[1]
        ):
            print("Error")
            break
        coordenadas_diagonales.append((apuntador_fila, apuntador_columna))
        apuntador_fila -= 1
        apuntador_columna -= 1

    # Diagonal superior derecha
    apuntador_fila = fila_reina - 1
    apuntador_columna = columna_reina + 1
    while apuntador_fila >= 0 and apuntador_columna < m:
        if (
            coordenadas_bloqueo
            and apuntador_fila == coordenadas_bloqueo.coordenada[0]
            and apuntador_columna == coordenadas_bloqueo.coordenada[1]
        ):
            print("Error")
            break

        coordenadas_diagonales.append((apuntador_fila, apuntador_columna))
        apuntador_fila -= 1
        apuntador_columna += 1

    # Diagonal inferior derecha
    apuntador_fila = fila_reina + 1
    apuntador_columna = columna_reina + 1
    while apuntador_fila < m and apuntador_columna < m:
        if (
            coordenadas_bloqueo
            and apuntador_fila == coordenadas_bloqueo.coordenada[0]
            and apuntador_columna == coordenadas_bloqueo.coordenada[1]
        ):
            print("Error")

            break

        coordenadas_diagonales.append((apuntador_fila, apuntador_columna))
        apuntador_fila += 1
        apuntador_columna += 1

    # Diagonal inferior izquierda
    apuntador_fila = fila_reina + 1
    apuntador_columna = columna_reina - 1
    while apuntador_fila < m and apuntador_columna >= 0:
        if (
            coordenadas_bloqueo
            and apuntador_fila == coordenadas_bloqueo.coordenada[0]
            and apuntador_columna == coordenadas_bloqueo.coordenada[1]
        ):
            print("Error")

            break

        coordenadas_diagonales.append((apuntador_fila, apuntador_columna))
        apuntador_fila += 1
        apuntador_columna -= 1
    return coordenadas_diagonales


def numero_movimientos(m: int, coordenada_reina: X, bloqueo: X = None) -> list:
    if coordenada_reina.coordenada[0] >= m or coordenada_reina.coordenada[1] >= m:
        raise ValueError(
            "La coordenada de la reina no puede ser mayor o igual al tamaño del tablero"
        )
    # Posibles movimientos en la fila
    apuntador_fila = coordenada_reina.coordenada[0] - 1
    apuntador_columna = coordenada_reina.coordenada[1]
    cordenadas_filas = []
    cordenadas_columnas = []
    # Movimientos hacia arriba de la reina
    while apuntador_fila >= 0:
        if bloqueo and (apuntador_fila, apuntador_columna) == bloqueo.coordenada:
            break
        cordenadas_filas.append((apuntador_fila, apuntador_columna))
        apuntador_fila -= 1

    # Movimientos hacia abajo de la reina
    apuntador_fila = coordenada_reina.coordenada[0] + 1
    apuntador_columna = coordenada_reina.coordenada[1]
    while apuntador_fila < m:
        if bloqueo and (apuntador_fila, apuntador_columna) == bloqueo.coordenada:
            break
        cordenadas_filas.append((apuntador_fila, apuntador_columna))
        apuntador_fila += 1
    print("Cordenadas filas")
    pp.pprint(cordenadas_filas)
    # Movimiento hacia la izquierda de la reina
    apuntador_fila = coordenada_reina.coordenada[0]
    apuntador_columna = coordenada_reina.coordenada[1] - 1
    while apuntador_columna >= 0:
        if bloqueo and (apuntador_fila, apuntador_columna) == bloqueo.coordenada:
            break
        cordenadas_columnas.append((apuntador_fila, apuntador_columna))
        apuntador_columna -= 1

    # Movimiento hacia la derecha dde la reina
    apuntador_fila = coordenada_reina.coordenada[0]
    apuntador_columna = coordenada_reina.coordenada[1] + 1
    while apuntador_columna < m:
        if bloqueo and (apuntador_fila, apuntador_columna) == bloqueo.coordenada:
            break
        cordenadas_columnas.append((apuntador_fila, apuntador_columna))
        apuntador_columna += 1
    print("cordenadas columnas")
    pp.pprint(cordenadas_columnas)

    coordenadas_diagonales = lista_movimientos_diagonales(m, coordenada_reina, bloqueo)

    print("Coordenadas diagonales")
    pp.pprint(coordenadas_diagonales)

    return (
        len(cordenadas_columnas) + len(cordenadas_filas) + len(coordenadas_diagonales)
    )


coordenada_reina = X((3, 0), False)

print(
    numero_movimientos(m=6, coordenada_reina=coordenada_reina, bloqueo=X((1, 0), False))
)
