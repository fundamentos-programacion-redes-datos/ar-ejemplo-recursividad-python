
def invertir_cadena(cadena):
    """
    Invierte una cadena de texto utilizando recursión.

    Parámetro:
    - cadena: Cadena de texto a invertir.

    Retorna:
    - str: La cadena invertida.
    """
    if len(cadena) == 0:
        # Caso base: Si la cadena está vacía, retorna una cadena vacía.
        # Esto detiene la recursión evitando una llamada infinita.
        return ""
    else:
        # Paso recursivo:
        # - Se toma el último carácter de la cadena: cadena[-1]
        # - Se llama recursivamente a la función con el resto de la cadena (sin el último carácter): cadena[:-1]
        return cadena[-1] + invertir_cadena(cadena[:-1])

if __name__ == '__main__':
    # Lista de frases a invertir
    lista_frases = [
        "Ecuador, un país megadiverso.",
        "Ecuador tiene cuatro mundos en un solo país.",
        "Del Oriente al mar en un solo día.",
        "La mitad del mundo está aquí.",
    ]
    
    # Se recorre la lista de frases
    for i in lista_frases:
        # Se llama a la función recursiva para invertir la cadena
        resultado = invertir_cadena(i)
        # Se imprime la cadena original junto con su versión invertida
        print(f"La cadena invertida de '{i}' es |{resultado}|")
