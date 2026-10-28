def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """

    codigo, nombre, precio, cantidad = linea.strip().split(",")

    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad),}

def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    codigo, nombre, precio, cantidad = linea.strip().split(",")

    valor_total = round(float(precio) * int(cantidad),1)
    
    return f"{codigo} - {nombre}: ${valor_total}"
    
def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """

    lista_resumenes = []

    for linea in lineas:
        resumen = resumen_de_producto(linea)
        lista_resumenes.append(resumen)

    return lista_resumenes


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """

    suma_total = 0.0

    for linea in lineas:
       _, _, precio, cantidad = linea.strip().split(",")
    suma_total = suma_total + (float(precio) * int(cantidad))

    return round(suma_total, 1)

def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    max_valor = -1.0  
    resumen_maximo = ""

    for linea in lineas:
        codigo, nombre, precio, cantidad = linea.strip().split(",")
        valor_actual = float(precio) * int(cantidad)
        if valor_actual > max_valor:
            max_valor = valor_actual
            valor_redondeado = round(valor_actual, 1)
            resumen_maximo = f"{codigo} - {nombre}: ${valor_redondeado}"

    return resumen_maximo


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # ejemplos rápidos para visualizar (descomenta cuando implementes)
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
