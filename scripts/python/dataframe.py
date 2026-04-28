import pandas as pd

def crear_dataframe():
    # Crear un DataFrame de ejemplo
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    
    # Devolver 0 y el DataFrame
    return 0, df

# Ejecutar la función
resultado, dataframe = crear_dataframe()

print("Resultado:", resultado)
print("DataFrame:")
print(dataframe)
