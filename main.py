from selenium import webdriver
PATH = "./chromedriver.exe"
URL = "https://www.g2a.com/category/games-c189"
driver = webdriver.Chrome(PATH)
driver.get(URL)
game_list = driver.find_element_by_xpath(
    '//*[@id="de982c28-e63a-4bd7-b60d-1e5e0a335bc2"]/section/div/div[2]/section/div/ul')
game_titles = game_list.find_elements_by_class_name(
    "indexes__Title-wklrsw-94.indexes__StyledTitle-wklrsw-128.dVOrKe.lhyEfX")
game_prices = game_list.find_elements_by_class_name(
    "indexes__PriceCurrentBase-wklrsw-86.iPgINw")


for title, price in zip(game_titles, game_prices):
    print(
        f"Tytul: {title.find_element_by_tag_name('a').get_attribute('innerHTML')} Cena: {price.get_attribute('innerHTML')}")
