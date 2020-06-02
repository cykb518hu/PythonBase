from selenium import webdriver


def initialDriver():
    chrome_path = 'C:\\Dev Tool\\chromedriver_win32\\chromedriver.exe'
    chrom_opt = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2,
            'javascript': 2
        }
    }
    chrom_opt.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(executable_path=chrome_path,
                               chrome_options=chrom_opt)
    return browser
