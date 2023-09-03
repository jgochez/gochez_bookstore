# Author: Jovanny Gochez
# GitHub username: jgochez
# Date: July 7, 2023
# Description: Maple Grove Library Inventory

class LibraryItem:
    """Create parent class for item objects"""
    def __init__(self, item_id, title):  # object 1: creates library item object
        "Foundational item object data members"
        # [id, title, unique identifier]
        self._item_ID = item_id
        self._title = title

        self._checked_out_by = "None"  # patron id
        self._requested_by = "None"  # patron id
        self._get_location = "ON_SHELF"  # either "ON_SHELF", "ON_HOLD_SHELF", "CHECKED_OUT"
        self._date_checked_out = 0

    def get_info(self):
        list = [self._item_ID, self._title]
        return list

    def get_item_ID(self):
        return self._item_ID

    def get_title(self):
        return self._title

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_checked_out_by(self, member_name):
        self._checked_out_by = member_name
        return self._checked_out_by

    def get_requested_by(self):
        return self._requested_by

    def set_requested_by(self, member_name):
        self._requested_by = member_name
        return self._requested_by

    def get_location(self):
        return self._get_location

    def set_location(self, location):  # either on shelf, on hold, or checked out
        self._get_location = location

    def get_date_checked_out(self):
        return self._date_checked_out

    def set_date_checked_out(self, day):
        self._date_checked_out = day


class Book(LibraryItem):
    """Child class inheriting from LibraryItem class"""
    def __init__(self, item_id, title, author):
        "Created additional and unique data member: author"
        super().__init__(item_id, title)
        self._author = author

        self._check_out_length = 21

    def get_check_out_length(self):
        return self._check_out_length

    def set_check_out_length(self, length):
        self._check_out_length = length

    def get_author(self):
        return self._author


class Album(LibraryItem):
    """Child class inheriting from LibraryItem class"""
    def __init__(self, item_id, title, artist):
        "Additional and unique data member: artist"
        super().__init__(item_id, title)
        self._artist = artist

        self._check_out_length = 14

    def get_check_out_length(self):
        return self._check_out_length

    def set_check_out_length(self, length):
        self._check_out_length = length

    def get_artist(self):
        return self._artist


class Movie(LibraryItem):
    """Child class inheriting from LibraryItem class"""
    def __init__(self, item_id, title, director):
        "Create additional and unique data member: director"
        super().__init__(item_id, title)
        self._director = director

        self._check_out_length = 7

    def get_check_out_length(self):
        return self._check_out_length

    def set_check_out_length(self, length):
        self._check_out_length = length

    def get_director(self):
        return self._director


class Patron:
    """Class that created patron object"""
    def __init__(self, patron_id, patron_name):  # object 2: creates patron object
        "create patron data members"
        # [patron id, patron name]
        self._patron_id = patron_id
        self._patron_name = patron_name

        self._checked_out_items = []  # item objects
        # [ obj1, obj2, ... , objn]
        self._fine_amount = 0

    def info(self):
        list = [self._patron_id, self._patron_name]
        return list

    def get_patron_ID(self):
        return self._patron_id

    def get_patron_name(self):
        return self._patron_name

    def get_checked_out_items(self):  # looks up list of items corresponding to patron obj
        return self._checked_out_items

    def add_checked_out_item(self, lib_item):  # appends checked_out_items
        self._checked_out_items.append(lib_item)

    def remove_checked_out_item(self, lib_item):  # removes from checked_out_items
        self._checked_out_items.pop(lib_item)

    def amend_fine(self, payment):
        self._fine_amount -= payment

    def get_fine_amount(self):
        return round(self._fine_amount, 1)

    def set_fine_amount(self, fine):
        self._fine_amount += fine


class Library:
    """Create library object in this class"""
    def __init__(self):
        "Created data members which include lists that hold libraryItem and Patron objects"
        self._holding = []  # Library class produces this object and set by add_library_holding method [list of lists]
        self._members = []  # Patron class produces this object and set by add_patron method [list of lists]
        self._current_date = 0

    def add_library_item_holding(self, item_obj):  # Call library class [item id, item name, unique identifier]
        self._holding.append(item_obj)
        # print(item_obj.get_info())

    def add_patron(self, patron_object):  # Call patron class [patron id, patron name]
        self._members.append(patron_object)
        # print(patron_object.info())

    def lookup_patron_from_id(self, patron_id): # Lookup patron objects to see if patron id matches
        patron_obj = None
        for specific_obj in self._members:
            compare_id = specific_obj.get_patron_ID()
            if patron_id == compare_id:
                patron_obj = specific_obj

        return patron_obj

    def lookup_item_from_id(self, item_id): # lookup item objects to see if item id matches
        item_obj = None
        item_checked_out = ''  # patron id who checked it out
        item_requested_by = ''  # patron id who has it on hold
        item_location = ''  # on shelf, hold, or checked out
        date_checked_out = 0
        for specific_obj in self._holding:
            compare_id = specific_obj.get_item_ID()
            if item_id == compare_id:
                item_obj = specific_obj
                item_checked_out = item_obj.get_checked_out_by()
                item_requested_by = item_obj.get_requested_by()
                item_location = item_obj.get_location()
                date_checked_out = item_obj.get_date_checked_out()
            else:
                pass

        return item_obj, item_checked_out, item_requested_by, item_location, date_checked_out

    def check_out_library_item(self, patron_id, item_id): # Run through multiple scenarios to verify check out
        patron_obj = self.lookup_patron_from_id(patron_id)
        item_obj, item_checked_person, item_requested_by, item_location, date_checked_out = self.lookup_item_from_id(
            item_id)

        if patron_obj == None:
            print("Patron not in the system.")
        elif item_obj == None:
            print("Item not in system.")
        elif item_location == "CHECKED_OUT":
            print("Item has been checked out, sorry.")
        elif (item_location == "ON_HOLD_SHELF") and (patron_id == item_requested_by):
            item_obj.set_checked_out_by(patron_id)
            item_obj.set_location("CHECKED_OUT")
            item_obj.set_date_checked_out(self._current_date)
            item_obj.set_requested_by("None")
            patron_obj.add_checked_out_item(item_obj)
            item_obj.set_date_checked_out(date_checked_out)
            print("You had it on hold and have now successfully checked it out!")
        elif item_location == "ON_HOLD_SHELF":
            print("Item is on hold, sorry.")
        else:
            item_obj.set_checked_out_by(patron_id)
            item_obj.set_location("CHECKED_OUT")
            item_obj.set_date_checked_out(self._current_date)
            patron_obj.add_checked_out_item(item_obj)
            item_obj.set_date_checked_out(date_checked_out)
            print("Checkout Successful!")

    def return_library_item(self, item_id):  # verify item can be returned
        item_obj, item_checked_person, item_requested_by, item_location, date_checked_out = self.lookup_item_from_id(
            item_id)

        if item_obj == None:
            print("Item not in system.")
        elif item_location != "CHECKED_OUT":
            print("Item already in library.")
        elif (item_requested_by != "None") and (item_location == "CHECKED_OUT"):
            item_obj.set_location("ON_HOLD_SHELF")
            print("Item successfully returned and placed on hold for someone.")
        elif (item_requested_by == "None") and (item_location == "CHECKED_OUT"):
            item_obj.set_location("ON_SHELF")
            print("Item successfully returned.")

    def request_library_item(self, patron_id, item_id):  # Run through multiple scenario to approve request
        patron_obj = self.lookup_patron_from_id(patron_id)
        item_obj, item_checked_person, item_requested_by, item_location, date_checked_out = self.lookup_item_from_id(
            item_id)

        if patron_obj == None:
            print("Patron not in the system.")
        elif item_obj == None:
            print("Item not in system.")
        elif (item_location == "CHECKED_OUT") and (patron_id == item_checked_person):
            print("You currently have the item checked out.")
        elif (item_location == "ON_HOLD") and (patron_id == item_requested_by):
            print("You currently have the item on hold.")
        elif item_location == "ON_HOLD_SHELF":
            print("Item on hold by someone else.")
        elif (item_location == "CHECK_OUT") and (item_requested_by != "None"):
            print("Item is checked out and will be on hold when returned.")
        elif (item_location == "CHECKED_OUT") and (item_requested_by == "None"):
            print("Item is checked out and will be placed on hold for you when returned.")
            item_obj.set_requested_by(patron_id)
        elif (item_location == "ON_SHELF") and (item_requested_by == "None"):
            item_obj.set_requested_by(patron_id)
            item_obj.set_location("ON_HOLD_SHELF")
            print("Item placed on hold successful!")

    def pay_fine(self, patron_id, payment_value):  # get fine and subtract by payment
        for patron_obj in self._members:
            compare_id = patron_obj.get_patron_ID()
            if patron_id == compare_id:
                patron_obj.amend_fine(payment_value)

    def increment_current_date(self):  # subtract check out length after every increment
        self._current_date += 1

        for item_obj in self._holding:  # item object
            location = item_obj.get_location()
            if location == "CHECKED_OUT":
                patron_id = item_obj.get_checked_out_by()
                current_length = item_obj.get_check_out_length()
                updated_length = current_length - 1
                item_obj.set_check_out_length(updated_length)

                for patron_obj in self._members:
                    compare_id = patron_obj.get_patron_ID()
                    if compare_id == patron_id:
                        patron = patron_obj
                        pending_days = item_obj.get_check_out_length()
                        if pending_days < 0:
                            fine = 0.10
                            patron.set_fine_amount(fine)


def library_Simulation():
    # Item objects created
    book_obj_1 = Book("1cx3", "Book Title", "Author")
    album_obj_1 = Album("2dw2", "Album Title", "Artist")
    movie_obj_1 = Movie("3iu7", "Movie Title", "Director")

    # Patron objects created
    person_1 = Patron("person1_id", "Patron Name")
    person_2 = Patron("person2_id", "Patron Name")

    # Library object created
    lib_obj = Library()

    # Adding item to library to holdings
    lib_obj.add_library_item_holding(book_obj_1)
    lib_obj.add_library_item_holding(album_obj_1)
    lib_obj.add_library_item_holding(movie_obj_1)

    # Adding patrons to membership
    lib_obj.add_patron(person_1)
    lib_obj.add_patron(person_2)


    ### Simulation begins here:

    # Person 1 requests an item: output --> hold successful
    lib_obj.request_library_item("person1_id", "1cx3")
    # Person 1 checks out item they had on hold: output --> hold item successfully checked out
    lib_obj.check_out_library_item("person1_id", "1cx3")
    # Person 2 attempts to check out item checked out by person 2: output --> item checked out already
    lib_obj.check_out_library_item("person1_id", "1cx3")

    # 30 days go by and debt should begin to increment due to going past return dates
    for i in range(0, 30):
        lib_obj.increment_current_date()

    # Check out length is subtracted by days incremented IF CHECKED OUT: only book should have decreased
    print("Current check out length for book: ", book_obj_1.get_check_out_length()) # default days = 21
    print("Current check out length for album: ", album_obj_1.get_check_out_length()) # default days = 14
    print("Current check out length for movie: ", movie_obj_1.get_check_out_length()) # default days = 7

    # Check fine for person 1: Note: should be nonzero
    p1_fine_0 = person_1.get_fine_amount()
    print("Person 1 owes this much: $", p1_fine_0)

    # Check fine for person 2 : Note: should be zero
    p2_fine = person_2.get_fine_amount()
    print("Person 2 owes this much: $", p2_fine)

    # Person 1 is making a payment
    lib_obj.pay_fine("person1_id", 0.90)
    print(f"Thanks for the payment! New balance for person 1 is: $ {person_1.get_fine_amount()}")

    # Let three more days go buy: Note: Person 1 hasn't returned book so debt should increment again
    for i in range(0, 3):
        lib_obj.increment_current_date()
    # As expected, debt went up
    p1_fine_1 = person_1.get_fine_amount()
    print("Person 1 owes this much: $", p1_fine_1)

    # Person 1 is making a payment again
    lib_obj.pay_fine("person1_id", 0.30)
    p1_fine_2 = person_1.get_fine_amount()
    print(f"Thanks for the payment! New balance for person 1 is: $ {p1_fine_2}")

    # Person 1 is returning book after paying off debt
    lib_obj.return_library_item("1cx3")

    # Person 2 can finally check out the book! Enjoy!
    lib_obj.check_out_library_item("person2_id", "2dw2")

    ### End of simulation.

if __name__ == '__main__':
    library_Simulation()
