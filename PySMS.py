"""
PySMS is a program that utilizes SMS gateways to send text
messages through email to any Canadian phone number.

Phone numbers are parsed using Google's phonenumberslib
library. Carriers are identified by CarrierAnalyzer, a
module I wrote that cross-reference checks phone numbers
with a carrier prefix database using regex.

Process:
- Input phone number and message text
- Parse phone number using phonrnumberlib
- Find carrier info using carrier
- Find valid SMS gateway
- Send SMS message!
"""

from message import Message

if __name__ == "__main__":
    pass