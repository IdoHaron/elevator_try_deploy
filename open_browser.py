from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

# Uncomment the next line to start the browser in full screen mode
# chrome_options.add_argument("--start-fullscreen")
# Uncomment the next line to start the browser in kiosk mode
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(executable_path="path/to/chromedriver", chrome_options=chrome_options)
driver.get("https://elevator5.onrender.com/elevator/example")
while True:
    pass
