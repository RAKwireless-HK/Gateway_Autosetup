######################################################################################################################
# 
# Description: This is the main file to set the RAK Gateway with the specific settings
#              This automation script is based on WisGateOS 2.2.5
#              The settings are based on the gateway profile, which is the JSON file
#              The JSON file of WisGateOS2 XPath data is created by the Web_Controller.py
#              The Web_Controller.py is used to get the settings from the gateway web page
#              The JSON_Controller.py is used to search the specific settings from the JSON file
#              The RAKGateway_Controller.py is used to set the gateway with the specific settings
#              The RAKGateway_Controller.py is the main file to set the gateway
#              The Web_Controller.py and JSON_Controller.py are the helper files to get the settings from the gateway
#
######################################################################################################################

from RAKGateway_Controller import WisGateOS2_Operator

# Variables for the gateway setup
# ================================
_profile_path = "web_profile.json"
_browser = "firefox" # suggested using Firefox
_time_of_waiting = 1 # extra waiting time for the browser to load the page, the current is the figure of LAN connection, for WiFi connection, it may need more time to load the page, may be 4 or 5

_gateway_EUI = "AC1F09FFFE168F87" # Gateway EUI differs in every Gateway. ((Please revise this EUI for every Gateway. or use  input("The Gateway EUI is:"),  etc..))
_gateway_IP = "192.168.230.1" # This IP is the default IP connected by WiFi after the gateway is activated, BUT NOT SUGGEST TO USE WIFI CONNECT FOR ANY AUTO SETUP!!
#_gateway_IP = "" 
_username = "root"
_password = "************" # Your Gateway Login password, ((please revise it to your setting))

_work_mode = "Packet forwarder"  
''' Options: 
----------------
Packet forwarder
Basics station
Built-in network server
----------------
'''

_protocol = "LoRa Gateway MQTT Bridge" 
''' Options: 
----------------
Semtech UDP GWMP Protocol
LoRa Gateway MQTT Bridge
----------------
'''

_mqtt_protocol = "MQTT for ChirpStack 4.x (Protobuf)" 
''' Options: 
----------------
MQTT for Build-in LoRa Network Server
MQTT for ChirpStack 2.x
MQTT for ChirpStack 3.x (JSON)
MQTT for ChirpStack 3.x (Protobuf)
MQTT for ChirpStack 4.x (Protobuf)
----------------
'''

_target_ip_address = "xxx.xxx.xxx.xxx" # for setup packet forwarder 
_LAN_WiFi_Mode = "WPA2-PSK" 
''' Options: 
----------------
WPA-PSK
No Encryption
WPA2-PSK
WPA-PSK/WPA2-PSK Mixed Mode
----------------
'''

_wifi_password = _password
_WAN_Protocol = "Static address" 
''' Options: 
----------------
Static address
DHCP client
PPPoE
----------------
'''

_WAN_interface_option = "Enabled"
''' Options:
----------------
Enabled
Disabled
----------------
'''
_WAN_WiFi_Mode = "WPA2-PSK" 
''' Options: 
----------------
WPA-PSK
No Encryption
WPA2-PSK
WPA-PSK/WPA2-PSK Mixed Mode
----------------
'''

_IPv4_address = "192.168.168.105"  # for Setup WAN Ethernet
_IPv4_mask = "255.255.255.0" # for Setup WAN Ethernet
_IPv4_router = "192.168.168.102" # for Setup WAN Ethernet
_DNS_server = "192.168.168.102" # for Setup WAN Ethernet
_Country_Region = "Hong Kong, HK" # for Setup WAN Ethernet
''' Options:
----------------
Albania, AL
Algeria, DZ
American Samoa, AS
Anguilla, AI
Argentina, AR
Australia, AU
Bahamas, BS
Bangladesh, BD
Barbados, BB
Belize, BZ
Bermuda, BM
Bolivia, BO
Bonaire, Sint Eustatius and Saba, BQ
Bouvet Island, BV
Brazil, BR
Brunei Darussalam, BN
Cambodia, KH
Canada, CA
Chile, CL
Christmas Island, CX
Cocos (Keeling) Islands, CC
Colombia, CO
Comoros, KM
Cook Islands, CK
Costa Rica, CR
Cuba, CU
Curaçao, CW
Denmark, DK
Dominica, DM
Dominican Republic, DO
Ecuador, EC
El Salvador, SV
Estonia, EE
Greenland, GL
Grenada, GD
Guam, GU
Guatemala, GT
Guernsey, GG
Guyana, GY
Heard Island and McDonald Islands, HM
Honduras, HN
Hong Kong, HK
Hungary, HU
Indonesia, ID
Iran, IR
Ireland, IE
Isle of Man, IM
Israel, IL
Jamaica, JM
Japan, JP
Jersey, JE
Jordan, JO
Kuwait, KW
Lao People's Democratic Republic, LA
Liechtenstein, LI
Luxembourg, LU
Macao, MO
Malaysia, MY
Mexico, MX
Moldova, MD
Montserrat, MS
Myanmar, MM
New-Zealand, NZ
Nicaragua, NI
Niue, NU
Norfolk Island, NF
Northern Mariana Islands, MP
Norway, NO
Pakistan, PK
Papua New Guinea, PG
Paraguay, PY
Peru, PE
Philippines, PH
Poland, PL
Puerto Rico, PR
Qatar, QA
Republic of Korea (ROK), KR
Saint Kitts and Nevis, KN
Saint Lucia, LC
Saint Vincent and the Grenadines, VC
Saudi Arabia, SA
Singapore, SG
Slovakia, SK
Slovenia, SI
Solomon Islands, SB
Somalia, SO
South Georgia and the South Sandwich Islands, GS
Sri Lanka, LK
Suriname, SR
Svalbard and Jan Mayen, SJ
Switzerland, CH
Syrian Arab Republic, SY
Taiwan (Republic of China), TW
Tanzania, United Republic of, TZ
Thailand, TH
Tokelau, TK
Tonga, TO
Trinidad and Tobago, TT
Turks and Caicos Islands, TC
Uganda, UG
United Arab Emirates, AE
United Kingdom, GB
United States Minor Outlying Islands, UM
United States of America, US
Uruguay, UY
Vanuatu, VU
Venezuela, Bolivarian Republic of, VE
Vietnam, VN
Virgin Islands (British), VG
Virgin Islands, VI
Worldwide, WW
----------------
'''
Radio_Frequency = "AS923"
''' Options:
----------------
(As the list is dependent on the Country_Region, please refer to the list inside the gateway)
----------------
'''
_Sub_Radio_Frequency = "AS923-1"
''' Options:
----------------
(As the list is dependent on the Radio_Frequency, please refer to the list inside the gateway)
----------------
'''
_WAN_SSID = "SSID_1" # for setup WAN WiFi
_WAN_WiFi_Password = "PASSWORD_1" # for setup WAN WiFi

# ================================
import time

operator = WisGateOS2_Operator(_time_of_waiting, _username, _password, _browser, _gateway_EUI, _gateway_IP, _profile_path)

# ** How to use the operator **

## 1. Initial setup for Gateway Region, Radio Frequency and Sub Radio Frequency
#=============================================================================
#operator.initial_setup(_Country_Region, _Radio_Frequency, _Sub_Radio_Frequency)
#=============================================================================

## 2. Login to the gateway
## (If the gateway is already set, you can skip the initial setup and login to the gateway)
#=============================================================================
#operator.login()
#=============================================================================

## 3. Revise the Region, Radio Frequency and Sub Radio Frequency
## (It was supposed to setup in the initial setup)
#=============================================================================
#operator.set_Radio_Frequency(_Country_Region, _Radio_Frequency, _Sub_Radio_Frequency)
#=============================================================================

## 4. Setup packet forwarder
## (It will be used for the received data to forward to the LoRaWAN Network Server)
#=============================================================================
#operator.set_Packet_Forwarder_To_Gateway(_work_mode, _protocol, _mqtt_protocol, _target_ip_address)
#=============================================================================

## 5. Setup LAN WiFi password 
## (Acceess this Gaway via WiFi. If not setting a password, anyone can access and use the gateway network)
## (** Suggested to set it for security reasons **)
#=============================================================================
#operator.set_LAN_WiFi_Access_with_Password(_LAN_WiFi_Mode,_wifi_password)
#=============================================================================

## 6. Setup WAN Ethernet
## (Ethernet connection with static IP )
## (If the gateway is connected to a specific network, which requires a static IP, you can set it here)
#=============================================================================
#operator.set_WAN_Static_IP(_WAN_Protocol, _IPv4_address, _IPv4_mask, _IPv4_router, _DNS_server)
#=============================================================================

## 7. Setup WAN WiFi
## (Connect to the WiFi AP, using the WiFi of the WiFi AP as WAN)
#=============================================================================
#operator.set_WAN_WiFi_AP(_WAN_interface_option, _WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)
#=============================================================================

## 8. Revise WAN WiFi
#=============================================================================
## (update the settings for connecting to the WiFi AP)
#_WAN_SSID = "SSID_1"
#_WAN_WiFi_Password = "PASSWORD_1"
#operator.revise_WAN_WiFi_AP(_WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)
#operator.logout()

# --- Wait for 5 minutes to update the settings again, just for testing ---
#print("Sleeping for 5 minutes")
#time.sleep(5*60)
#_WAN_SSID = "SSID_2"
#_WAN_WiFi_Password = "PASSWORD_2"
#print(f"Changing WAN SSID to '{_WAN_SSID}'")
#operator.login()
#operator.revise_WAN_WiFi_AP(_WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)
# -----------------------------------------------------------------------------
#=============================================================================

## 9. Logout and close from the gateway
#=============================================================================
#operator.logout()
#operator.close()
#=============================================================================


