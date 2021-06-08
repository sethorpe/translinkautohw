import os
import shutil
import utility
import unittest
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestTranslinkAuto(unittest.TestCase):

    # Clean the Translink Screenshots folder before every run.
    if os.path.isdir('Translink_Screenshots'):
        # Folder exists! Delete it
        shutil.rmtree('Translink_Screenshots')
        # Create a new folder for this code run
        os.mkdir('Translink_Screenshots')
    else:
        # Folder doesn't exist, so create one
        os.mkdir ('Translink_Screenshots')

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(10)
        #Open URL
        self.driver.get("https://new.translink.ca")
        #Maximize Window / Set Window Size
        # self.driver.maximize_window()
        self.driver.set_window_size(1440, 800)
        
    
    def tearDown(self):
        # As a note, In addCleanup, the first in, is executed last.
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screen_shot)
    
    def screen_shot(self):
        # Take a Screen-shot of the page on which a failure occurs.
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Errors/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")
    
    def test_find_bus_route(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()
        self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")

   
    def test_find_bus_route_and_save_to_favs(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

    def test_validate_edit_favs(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Click on 'Edit' button
        self.driver.find_element(By.CLASS_NAME, 'editFavouriteButton').click()

        # Change the favourite name
        self.driver.find_element(By.NAME, "currentFavourite").clear()
        self.driver.find_element(By.NAME, 'currentFavourite').send_keys('99 Commercial to UBC')

        # Save the new name
        self.driver.find_element(By.NAME, 'btnEditFav').click()

        # Validate the name change
        my_route = self.driver.find_element(By.LINK_TEXT, '99 Commercial to UBC')
        self.assertEqual(my_route.text, '99 Commercial to UBC', 'Link text does not match expected result')
        self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")



    def test_validate_favs_link_title(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present.
        # First we check the link text matches, then we check the URLs too.
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
        self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")

        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

    
    def test_validate_route_title_displayed(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
       
        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

        # Select frame element on the page, set to variable "iframe" and switch to it
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
             "99 Commercial-Broadway / UBC (B-Line)", "The text displayed does not match expected result")
        self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")

   

    def test_validate_stop_no_displayed(self):
        self.driver.find_element(By.LINK_TEXT,'Next Bus').click()

        # Find the search box, first clear it and then enter search parameter '99'
        self.driver.find_element_by_id('NextBusSearchTerm').clear()
        self.driver.find_element_by_id('NextBusSearchTerm').send_keys('99')

        # Click on 'Find My Next Bus'
        self.driver.find_element(By.CSS_SELECTOR, ".verticallyCenteredContent > button").click()

        # Click on "Add Fav" Icon
        self.driver.find_element(By.CLASS_NAME, 'AddDelFav').click()

        # Click the dialog box
        self.driver.find_element(By.ID, "add-to-favourites_dialog").click()

        # First clear the text field, then type in "TransLink Auto Homework"
        self.driver.find_element(By.NAME, 'newFavourite').clear()
        self.driver.find_element(By.NAME, 'newFavourite').send_keys('Translink Auto Homework')

        # Click on Add to Favorites button to save
        self.driver.find_element(By.XPATH, '//button[contains(text(),\'Add to Favourites\')]').click()
        # Wait 5 seconds before moving on
        sleep(5)

        # Get current url and save to param for comparison later
        my_route_url = self.driver.current_url

        # Click on "My Favs" icon
        self.driver.find_element(By.LINK_TEXT, 'My Favs').click()

        # Validate “Translink Auto Homework” link is present
        # Set variable
        my_route = self.driver.find_element(By.LINK_TEXT, 'Translink Auto Homework')
        self.assertEqual(my_route.text, 'Translink Auto Homework', 'Link text does not match expected result')
       
        # Click on "Translink Auto Homework" link
        my_route.click()

        # Now get the current url and compare with param my_route_url from earlier.
        self.assertEqual(self.driver.current_url, my_route_url, 'URLs do not match!')

        # Select frame element on the page, set to variable "iframe" and switch to it
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) main:nth-child(14) div.gridContainer.NarrowFlexColumnBlockLayout.noBottomPadding.introBlockTheme:nth-child(7) section.CopyMain > iframe:nth-child(1)')
        self.driver.switch_to.frame(iframe)

        # Validate “99 Commercial-Broadway / UBC (B-Line)” is displayed on page
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".txtRouteTitle").text,\
             "99 Commercial-Broadway / UBC (B-Line)", "The text displayed does not match expected result")

        # Click on 'To Comm'l-Bdway Stn / Boundary B-Line'
        self.driver.find_element(By.LINK_TEXT, 'To Comm\'l-Bdway Stn / Boundary B-Line').click()

        # Wait for page load
        sleep(5)

        # Click on UBC Exchange Bay 7
        self.driver.find_element(By.LINK_TEXT, 'UBC Exchange Bay 7').click()
        
        # Wait for page load
        sleep(5)

        # Validate “Stop # 61935” is displaying
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, '.stopNo').text,\
             "Stop # 61935", "The Stop # displayed does not match expected result")
        self.driver.get_screenshot_as_file(os.getcwd() + "/Translink_Screenshots/" + "screenshot_" + self.id() + "__" + utility.current_time() + ".png")

if __name__ == '__main__':
    unittest.main()