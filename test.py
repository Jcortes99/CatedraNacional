from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el controlador de Chrome
driver = webdriver.Chrome()

# Abre la página web en el navegador controlado por Selenium
driver.get('https://www.ejemplo.com')  # Reemplaza con la URL que desees

# Realiza una acción que cause la aparición de la pantalla de carga (por ejemplo, hacer clic en un botón)

# Espera a que el elemento de pantalla de carga desaparezca
try:
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, 'elemento_de_pantalla_de_carga'))
    )
except Exception as e:
    print(f'Error al esperar que desaparezca la pantalla de carga: {str(e)}')

# Continúa con tu script de Selenium después de que la pantalla de carga haya desaparecido
# Por ejemplo, interactúa con otros elementos en la página
elemento = driver.find_element_by_id('otro_elemento')
elemento.click()

# Cierra el navegador controlado por Selenium cuando hayas terminado
driver.quit()