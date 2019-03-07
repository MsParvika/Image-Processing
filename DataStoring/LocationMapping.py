import xml.etree.ElementTree as ET


def mapLocationIdWithName(dirPath):
    location_dict = {}
    tree = ET.parse(dirPath+'\\devset_topics.xml')
    root = tree.getroot()
    for topic in root.iter('topic'):
        number = topic.find('number').text
        title = topic.find('title').text
        location_dict[number] = title

    return location_dict
