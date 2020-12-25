"""
Kivy extensions
"""
from kivy.lang import Builder
from kivy.app import App
from kivy.uix import filechooser
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config

"""
Pandas
"""
import pandas as pd

"""
Selenium P
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
System extensions
"""
import time

# global phone_result, time_result, address_result, map__pos, mobile_phone, crossed
# global file_path, driver, cols, addresses_list, aim_cols_to_use, login, password
# global check_mobile_phone


# class to storage object in Popup
class FileChoosePopup(Popup):
    load = ObjectProperty()


class Tab(TabbedPanel):
    Config.set('graphics', 'resizable', False)

    """
    Kivy
    """
    # when user don't choose any file and trying to load path:
    file_path = StringProperty("No file chosen")
    the_popup = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    keyword = ObjectProperty(None)

    def get_data(self, path=file_path):

        get_email = self.email.text
        get_password = self.password.text
        get_keyword = self.keyword.text
        file_path = self.get_file.text

        """
            Pandas
            """
        # change regarding to input from user
        login = get_email
        password = get_password
        addresses_cols_to_use = 1
        comments_cols_to_use = 1
        mobile_phone = int(get_keyword)

        ###
        # empty storage for list of cols that will be used to work with:
        ###
        cols = []
        # I use one more list for addresses because I'll need to use for loop
        # to iterate through addresses, but cols I'll use only to set the range of
        # working with cols for pandas
        addresses_list = []

        ###
        # aims cols to use(at that moment users need to follow the guide
        # and set up the DB regarding described steps
        ###
        aim_cols_to_use = "Phone_num"
        time_cols_to_use = "Time"
        comment = "Connections"
        address = "Location"
        addresses_list.append(address)

        cols.extend((comment, aim_cols_to_use, time_cols_to_use, address))
        """
        pandas read csv file that user chose
        """
        use_db = file_path
        self.da = pd.read_csv(filepath_or_buffer=use_db,
                usecols=cols)
        # da = pd.read_csv(filepath_or_buffer=use_db,
        #                  usecols=cols)

        # check for m. phone that user provided
        check_mobile_phone = self.da.loc[self.da[aim_cols_to_use] == mobile_phone]

        # FOR TESTING PURPOSES, delete:
        print("email: ", get_email,
              "\npassword: ", get_password,
              "\nkeyword: ", get_keyword,
              "\ntype of keyword ", type(get_keyword),
              "\nfilepath: ", file_path)

        # empty lists to work with data that we will get from csv file
        person__info_address = []
        person__info_number = []
        person__info_time = []
        name__index = 0

        """
        declaring methods related with pandas:
        """
        def isEmpty(param):
            return param.empty

        """
        pandas explicitly wait functions 
        """

        # explicit wait with input for a single text_box BY ID:
        def exp_wait__singleId(element_inp, key):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, element_inp))
                )
            finally:
                inp = driver.find_element_by_id(element_inp)
                inp.clear()
                inp.send_keys(key)
                inp.send_keys(Keys.RETURN)

        # explicit wait with input for a single text_box BY CLASS:
        def exp_wait__singleClass(element_inp, key):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, element_inp))
                )
            finally:
                inp = driver.find_element_by_class_name(element_inp)
                inp.clear()
                inp.send_keys(key)
                inp.send_keys(Keys.RETURN)

        # explicit wait with input for a single text_box BY CSSselector:
        def exp_wait__singleCSSselector(element_inp, key):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, element_inp))
                )
            finally:
                inp = driver.find_element_by_css_selector(element_inp)
                inp.clear()
                inp.send_keys(key)
                inp.send_keys(Keys.RETURN)

        # explicit wait with input for a single text_box BY Xpath:
        def exp_wait__singleXpath(element_inp, key):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element_inp))
                )
            finally:
                inp = driver.find_element_by_xpath(element_inp)
                # inp.clear()
                inp.send_keys(key)
                inp.send_keys(Keys.RETURN)

        # explicit wait with click functionality searching by ID
        def exp_wait__clickId(element_inp):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, element_inp))
                )
            finally:
                inp = driver.find_element_by_id(element_inp).click()

        # explicit wait with click functionality searching by CLASS
        def exp_wait__clickClass(element_inp):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, element_inp))
                )
            finally:
                inp = driver.find_element_by_class_name(element_inp).click()

        # explicit wait with click func searching BY CSSselector:
        def exp_wait__clickCSSselector(element_inp):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, element_inp))
                )
            finally:
                inp = driver.find_element_by_css_selector(element_inp).click()

        # explicit wait with input for a single text_box BY Xpath:
        def exp_wait__clickXpath(element_inp):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element_inp))
                )
            finally:
                time.sleep(2)
                inp = driver.find_element_by_xpath(element_inp)
                time.sleep(2)
                inp.click()

        # explicit wait until element will be clickable:
        def exp_wait__untilClickable(element_inp):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, element_inp))
                )
            finally:
                inp = driver.find_element_by_xpath(element_inp).click()


        if isEmpty(check_mobile_phone) is True:
            print("Keyword not exists")
        for index, row in check_mobile_phone.iterrows():

            for ad in addresses_list:
                map__pos = row[ad]

            for information in row:
                address_result = row[-1]
                phone_result = row[-3]
                time_result = row[-2]
            person__info_address.append(address_result)
            person__info_number.append(phone_result)
            person__info_time.append(time_result)

            max__index = len(person__info_address)
            crossed = False

            # check if data exist in csv:
        if isEmpty(check_mobile_phone) is False:
            ###
            # using webdriver-manager chromedriver will check current version of
            # driver, and work with actualized version not locally but in cache
            # with default path: ~/.m2/repository/webdriver
            ###
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get("http://www.googlemaps.com")

            if len(person__info_address) > 1:

                ###
                # sign in process
                ###

                # sign in button:
                exp_wait__clickId("gb_70")
                exp_wait__singleCSSselector("input[name='identifier'][type='email']", login)
                time.sleep(1)
                exp_wait__singleXpath("//input[@type='password'][@name='password']", password)
                time.sleep(1)
                # dropdown menu 
                exp_wait__clickXpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[1]")
                # my places
                exp_wait__clickXpath("/html/body/jsl/div[3]/div[9]/div[23]/div/div[2]/ul/ul[1]/li[2]/button")
                # maps 
                exp_wait__clickXpath("//*[@id='pane']/div/div[1]/div/div/div[2]/button[4]")
                time.sleep(1)

                ###
                # get the redirecting link according with url when generating link
                # for multiple addresses custom map
                ###
                url__cmaps = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/span/a[3]")
                url__cmaps_text = url__cmaps.text
                url__cmaps_value = url__cmaps.get_attribute("href")

                # redirecting using previous created link
                driver.get(url__cmaps_value)  # updating driver to work with different url
                time.sleep(1)

                # iterates through list with addresses for phone num we searching for:
                while not crossed:
                    time.sleep(1)
                    if name__index < max__index:
                        exp_wait__singleId("mapsprosearch-field", person__info_address[name__index])
                        time.sleep(1)
                        exp_wait__clickId("addtomap-button")
                        name__index += 1  # going on the next element id in list (next address)
                    elif name__index >= max__index:
                        crossed = True

                # changing style for points on the map:
                time.sleep(1)
                exp_wait__clickXpath("//*[@id='ly0-layerview-stylepopup-link']/div[2]/div")
                time.sleep(1)
                exp_wait__clickXpath("//*[@id='layer-style-popup']/div[3]")
                time.sleep(1)
                exp_wait__clickXpath("//*[@id='style-by-type-selector-type-4']/div")

            # before bug fixing here was addresses_list as attribute in len() function
            elif len(person__info_address) == 1:
                exp_wait__singleId("searchboxinput",
                                   person__info_address[name__index])  # google maps text box for addresses

    def open_popup(self):
        # loads data for popup:
        self.the_popup = FileChoosePopup(load=self.load)

        # opens popup with loaded data:
        self.the_popup.open()

    def load(self, selection):
        # save data
        self.file_path = str(selection[0])
        # after button pressed, and data selected -> close popup
        self.the_popup.dismiss()

        # check for non-empty list i.e file selected:
        if self.file_path:
            self.ids.get_file.text = self.file_path


Builder.load_file('app_design_FINAL.kv')


class AppAnalizer(App):

    def build(self):
        return Tab()


if __name__ == "__main__":
    AppAnalizer().run()


