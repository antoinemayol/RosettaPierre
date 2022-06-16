from selenium import webdriver
from time import sleep
import sys, threading


class Bot():

    def __init__(self, email, password) -> None:

        self.email = email
        self.password = password

        if(email == None):
            print("Missing email")
            return

        if (password == None):
            print("Missing password")
            return

        self.StartNav()

        self.rosetta_link_login = "https://learn.rosettastone.com/"
        self.rosetta_link_launchpad = "https://login.rosettastone.com/#/launchpad"
        self.driver.get(self.rosetta_link_login)

        self.Login()


        sleep(5)
        #Looking for Testing button
        try:
            self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div[2]/div[1]").click()
        except:
            pass

        #Going into lesson menu
        self.driver.find_element_by_xpath("//*[text()='Fluency Builder']").click()

        print("Please select a lesson..")

        input("Pess ENTER when you are ready")

        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[3]/div").click()

        self.DoLesson()

    def StartNav(self):
        try:
            self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        except:
            print("Please make sure that the given chrome driver is up-to-date")

    def Login(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/input').send_keys(self.email)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/div/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]').click()

        self.wait = webdriver.support.ui.WebDriverWait(self.driver, 999)
        self.wait_for_correct_current_url(self.rosetta_link_launchpad)
        self.wait_for_correct_current_url(self.rosetta_link_launchpad)

    def DoLesson(self):

        sleep(2)
        tasks_contener_xpath = "//*[@id='root']/div/div/div[1]/div[1]"
        tasks_contener = self.driver.find_element_by_xpath(tasks_contener_xpath)
        tasks_contener_list = tasks_contener.find_elements_by_tag_name("div[data-qa='MapItemText']")

        while True:
            for e in tasks_contener_list[1::]:
                e.click()
                sleep(90)

    def wait_for_correct_current_url(self, desired_url):
        self.wait.until(
            lambda driver: driver.current_url == desired_url)

if __name__ == "__main__":
    my_bot = Bot(sys.argv[1],sys.argv[2])