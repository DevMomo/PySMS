"""This module is a message class.

A message object contains attributes for
message recipients, as well as message text
content.

Attributes:
    recipientNumber (PhoneNumber): PhoneNumber object containing parsed recipient phone number
    messageText (str): Message text content to be sent
"""

class message():
    def __init__(self, recipientNumber, messageText):
        self.phoneNo = recipientNumber
        self.message = messageText