from cbc import ChromeBrowserController
from room_reservation import RoomReservation
from getpass import getpass

driver_path = 'C:\SoftwareFiles\chromedriver.exe'
root_url = 'https://lib.utsa.edu/services/study-rooms'

def main():
    chrome = ChromeBrowserController(driver_path, False)

    reservation_room = RoomReservation(chrome)
    reservation_room.load_root_page(root_url)

    username = input("username: ")
    password = getpass("password: ")
    
    reservation_room.login_form(username, password)
    reservation_room.rhd_form(room_index=1, duration_index=1, time_index=1)
    reservation_room.location_form(location_index=2, mute=True)
    reservation_room.time_allocation_form()
    reservation_room.room_number_form()
    reservation_room.confirmation_page()
    reservation_room.reservation_response()


if __name__ == "__main__":
    main()