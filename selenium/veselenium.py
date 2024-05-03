from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com")

# Encontrar el cuadro de búsqueda por el atributo 'name'
search_box = driver.find_element(By.NAME, "q")

# Escribir "entorno virtual" en el cuadro de búsqueda
search_box.send_keys("Que es selenium")

# Presionar Enter
search_box.send_keys(Keys.RETURN)

# Esperar un momento para que los resultados se carguen
time.sleep(2)

# Encontrar los títulos de los primeros resultados de búsqueda y mostrarlos
result_titles = driver.find_elements(By.CSS_SELECTOR, "h3")
for title in result_titles:
    print(title.text)

# Cerrar el navegador
driver.quit()
