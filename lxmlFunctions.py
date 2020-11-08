# TUTORIALS USED:
# https://lxml.de/tutorial.html
# https://stackoverflow.com/questions/22718101/pretty-print-option-in-tostring-not-working-in-lxml

from lxml import etree
from io import BytesIO



root = etree.Element("root")
child2 = etree.SubElement(root, "ThisIsATagName")
child3 = etree.SubElement(root, "child3")


#print(root.tag)
#print(child2.tag)
#print(child3.tag)

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
print(etree.tostring(profile, pretty_print=True).decode())
print(len(profile))