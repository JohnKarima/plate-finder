import time
time.sleep(2)
print("Hello!")
time.sleep(2)
print(" ")
print("This is a simple Python program...")
time.sleep(2)
print(" ")
print("It takes the first part of a Chartered Diplomat's (CD) numberplate...")
time.sleep(2)
print(" ")
print("And tells you what country it belongs to!")
time.sleep(2)
print(" ")
print("Some lore...")
time.sleep(2)
print(" ")
print("This order was decided based on when the respective country recognized our independence!")
time.sleep(2)
print(" ")
print("Have a go!")
print(" ")

master_list = {
    1: "Germany",
    2: "Russian Federation",
    3: "Ethiopia",
    4: "China",
    5: "Norway",
    6: "Hungary",
    7: "Egypt",
    8: "Serbia",
    9: "Italy",
    10: "France",
    11: "Slovakia",
    12: "Denmark",
    13: "Japan",
    14: "Sudan",
    15: "Austria",
    16: "India",
    17: "Australia",
    18: "Canada",
    19: "Holy See (The Vatican)",
    20: "Finland",
    21: "Switzerland",
    22: "Britain",
    23: "Liberia",
    24: "Israel",
    25: "Nigeria",
    26: "Ghana",
    27: "Netherlands",
    28: "Malawi",
    29: "United States of America (USA)",
    30: "Belgium",
    31: "Sweden",
    32: "Pakistan",
    33: "Poland",
    34: "Korea",
    35: "Bulgaria",
    36: "Greece",
    37: "Cuba",
    38: "Kuwait",
    39: "Spain",
    40: "United Nations Development Programme (UNDP)",
    41: "World Health Organization (WHO)",
    42: "United Nations Educational, Scientific and Cultural Organization (UNESCO)",
    43: "International Bank for Reconstruction and Development (The World Bank)",
    44: "Food and Agriculture Organization of the United Nations (FAO)",
    45: "World Food Programme (WFP)",
    46: "Romania",
    47: "Thailand",
    48: "The African Union (A.U)",
    49: "Colombia",
    50: "India",
    51: "Somalia",
    52: "Brazil",
    53: "Turkey",
    54: "Lesotho",
    55: "Zambia",
    56: "Madagascar",
    57: "Malaysia",
    58: "D.R. Congo (DRC)",
    59: "Swaziland",
    60: "Sri Lanka",
    61: "Iraq",
    62: "Rwanda",
    63: "United Nations High Commissioner for Refugees / UN Refugee Agency (UNHCR)",
    64: "United Nations Children’s Fund (UNICEF) Eastern & Southern African Regional Office",
    65: "Iran",
    66: "Cyprus",
    67: "Argentina",
    68: "United Nations Information Centre (UNIC)",
    69: "Philippines",
    70: "Burundi",
    71: "Chile",
    72: "Oman",
    73: "League of Arab States / Arab League",
    74: "European Union",
    75: "Yemen",
    76: "Kenya Mission to UNEP",
    77: "Côte d’Ivoire (Consulate)",
    78: "Bangladesh",
    79: "Saudi Arabia",
    80: "United Nations Centre for Human Settlements / UN-Habitat (UNCHS)",
    81: "Libya",
    82: "Ireland (Consulate)",
    83: "United Nations Centre for Human Settlements / UN-Habitat (Kenya Mission)",
    84: "Algeria",
    85: "Palestine",
    86: "Uganda",
    87: "Mexico",
    88: "Morocco",
    89: "Costa Rica (Consulate)",
    90: "Gabon (Consulate)",
    91: "United Nations Children’s Fund (UNICEF) Kenya Country Office",
    92: "Indonesia",
    93: "Portugal",
    94: "Venezuela",
    95: "Zimbabwe",
    96: "International Civil Aviation Organization (I.C.A.O)",
    97: "Asian Development Bank",
    99: "Peru",
    100: "International Finance Corporation (I.F.C)",
    101: "United Nations Environment Programme (UNEP) Norwegian Mission",
    102: "Mozambique",
    103: "South Africa",
    104: "Eritrea",
    105: "United Nations Office in Nairobi (UNON)",
    106: "Czech Republic",
    107: "The Aga Khan",
    108: "UNFPA",
    110: "UNIDO (United Nations Industrial Development Organization)",
    115: "Ukraine",
    116: "Sahrawi",
    117: "Djibouti",
    118: "Sierra Leone",
    121: "South Sudan",
    123: "United Arab Emirates"
}

CD_Code = input("Write the first digit(s) of the Chartered Diplomat's numberplate to see what country they belong to, or write 'ALL' to see our master list ")

if CD_Code == "ALL":
    print("You typed in ALL!")
    for key in master_list.keys():
        print ('CD: {}, Country: {}!'.format(key, master_list[key]))
if CD_Code in master_list:
    print ('CD: {}, Country: {}!'.format(CD_Code, master_list[CD_Code]))
else:
    print('Starting a new country all by yourself sexy? Our records dont have one with the Chartered Diplomat Number:{}.'.format(CD_Code))
