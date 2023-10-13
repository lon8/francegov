from time import sleep
from seleniumwire import webdriver  # Импортируем webdriver из seleniumwire
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import cairosvg
import json
from time import sleep
from selenium import webdriver  # Импортируем webdriver из seleniumwire
from decouple import config


from twocaptcha import TwoCaptcha
from PIL import Image
# Создаем драйвер с использованием seleniumwire

solver = TwoCaptcha('e324c58b463ea325f43d8b0a0216a581')

mdriver = webdriver.Chrome()

def get_sessionid(driver : webdriver.Chrome):

    # Переходим на страницу
    try:
        driver.get('https://consulat.gouv.fr/en/ambassade-de-france-a-nicosie/appointment?name=Visa')

        sleep(2.5)
        # Берем код страницы
        source = driver.page_source
        
        soup = BeautifulSoup(source, 'lxml')
        # Ищем изображение
        image = soup.find('img', id='captcha-image')['src']

        mdriver.get(image)
        # Достаем исходный файл
        req = mdriver.page_source
        # Записываем его
        with open('image.svg', 'w') as file:
            file.write(req)
        # Конвертируем svg в png
        cairosvg.svg2png(url='image.svg', write_to='output.png')
        # Решаем капчу
        result = solver.normal('output.png')
        # Вводим капчу в поле
        input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/input')
        input.send_keys(result['code'])
        # Кликаем на кнопку, чтобы продолжить
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/button')
        button.click()
    except:
        get_sessionid(driver) # Это на случай, если капча не решится
    
    sleep(2.5) # Все паузы нужны для прогрузки страницы. Если ваш интернет не успевает, то можете их сделать больше
    # Здесь нажимаем на Demand de passeport 
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div/div[2]/fieldset/div/div[2]/div/div/button[2]')
    button.click()
    # Нажимаем на "To confirm"
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div/div[4]/button')
    button.click()
    
    sleep(2)
    # Подтверждаем, что прочитали что-то
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/label')
    button.click()
    # Нажимаем на "Book an appointment"
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/button')
    button.click()
    
    sleep(3.5)
    
    # Выбираем время встречи
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div/span')
    button.click()
    # Нажимаем Validate the calendar
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[3]/button')
    button.click()
    
    sleep(2.5)
    
    # Дальше мы вводим данные от полей
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div[1]/input')
    input.send_keys('Bobrov')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input')
    input.send_keys('Dima')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div[1]/input')
    input.send_keys('vladics20000@ya.ru')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[4]/div/div/div[1]/input')
    input.send_keys('vladics20000@ya.ru')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[5]/div/div/div[1]/div[1]/input')
    input.send_keys('+357 96 123544')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[6]/div/div/div[1]/input')
    input.send_keys('08/06/1984')
    
    input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[3]/div/fieldset/div/div/div/input')
    input.send_keys('kek')
    
    label = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[3]/div/fieldset/fieldset/div/div/div[2]/div[1]/label')
    label.click()
    
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div/div/button')
    button.click()
    
    sleep(1.5)
    
    # Здесь тоже нажимаем на подтверждение прочитанного
    # Только здесь реализован отступ, чтобы не нажать на ссылку, которая ведет к документам
    
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/label')
    
    element_size = button.size
    element_location = button.location

    # Вычислите координаты середины левой части элемента
    left_x = element_location['x']
    middle_y = element_location['y'] + element_size['height'] / 2
    actions = ActionChains(driver)
    actions.move_by_offset(left_x, middle_y)
    actions.click() 
    actions.perform() # Кликаем
    
    # Нажимаем "To confirm"
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div[2]/button[1]')
    button.click()
    
    # Готово
    
    
def kernel():

    CHROME_BIN_PATH = config('CHROME_BIN_PATH')

    from getsessionid import get_sessionid

    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_BIN_PATH

    driver = webdriver.Chrome()

    get_sessionid(driver)
    
    sleep(5) # Здесь потом можете поменять время в зависимости от вашего интернета

    print('Программа отработала успешно')
