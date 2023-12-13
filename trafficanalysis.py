import dpkt  # Import dpkt library for parsing packet capture files
import socket  # Import socket library for network interactions
import pygeoip  # Import pygeoip library for IP geolocation services

gi = pygeoip.GeoIP('GeoLiteCity.dat')  # Initialize the GeoIP object with the GeoLiteCity database

def main():
    f = open('PCAPFILE', 'rb')  # Open the .pcap file in binary read mode
    pcap = dpkt.pcap.Reader(f)  # Create a pcap Reader object for parsing the .pcap file
    # Define the header part of the KML file with XML version, KML schema, and custom style
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
                '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'  # Define the footer part of the KML file
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter  # Combine header, generated KML content, and footer
    print(kmldoc)  # Print the complete KML document

def plotIPs(pcap):
    kmlPts = ''  # Initialize an empty string to store KML placemarks
    for (ts, buf) in pcap:  # Iterate through each packet in the pcap file
        try:
            eth = dpkt.ethernet.Ethernet(buf)  # Parse the Ethernet layer of the packet
            ip = eth.data  # Extract the IP layer from the Ethernet layer
            src = socket.inet_ntoa(ip.src)  # Convert source IP address to a readable format
            dst = socket.inet_ntoa(ip.dst)  # Convert destination IP address to a readable format
            KML = retKML(dst, src)  # Generate KML for the source and destination IP addresses
            kmlPts += KML  # Append the generated KML to the kmlPts string
        except:
            pass  # Ignore errors and continue with the next packet
    return kmlPts  # Return the accumulated KML placemarks

def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)  # Get geolocation info for the destination IP
    src = gi.record_by_name(srcip)  # Get geolocation info for the source IP
    try:
        dstlongitude = dst['longitude']  # Extract the longitude of the destination IP
        dstlatitude = dst['latitude']  # Extract the latitude of the destination IP
        srclongitude = src['longitude']  # Extract the longitude of the source IP
        srclatitude = src['latitude']  # Extract the latitude of the source IP
        # Format the KML placemark with coordinates and other details
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml  # Return the formatted KML placemark
    except:
        return ''  # If an error occurs, return an empty string

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly
