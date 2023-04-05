import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

ISP_HANDLE = "@sparklightcares"
USERNAME = "isp_complainer_"
PASSWORD = "************"

options = webdriver.FirefoxOptions()
service = Service("/home/hoods/Documents/development/geckodriver")


def rest(s):
    time.sleep(s)


def q_rest():
    time.sleep(3)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.upload_speed = None
        self.download_speed = None
        self.driver = webdriver.Firefox(service=service, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # Check my internet speed
        self.driver.get('https://www.speedtest.net')
        rest(10)
        self.driver.maximize_window()
        rest(5)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        rest(20)
        dl_speed_element = self.driver.find_element(By.CLASS_NAME,
                                                    "result-data-large.number.result-data-value.download-speed")
        # Isolate the download speed as a float
        self.download_speed = float(dl_speed_element.text)
        print(self.download_speed)
        rest(20)
        ul_speed_element = self.driver.find_element(By.CLASS_NAME,
                                                    "result-data-large.number.result-data-value.upload-speed")
        # Isolate the upload speed as a float
        self.upload_speed = float(ul_speed_element.text)
        print(self.upload_speed)
        q_rest()
        exit_microsoft_bullshit = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/"
                                                                     "div[3]/div[3]/div/div[8]/div/div/div[2]/a")
        exit_microsoft_bullshit.click()

    def tweet_at_provider(self, down_speed, up_speed):
        self.driver.get("https://Twitter.com")
        q_rest()
        self.driver.maximize_window()
        q_rest()
        # Login to Twitter
        login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/"
                                                   "div[2]/div/div/div[1]/a")
        login.click()
        q_rest()
        user_entry = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/"
                                                        "div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/"
                                                        "div/div[2]/div/input")
        user_entry.send_keys(USERNAME)
        next_login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div["
                                                        "2]/div/div/div/div/div/div[2]/"
                                                        "div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_login.click()
        q_rest()
        pass_entry = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/"
                                                        "div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/"
                                                        "label/div/div[2]/div[1]/input")
        pass_entry.send_keys(PASSWORD)
        submit_login = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/"
                                                          "div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/"
                                                          "div/div/div")
        submit_login.click()
        q_rest()
        # Send dissatisfied tweet
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftEditor-content[contenteditable="true"]')
        tweet_box.click()
        tweet_box.send_keys(
            f"Hey, {ISP_HANDLE}, in our contract you guaranteed my download speeds would be 200Mbps and "
            f"my upload speeds 20Mbps. My curent speeds via www.speedtest.net are {down_speed} and"
            f" {up_speed}. I am thoroughly dissatisfied. I live in Joplin, MO.")
        q_rest()
        send_it = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/"
                                                     "div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/"
                                                     "div[2]/div[3]/div")
        send_it.click()
