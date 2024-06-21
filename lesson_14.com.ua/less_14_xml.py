import xml.etree.ElementTree as ET
from pathlib import Path

current_file_path = Path(__file__)
try_xml = current_file_path.parent / "group.xml"

tree = ET.parse(try_xml)

root = tree.getroot()
# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib, child.text)
    for subchild in child:
        print("SUB:", subchild.tag, subchild.attrib, subchild.text)

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        print(timing_exbytes.find('micro').text)

number = 0
v = root.findall(f".//group[number='{number}']")
values = [x.text for x in v ]
for child in v:
    value = child.find('timingExbytes/micro')
    if value is None:
        print("NONE")
        continue
        #raise ValueError("опис що чи чому значення нема")
    print(value.text)

