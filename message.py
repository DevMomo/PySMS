"""This module is a message class.

A message object contains attributes for
message recipients, as well as message text
content.

Attributes:
    phoneNo (PhoneNumber): PhoneNumber object containing parsed recipient phone number
    carrier (str) : String containing name of carrier
    message (str): Message text content to be sent
"""

import phonenumbers
from phonenumbers import carrier


class Message():
    def __init__(self, recipient=0, messageText=""):
        """We cast phone the received number input as string. Both attributes are given default values"""
        self.phoneNo = phonenumbers.parse(str(recipient), "CA")
        self.carrier = carrier.name_for_number(self.phoneNo, "en")
        self.message = messageText

    def get_recipient(self):
        """Print recipient's phone number"""
        return self.phoneNo

    def get_carrier(self):
        """Print phone number carrier"""
        return self.carrier

    def get_message(self):
        """Print text message"""
        return self.message