from selenium import webdriver
from fake_useragent import UserAgent

# These are our options for performance and opens up the possibility for multithreadding
# Note that these lists are not exhaustive and may be changed/added to further increase our performance/stability
# For more info on these command lines -> https://peter.sh/experiments/chromium-command-line-switches/

def performance():
	ua = UserAgent()
	user_agent = ua.random
	options = webdriver.ChromeOptions()
	#options.headless = True
	options.add_argument(f'user-agent={user_agent}')
	options.add_argument("--window-size=1920,1080")
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument("--disable-extensions")
	options.add_argument("--start-maximized")
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox-and-elevated')
	options.add_argument('--disable-infobars')
	options.add_experimental_option("prefs", {"profile.default_content_settings_values.notifications": 1})
	#options.add_argument("--proxy-server='direct://'")
	#options.add_argument("--proxy-bypass-list=*")
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH, options=options)
	return driver
