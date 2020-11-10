# TUTORIALS USED:
# https://lxml.de/tutorial.html
# https://stackoverflow.com/questions/22718101/pretty-print-option-in-tostring-not-working-in-lxml
# https://python101.pythonlibrary.org/chapter31_lxml.html
# https://www.experts-exchange.com/questions/28029302/Python-lxml-encoding.html
# https://stackoverflow.com/questions/28237694/xpath-get-parent-node-from-child-node

from lxml import etree
from io import BytesIO



root = etree.Element("root")
child2 = etree.SubElement(root, "ThisIsATagName")
subchild2_1 = etree.SubElement(child2, "ThisIsASubElementOfChild2")
subchild2_2 = etree.SubElement(child2, "ThisIsAnotherSubElementOfChild2")
child3 = etree.SubElement(root, "child3")


#print(root.tag)
#print(child2.tag)
#print(child3.tag)
print(root.getchildren())  # proof that getchildren() method ONLY GETS FIRST ELEMENT LAYER; YOU HAVE TO ITERATE THROUGH ALL DEEPER ELEMENT LAYERS

#printfile = open("etree_print.txt", "a")
#printfile.write(etree.tostring(root, pretty_print=True).decode())
#printfile.close()

print(len(root))
print(etree.tostring(root, pretty_print=True).decode())
print("\n================\n")
#profile = open("profiles\\testprofile.xml")
#print(profile)

#some_file_or_file_like_object =

profile = etree.parse("profiles\\testprofile.xml")
testoutput = etree.tostring(profile, pretty_print=True).decode()
print(testoutput)
#print(len(profile))
#print(etree.Element().iter)
rootTag = etree.fromstring(testoutput)

def parseXML(xmlFile):
    """
    Parse xml file
    :param xmlFile:
    :return:
    """
    with open(xmlFile, encoding='utf-8') as fobj:
        xml = fobj.read()

    xmlRoot = etree.fromstring(xml)

    ## This for loop implements a "search for every GERMAN term in termbase and print it"
    ## TODO: for loops to get specific language pair termbases, specific entry ids, specific confidence scores
    for SubElement1 in xmlRoot:
        # First subchildren layer (username, termbase)
        for entry in SubElement1:
            # Second layer (entry)
            #print("Position of child within: " + entry.index(xmlRoot))
            for term in entry:
                # Third layer (term)
                if term.get("lang") == "de":
                    print(term.text)
                #print(term.get("lang"))

#parseXML("profiles\\testprofile_NoEncodingDeclaration.xml")