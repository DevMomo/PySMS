"""This module is a message class.

This class represents an SMS text message
object. A Message object is used my the main
PySMS module when acquiring a message and recipient
phone number from the user to send.

Attributes:
    phoneNo (PhoneNumber): PhoneNumber object containing parsed recipient phone number
    nationalNo (str): Phone number excluding country code
    carrier (str) : String containing name of carrier
    message (str): Message text content to be sent

>>> x = Message("+17802001714", "hi")
>>> x.message
'hi'
>>> str(x.get_recipient())
'Country Code: 1 National Number: 7802001714'
>>> x.nationalNo
'7802001714'

>>> x = Message("7802001714", "hi")
>>> x.message
'hi'
>>> str(x.get_recipient())
'Country Code: 1 National Number: 7802001714'
>>> x.nationalNo
'7802001714'
"""

import phonenumbers


class Message():
    def __init__(self, recipient="", message_text=""):
        """We cast phone the received number input as string. Both attributes are given default values"""
        self.recipient = ""
        self.phoneNo = phonenumbers.parse(str(recipient), "CA")
        self.nationalNo = phonenumbers.national_significant_number(self.phoneNo)
        self.message = message_text

    def get_recipient(self):
        """Returns recipient's phone number"""
        return self.phoneNo

    def get_message(self):
        """Returns text message"""
        return self.message

if __name__ == "__main__":
    import doctest
    doctest.testmod()