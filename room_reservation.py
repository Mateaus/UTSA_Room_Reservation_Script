class RoomReservation:

    def __init__(self, chrome):
        self.chrome = chrome
        self.driver = chrome.driver

    def load_root_page(self, url):
        self.driver.get(url)
        xpath = "//a[@class='callToAction']"
        link = self.driver.find_element_by_xpath(xpath)
        url_login = link.get_attribute("href")
        self.driver.get(url_login)

    def login_form(self, username, password):
        old_url = self.driver.current_url
        self.__login_input(username)
        self.__password_input(password)
        self.__submit_login_request()
        self.chrome.wait_page_to_load(20, old_url)

    def __login_input(self, username):
        xpath = "//input[@id='username']"
        login_input_element = self.driver.find_element_by_xpath(xpath)
        login_input_element.send_keys(username)
    
    def __password_input(self, password):
        xpath = "//input[@id='password']"
        password_input_element = self.driver.find_element_by_xpath(xpath)
        password_input_element.send_keys(password)

    def __submit_login_request(self):
        xpath = "//button[@type='submit']"
        submit_buttom = self.driver.find_element_by_xpath(xpath)
        submit_buttom.click()

    def __print_selection_details(self, title, options):
        print(title)
        for index, available_option in enumerate(options):
            print("[{option}] {room_size}".format(option=index, room_size=available_option.text))

    # Room, Hour, Date form selection
    def rhd_form(self, room_index=None, duration_index=None, time_index=None, mute=False):
        old_url = self.driver.current_url
        self.__room_size_selection(room_index, mute)
        self.__duration_selection(duration_index, mute)
        self.__time_selection(time_index, mute)
        self.__date_selection()
        self.__search_action()
        self.chrome.wait_page_to_load(20, old_url)

    def __room_size_selection(self, room_index=None, mute=False):
        xpath = "//select[@id='SelectedRoomSize']"
        room_size_selection = self.chrome.select_elements_by_xpath(xpath)
        if not mute:
            self.__print_selection_details("\n\nRoom Size for:", room_size_selection.options)
        
        if room_index:
            room_selected = int(room_index)
        else:
            room_selected = int(input("Select Room Size: "))
    
        room_size_selection.options[room_selected].click()

    def __duration_selection(self, duration_index=None, mute=False):
        xpath = "//select[@id='SelectedTime']"
        duration_selection = self.chrome.select_elements_by_xpath(xpath)
        if not mute:
            self.__print_selection_details("\n\nDurations:", duration_selection.options)

        if duration_index:
            duration_selected = int(duration_index)
        else:
            duration_selected = int(input("Select Duration: "))

        duration_selection.options[duration_selected].click()

    def __time_selection(self, time_index=None, mute=False):
        xpath = "//select[@id='SelectedTimeSort']"
        time_selection = self.chrome.select_elements_by_xpath(xpath)

        if not mute:
            self.__print_selection_details("\n\nTime at:", time_selection.options)

        if time_index:
            time_selected = int(time_index)
        else:
            time_selected = int(input("Select Time:"))
        
        time_selection.options[time_selected].click()

    def __date_selection(self):
        xpath = "//select[@id='SelectedSearchDate']"
        date_selection = self.chrome.select_elements_by_xpath(xpath)
        self.__print_selection_details("\n\nDates:", date_selection.options)
        
        date_selected = int(input("Select Date:"))
        date_selection.options[date_selected].click()

    def __search_action(self):
        xpath = "//input[@value='Search']"
        search_button = self.driver.find_element_by_xpath(xpath)
        search_button.click()

    def location_form(self, location_index=None, mute=False):
        old_url = self.driver.current_url
        self.__location_selection()
        self.chrome.wait_page_to_load(20, old_url)

    def __location_selection(self, location_index=None, mute=False):
        xpath = "//div[@class='item-link']"
        location_selection = self.driver.find_element_by_xpath(xpath)

        if not mute:
            self.__print_selection_details("\n\nLocations:", location_selection)
        
        if location_index:
            location_selected = int(location_index)
        else:
            location_selected = int(input("Select Location:"))
        
        location_selection[location_selected].click()

    def time_allocation_form(self):
        old_url = self.driver.current_url
        self.__time_allocation_selection()
        self.chrome.wait_page_to_load(20, old_url)

    def __time_allocation_selection(self):
        xpath = "//div[@class='item-link']"
        time_allocation_selection = self.driver.find_element_by_xpath(xpath)
        self.__print_selection_details("\n\nTime Allocations:", time_allocation_selection)
        
        time_allocation_selected = int(input("Select Time Allocation:"))
        time_allocation_selection[time_allocation_selected].click()

    def room_number_form(self):
        old_url = self.driver.current_url
        self.__room_number_selection()
        self.chrome.wait_page_to_load(20, old_url)

    def __room_number_selection(self):
        xpath = "//div[@class='item-link']"
        room_number_selection = self.driver.find_element_by_xpath(xpath)
        self.__print_selection_details("\n\nRoom Number:", room_number_selection)
       
        room_number_selected = int(input("Select Room Number:"))
        room_number_selection[room_number_selected].click()

    def confirmation_page(self):
        old_url = self.driver.current_url
        self.__confirmation_page_details()
        self.__phone_text_notification()
        self.__submit_reservation()
        self.chrome.wait_page_to_load(20, old_url)

    def __confirmation_page_details(self):
        print("\n\nRegistration Information:")
        first_name_xpath = "//input[@id='FirstName']"
        first_name = driver.find_element_by_xpath(first_name_xpath).get_attribute("value")
        last_name_xpath = "//input[@id='LastName']"
        last_name = driver.find_element_by_xpath(last_name_xpath).get_attribute("value")
        email_address_xpath = "//input[@id='EmailAddress']"
        email_address = driver.find_element_by_xpath(email_address_xpath).get_attribute("value")

        print("  First Name: {first_name}".format(first_name=first_name))
        print("   Last Name: {last_name}".format(last_name=last_name))
        print("Email Adress: {email_address}".format(email_address=email_address))

    def __phone_text_notification(self):
        text_notification = input("Phone Notification?(y/n):")
        if text_notification == 'y' or text_notification == 'Y':
            phone_number = input("Phone Number:")
            phone_input_xpath = "//input[@id='Phone']"
            phone_input_element = driver.find_element_by_xpath(phone_element_xpath)
            phone_input_element.send_keys(phone_number)

    def __submit_reservation(self):
        submit_reservation = input("Submit Reservation?(y/n):")
        if submit_reservation == 'y' or submit_reservation == 'Y':
            submit_button_xpath = "//button[@id='btnCallDibs']"
            submit_button_element = driver.find_element_by_xpath(submit_button_xpath)
            submit_button_element.click()
        else:
            self.driver.quit()

    def reservation_response(self):
        xpath = "//div[@class='well well-small well-dark']"
        room_reserve_information = self.driver.find_element_by_xpath(xpath)
        if room_reserve_information:
            print("\n\nReservation Successful!")
            print("\nReservation Location:")
            print(room_reserved_inf.text)
        else:
            print("\n\nFailed to Reserve Room")

    

