"""
This program utilizes email to SMS gateways to send
text messages. SMS gateway configuration is determined
by determining carrier ID using LibPhoneNumber, Google's
phone number parser. Current implementation only works with 
Canadian phone numbers.

Process:
- Input phone number and text content
- Parse phone number and determine carrier
- Configure appropriate carrier SMS gateway 
- Send SMS message!
"""

from message import Message


if __name__ == "__main__":
    # test message object
    x = Message("+17802008960", "hi")
    x.display_message()
    x.display_recipient()
