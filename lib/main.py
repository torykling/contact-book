from peewee import *

db = PostgresqlDatabase('contacts', user='postgres',
                        password='', host='localhost', port='5432')


db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
    email = CharField()


db.create_tables([Contact])


class ContactBook:

    def start(self):
        task = input(
            "\n What would you like to do? \n Show all contacts- s \n Add a contact- a\n Find a contact -f \n or quit Contact Book -q")
        if task == "s":
            self.show()
        elif task == "a":
            self.add()
        elif task == "f":
            self.search()
        elif task == "q":
            return
        else:
            self.start()

    def show(self):
        for contact in Contact.select():
            print(
                f' \n first name: {contact.first_name}\n last name: {contact.last_name}\n phone: {contact.phone}\n email: {contact.email} \n')
        self.start()

    def add(self):
        new_first = input("What is this contact's first name?")
        new_last = input("What is this contact's last name?")
        new_phone = input("What is this contact's phone number?")
        new_email = input("What is this contact's email?")
        new_contact = Contact(first_name=new_first,
                              last_name=new_last, phone=new_phone, email=new_email)
        new_contact.save()
        self.start()

    def search(self):
        search_name = input(
            "What is the first name of the contact you'd like to find?")
        search_result = Contact.get(Contact.first_name == search_name)
        print(
            f'\n first name: {search_result.first_name}\n last name: {search_result.last_name}\n phone: {search_result.phone}\n email: {search_result.email}\n')
        update = input("Would you like to update this contact? y/n")
        if update == 'y':
            updated_first = input(
                "What is the updated first name of this contact?")
            updated_last = input(
                "What is the updated last name of this contact?")
            updated_phone = input(
                "What is the updated phone number for this contact?")
            updated_email = input(
                "What is the updated email for this contact?")
            search_result.first_name = updated_first
            search_result.last_name = updated_last
            search_result.phone = updated_phone
            search_result.email = updated_email
            search_result.save()
            print("\n This contact has been updated.\n")
            self.start()
        else:
            delete = input("Would you like to delete this contact? y/n")
            if delete == 'y':
                search_result.delete_instance()
                print("\n This contact has been deleted.\n")
                self.start()
            else:
                self.start()


contact_book = ContactBook()
contact_book.start()
