import xml.etree.ElementTree as ET

class XMLParser():

    """A simple parser based on the DOM API"""

    def __init__(self, file):
        self.tree = ET.parse(file)
        self.root = tree.getroot()

    def printItem(self):
        pass

    def printAttribs(self):
        self.tree

    def printAttribs(self):

        # # one specific item attribute
        # print('Item #2 attribute:')
        # print(root[0][1].attrib)

        # all item attributes
        print('\nAll attributes:')
        for elem in root:
            for subelem in elem:
                print(subelem.attrib)

        # one specific item's data
        # print('\nItem #2 data:')
        # print(root[0][1].text)

        # all items data
        print('\nAll item data:')

        for elem in root:
            for subelem in elem:
                print(subelem.text)


if __name__ == '__main__':

    testfile = 'Counting.metamind'
    parser = XMLParser(testfile)

