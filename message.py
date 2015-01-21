"""This module is a message class.

A message object contains attributes for
message recipients, as well as message text
content.

Attributes:
    recipientNumber (PhoneNumber): PhoneNumber object containing parsed recipient phone number
    messageText (str): Message text content to be sent
"""


class Message():
    def __init__(self, recipient=0000000000, messagetext="No Message"):
        self.phoneNo = recipient
        self.message = messagetext

    def display_recipient(self):
        """Print recipient's phone number"""
        print(self.phoneNo)

    def display_message(self):
        """Print text message"""
        print(self.message)