"""
This module is used to analyze carrier information given a Canadian phone numbers.

This module will be referencing area code/prefix data (aka. NPA/NXX codes)
provided by the Canadian Numbering Administrator here: http://www.cnac.ca/co_codes/co_code_status.htm
where we load the page based on a given area code, then search the page for corresponding CO Code.

Example:
Number: (780) 200 1010
Then, area code = 780 and CO code = 200.
So what we have is 780 corresponding to Edmonton, AB and 200 correponding to WIND Mobile Corp.

The website is scraped using the Beautiful Soup library.

Note on phone number portability:
In Canada, phone numbers are portable, meaning that owners can change carriers while
keeping their existing phone numbers. This carrier lookup method only returns the
ORIGINAL carrier for a given number.

Attributes:
    baseURL (str): Contains base URL for Canadian Numbering Administrator site containing area code carrier information
    carrierName (str): Carrier name will be stored in this once resolved 
"""

import phonenumbers
import urllib.request
from bs4 import BeautifulSoup


class CarrierAnalyzer():
    def __init__(self):
        """Return base URL used for scraping carrier information and carrier name"""
        self.baseURL = "http://www.cnac.ca/data/COCodeStatus_NPA" # followed by "[areaCode].htm"
        self.carrierName = None # carrier initially null

    def analyzeNumber(self, number):
        """Recieve Canadian phone number and determine carrier name"""
        areaCode = number[0,2] # first 3 digits of a national number represent the area code
        COCode = number[3,5] # second 3 digits of a national number represent the CO Code (carrier indicator)

        soup = BeatifulSoup(urllib.request.urlopen(baseURL+areaCode+".htm").read())




