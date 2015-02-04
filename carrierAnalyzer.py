"""
This module is used to analyze carrier information for Canadian phone numbers.

This module will be referencing area code/prefix data (aka. NPA/NXX codes)
provided by the Canadian Numbering here: http://www.cnac.ca/co_codes/co_code_status.htm

Note on phone number portability:
In Canada, phone numbers are portable, meaning that owners can change carriers while
keeping their existing phone numbers. This carrier lookup method only returns the
ORIGINAL carrier for a given number.
"""

import phonenumbers


class CarrierAnalyzer():
    def __init__(self):
        self.carrier = ""