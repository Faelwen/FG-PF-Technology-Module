import zipfile
import shutil
import csv
from lxml import etree
import html

module_file_name = "TechnologyGuide.mod"
xml_definition_file = "definition.xml"
xml_database_file = "db.xml"
license_file = "license.html"
armor_csv_file = "data/Armor.csv"
weapon_csv_file = "data/Weapons.csv"

FG_module_directory = "E:\\Fantasy Grounds\\DataDir\\modules"

module_name = "Technology Guide"
module_author = "Faelwen"
module_ruleset = "PFRPG"
library_tag_name = "TechnologyGuide"
library_name = "Technology Guide"
library_category = "PFRPG"

library_entries =   [{"Entry name":"---Legal Notice---",
                    "Entry tag":"AA.License",
                    "Link type":"librarylink",
                    "Window class":"referencetext",
                    "Record name": "License"}]

def populate_library_entries(xml_library_entries):
    for entry in library_entries:
        xml_library_entry =  etree.SubElement(xml_library_entries, entry["Entry tag"])
        xml_library_entry_linktype = etree.SubElement(xml_library_entry, entry["Link type"], type="windowreference")
        xml_library_entry_linktype_class = etree.SubElement(xml_library_entry_linktype, "class")
        xml_library_entry_linktype_class.text = entry["Window class"]
        xml_library_entry_linktype_recordname = etree.SubElement(xml_library_entry_linktype, "recordname")
        xml_library_entry_linktype_recordname.text = entry["Record name"]
        xml_library_entry_name = etree.SubElement(xml_library_entry, "name", type="string")
        xml_library_entry_name.text = entry["Entry name"]


def populate_license(xml_root):
    xml_license = etree.SubElement(xml_root, "License", static="true")
    xml_license_link = etree.SubElement(xml_license,"librarylink", type="windowreference")
    xml_license_link_class = etree.SubElement(xml_license_link, "class")
    xml_license_link_class.text = "referencetext"
    xml_license_link_recordname = etree.SubElement(xml_license_link, "recordname")
    xml_license_link_recordname.text = ".."
    xml_license_name = etree.SubElement(xml_license,"name", type="string")
    xml_license_name.text = "License"
    xml_license_text = etree.SubElement(xml_license,"text", type="formattedtext")
    with open(license_file, 'r') as file:
        license_test = file.read()
    xml_license_text.text = license_test


def generate_xml_def_file():
    xml_def_root = etree.Element('root')
    xml_def_name = etree.SubElement(xml_def_root, "name")
    xml_def_name.text = module_name
    xml_def_author = etree.SubElement(xml_def_root, "author")
    xml_def_author.text = module_author
    xml_def_ruleset = etree.SubElement(xml_def_root, "ruleset")
    xml_def_ruleset.text = module_ruleset
    with open(xml_definition_file, 'w') as file:
        file.write(etree.tostring(xml_def_root,pretty_print=True,encoding="iso-8859-1",xml_declaration=True).decode("iso-8859-1"))


def generate_xml_db_file(xml_root):
    with open(xml_database_file, 'w', encoding="iso-8859-1") as file:
        xmldoc = html.unescape(etree.tostring(xml_root,pretty_print=True,encoding="iso-8859-1",xml_declaration=True).decode("iso-8859-1"))
        file.write(xmldoc)


def generate_module():
    with zipfile.ZipFile(module_file_name, 'w', zipfile.ZIP_DEFLATED) as file:
        file.write('db.xml')
        file.write('definition.xml')
        #myzip.write('thumbnail.png')
    print("Module generated")


def copy_to_Fantasy_Grounds():
    shutil.copy(module_file_name, FG_module_directory)
    print("Module copied to Fantasy Grounds")


def generate_xml_structure(xml_root):
    xml_libraries = etree.SubElement(xml_root, "library", static="true")
    xml_library = etree.SubElement(xml_libraries, library_tag_name)
    xml_library_name = etree.SubElement(xml_library, "name", type="string")
    xml_library_name.text = library_name
    xml_library_categoryname = etree.SubElement(xml_library, "categoryname", type="string")
    xml_library_categoryname.text = library_category
    xml_library_entries = etree.SubElement(xml_library, "entries")
    xml_reference = etree.SubElement(xml_root, "reference", static="true")
    xml_ref_armor = etree.SubElement(xml_reference,"armor")
    xml_ref_equipment = etree.SubElement(xml_reference,"equipment")
    xml_ref_feats = etree.SubElement(xml_reference,"feats")
    xml_ref_npcdata = etree.SubElement(xml_reference,"npcdata")
    xml_ref_skills = etree.SubElement(xml_reference,"skills")
    xml_ref_spells = etree.SubElement(xml_reference,"spells")
    xml_ref_tables = etree.SubElement(xml_reference,"tables")
    xml_ref_weapon = etree.SubElement(xml_reference,"weapon")
    xml_lists = etree.SubElement(xml_root, "lists", static="true")

    populate_library_entries(xml_library_entries)
    populate_license(xml_root)

    populate_armor(xml_ref_armor)
    populate_weapon(xml_ref_weapon)


def populate_armor(xml_ref_armor):
    with open(armor_csv_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "armor"

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_price, i_armor_bonus, i_maxbonus,
            i_penalty, i_spellfail, i_speed30, i_speed20, i_weight, i_capacity,
            i_usage, i_craft, i_description] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_armor, item_ref)
            #Type
            xml_ref_type = etree.SubElement(xml_ref, "type", type="string")
            xml_ref_type.text = i_type.strip()
            #Subtype
            xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
            xml_ref_subtype.text = i_subtype.strip()
            #Name
            xml_ref_name = etree.SubElement(xml_ref, "name", type="string")
            xml_ref_name.text = i_name.strip()
            #Price
            xml_ref_cost = etree.SubElement(xml_ref, "cost", type="string")
            xml_ref_cost.text = i_price.strip()
            #Armor bonus
            xml_ref_ac = etree.SubElement(xml_ref, "ac", type="number")
            xml_ref_ac.text = i_armor_bonus.strip()
            #Max dex bonus
            if i_maxbonus != "—":
                xml_ref_maxdex = etree.SubElement(xml_ref, "maxstatbonus", type="number")
                xml_ref_maxdex.text = i_maxbonus.strip()
            #Armor check penalty
            xml_ref_penalty = etree.SubElement(xml_ref, "checkpenalty", type="number")
            xml_ref_penalty.text = i_penalty.strip()
            #Arcane spell failure
            xml_ref_fail = etree.SubElement(xml_ref, "spellfailure", type="number")
            xml_ref_fail.text = i_spellfail.strip()
            #Speed 20 feet
            if i_speed20 != "—":
                xml_ref_speed20 = etree.SubElement(xml_ref, "speed20", type="number")
                xml_ref_speed20.text = i_speed20.strip()
            #Speed 30 feet
            if i_speed30 != "—":
                xml_ref_speed30 = etree.SubElement(xml_ref, "speed30", type="number")
                xml_ref_speed30.text = i_speed30.strip()
            #Weight
            xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
            xml_ref_weight.text = i_weight.strip()
            #Crafting
            xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
            xml_ref_reqs.text = i_craft.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = "<p><b>Capacity:</b> {0}; <b>Usage:</b> {1}</p>{2}".format(i_capacity, i_usage, i_description).strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')



def populate_weapon(xml_ref_weapons):
    with open(weapon_csv_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "weapon"

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_price, i_dmg_s, i_dmg_m, i_critical,
            i_range, i_capacity, i_usage, i_weight, i_dmg_type, i_special,
            i_description, i_crafting, i_bonus, i_cl, i_aura] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_weapons, item_ref)
            #Type
            xml_ref_type = etree.SubElement(xml_ref, "type", type="string")
            xml_ref_type.text = i_type.strip()
            #Subtype
            xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
            xml_ref_subtype.text = i_subtype.strip()
            #Name
            xml_ref_name = etree.SubElement(xml_ref, "name", type="string")
            xml_ref_name.text = i_name.strip()
            #Price
            xml_ref_cost = etree.SubElement(xml_ref, "cost", type="string")
            xml_ref_cost.text = i_price.strip()
            #Damage
            xml_ref_damage = etree.SubElement(xml_ref, "damage", type="string")
            xml_ref_damage.text = i_dmg_m.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Critical
            xml_ref_crit = etree.SubElement(xml_ref, "critical", type="string")
            xml_ref_crit.text = i_critical.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Range
            if i_range != "":
                xml_ref_range = etree.SubElement(xml_ref, "range", type="number")
                xml_ref_range.text = i_range.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Weight
            xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
            xml_ref_weight.text = i_weight.strip()
            #Damage type
            if i_dmg_type != "—":
                xml_ref_damagetype = etree.SubElement(xml_ref, "damagetype", type="string")
                xml_ref_damagetype.text = i_dmg_type.strip()
            #Properties
            if i_special != "—":
                xml_ref_prop = etree.SubElement(xml_ref, "properties", type="string")
                xml_ref_prop.text = i_special.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = "<p><b>Capacity:</b> {0}; <b>Usage:</b> {1}</p>{2}".format(i_capacity, i_usage, i_description).strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Crafting
            xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
            xml_ref_reqs.text = i_crafting.strip()
            #Bonus
            if i_bonus != "":
                xml_ref_bonus = etree.SubElement(xml_ref, "bonus", type="number")
                xml_ref_bonus.text = i_bonus.strip()
            #Aura
            if i_aura != "":
                xml_ref_aura = etree.SubElement(xml_ref, "aura", type="string")
                xml_ref_aura.text = i_aura.strip()
            #CL
            if i_cl != "":
                xml_ref_cl = etree.SubElement(xml_ref, "cl", type="number")
                xml_ref_cl.text = i_cl.strip()


weapon_csv_file

def main():
    xml_root = etree.Element('root', version="2.0")
    generate_xml_structure(xml_root)
    generate_xml_db_file(xml_root)
    generate_xml_def_file()
    generate_module()
    copy_to_Fantasy_Grounds()


if __name__ == '__main__':
    main()