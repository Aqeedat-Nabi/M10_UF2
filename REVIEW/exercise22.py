import xml.etree.ElementTree as ET

def xml_file() :
    root_Element = ET.Element("Students")
    
# 1ST
    student1 = ET.SubElement(root_Element , "student")
    student1.set("id", "1")

    name1 = ET.SubElement(student1 , "name")
    name1.text = "Noah"

    surname1 = ET.SubElement(student1 , "surname")
    surname1.text = "Chris"

    email1 = ET.SubElement(student1 , "email")
    email1.text = "noah@gmail.com"

    dni1 = ET.SubElement(student1 , "DNI")
    dni1.text = "12345678A"

# 2ND
    student2 = ET.SubElement(root_Element , "student")
    student2.set("id", "2")

    name2 = ET.SubElement(student2 , "name")
    name2.text = "Jake"

    surname2 = ET.SubElement(student2 , "surname")
    surname2.text = "David"

    email2 = ET.SubElement(student2 , "email")
    email2.text = "jake@gmail.com"

    dni2 = ET.SubElement(student2, "DNI")
    dni2.text = "87654321B"
    
# 3RD
    student2 = ET.SubElement(root_Element , "student")
    student2.set("id", "3")

    name2 = ET.SubElement(student2 , "name")
    name2.text = "Jackson"

    surname2 = ET.SubElement(student2 , "surname")
    surname2.text = "Smith"

    email2 = ET.SubElement(student2 , "email")
    email2.text = "jackson@gmail.com"

    dni2 = ET.SubElement(student2, "DNI")
    dni2.text = "87653421C"
        
# 4TH
    student2 = ET.SubElement(root_Element , "student")
    student2.set("id", "4")

    name2 = ET.SubElement(student2 , "name")
    name2.text = "Warner"

    surname2 = ET.SubElement(student2 , "surname")
    surname2.text = "Kane"

    email2 = ET.SubElement(student2 , "email")
    email2.text = "kane@gmail.com"

    dni2 = ET.SubElement(student2, "DNI")
    dni2.text = "67854321D"
        
# 5TH
    student2 = ET.SubElement(root_Element , "student")
    student2.set("id", "5")

    name2 = ET.SubElement(student2 , "name")
    name2.text = "Alex"

    surname2 = ET.SubElement(student2 , "surname")
    surname2.text = "John"

    email2 = ET.SubElement(student2 , "email")
    email2.text = "alex@gmail.com"

    dni2 = ET.SubElement(student2, "DNI")
    dni2.text = "54321321E"
    

    xml_content = ET.tostring(root_Element, encoding="utf-8").decode("utf-8")
    print(xml_content)

    # XML file
    with open("exercise22.xml", "wt") as xml_file:
        xml_file.write(xml_content)

# Call
xml_file()
        