import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el controlador de Selenium (asegúrate de tener el controlador del navegador instalado)
driver = webdriver.Chrome()  # Reemplaza con la ubicación de tu controlador

# URL de la página web que deseas acceder
url = 'https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas'

# Abre la página web en el navegador controlado por Selenium
driver.get(url)

# time.sleep(3)


# Primer select pregrado/posgrado...
# =========================================================================================

# Encuentra el primer elemento <select> por su identificador, nombre, u otro selector
elemento = driver.find_element(By.ID, 'pt1:r1:0:soc1::content')

# Convierte el elemento <select> en un objeto Select
select = Select(elemento)

# Utiliza select_by_value para seleccionar una opción por su valor
select.select_by_value('0')

time.sleep(1)

# Segundo select sede
# =========================================================================================

# Encuentra el primer elemento <select> por su identificador, nombre, u otro selector
elemento = driver.find_element(By.ID, 'pt1:r1:0:soc9::content')

# Convierte el elemento <select> en un objeto Select
select = Select(elemento)

# Utiliza select_by_value para seleccionar una opción por su valor
select.select_by_value('6')

time.sleep(1)

# tercer select facultad
# =========================================================================================

# Encuentra el primer elemento <select> por su identificador, nombre, u otro selector
elemento = driver.find_element(By.ID, 'pt1:r1:0:soc2::content')

# Convierte el elemento <select> en un objeto Select
select = Select(elemento)

# Utiliza select_by_value para seleccionar una opción por su valor
select.select_by_value('4')

time.sleep(1)

# cuarto select plan de estudios
# =========================================================================================

# Encuentra el primer elemento <select> por su identificador, nombre, u otro selector
elemento = driver.find_element(By.ID, 'pt1:r1:0:soc3::content')

# Convierte el elemento <select> en un objeto Select
select = Select(elemento)


# Utiliza select_by_value para seleccionar una opción por su valor
select.select_by_value('12')

time.sleep(1)

# Presionar boton
# =========================================================================================
# Ubica el elemento <a> por su clase "af_button_link"
boton_mostrar = driver.find_element(By.CLASS_NAME, 'af_button_link')

# Hace clic en el botón
boton_mostrar.click()

time.sleep(1)


# extraer datos
# =========================================================================================

# Encuentra el primer elemento <select> por su identificador, nombre, u otro selector
elemento = driver.find_element(By.ID, 'pt1:r1:0:t4::db')

# Convierte el elemento <select> en un objeto Select
# select = Select(elemento)

# Obtiene el texto del elemento
texto = elemento.text

with open('recoveryFile.txt', 'w', encoding='utf-8') as file:
        # Itera a través de cada elemento <select> y escribe su contenido en el archivo
        file.write(str(texto)) 

# Imprime el texto
# print(texto)




# a = input('waiting')

# elemento = driver.find_element_by_id('pt1:r1:0:pb3')
# elemento.click()

# Cierra el navegador controlado por Selenium cuando hayas terminado
driver.quit()
