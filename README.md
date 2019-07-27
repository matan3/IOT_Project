# IOT_Project
Project on IOT

Goal:
Record a network traffic and through a Machine-Learning to classify which devices are an IOT or not.

Tools:
Used Python and Pandas library, Wireshark, Tshark , CSV.

The process of creating a Data-Set from Pcap file:

    This project will record a network traffic and save it in a pcap file ->
    This pcap file will convert to a CSV file ->
    Using python the CSV file will fill into a data structor of type - dict of dict ->
    This data structor will split according to specific IOT device ->
    Each of IOT device will split into time segment of X seconds ->
    Each segment will perform an action on specific feature (like sum or average) ->
    The result of the segment will call a Sample ->
    The sample will transfer into a row in the Data-Set ->
    Each Sample will have his id, time segment and the features we perform an action.
