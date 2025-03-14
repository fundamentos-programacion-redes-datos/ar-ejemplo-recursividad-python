
def invertir_cadena(cadena):
    """
    Invierte una cadena de texto utilizando recursión.

    Parámetro:
    - cadena: Cadena de texto a invertir.

    Retorna:
    - str: La cadena invertida.
    """
    if len(cadena) == 0:
        # Caso base: si la cadena está vacía, retorna una cadena vacía
        return ""
    else:
        # Paso recursivo: toma el último carácter y llama recursivamente con el resto de la cadena
        return cadena[-1] + invertir_cadena(cadena[:-1])

if __name__ == '__main__':
    # Ejemplo de uso
    lista_frases = [
        "Ecuador, un país megadiverso.",
        "Ecuador tiene cuatro mundos en un solo país.",
        "Del Oriente al mar en un solo día.",
        "La mitad del mundo está aquí.",
    ]
    
    for i in lista_frases:
        resultado = invertir_cadena(i)
        print(f"La cadena invertida de '{i}' es |{resultado}|")
