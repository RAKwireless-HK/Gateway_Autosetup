import Web_Controller as wc
import JSON_Controller as jc
import time

# This class is used to define the Web Profile of the WisGate OS2
class WisGateOS2_WebProfile:
    def __init__(self, _inProfilePath):
        self.ProfilePath = _inProfilePath
        self.JSONSearcher = jc.JSONSearcher(self.ProfilePath)
        self.Profile = None
    
    def get_field_name(self, _inTarget):
        result = self.JSONSearcher.search_field(_inTarget)
        if result:
            field_name, waiting_time = result
            return field_name
        else:
            return None

# This class is used to define the WisGate OS2
class WisGateOS2:
    def __init__(self, _inUsername, _inPassword, in_ProfilePath, _inBrowser, _inGateway_IP=""):
        self.json_file = in_ProfilePath
        self.IPAddress = _inGateway_IP
        print(_inGateway_IP)
        self.Username = _inUsername
        self.Password = _inPassword
        self.driver = None
        self.waiting_time = 10
        self.browser = _inBrowser
        self.webprofile = WisGateOS2_WebProfile(self.json_file)
    
    def browse_path(self, _inPath=""):        
        self.driver = wc.Web_Controller(self.browser, f"http://{self.IPAddress}{_inPath}", self.Username, self.Password, self.waiting_time)

    def _fill_in_textfield(self, _inPath, _inValue):
        textfield = self.webprofile.get_field_name(_inPath)
        self.driver.send_keys(textfield, _inValue)

    def _click_checkbox(self, _inPath):
        checkbox = self.webprofile.get_field_name(_inPath)
        self.driver.click(checkbox)

    def slide_n_click(self, _inPath):
        slider = self.webprofile.get_field_name(_inPath)
        self.driver.click_with_scroll(slider)

    def _click_button(self, _inPath):
        button = self.webprofile.get_field_name(_inPath)
        self.driver.click(button)
    
    def _multivalue_dropdown_select(self, _inDropDownPath, inListPath, _inValue):
        _dropdown_box = self.webprofile.get_field_name(_inDropDownPath)
        _list_items = self.webprofile.get_field_name(inListPath)
        self.driver.select_multivalue_dropdown_option_by_value(_dropdown_box, _list_items, _inValue)

    def _dropdown_select(self, _inDropDownPath, _inValue):
        _dropdown_box = self.webprofile.get_field_name(_inDropDownPath)
        self.driver.select_dropdown_option_by_value(_dropdown_box, _inValue)

    def _fill_in_password(self, _inPath):
        password_field = self.webprofile.get_field_name(_inPath)
        self.driver.send_keys(password_field, self.Password)
    
    def _click_radio_button(self, _inPath, _inValue):
        radio_button = self.webprofile.get_field_name(_inPath)
        self.driver.click_radio_button(radio_button, _inValue)

    def _click_horizontal_radio_button(self, _inPath, _inValue):
        radio_button = self.webprofile.get_field_name(_inPath)
        self.driver.click_horizontal_radio_button(radio_button, _inValue)

    def _close_netvigation(self):
        self.driver.close()

    def _element_exists(self, _inPath):
        element = self.webprofile.get_field_name(_inPath)
        return self.driver.element_exists(element)

# This class is used to define the RAK Gateway
class RAKGateway:
    def check_IPAddress(self, _inGatewayEUI):
        # get the last 4 digit of_inMAC, split it into 2 parts
        _3rd = _inGatewayEUI[-4:-2]
        #print(_3rd)
        _4th = _inGatewayEUI[-2:]
        #print(_4th)
        # convert from hex to decimal
        _3rd = int(_3rd, 16)
        _4th = int(_4th, 16)
        # set the IP address to 169.254.x.x
        return f"169.254.{_3rd}.{_4th}"
        #print(self.IPAddress)
   
    def get_work_mode(self, _in_work_mode):
        # Set the Work mode to Packet forwarder
        # check if _in_work_mode value:
        # Packet Forwarder --> PF
        # Basics station --> BS
        # Built-in network server --> NS
        if _in_work_mode.upper().replace(" ", "") == "Packet forwarder".upper().replace(" ", ""):
            return "PF"
        elif _in_work_mode.upper().replace(" ", "") == "Basics station".upper().replace(" ", ""):
            return "BS"
        elif _in_work_mode.upper().replace(" ", "") == "Built-in network server".upper().replace(" ", ""):
            return "NS"
    def get_Protocol_model(self, _in_protocol):
        # Semtech UDP GWMP Protocol --> GWMP
        #LoRa Gateway MQTT Bridge --> MQTT
        if _in_protocol.upper().replace(" ", "") == "Semtech UDP GWMP Protocol".upper().replace(" ", ""):
            return "GWMP"
        elif _in_protocol.upper().replace(" ", "") == "LoRa Gateway MQTT Bridge".upper().replace(" ", ""):
            return "MQTT"
    def get_MQTT_Protocol(self, _mqtt_protocol):
        # MQTT for Build-in LoRa Network Server --> RAK
        # MQTT for ChirpStack 2.x --> CHIRP_STACK_2
        # MQTT for ChirpStack 3.x (JSON) --> CHIRP_STACK_3_JSON
        # MQTT for ChirpStack 3.x (Protobuf) --> CHIRP_STACK_3_PBUF
        # MQTT for ChirpStack 4.x (Protobuf) --> CHIRP_STACK_4_PBUF
        if _mqtt_protocol.upper().replace(" ", "") == "MQTT for Build-in LoRa Network Server".upper().replace(" ", ""):
            return "RAK"
        elif _mqtt_protocol.upper().replace(" ", "") == "MQTT for ChirpStack 2.x".upper().replace(" ", ""):
            return "CHIRP_STACK_2"
        elif _mqtt_protocol.upper().replace(" ", "") == "MQTT for ChirpStack 3.x (JSON)".upper().replace(" ", ""):
            return "CHIRP_STACK_3_JSON"
        elif _mqtt_protocol.upper().replace(" ", "") == "MQTT for ChirpStack 3.x (Protobuf)".upper().replace(" ", ""):
            return "CHIRP_STACK_3_PBUF"
        elif _mqtt_protocol.upper().replace(" ", "") == "MQTT for ChirpStack 4.x (Protobuf)".upper().replace(" ", ""):
            return "CHIRP_STACK_4_PBUF"
    def get_WiFi_Mode(self, _in_mode):
        # WPA-PSK --> WPA_PSK
        # No Encryption --> NO_ENC
        # WPA2-PSK --> WPA2_PSK
        # WPA-PSK/WPA2-PSK Mixed Mode --> MIX_MODE
        if _in_mode.upper().replace(" ", "") == "WPA-PSK".upper().replace(" ", ""):
            return "WPA_PSK"
        elif _in_mode.upper().replace(" ", "") == "No Encryption".upper().replace(" ", ""):
            return "NO_ENC"
        elif _in_mode.upper().replace(" ", "") == "WPA2-PSK".upper().replace(" ", ""):
            return "WPA2_PSK"
        elif _in_mode.upper().replace(" ", "") == "WPA-PSK/WPA2-PSK Mixed Mode".upper().replace(" ", ""):
            return "MIX_MODE"
    def get_Protocol(self, _in_protocol):
        # Static address --> STATIC
        # DHCP client --> DHCP
        # PPPoE --> PPPOE
        if _in_protocol.upper().replace(" ", "") == "Static address".upper().replace(" ", ""):
            return "STATIC"
        elif _in_protocol.upper().replace(" ", "") == "DHCP client".upper().replace(" ", ""):
            return "DHCP"
        elif _in_protocol.upper().replace(" ", "") == "PPPoE".upper().replace(" ", ""):
            return "PPPOE"


# This class is used to define the WisGate OS2 Operator, which is used to control the WisGate OS2. It is the major class that is used to control the WisGate OS2
# It is used to control the WisGate OS2, such as setting the Packet Forwarder to Gateway, setting the LAN WiFi Access with Password, setting the WAN connected to a Static IP address
# It is also used to login to the WisGate OS2 and to do the initial setup of the WisGate OS2
# It is also used to set the IP address of the WisGate OS2
# The logic of this class is to use the name of the field in the JSON file to control the WisGate OS2, the JSON file is used to define the Web Profile of the WisGate OS2. The JSON file is used to define the field name of the WisGate OS2.
class WisGateOS2_Operator:
    def __init__(self, _time_of_waiting, _inUsername, _inPassword, _inBrowser, _inGatewayEUI="", _inGateway_IP="", _inProfilePath="web_profile.json"):
        self.GatewayEUI = _inGatewayEUI
        self.GatewayIP = self.set_IP(_inGatewayEUI, _inGateway_IP)
        self.Username = _inUsername
        self.Password = _inPassword
        self.wisgateos2 = None
        self.profile = _inProfilePath
        self.browser = _inBrowser
        self.time_of_waiting = _time_of_waiting
        self.gateway = RAKGateway()
    
    def set_IP(self, _inEUI, _inGatewayIP):
        if _inGatewayIP == "":
            rak_gateway = RAKGateway()
            _inGatewayIP = rak_gateway.check_IPAddress(_inEUI)
        return _inGatewayIP

    def goto_Configuration_Configuration(self):
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Configurations")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Con.Configuration")

    def goto_Network_LAN(self):
        self.wisgateos2._click_button("Network")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.LAN")
        time.sleep(1+self.time_of_waiting)

    def goto_Network_WAN(self):
        self.wisgateos2._click_button("Network")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN")
        time.sleep(1+self.time_of_waiting)

    # Auto Initial setup of the WisGate OS2
    def initial_setup(self, _in_country, _in_radio_region, _in_radio_sub_region):
        time.sleep(1+self.time_of_waiting)
        self.GatewayIP = self.set_IP(self.GatewayEUI, "")
        self.wisgateos2 = WisGateOS2(self.Username, self.Password, self.profile, self.browser, self.GatewayIP)
        self.wisgateos2.browse_path()
        # setup the password
        self.wisgateos2._fill_in_textfield("Initial_Setup.1.Set_your_password", self.Password)
        self.wisgateos2._fill_in_textfield("Initial_Setup.1.Confirm_your_password", self.Password)
        self.wisgateos2._click_checkbox("Initial_Setup.1.I_agree_to_the_terms_and_conditions")
        self.wisgateos2._click_button("Initial_Setup.1.Confirm_your_password_button")
        time.sleep(3+self.time_of_waiting)
        # setup the Country
        self.wisgateos2._multivalue_dropdown_select("Initial_Setup.2.Select_your_country", "Initial_Setup.2.Select_your_country_ListItems" ,_in_country)
        time.sleep(self.time_of_waiting)
        # setup the LoRaWAN region
        self.wisgateos2._dropdown_select("Initial_Setup.2.Select_your_region", _in_radio_region)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._dropdown_select("Initial_Setup.2.Select_your_region_AS923-1_dropdown", _in_radio_sub_region)
        self.wisgateos2._click_checkbox("Initial_Setup.2.I_agree_to_the_terms_and_conditions")
        self.wisgateos2._click_button("Initial_Setup.2.Confirm_button")
        time.sleep(1+self.time_of_waiting)
        self.wisgateos2._click_button("Update_n_Save_button")
        time.sleep(14+self.time_of_waiting)

    # Set the Packet Forwarder to Gateway, if needed, set the Protocol, MQTT Protocol, and Target IP Address
    def set_Packet_Forwarder_To_Gateway(self, _in_work_mode, _in_protocol, _mqtt_protocol, _target_ip_address):
        time.sleep(1+self.time_of_waiting)
        self.goto_Configuration_Configuration()
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_radio_button("Con.Configuration.Packet_Forwarder_option", self.gateway.get_work_mode(_in_work_mode))
        
        time.sleep(1+self.time_of_waiting)
        self.wisgateos2.slide_n_click("Con.Configuration.Packet_Forwarder.Protocol_Page")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_radio_button("Con.Configuration.Packet_Forwarder.Protocol_Page.Set_To_LoRaWAN", self.gateway.get_Protocol_model(_in_protocol))
        time.sleep(self.time_of_waiting)
        self.wisgateos2._multivalue_dropdown_select("Con.Configuration.Packet_Forwarder.Protocol_Page.LoRaGatewayMQTTBridgeParameters.MQTT_Protocol", "Con.Configuration.Packet_Forwarder.Protocol_Page.LoRaGatewayMQTTBridgeParameters.MQTT_Protocol_ListItems",_mqtt_protocol)
        time.sleep(1+self.time_of_waiting)
        self.wisgateos2._fill_in_textfield("Con.Configuration.Packet_Forwarder.Protocol_Page.LoRaGatewayMQTTBridgeParameters.MQTT_Broker_Address", _target_ip_address)
        time.sleep(self.time_of_waiting)
        self.wisgateos2.slide_n_click("Update_n_Save_button")
        time.sleep(14+self.time_of_waiting)

    # login to the WisGate OS2
    def login(self):
        self.wisgateos2 = WisGateOS2(self.Username, self.Password, self.profile, self.browser, self.GatewayIP)
        self.wisgateos2.browse_path()
        self.wisgateos2._fill_in_password("password")
        self.wisgateos2._click_button("login_button")
        time.sleep(4+self.time_of_waiting)

    # Set the LAN WiFi Access with Password
    def set_LAN_WiFi_Access_with_Password(self, _in_WiFi_Mode, _inPassword):
        time.sleep(1+self.time_of_waiting)
        self.goto_Network_LAN()
        self.wisgateos2._click_button("Net.LAN.WiFi_Page")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.LAN.WiFi_Page.Setting_Button")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._multivalue_dropdown_select("Net.LAN.WiFi_Page.WiFi_Setting.Encryption", "Net.LAN.WiFi_Page.WiFi_Setting.Encryption_ListItems", _in_WiFi_Mode)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._fill_in_textfield("Net.LAN.WiFi_Page.WiFi_Setting.Password", _inPassword)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.LAN.WiFi_Page.WiFi_Setting.Save_Button")
        time.sleep(2+self.time_of_waiting)
        self.wisgateos2._click_button("Net.LAN.WiFi_Page.WiFi_Setting.Close_Button")
        time.sleep(14+self.time_of_waiting)

    # Set the WAN connected to a Static IP address
    def set_WAN_Static_IP(self, _in_Protocol, _inIPv4_Address, _inIPv4_Mask, _inIPv4_Router, _inDNS_Server):
        time.sleep(1+self.time_of_waiting)
        self.goto_Network_WAN()
        self.wisgateos2._click_button("Net.WAN.Ethernet_Page")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.Ethernet_Page.Setting_Button")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_horizontal_radio_button("Net.WAN.Ethernet_Page.Protocol",_in_Protocol)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._fill_in_textfield("Net.WAN.Ethernet_Page.IPv4_Address", _inIPv4_Address)
        self.wisgateos2._fill_in_textfield("Net.WAN.Ethernet_Page.IPv4_netmask", _inIPv4_Mask)
        self.wisgateos2._fill_in_textfield("Net.WAN.Ethernet_Page.IPv4_router", _inIPv4_Router)
        self.wisgateos2._fill_in_textfield("Net.WAN.Ethernet_Page.DNS_Server", _inDNS_Server)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.Ethernet_Page.Add_Button")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.Ethernet_Page.Save_Button")
        time.sleep(2+self.time_of_waiting)
        self.wisgateos2._click_button("Net.LAN.WiFi_Page.WiFi_Setting.Close_Button")
        time.sleep(14+self.time_of_waiting)
    
    def set_Radio_Frequency(self, _in_country, _in_radio_region, _in_radio_sub_region):
        time.sleep(1+self.time_of_waiting)
        self.goto_Configuration_Configuration()
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Con.Configuration.Frequency_Plan.Button")
        time.sleep(1+self.time_of_waiting)
        # setup the Country
        self.wisgateos2._multivalue_dropdown_select("Initial_Setup.2.Select_your_country", "Initial_Setup.2.Select_your_country_ListItems" ,_in_country)
        time.sleep(self.time_of_waiting)
        # setup the LoRaWAN region
        self.wisgateos2._dropdown_select("Initial_Setup.2.Select_your_region", _in_radio_region)
        time.sleep(self.time_of_waiting)
        self.wisgateos2._dropdown_select("Initial_Setup.2.Select_your_region_AS923-1_dropdown", _in_radio_sub_region)
        self.wisgateos2._click_checkbox("Initial_Setup.2.I_agree_to_the_terms_and_conditions")
        self.wisgateos2._click_button("Initial_Setup.2.Confirm_button")
        time.sleep(1+self.time_of_waiting)
        self.wisgateos2._click_button("Update_n_Save_button")
        time.sleep(14+self.time_of_waiting)

    def set_WAN_WiFi_AP(self, _in_Interface_option, _IN_SSID ,_in_WiFi_Mode, _inPassword, _in_Protoco=""):
        time.sleep(1+self.time_of_waiting)
        self.goto_Network_WAN()
        self.wisgateos2._click_button("Net.WAN.WiFi_Page")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.WiFi_Page.Setting_Button")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_horizontal_radio_button("Net.WAN.WiFi_Page.Interface_option", _in_Interface_option)
        time.sleep(1+self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.WiFi_Page.Interface_option_warning_close")
        time.sleep(1+self.time_of_waiting)
        self.goto_Network_WAN()
        time.sleep(1+self.time_of_waiting)
        if self.wisgateos2._element_exists("Net.WAN.WiFi_Page.Interface_option_Leave_page"):
            self.wisgateos2._click_button("Net.WAN.WiFi_Page.Interface_option_Leave_page")
            time.sleep(14+self.time_of_waiting)

        self.revise_WAN_WiFi_AP(_IN_SSID ,_in_WiFi_Mode, _inPassword, _in_Protoco)

    def revise_WAN_WiFi_AP(self, _IN_SSID ,_in_WiFi_Mode, _inPassword, _in_Protoco=""):
        self.goto_Network_WAN()
        time.sleep(1+self.time_of_waiting)
        # Re-enter the WAN WiFi page        
        self.wisgateos2._click_button("Net.WAN.WiFi_Page")
        time.sleep(self.time_of_waiting)
        
        self.wisgateos2._click_button("Net.WAN.WiFi_Page.Setting_Button")
        time.sleep(1+self.time_of_waiting)

        if self.wisgateos2._element_exists("Net.WAN.WiFi_Page.Enter_SSID_Button"):
            self.wisgateos2._click_button("Net.WAN.WiFi_Page.Enter_SSID_Button")
            time.sleep(self.time_of_waiting)
        # set the SSID, Encryption, and Password
        self.wisgateos2._fill_in_textfield("Net.WAN.WiFi_Page.SSID_Textbox", _IN_SSID)
        self.wisgateos2._multivalue_dropdown_select("Net.WAN.WiFi_Page.Encryption_Drpodown", "Net.WAN.WiFi_Page.Encryption_ListItems", _in_WiFi_Mode)
        self.wisgateos2._fill_in_textfield("Net.WAN.WiFi_Page.Password_Textbox", _inPassword)

        # using the default DHCP client
        # no extra setting is needed

        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("Net.WAN.WiFi_Page.Save_Button")
        time.sleep(3)
        self.wisgateos2._click_button("Net.WAN.WiFi_Page.Close_Button")
        time.sleep(20)

    def logout(self):
        self.wisgateos2._click_button("Bottom_Icon")
        time.sleep(self.time_of_waiting)
        self.wisgateos2._click_button("BI.Logout")
        time.sleep(self.time_of_waiting)

    def close(self):
        self.wisgateos2._close_netvigation()


"""
# TEST CODE
_gateway_EUI = "AC1F09FFFE168F87"
_gateway_IP = "192.168.168.105"
#_gateway_IP = ""
_username = "root"
_password = "rak@12345678"
_profile_path = "web_profile.json"

operator = WisGateOS2_Operator(_username, _password, _gateway_EUI, _gateway_IP, _profile_path)
operator.login()
"""        

    
