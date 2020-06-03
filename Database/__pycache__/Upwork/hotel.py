from selenium import webdriver
import time

chrome_path = 'C:\\Dev Tool\\chromedriver_win32\\chromedriver.exe'
chrom_opt = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'javascript': 2
    }
}
proxy = "10.152.102.9:8080"
chrom_opt.add_experimental_option("prefs", prefs)
#chrom_opt.add_argument('--proxy-server=%s' % proxy)
browser = webdriver.Chrome(executable_path=chrome_path,
                           chrome_options=chrom_opt)

browser.get(
    "https://www.salvemosrestaurantes.ec/restaurante-y-bares/restaurante/?city=2&zone=all&neighborhood=all&title=&page=14"
)

list = []
try:
    page = 0
    while page < 20:
        cardList = browser.find_elements_by_xpath(
            "//a[@class='selection-link']")
        for card in cardList:
            title = card.find_element_by_xpath(".//h4").text
            address = card.find_element_by_xpath(".//p").text
            link = card.get_attribute('href')
            phoneNumber = "N/A"
            js = 'window.open("' + link + '");'
            browser.execute_script(js)
            all_hand = browser.window_handles
            browser.switch_to_window(all_hand[-1])

            phoneList = browser.find_elements_by_xpath(
                "//a[contains(@class,'text-green-500')]")
            for phone in phoneList:
                url = phone.get_attribute('href')
                if (url.find("wa.me") > 0):
                    phoneNumber = url.split("?")[0].replace(
                        "https://wa.me/", "")
            time.sleep(2)
            browser.close()
            browser.switch_to_window(all_hand[0])
            data = [title, address, phoneNumber]
            list.append(data)
        browser.find_element_by_xpath(
            "//li[@class='page-item active']/following-sibling::li[1]").click(
            )
        page = page + 1
except Exception as err:
    print(err)
finally:
    print(list)