from selenium import webdriver

chrome_driver_path = "C:\Devellopment\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/-/es/Cartas-surtidas-Pok%C3%A9mon-50-unidades/dp/B001CJVTLC/ref=lp_16225015011_1_1")
# price = driver.find_element_by_id("price_inside_buybox")
# print(price.text)
driver.get("https://www.python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)


# doc = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc.text)
#
# finder = driver.find_element_by_xpath('//*[@id="container"]/li[6]/ul/li[1]/a')
#
# print(finder.text)
fechas = []
eventos = []
for i in range(1,6):
    fecha = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    evento = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    fechas.append(fecha.get_attribute("datetime").split("T")[0])
    eventos.append(evento.text)

dict_eventos = {i:{"time":fechas[i],"name":eventos[i]} for i in range(0,5)}
print(dict_eventos)
driver.quit()