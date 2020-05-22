class User:

    def __init__(self, name, DNI, postal_address, phone_number, email):
        self.name = name
        self.DNI = DNI
        self.postal_address = postal_address
        self.phone_number = phone_number
        self.email = email

    def check_billing_user(self):
        if len(self.phone_number) != 9 or not self.phone_number.isdigit():
            return False
        elif len(self.DNI) != 9 or not self.DNI[-1].isalpha() \
                or not self.DNI[0:-1].isdigit():
            return False
        elif len(self.postal_address) != 5 or not self.postal_address.isdigit():
            return False
        elif not ("".join([c for c in self.name if c is not " "])).isalpha():
            return False
        elif '@' not in self.email:
            return False
        else:
            return True
