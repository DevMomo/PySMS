"""
This program utilizes email to SMS gateways to send
text messages. SMS gateway configuration is determined
by determining carrier ID using LibPhoneNumber, Google's
phone number parser. Current implementation only works with 
Canadian phone numbers.

Process:
- Input phone number and message text
- Parse phone number using phonrnumberlib
- Find carrier info using carrier
- Configure appropriate carrier SMS gateway 
- Send SMS message!
"""

from message import Message


if __name__ == "__main__":
    # test message object
    x = Message("+17809524259", "hi")
    print(x.get_message())
    print(x.get_carrier())
    print(x.get_recipient())

