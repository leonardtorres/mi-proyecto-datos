import pandas as pd
from transformaciones import normalizar_texto

def test_normalizar_texto():
    # 1. Creamos datos de prueba desordenados
    datos_entrada = pd.DataFrame({"ciudad": ["  cusco  ", "lima ", " arequipa"]})
    
    # 2. Ejecutamos la función que queremos testear
    resultado = normalizar_texto(datos_entrada, "ciudad")
    
    # 3. Comprobamos que el resultado sea el esperado
    assert resultado["ciudad"].iloc[0] == "CUSCO"
    assert resultado["ciudad"].iloc[1] == "LIMA"
    assert resultado["ciudad"].iloc[2] == "AREQUIPA"