# About RAK
![](https://res.rakwireless.com/tracked/rak/logo/blue-logo-registered-latest.svg)

RAKwireless is a leading player in the global IoT landscape, dedicated to simplifying design and accelerating time-to-market. 
We help everyone who needs IoT.
- System Integrator: Everything they need to build their own IoT solutions, from LoRaWAN® gateways to sensor hub devices and countless sensors.
- Network Provider: They can build an IoT network with RAK’s range of indoor and outdoor gateways.
- Sensor Device maker: They can use the RAK WisDuo Module to make your products compatible with the worldwide LoRaWAN® ecosystem, including networks like Helium and TTN.
- Solution Builder: They can focus on software, while RAK takes care of the IoT connection and so gets to market faster.

We help transform ideas into IoT solutions.
Whether you’re a lone developer or a large business, we have what you need to prototype ideas fast and realistically.

Please visit our website:
- [RAKwireless](https://www.rakwireless.com/)
- [Online Store of RAKwireless](https://store.rakwireless.com/)

# About this project
## WisGateOS2 Setup Automation
This initiative focuses on sharing automation scripts specifically designed for setting up the RAK LoRaWAN Gateway. By providing these scripts, we aim to simplify and streamline the installation process, making it easier for users to implement and effectively manage their LoRaWAN networks.
Our project automates the setup of the RAK WisGateOS2 gateway using Selenium WebDriver. The automation script is developed based on WisGateOS version 2.2.5 and employs a JSON file to define the web profile of the gateway, ensuring a smooth and efficient configuration experience.

## Project Structure
- `__Main.py`: The main script to setup the RAK Gateway with specific settings.
- `JSON_Controller.py`: Handles reading and searching within the JSON profile.
- `RAKGateway_Controller.py`: Contains classes to control the WisGateOS2 and RAK Gateway.
- `Web_Controller.py`: Uses Selenium WebDriver to interact with the web interface of the gateway.
- `web_profile.json`: JSON file defining the web profile of the WisGateOS2.

## Setup
1. Install the required Python packages:
    ```sh
    pip install selenium
    ```

2. Ensure you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).

3. Update the variables in 

__Main.py

 to match your gateway settings.

## Usage

### Initial Setup

To perform the initial setup for the gateway region, radio frequency, and sub-radio frequency:
```python
operator.initial_setup(_Country_Region, _Radio_Frequency, _Sub_Radio_Frequency)
```

### Login to the Gateway

To login to the gateway:
```python
operator.login()
```

### Set Packet Forwarder

To set the packet forwarder to gateway:
```python
operator.set_Packet_Forwarder_To_Gateway(_work_mode, _protocol, _mqtt_protocol, _target_ip_address)
```

### Set LAN WiFi Access

To set the LAN WiFi access with a password:
```python
operator.set_LAN_WiFi_Access_with_Password(_LAN_WiFi_Mode, _wifi_password)
```

### Set WAN Static IP

To set the WAN connected to a static IP address:
```python
operator.set_WAN_Static_IP(_WAN_Protocol, _IPv4_address, _IPv4_mask, _IPv4_router, _DNS_server)
```

### Set WAN WiFi

To set the WAN WiFi:
```python
operator.set_WAN_WiFi_AP(_WAN_interface_option, _WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)
```

### Revise WAN WiFi

To revise the WAN WiFi settings:
```python
operator.revise_WAN_WiFi_AP(_WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)
```

### Logout and Close

To logout and close the connection to the gateway:
```python
operator.logout()
operator.close()
```

## Example

Here is an example of how to use the operator in 

__Main.py

:
### Example 1
1) Initial setup
2) Setup the LAN WiFi access with a password
3) Setup the WAN WiFi connection to a WiFi AP
```python
operator = WisGateOS2_Operator(_time_of_waiting, _username, _password, _browser, _gateway_EUI, _gateway_IP, _profile_path)

# Initial setup
operator.initial_setup(_Country_Region, _Radio_Frequency, _Sub_Radio_Frequency)

# Set LAN WiFi access with password
operator.set_LAN_WiFi_Access_with_Password(_LAN_WiFi_Mode, _wifi_password)

# Set WAN WiFi
operator.set_WAN_WiFi_AP(_WAN_interface_option, _WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)

# Logout and close
operator.logout()
operator.close()
```
### Example 2
1) Login to the Gateway
2) update the WAN WiFi connection to another WiFiAP

```python
operator = WisGateOS2_Operator(_time_of_waiting, _username, _password, _browser, _gateway_EUI, _gateway_IP, _profile_path)

# Login to the gateway
#operator.login()

# Set WAN WiFi AP
operator.revise_WAN_WiFi_AP(_WAN_SSID, _WAN_WiFi_Mode, _WAN_WiFi_Password)

# Logout and close
operator.logout()
operator.close()
```
### Example 3
1) Login to the Gateway
2) Setup packet forwarder
3) Setup the WAN LAN to connect to a static IP

```python
operator = WisGateOS2_Operator(_time_of_waiting, _username, _password, _browser, _gateway_EUI, _gateway_IP, _profile_path)

# Login to the gateway
#operator.login()

# Set packet forwarder
operator.set_Packet_Forwarder_To_Gateway(_work_mode, _protocol, _mqtt_protocol, _target_ip_address)

# Set WAN static IP
operator.set_WAN_Static_IP(_WAN_Protocol, _IPv4_address, _IPv4_mask, _IPv4_router, _DNS_server)

# Logout and close
operator.logout()
operator.close()
```

## License

This project is licensed under the Apache-2.0 license.
```
