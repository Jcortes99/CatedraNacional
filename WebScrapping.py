import requests
from bs4 import BeautifulSoup

# URL de la página web que deseas obtener
url = 'https://www.google.com/url?client=internal-element-cse&cx=008572255874373046644:chip1p1uf-4&q=https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf%3BPortalJSESSION%3DdBPgSewfsrHLbNgvEf4MYJvBthWw5hkhQzjOC1XQzXkSJJmNdMZy!1891780822%3FtaskflowId%3Dtask-flow-AC_CatalogoAsignaturas&sa=U&ved=2ahUKEwip-8TcqKmBAxVPRzABHeuWAPoQFnoECAYQAQ&usg=AOvVaw2_YModhnDvcyaJ8n8jbejC'

# Realiza una solicitud HTTP GET a la URL
response = requests.get(url)

# Verifica si la solicitud se realizó correctamente (código de respuesta 200)
if response.status_code == 200:
    # Obtén el contenido HTML de la página
    html_content = response.text
    
    # Parsea el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    
    # Encuentra todos los elementos <select> en la página
    select_elements = soup.find_all('select')
    with open('selectlist.txt', 'w', encoding='utf-8') as file:
    # Itera a través de cada elemento <select> y escribe su contenido en el archivo
        for select_element in select_elements:
            file.write(str(select_element) + '\n')
    # options = [0,6,26]
    # iterator = 0
    # # Itera a través de cada elemento <select>
    # for select_element in select_elements:
    #     print(select_element,'\n')
    #     option_to_select = select_element.find('option', {'value': str(options[iterator])})
    #     iterator += 1
    #     print(option_to_select)
    #     if option_to_select:
    #         # Cambia el atributo 'selected' de la opción para seleccionarla
    #         option_to_select['selected'] = 'selected'
    
    
else:
    print(f'Error al obtener la página. Código de respuesta: {response.status_code}')
