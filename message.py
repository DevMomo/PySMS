"""This module is a message class.

A message object contains attributes for
message recipients, as well as message text
content.

Attributes:
    phoneNo (PhoneNumber): PhoneNumber object containing parsed recipient phone number
    carrier (str) : String containing name of carrier
    message (str): Message text content to be sent

>>> x = Message("+17802001714", "hi")
>>> x.get_message()
'hi'
>>> str(x.get_recipient())
'Country Code: 1 National Number: 7802001714'
"""

import phonenumbers


class Message():
    def __init__(self, recipient=0, message_text=""):
        """We cast phone the received number input as string. Both attributes are given default values"""
        self.phoneNo = phonenumbers.parse(str(recipient), "CA")
        self.message = message_text
        self.gateway = ""

    def get_recipient(self):
        """Returns recipient's phone number"""
        return self.phoneNo

    def get_gateway(self):
        """Returns valid SMS gateway"""
        return self.carrier

    def get_message(self):
        """Returns text message"""
        return self.message

if __name__ == "__main__":
    import doctest
    doctest.testmod()