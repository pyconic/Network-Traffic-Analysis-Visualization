# Network-Traffic-Analysis-Visualization

# Description
This project is a Python-based tool for visualizing network traffic, integrating functionalities from dpkt, socket, and pygeoip libraries. It processes network traffic data captured in a .pcap file, typically generated using Wireshark, and visualizes the geographical locations of IP addresses in the network traffic.

# Features
• `Integration with Wireshark`: The tool is designed to work with .pcap files, commonly produced by Wireshark, a 
   widely-used network packet analysis tool. <br>
• `Network Traffic Parsing`: Reads .pcap files to extract and analyze network traffic data. <br>
• `Geolocation Mapping`: Utilizes pygeoip to map IP addresses to their corresponding geographical locations. <br>
• `KML Document Creation`: Generates KML (Keyhole Markup Language) files, enabling the visualization of network paths 
   on geographic mapping services like Google Earth.

# How it Works
• `Wireshark Packet Capture`: The tool is compatible with packet capture files (.pcap) created by Wireshark. <br>
• `Parsing Packet Captures`: Opens and reads a .pcap file, extracting source and destination IP addresses from the 
   network packets. <br>
• `IP Geolocation`: Determines geographical locations (longitude and latitude) for each IP address using the 
   GeoLiteCity.dat database. <br>
• `KML Generation`: Produces a KML file that plots points and lines representing network traffic flows between source 
   and destination IPs.

# Usage
`Install necessary Python libraries`: dpkt, socket, and pygeoip. 

Ensure that your .pcap file (generated from Wireshark) and GeoLiteCity.dat are in the same directory as the script.
Execute the script to generate KML output, which can be viewed in geographic mapping applications.

# Dependencies
• `Python 3.x` <br>
• `dpkt`: For parsing .pcap files. <br>
• `socket`: For network interactions. <br>
• `pygeoip`: For converting IP addresses to geographic locations.

# Limitations
The geolocation accuracy relies on the GeoLiteCity.dat database.
Encrypted or malformed packets are not processed by the script.
