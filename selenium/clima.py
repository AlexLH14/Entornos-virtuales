from selenium import webdriver
import time

# Configurar el controlador de Chrome
driver = webdriver.Chrome()

# Navegar hasta la página del clima de Chignahuapan
driver.get("https://weather.com/es-MX/clima/hoy/l/21.05,-98.05")

# Esperar un momento para que la página se cargue completamente
time.sleep(5)

# Encontrar y extraer los datos del clima
clima_actual_element = driver.find_element_by_css_selector(".CurrentConditions--phraseValue--2xXSr")
temperatura_element = driver.find_element_by_css_selector(".CurrentConditions--tempValue--3KcTQ")
sensacion_termica_element = driver.find_element_by_css_selector(".TodayDetailsCard--feelsLikeTempValue--2icPt")

# Obtener el texto de los elementos
clima_actual = clima_actual_element.text
temperatura = temperatura_element.text
sensacion_termica = sensacion_termica_element.text

# Imprimir los datos del clima
print("Clima actual en Chignahuapan:", clima_actual)
print("Temperatura:", temperatura)
print("Sensación térmica:", sensacion_termica)

# Cerrar el navegador
driver.quit()
