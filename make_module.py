import zipfile
import shutil
import csv
from lxml import etree
import html

module_file_name = "PFRPG-TechnologyGuide.mod"
xml_definition_file = "definition.xml"
xml_database_file = "db.xml"
license_file = "license.html"
armor_csv_file = "data/Armor.csv"
artifact_csv_file = "data/Artifacts.csv"
ai_file = "data/Artificial Intelligences.csv"
cybertech_file = "data/Cybertech.csv"
feats_file = "data/Feats.csv"
pharmaceuticals_file = "data/Pharmaceuticals.csv"
skills_file = "data/Skills.csv"
spells_file = "data/Spells.csv"
tech_gear_file = "data/Technological Gear.csv"
timeworntables_file = "data/TimewornTables.csv"
traps_file = "data/Traps.csv"
weapon_csv_file = "data/Weapons.csv"
artifact_rules_file = "data/artifacts.html"
archetype_rules_file = "data/Technology-Themed Archetypes.html"
armor_rules_file = "data/armor.html"
ai_rules_file = "data/ai.html"
craft_rules_file = "data/Crafting High-Tech Items.html"
equipment_rules_file = "data/Technological Equipment.html"
feat_rules_file = "data/feats.html"
hasards_rules_file = "data/hasards.html"
spells_rules_file = "data/spells.html"
weapon_rules_file = "data/weapon.html"
skills_rules_file = "data/skills.html"
techgear_rules_file = "data/Technological Gear.html"
prestigeclass_rules_file = "data/Prestige Class - Technomancer.html"
techequip_rules_file = "data/Technological Equipment.html"
pharmas_rules_file = "data/pharmaceuticals.html"
cybertech_rules_file = "data/Cybertech.html"

FG_module_directory = "E:\\Fantasy Grounds\\DataDir\\modules"

module_name = "Technology Guide"
module_author = "Faelwen"
module_ruleset = "PFRPG"
library_tag_name = "TechnologyGuide"
library_name = "Technology Guide"
library_category = "PFRPG Extras"

library_entries =   [{"Entry name":"---Legal Notice---",
                    "Entry tag":"AA.License",
                    "Link type":"librarylink",
                    "Window class":"referencetext",
                    "Record name": "License"},
                    {"Entry name":"[Items] All Items",
                    "Entry tag":"BA.AllItems",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.Allitems@" + module_name},
                    {"Entry name":"[Items] Armor",
                    "Entry tag":"CA.Armor",
                    "Link type":"librarylink",
                    "Window class":"reference_armortablelist",
                    "Record name": "lists.armor@" + module_name},
                    {"Entry name":"[Items] Artifact",
                    "Entry tag":"DA.Artifact",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.artifact@" + module_name},
                     {"Entry name":"[Items] Cybertech",
                    "Entry tag":"EA.Cybertech",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.cybertech@" + module_name},
                    {"Entry name":"[Items] Pharmaceuticals",
                    "Entry tag":"FA.Pharmaceuticals",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.pharmaceutical@" + module_name},
                    {"Entry name":"[Items] Technological Gear",
                    "Entry tag":"GA.TechnologicalGear",
                    "Link type":"librarylink",
                    "Window class":"reference_equipmenttablelist",
                    "Record name": "lists.techgear@" + module_name},
                    {"Entry name":"[Items] Weapon",
                    "Entry tag":"HA.Weapon",
                    "Link type":"librarylink",
                    "Window class":"reference_weapontablelist",
                    "Record name": "lists.weapon@" + module_name},
                    {"Entry name":"[Rules] Archetypes",
                    "Entry tag":"IA.Archetypes",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.archetyperules.archetypelist@" + module_name},
                    {"Entry name":"[Rules] Armor",
                    "Entry tag":"JA.Armor",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.armorrules@" + module_name},
                    {"Entry name":"[Rules] Artifacts",
                    "Entry tag":"KA.Artifacts",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.artifactrules@" + module_name},
                    {"Entry name":"[Rules] Artificial Intelligences",
                    "Entry tag":"LA.ArtificialIntelligences",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.AIRules@" + module_name},
                    {"Entry name":"[Rules] Crafting",
                    "Entry tag":"MA.Crafting",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.CraftingRules@" + module_name},
                    {"Entry name":"[Rules] Cybertech",
                    "Entry tag":"NA.Cybertech",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.cybertechrules@" + module_name},
                    {"Entry name":"[Rules] Feats",
                    "Entry tag":"PA.Feats",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.FeatsRules@" + module_name},
                    {"Entry name":"[Rules] Hazards",
                    "Entry tag":"QA.Hazards",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.HazardsRules@" + module_name},
                    {"Entry name":"[Rules] Pharmaceuticals",
                    "Entry tag":"RA.Pharmaceuticals",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.pharmarules@" + module_name},
                    {"Entry name":"[Rules] Prestige Class: Technomancer",
                    "Entry tag":"SA.Technomancer",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.prestigerules.technomancer.statblock@" + module_name},
                    {"Entry name":"[Rules] Skills",
                    "Entry tag":"TA.Skills",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.skillrules@" + module_name},
                    {"Entry name":"[Rules] Spells",
                    "Entry tag":"UA.Spells",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.spellrules@" + module_name},
                    {"Entry name":"[Rules] Technological Equipment",
                    "Entry tag":"VA.TechnologicalEquipment",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.techequiprules@" + module_name},
                    {"Entry name":"[Rules] Technological Gear",
                    "Entry tag":"WA.TechnologicalGear",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.techgearrules@" + module_name},
                     {"Entry name":"[Rules] Weapons",
                    "Entry tag":"XA.Weapon",
                    "Link type":"librarylink",
                    "Window class":"referencetextwide",
                    "Record name": "lists.weaponrules@" + module_name}]

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
        license_text = file.read()
    xml_license_text.text = license_text


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
        file.write('thumbnail.png')
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

    #All items description
    xml_list_allitems = etree.SubElement(xml_lists, "Allitems")
    xml_list_allitems_description = etree.SubElement(xml_list_allitems, "description", type="string")
    xml_list_allitems_description.text = "All Items"
    xml_list_allitems_groups = etree.SubElement(xml_list_allitems, "groups")
    #All items armor
    xml_list_allitems_groups_armor = etree.SubElement(xml_list_allitems_groups, "armor")
    xml_list_allitems_groups_armor_description = etree.SubElement(xml_list_allitems_groups_armor, "description", type="string")
    xml_list_allitems_groups_armor_description.text = "All Items"
    xml_list_allitems_groups_armor_subdescription = etree.SubElement(xml_list_allitems_groups_armor, "subdescription", type="string")
    xml_list_allitems_groups_armor_subdescription.text = "Armor"
    xml_list_allitems_groups_armor_equipment = etree.SubElement(xml_list_allitems_groups_armor, "equipment")
    #All items artifacts
    xml_list_allitems_groups_artifacts = etree.SubElement(xml_list_allitems_groups, "artifacts")
    xml_list_allitems_groups_artifacts_description = etree.SubElement(xml_list_allitems_groups_artifacts, "description", type="string")
    xml_list_allitems_groups_artifacts_description.text = "All Items"
    xml_list_allitems_groups_artifacts_subdescription = etree.SubElement(xml_list_allitems_groups_artifacts, "subdescription", type="string")
    xml_list_allitems_groups_artifacts_subdescription.text = "Artifacts"
    xml_list_allitems_groups_artifacts_equipment = etree.SubElement(xml_list_allitems_groups_artifacts, "equipment")
    #All items cybertech
    xml_list_allitems_groups_cybertech = etree.SubElement(xml_list_allitems_groups, "cybertech")
    xml_list_allitems_groups_cybertech_description = etree.SubElement(xml_list_allitems_groups_cybertech, "description", type="string")
    xml_list_allitems_groups_cybertech_description.text = "All Items"
    xml_list_allitems_groups_cybertech_subdescription = etree.SubElement(xml_list_allitems_groups_cybertech, "subdescription", type="string")
    xml_list_allitems_groups_cybertech_subdescription.text = "Cybertech"
    xml_list_allitems_groups_cybertech_equipment = etree.SubElement(xml_list_allitems_groups_cybertech, "equipment")
    #All items pharmaceuticals
    xml_list_allitems_groups_pharmaceutical = etree.SubElement(xml_list_allitems_groups, "pharmaceutical")
    xml_list_allitems_groups_pharmaceutical_description = etree.SubElement(xml_list_allitems_groups_pharmaceutical, "description", type="string")
    xml_list_allitems_groups_pharmaceutical_description.text = "All Items"
    xml_list_allitems_groups_pharmaceutical_subdescription = etree.SubElement(xml_list_allitems_groups_pharmaceutical, "subdescription", type="string")
    xml_list_allitems_groups_pharmaceutical_subdescription.text = "Pharmaceutical"
    xml_list_allitems_groups_pharmaceutical_equipment = etree.SubElement(xml_list_allitems_groups_pharmaceutical, "equipment")
    #All items technological gear
    xml_list_allitems_groups_techgear = etree.SubElement(xml_list_allitems_groups, "techgear")
    xml_list_allitems_groups_techgear_description = etree.SubElement(xml_list_allitems_groups_techgear, "description", type="string")
    xml_list_allitems_groups_techgear_description.text = "All Items"
    xml_list_allitems_groups_techgear_subdescription = etree.SubElement(xml_list_allitems_groups_techgear, "subdescription", type="string")
    xml_list_allitems_groups_techgear_subdescription.text = "Technological Gear"
    xml_list_allitems_groups_techgear_equipment = etree.SubElement(xml_list_allitems_groups_techgear, "equipment")
    #All items weapon
    xml_list_allitems_groups_weapon = etree.SubElement(xml_list_allitems_groups, "weapon")
    xml_list_allitems_groups_weapon_description = etree.SubElement(xml_list_allitems_groups_weapon, "description", type="string")
    xml_list_allitems_groups_weapon_description.text = "All Items"
    xml_list_allitems_groups_weapon_subdescription = etree.SubElement(xml_list_allitems_groups_weapon, "subdescription", type="string")
    xml_list_allitems_groups_weapon_subdescription.text = "Weapon"
    xml_list_allitems_groups_weapon_equipment = etree.SubElement(xml_list_allitems_groups_weapon, "equipment")

    #Armor library
    xml_list_armor = etree.SubElement(xml_lists, "armor")
    xml_list_armor_description = etree.SubElement(xml_list_armor, "description", type="string")
    xml_list_armor_description.text = "Armor"
    xml_list_armor_groups = etree.SubElement(xml_list_armor, "groups")
    #artifact library
    xml_list_artifact = etree.SubElement(xml_lists, "artifact")
    xml_list_artifact_description = etree.SubElement(xml_list_artifact, "description", type="string")
    xml_list_artifact_description.text = "artifact"
    xml_list_artifact_groups = etree.SubElement(xml_list_artifact, "groups")
    #cybertech library
    xml_list_cybertech = etree.SubElement(xml_lists, "cybertech")
    xml_list_cybertech_description = etree.SubElement(xml_list_cybertech, "description", type="string")
    xml_list_cybertech_description.text = "cybertech"
    xml_list_cybertech_groups = etree.SubElement(xml_list_cybertech, "groups")
    #pharmaceutical library
    xml_list_pharmaceutical = etree.SubElement(xml_lists, "pharmaceutical")
    xml_list_pharmaceutical_description = etree.SubElement(xml_list_pharmaceutical, "description", type="string")
    xml_list_pharmaceutical_description.text = "pharmaceutical"
    xml_list_pharmaceutical_groups = etree.SubElement(xml_list_pharmaceutical, "groups")
    #technological gear library
    xml_list_techgear = etree.SubElement(xml_lists, "techgear")
    xml_list_techgear_description = etree.SubElement(xml_list_techgear, "description", type="string")
    xml_list_techgear_description.text = "techgear"
    xml_list_techgear_groups = etree.SubElement(xml_list_techgear, "groups")
    #Weapon library
    xml_list_weapon = etree.SubElement(xml_lists, "weapon")
    xml_list_weapon_description = etree.SubElement(xml_list_weapon, "description", type="string")
    xml_list_weapon_description.text = "weapon"
    xml_list_weapon_groups = etree.SubElement(xml_list_weapon, "groups")
    #Armor rules
    xml_list_armorrules = etree.SubElement(xml_lists, "armorrules")
    #Artifact rules
    xml_list_artifactrules = etree.SubElement(xml_lists, "artifactrules")
    #Archetype rules
    xml_list_archetyperules = etree.SubElement(xml_lists, "archetyperules")
    #AI rules
    xml_list_airules = etree.SubElement(xml_lists, "AIRules")
    #Crafting rules
    xml_list_craftingrules = etree.SubElement(xml_lists, "CraftingRules")
    #Cybertech rules
    xml_list_cybertechrules = etree.SubElement(xml_lists, "cybertechrules")
    #Equipment rules
    xml_list_equipmentrules = etree.SubElement(xml_lists, "EquipmentRules")
    #Feats rules
    xml_list_featsrules = etree.SubElement(xml_lists, "FeatsRules")
    #Hazards rules
    xml_list_hazardsrules = etree.SubElement(xml_lists, "HazardsRules")
    #Pharmaceutical rules
    xml_list_pharmarules = etree.SubElement(xml_lists, "pharmarules")
    #Prestige rules
    xml_list_prestigerules = etree.SubElement(xml_lists, "prestigerules")
    #Spell rules
    xml_list_spellrules = etree.SubElement(xml_lists, "spellrules")
    #Technological gear rules
    xml_list_techgearrules = etree.SubElement(xml_lists, "techgearrules")
    #Skill rules
    xml_list_skillrules = etree.SubElement(xml_lists, "skillrules")
    #Weapon rules
    xml_list_weaponrules = etree.SubElement(xml_lists, "weaponrules")

    #Populate data
    populate_library_entries(xml_library_entries)
    populate_license(xml_root)
    populate_armor(xml_ref_armor, xml_list_allitems_groups_armor_equipment, xml_list_armor_groups)
    populate_artifact(xml_ref_equipment, xml_list_allitems_groups_artifacts_equipment, xml_list_artifact_groups)
    populate_ai(xml_ref_npcdata)
    populate_cybertech(xml_ref_equipment, xml_list_allitems_groups_cybertech_equipment, xml_list_cybertech_groups)
    populate_feats(xml_ref_feats)
    populate_pharmaceuticals(xml_ref_equipment, xml_list_allitems_groups_pharmaceutical_equipment, xml_list_pharmaceutical_groups)
    populate_skills(xml_ref_skills)
    populate_spells(xml_ref_spells)
    populate_tech_gear(xml_ref_equipment, xml_list_allitems_groups_techgear_equipment, xml_list_techgear_groups)
    populate_timeworn_tables(xml_ref_tables)
    populate_traps(xml_ref_npcdata)
    populate_weapon(xml_ref_weapon, xml_list_allitems_groups_weapon_equipment, xml_list_weapon_groups)
    populate_armor_rules(xml_list_armorrules)
    populate_artifact_rules(xml_list_artifactrules)
    populate_archetypes_rules(xml_list_archetyperules)
    populate_ai_rules(xml_list_airules)
    populate_craft_rules(xml_list_craftingrules)
    populate_equipment_rules(xml_list_equipmentrules)
    populate_feats_rules(xml_list_featsrules)
    populate_hazard_rules(xml_list_hazardsrules)
    populate_spell_rules(xml_list_spellrules)
    populate_techgear_rules(xml_list_techgearrules)
    populate_weapon_rules(xml_list_weaponrules)
    populate_prestige_rules(xml_list_prestigerules)
    populate_skill_rules(xml_list_skillrules)
    populate_pharma_rules(xml_list_pharmarules)
    populate_cybertech_rules(xml_list_cybertechrules)


def populate_timeworn_tables(xml_ref_tables):
    with open(timeworntables_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header

        for row in csvreader:
            [i_ref, i_data] = row
            #Ref
            xml_ref = etree.SubElement(xml_ref_tables, i_ref.strip())
            #Data
            xml_ref.text = i_data.strip()


def populate_skills(xml_ref_skills):
    with open(skills_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        skill_number = 0
        prefix = "skill"

        for row in csvreader:
            skill_number += 1
            [i_name, i_ability, i_trained, i_penmult, i_description] = row
            #Ref
            skill_ref = prefix + "{:04d}".format(skill_number)
            xml_ref = etree.SubElement(xml_ref_skills, skill_ref)
            #Name
            skill_ref_name = etree.SubElement(xml_ref, "name", type="string")
            skill_ref_name.text = i_name.strip()
            #Ability
            skill_ref_ability = etree.SubElement(xml_ref, "ability", type="string")
            skill_ref_ability.text = i_ability.strip();
            #Trained
            skill_ref_trained = etree.SubElement(xml_ref, "trained", type="number")
            if i_trained.strip() == "no":
                skill_ref_trained.text = "0"
            else:
                skill_ref_trained.text = "1"
            #AC penalty multiplier
            skill_ref_mult = etree.SubElement(xml_ref, "armorcheckpenalty", type="number")
            skill_ref_mult.text = i_penmult.strip()
            #Description
            skill_ref_desc = etree.SubElement(xml_ref, "text", type="formattedtext")
            skill_ref_desc.text = i_description.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')


def populate_feats(xml_ref_feats):
    with open(feats_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        feat_number = 0
        prefix = "feat"

        for row in csvreader:
            feat_number += 1
            [i_name, i_prereqs, i_effect1, i_effect2, i_benefit,
            i_normal, i_special] = row
            #Ref
            feat_ref = prefix + "{:04d}".format(feat_number)
            xml_ref = etree.SubElement(xml_ref_feats, feat_ref)
            #Name
            feat_ref_name = etree.SubElement(xml_ref, "name", type="string")
            feat_ref_name.text = i_name.strip()
            #Type
            feat_ref_type = etree.SubElement(xml_ref, "type", type="string")
            feat_ref_type.text = "Technological"
            #Prerequisites
            if i_prereqs != "—":
                feat_ref_prereqs = etree.SubElement(xml_ref, "prerequisites", type="string")
                feat_ref_prereqs.text = i_prereqs.strip()
            #Benefit
            feat_ref_benefit = etree.SubElement(xml_ref, "benefit", type="formattedtext")
            feat_ref_benefit.text = "<frame>{0}</frame>{1}".format(i_effect2, i_benefit).strip().replace('\u2014','-').replace('\u2013','-')
            #Normal
            if i_normal != "":
                feat_ref_normal = etree.SubElement(xml_ref, "normal", type="formattedtext")
                feat_ref_normal.text = i_normal.strip().replace('\u2014','-').replace('\u2013','-')
            #Special
            if i_special != "":
                feat_ref_special = etree.SubElement(xml_ref, "special", type="formattedtext")
                feat_ref_special.text = i_special.strip().replace('\u2014','-').replace('\u2013','-')
            #Source
            feat_ref_source = etree.SubElement(xml_ref, "source", type="string")
            feat_ref_source.text = "Technology Guide"



def populate_spells(xml_ref_spells):
    with open(spells_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        spell_number = 0
        prefix = "spell"

        for row in csvreader:
            spell_number += 1
            [i_name, i_school, i_level, i_components, i_castingtime,
            i_range, i_target, i_duration, i_save, i_sr, i_description] = row
            #Ref
            spell_ref = prefix + "{:04d}".format(spell_number)
            xml_ref = etree.SubElement(xml_ref_spells, spell_ref)
            #Name
            spell_ref_name = etree.SubElement(xml_ref, "name", type="string")
            spell_ref_name.text = i_name.strip()
            #School
            spell_ref_school = etree.SubElement(xml_ref, "school", type="string")
            spell_ref_school.text = i_school.strip()
            #Level
            spell_ref_level = etree.SubElement(xml_ref, "level", type="string")
            spell_ref_level.text = i_level.strip()
            #Components
            spell_ref_component = etree.SubElement(xml_ref, "components", type="string")
            spell_ref_component.text = i_components.strip()
            #Casting time
            spell_ref_casttime = etree.SubElement(xml_ref, "castingtime", type="string")
            spell_ref_casttime.text = i_castingtime.strip()
            #Range
            spell_ref_range = etree.SubElement(xml_ref, "range", type="string")
            spell_ref_range.text = i_range.strip()
            #Target/Area/Effect
            spell_ref_target = etree.SubElement(xml_ref, "effect", type="string")
            spell_ref_target.text = i_target.strip()
            #Duration
            spell_ref_duration = etree.SubElement(xml_ref, "duration", type="string")
            spell_ref_duration.text = i_duration.strip()
            #Save
            spell_ref_save = etree.SubElement(xml_ref, "save", type="string")
            spell_ref_save.text = i_save.strip()
            #Spell resistance
            spell_ref_sr = etree.SubElement(xml_ref, "sr", type="string")
            spell_ref_sr.text = i_sr.strip()
            #Description
            spell_ref_description = etree.SubElement(xml_ref, "description", type="formattedtext")
            spell_ref_description.text = i_description.strip().replace('\u2014','-').replace('\u2013','-')
            #Source
            spell_ref_source = etree.SubElement(xml_ref, "source", type="string")
            spell_ref_source.text = "Technology Guide"



def populate_tech_gear(xml_ref_equipment, xml_allitemslist, xml_itemlist):
    with open(tech_gear_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "techgear"
        previous_type = ""
        previous_subtype = ""

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_price, i_weight, i_capacity,
            i_usage, i_description, i_crafting] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_equipment, item_ref)
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
            #Weight
            if i_weight != "" and i_weight != "—":
                xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
                xml_ref_weight.text = i_weight.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = "<p><b>Capacity:</b> {0}; <b>Usage:</b> {1}</p>{2}".format(i_capacity, i_usage, i_description).strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Crafting
            xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
            xml_ref_reqs.text = i_crafting.strip()
            #Link item to allitems list
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "referenceequipment"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.equipment." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = i_price.replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = i_weight.replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #techgear library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_itemlist_section = etree.SubElement(xml_itemlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-").replace(",","-"))
                xml_itemlist_section_description = etree.SubElement(xml_itemlist_section, "description", type="string")
                xml_itemlist_section_description.text = i_type
                xml_itemlist_section_subdescription = etree.SubElement(xml_itemlist_section, "subdescription", type="string")
                xml_itemlist_section_subdescription.text = i_subtype
                xml_itemlist_section_item = etree.SubElement(xml_itemlist_section, "equipment")
            xml_itemlist_section_item_ref = etree.SubElement(xml_itemlist_section_item, item_ref)
            xml_itemlist_section_item_ref_link = etree.SubElement(xml_itemlist_section_item_ref, "link", type="windowreference")
            xml_itemlist_section_item_ref_link_class = etree.SubElement(xml_itemlist_section_item_ref_link, "class")
            xml_itemlist_section_item_ref_link_class.text = "item"
            xml_itemlist_section_item_ref_link_recordname = etree.SubElement(xml_itemlist_section_item_ref_link, "recordname")
            xml_itemlist_section_item_ref_link_recordname.text = "reference.equipment.{0}@{1}".format(item_ref, module_name)
            xml_itemlist_section_item_ref_name = etree.SubElement(xml_itemlist_section_item_ref, "name", type="string")
            xml_itemlist_section_item_ref_name.text = i_name.strip()
            xml_itemlist_section_item_ref_cost = etree.SubElement(xml_itemlist_section_item_ref, "cost", type="string")
            xml_itemlist_section_item_ref_cost.text = i_price.strip()
            xml_itemlist_section_item_ref_weight = etree.SubElement(xml_itemlist_section_item_ref, "weight", type="string")
            xml_itemlist_section_item_ref_weight.text = i_weight.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-') + " lbs."
            previous_type = i_type
            previous_subtype = i_subtype


def populate_cybertech(xml_ref_equipment, xml_allitemslist, xml_itemlist):
    with open(cybertech_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "cybertech"
        previous_type = ""
        previous_subtype = ""

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_price, i_weight, i_implant,
            i_installDC, i_description, i_crafting] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_equipment, item_ref)
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
            #Weight
            if i_weight != "":
                xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
                xml_ref_weight.text = i_weight.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = "<p><b>Implant:</b> {0}; <b>Install:</b> {1}</p>{2}".format(i_implant, i_installDC, i_description).strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Crafting
            xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
            xml_ref_reqs.text = i_crafting.strip()
            #Link item to allitems list
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "referenceequipment"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.equipment." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = i_price
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = i_weight
            #cybertech library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_itemlist_section = etree.SubElement(xml_itemlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-"))
                xml_itemlist_section_description = etree.SubElement(xml_itemlist_section, "description", type="string")
                xml_itemlist_section_description.text = i_type
                xml_itemlist_section_subdescription = etree.SubElement(xml_itemlist_section, "subdescription", type="string")
                xml_itemlist_section_subdescription.text = i_subtype
                xml_itemlist_section_item = etree.SubElement(xml_itemlist_section, "equipment")
            xml_itemlist_section_item_ref = etree.SubElement(xml_itemlist_section_item, item_ref)
            xml_itemlist_section_item_ref_link = etree.SubElement(xml_itemlist_section_item_ref, "link", type="windowreference")
            xml_itemlist_section_item_ref_link_class = etree.SubElement(xml_itemlist_section_item_ref_link, "class")
            xml_itemlist_section_item_ref_link_class.text = "item"
            xml_itemlist_section_item_ref_link_recordname = etree.SubElement(xml_itemlist_section_item_ref_link, "recordname")
            xml_itemlist_section_item_ref_link_recordname.text = "reference.equipment.{0}@{1}".format(item_ref, module_name)
            xml_itemlist_section_item_ref_name = etree.SubElement(xml_itemlist_section_item_ref, "name", type="string")
            xml_itemlist_section_item_ref_name.text = i_name.strip()
            xml_itemlist_section_item_ref_cost = etree.SubElement(xml_itemlist_section_item_ref, "cost", type="string")
            xml_itemlist_section_item_ref_cost.text = i_price.strip()
            xml_itemlist_section_item_ref_weight = etree.SubElement(xml_itemlist_section_item_ref, "weight", type="string")
            xml_itemlist_section_item_ref_weight.text = i_weight.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-') + " lbs."
            previous_type = i_type
            previous_subtype = i_subtype


def populate_pharmaceuticals(xml_ref_equipment, xml_allitemslist, xml_itemlist):
    with open(pharmaceuticals_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "pharmaceuticals"
        previous_type = ""
        previous_subtype = ""

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_price, i_description, i_crafting] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_equipment, item_ref)
            #Type
            xml_ref_type = etree.SubElement(xml_ref, "type", type="string")
            xml_ref_type.text = i_type.strip()
            #Name
            xml_ref_name = etree.SubElement(xml_ref, "name", type="string")
            xml_ref_name.text = i_name.strip()
            #Price
            xml_ref_cost = etree.SubElement(xml_ref, "cost", type="string")
            xml_ref_cost.text = i_price.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = i_description.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Crafting
            xml_ref_reqs = etree.SubElement(xml_ref, "prerequisites", type="string")
            xml_ref_reqs.text = i_crafting.strip()
            #Link item to allitems list
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "referenceequipment"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.equipment." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = i_price
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = "0"
            #pharma library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_itemlist_section = etree.SubElement(xml_itemlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-"))
                xml_itemlist_section_description = etree.SubElement(xml_itemlist_section, "description", type="string")
                xml_itemlist_section_description.text = i_type
                xml_itemlist_section_subdescription = etree.SubElement(xml_itemlist_section, "subdescription", type="string")
                xml_itemlist_section_subdescription.text = i_subtype
                xml_itemlist_section_item = etree.SubElement(xml_itemlist_section, "equipment")
            xml_itemlist_section_item_ref = etree.SubElement(xml_itemlist_section_item, item_ref)
            xml_itemlist_section_item_ref_link = etree.SubElement(xml_itemlist_section_item_ref, "link", type="windowreference")
            xml_itemlist_section_item_ref_link_class = etree.SubElement(xml_itemlist_section_item_ref_link, "class")
            xml_itemlist_section_item_ref_link_class.text = "item"
            xml_itemlist_section_item_ref_link_recordname = etree.SubElement(xml_itemlist_section_item_ref_link, "recordname")
            xml_itemlist_section_item_ref_link_recordname.text = "reference.equipment.{0}@{1}".format(item_ref, module_name)
            xml_itemlist_section_item_ref_name = etree.SubElement(xml_itemlist_section_item_ref, "name", type="string")
            xml_itemlist_section_item_ref_name.text = i_name.strip()
            xml_itemlist_section_item_ref_cost = etree.SubElement(xml_itemlist_section_item_ref, "cost", type="string")
            xml_itemlist_section_item_ref_cost.text = i_price.strip()
            xml_itemlist_section_item_ref_weight = etree.SubElement(xml_itemlist_section_item_ref, "weight", type="string")
            xml_itemlist_section_item_ref_weight.text = "- lbs."
            previous_type = i_type
            previous_subtype = i_subtype

def populate_ai(xml_ref_npcdata):
    with open(ai_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header

        for row in csvreader:
            [i_ref, i_data] = row
            #Ref
            xml_ref = etree.SubElement(xml_ref_npcdata, i_ref.strip())
            #Data
            xml_ref.text = i_data.strip()


def populate_traps(xml_ref_npcdata):
    with open(traps_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header

        for row in csvreader:
            [i_ref, i_data] = row
            #Ref
            xml_ref = etree.SubElement(xml_ref_npcdata, i_ref.strip())
            #Data
            xml_ref.text = i_data.strip()


def populate_armor(xml_ref_armor, xml_allitemslist, xml_armorlist):
    with open(armor_csv_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "armor"
        previous_type = ""
        previous_subtype = ""

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
            #All item library ref
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "item"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.armor." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = i_price
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = i_weight

            #Armor library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_armorlist_section = etree.SubElement(xml_armorlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-"))
                xml_armorlist_section_description = etree.SubElement(xml_armorlist_section, "description", type="string")
                xml_armorlist_section_description.text = i_type
                xml_armorlist_section_subdescription = etree.SubElement(xml_armorlist_section, "subdescription", type="string")
                xml_armorlist_section_subdescription.text = i_subtype
                xml_armorlist_section_armor = etree.SubElement(xml_armorlist_section, "armor")
            xml_armorlist_section_armor_ref = etree.SubElement(xml_armorlist_section_armor, item_ref)
            xml_armorlist_section_armor_ref_link = etree.SubElement(xml_armorlist_section_armor_ref, "link", type="windowreference")
            xml_armorlist_section_armor_ref_link_class = etree.SubElement(xml_armorlist_section_armor_ref_link, "class")
            xml_armorlist_section_armor_ref_link_class.text = "item"
            xml_armorlist_section_armor_ref_link_recordname = etree.SubElement(xml_armorlist_section_armor_ref_link, "recordname")
            xml_armorlist_section_armor_ref_link_recordname.text = "reference.armor.{0}@{1}".format(item_ref, module_name)
            xml_armorlist_section_armor_ref_name = etree.SubElement(xml_armorlist_section_armor_ref, "name", type="string")
            xml_armorlist_section_armor_ref_name.text = i_name.strip()
            #xml_armorlist_section_armor_ref_cost = etree.SubElement(xml_armorlist_section_armor_ref, "cost", type="string")
            #xml_armorlist_section_armor_ref_cost.text = i_price.strip()
            xml_armorlist_section_armor_ref_weight = etree.SubElement(xml_armorlist_section_armor_ref, "weight", type="string")
            xml_armorlist_section_armor_ref_weight.text = i_weight.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-') + " lbs."
            xml_armorlist_section_armor_ref_ac = etree.SubElement(xml_armorlist_section_armor_ref, "ac", type="string")
            xml_armorlist_section_armor_ref_ac.text = i_armor_bonus.strip()
            xml_armorlist_section_armor_ref_maxstatbonus = etree.SubElement(xml_armorlist_section_armor_ref, "maxstatbonus", type="string")
            xml_armorlist_section_armor_ref_maxstatbonus.text = i_maxbonus.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_armorlist_section_armor_ref_checkpenalty = etree.SubElement(xml_armorlist_section_armor_ref, "checkpenalty", type="string")
            xml_armorlist_section_armor_ref_checkpenalty.text = i_penalty.strip()
            xml_armorlist_section_armor_ref_spellfailure = etree.SubElement(xml_armorlist_section_armor_ref, "spellfailure", type="string")
            xml_armorlist_section_armor_ref_spellfailure.text = i_spellfail.strip() + "%"
            xml_armorlist_section_armor_ref_speed30 = etree.SubElement(xml_armorlist_section_armor_ref, "speed30", type="string")
            xml_armorlist_section_armor_ref_speed30.text = i_speed30.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_armorlist_section_armor_ref_speed20 = etree.SubElement(xml_armorlist_section_armor_ref, "speed20", type="string")
            xml_armorlist_section_armor_ref_speed20.text = i_speed20.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            previous_type = i_type
            previous_subtype = i_subtype





def populate_artifact(xml_ref_equipment, xml_allitemslist, xml_artifactlist):
    with open(artifact_csv_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "artifact"
        previous_type = ""
        previous_subtype = ""

        for row in csvreader:
            item_number += 1
            [i_type, i_subtype, i_name, i_weight, i_capacity, i_usage, i_description] = row
            #Ref
            item_ref = prefix + "{:04d}".format(item_number)
            xml_ref = etree.SubElement(xml_ref_equipment, item_ref)
            #Type
            xml_ref_type = etree.SubElement(xml_ref, "type", type="string")
            xml_ref_type.text = i_type.strip()
            #Subtype
            xml_ref_subtype = etree.SubElement(xml_ref, "subtype", type="string")
            xml_ref_subtype.text = i_subtype.strip()
            #Name
            xml_ref_name = etree.SubElement(xml_ref, "name", type="string")
            xml_ref_name.text = i_name.strip()
            #Weight
            if i_weight != "":
                xml_ref_weight = etree.SubElement(xml_ref, "weight", type="number")
                xml_ref_weight.text = i_weight.strip()
            #Description
            xml_ref_desc = etree.SubElement(xml_ref, "description", type="formattedtext")
            xml_ref_desc.text = "<p><b>Capacity:</b> {0}; <b>Usage:</b> {1}</p>{2}".format(i_capacity, i_usage, i_description).strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            #Link item to allitems list
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "referenceequipment"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.equipment." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = ""
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = i_weight
            #artifact library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_artifactlist_section = etree.SubElement(xml_artifactlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-"))
                xml_artifactlist_section_description = etree.SubElement(xml_artifactlist_section, "description", type="string")
                xml_artifactlist_section_description.text = i_type
                xml_artifactlist_section_subdescription = etree.SubElement(xml_artifactlist_section, "subdescription", type="string")
                xml_artifactlist_section_subdescription.text = i_subtype
                xml_artifactlist_section_artifact = etree.SubElement(xml_artifactlist_section, "equipment")
            xml_artifactlist_section_artifact_ref = etree.SubElement(xml_artifactlist_section_artifact, item_ref)
            xml_artifactlist_section_artifact_ref_link = etree.SubElement(xml_artifactlist_section_artifact_ref, "link", type="windowreference")
            xml_artifactlist_section_artifact_ref_link_class = etree.SubElement(xml_artifactlist_section_artifact_ref_link, "class")
            xml_artifactlist_section_artifact_ref_link_class.text = "item"
            xml_artifactlist_section_artifact_ref_link_recordname = etree.SubElement(xml_artifactlist_section_artifact_ref_link, "recordname")
            xml_artifactlist_section_artifact_ref_link_recordname.text = "reference.equipment.{0}@{1}".format(item_ref, module_name)
            xml_artifactlist_section_artifact_ref_name = etree.SubElement(xml_artifactlist_section_artifact_ref, "name", type="string")
            xml_artifactlist_section_artifact_ref_name.text = i_name.strip()
            xml_artifactlist_section_artifact_ref_cost = etree.SubElement(xml_artifactlist_section_artifact_ref, "cost", type="string")
            xml_artifactlist_section_artifact_ref_cost.text = "-"
            xml_artifactlist_section_artifact_ref_weight = etree.SubElement(xml_artifactlist_section_artifact_ref, "weight", type="string")
            xml_artifactlist_section_artifact_ref_weight.text = i_weight.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-') + " lbs."
            previous_type = i_type
            previous_subtype = i_subtype


def populate_weapon(xml_ref_weapons, xml_allitemslist, xml_weaponlist):
    with open(weapon_csv_file, 'r',encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        row = next(csvreader) #skip header
        item_number = 0
        prefix = "weapon"
        previous_type = ""
        previous_subtype = ""

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
            #Link item to allitems list
            xml_allitemslist_ref = etree.SubElement(xml_allitemslist, item_ref)
            xml_allitemslist_ref_link = etree.SubElement(xml_allitemslist_ref, "link", type="windowreference")
            xml_allitemslist_ref_link_class = etree.SubElement(xml_allitemslist_ref_link, "class")
            xml_allitemslist_ref_link_class.text = "item"
            xml_allitemslist_ref_link_recordname = etree.SubElement(xml_allitemslist_ref_link, "recordname")
            xml_allitemslist_ref_link_recordname.text = "reference.weapon." + item_ref + '@' + module_name
            xml_allitemslist_ref_name = etree.SubElement(xml_allitemslist_ref, "name", type="string")
            xml_allitemslist_ref_name.text = i_name
            xml_allitemslist_ref_cost = etree.SubElement(xml_allitemslist_ref, "cost", type="string")
            xml_allitemslist_ref_cost.text = i_price
            xml_allitemslist_ref_weight = etree.SubElement(xml_allitemslist_ref, "weight", type="string")
            xml_allitemslist_ref_weight.text = i_weight

            #Weapon library ref
            if (i_type != previous_type) or (i_subtype != previous_subtype):
                xml_weaponlist_section = etree.SubElement(xml_weaponlist, "{0}-{1}".format(i_type, i_subtype).replace(" ","-"))
                xml_weaponlist_section_description = etree.SubElement(xml_weaponlist_section, "description", type="string")
                xml_weaponlist_section_description.text = i_type
                xml_weaponlist_section_subdescription = etree.SubElement(xml_weaponlist_section, "subdescription", type="string")
                xml_weaponlist_section_subdescription.text = i_subtype
                xml_weaponlist_section_weapon = etree.SubElement(xml_weaponlist_section, "weapons")
            xml_weaponlist_section_weapon_ref = etree.SubElement(xml_weaponlist_section_weapon, item_ref)
            xml_weaponlist_section_weapon_ref_link = etree.SubElement(xml_weaponlist_section_weapon_ref, "link", type="windowreference")
            xml_weaponlist_section_weapon_ref_link_class = etree.SubElement(xml_weaponlist_section_weapon_ref_link, "class")
            xml_weaponlist_section_weapon_ref_link_class.text = "item"
            xml_weaponlist_section_weapon_ref_link_recordname = etree.SubElement(xml_weaponlist_section_weapon_ref_link, "recordname")
            xml_weaponlist_section_weapon_ref_link_recordname.text = "reference.weapon.{0}@{1}".format(item_ref, module_name)
            xml_weaponlist_section_weapon_ref_name = etree.SubElement(xml_weaponlist_section_weapon_ref, "name", type="string")
            xml_weaponlist_section_weapon_ref_name.text = i_name.strip()
            xml_weaponlist_section_weapon_ref_cost = etree.SubElement(xml_weaponlist_section_weapon_ref, "cost", type="string")
            xml_weaponlist_section_weapon_ref_cost.text = i_price.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_weaponlist_section_weapon_ref_weight = etree.SubElement(xml_weaponlist_section_weapon_ref, "weight", type="string")
            xml_weaponlist_section_weapon_ref_weight.text = i_weight.strip().strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-') + " lbs."
            xml_weaponlist_section_weapon_ref_damage = etree.SubElement(xml_weaponlist_section_weapon_ref, "damage", type="string")
            xml_weaponlist_section_weapon_ref_damage.text = i_dmg_m.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_weaponlist_section_weapon_ref_critical = etree.SubElement(xml_weaponlist_section_weapon_ref, "critical", type="string")
            xml_weaponlist_section_weapon_ref_critical.text = i_critical.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_weaponlist_section_weapon_ref_range = etree.SubElement(xml_weaponlist_section_weapon_ref, "range", type="string")
            xml_weaponlist_section_weapon_ref_range.text = i_range.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_weaponlist_section_weapon_ref_properties = etree.SubElement(xml_weaponlist_section_weapon_ref, "properties", type="string")
            xml_weaponlist_section_weapon_ref_properties.text = i_special.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')
            xml_weaponlist_section_weapon_ref_damagetype = etree.SubElement(xml_weaponlist_section_weapon_ref, "damagetype", type="string")
            xml_weaponlist_section_weapon_ref_damagetype.text = i_dmg_type.strip().replace('\ufffd','-').replace('\u2014','-').replace('\u2013','-')


def populate_artifact_rules(xml_list_artifactrules):
    xml_list_artifactrules_name = etree.SubElement(xml_list_artifactrules, "name", type="string")
    xml_list_artifactrules_name.text = "Technological Artifacts"
    xml_list_artifactrules_text = etree.SubElement(xml_list_artifactrules, "text", type="formattedtext")
    with open(artifact_rules_file, 'r') as file:
        artifact_rules = file.read()
    xml_list_artifactrules_text.text = artifact_rules


def populate_archetypes_rules(xml_list_archetyperules):
    with open(archetype_rules_file, 'r') as file:
        archetype_rules = file.read()
    xml_list_archetyperules.text = archetype_rules


def populate_prestige_rules(xml_list_prestigerules):
    with open(prestigeclass_rules_file, 'r') as file:
        prestige_rules = file.read()
    xml_list_prestigerules.text = prestige_rules


def populate_armor_rules(xml_list_armorrules):
    xml_list_armorrules_name = etree.SubElement(xml_list_armorrules, "name", type="string")
    xml_list_armorrules_name.text = "Armor"
    xml_list_armorrules_text = etree.SubElement(xml_list_armorrules, "text", type="formattedtext")
    with open(armor_rules_file, 'r') as file:
        armor_rules = file.read()
    xml_list_armorrules_text.text = armor_rules


def populate_ai_rules(xml_list_airules):
    xml_list_airules_name = etree.SubElement(xml_list_airules, "name", type="string")
    xml_list_airules_name.text = "Artificial Intelligences"
    xml_list_airules_text = etree.SubElement(xml_list_airules, "text", type="formattedtext")
    with open(ai_rules_file, 'r') as file:
        ai_rules = file.read()
    xml_list_airules_text.text = ai_rules


def populate_craft_rules(xml_list_craftrules):
    xml_list_craftrules_name = etree.SubElement(xml_list_craftrules, "name", type="string")
    xml_list_craftrules_name.text = "Crafting High-Tech Items"
    xml_list_craftrules_text = etree.SubElement(xml_list_craftrules, "text", type="formattedtext")
    with open(craft_rules_file, 'r') as file:
        craft_rules = file.read()
    xml_list_craftrules_text.text = craft_rules


def populate_equipment_rules(xml_list_equipmentrules):
    xml_list_equipmentrules_name = etree.SubElement(xml_list_equipmentrules, "name", type="string")
    xml_list_equipmentrules_name.text = "Technological Equipment"
    xml_list_equipmentrules_text = etree.SubElement(xml_list_equipmentrules, "text", type="formattedtext")
    with open(equipment_rules_file, 'r') as file:
        equipment_rules = file.read()
    xml_list_equipmentrules_text.text = equipment_rules


def populate_feats_rules(xml_list_featsrules):
    xml_list_featsrules_name = etree.SubElement(xml_list_featsrules, "name", type="string")
    xml_list_featsrules_name.text = "Technological feats"
    xml_list_featsrules_text = etree.SubElement(xml_list_featsrules, "text", type="formattedtext")
    with open(feat_rules_file, 'r') as file:
        feats_rules = file.read()
    xml_list_featsrules_text.text = feats_rules


def populate_hazard_rules(xml_list_hazardsrules):
    xml_list_hazardsrules_name = etree.SubElement(xml_list_hazardsrules, "name", type="string")
    xml_list_hazardsrules_name.text = "Technological hazards"
    xml_list_hazardsrules_text = etree.SubElement(xml_list_hazardsrules, "text", type="formattedtext")
    with open(hasards_rules_file, 'r') as file:
        hazards_rules = file.read()
    xml_list_hazardsrules_text.text = hazards_rules


def populate_weapon_rules(xml_list_weaponrules):
    xml_list_weaponrules_name = etree.SubElement(xml_list_weaponrules, "name", type="string")
    xml_list_weaponrules_name.text = "Weapons"
    xml_list_weaponrules_text = etree.SubElement(xml_list_weaponrules, "text", type="formattedtext")
    with open(weapon_rules_file, 'r') as file:
        weapon_rules = file.read()
    xml_list_weaponrules_text.text = weapon_rules


def populate_spell_rules(xml_list_spellsrules):
    xml_list_spellsrules_name = etree.SubElement(xml_list_spellsrules, "name", type="string")
    xml_list_spellsrules_name.text = "Spells"
    xml_list_spellsrules_text = etree.SubElement(xml_list_spellsrules, "text", type="formattedtext")
    with open(spells_rules_file, 'r') as file:
        spells_rules = file.read()
    xml_list_spellsrules_text.text = spells_rules


def populate_techgear_rules(xml_list_techgearrules):
    xml_list_techgearrules_name = etree.SubElement(xml_list_techgearrules, "name", type="string")
    xml_list_techgearrules_name.text = "Technological Gear"
    xml_list_techgearrules_text = etree.SubElement(xml_list_techgearrules, "text", type="formattedtext")
    with open(techgear_rules_file, 'r') as file:
        techgear_rules = file.read()
    xml_list_techgearrules_text.text = techgear_rules


def populate_skill_rules(xml_list_skillrules):
    xml_list_skillrules_name = etree.SubElement(xml_list_skillrules, "name", type="string")
    xml_list_skillrules_name.text = "Skills"
    xml_list_skillrules_text = etree.SubElement(xml_list_skillrules, "text", type="formattedtext")
    with open(skills_rules_file, 'r') as file:
        skill_rules = file.read()
    xml_list_skillrules_text.text = skill_rules


def populate_pharma_rules(xml_list_pharmarules):
    xml_list_pharmarules_name = etree.SubElement(xml_list_pharmarules, "name", type="string")
    xml_list_pharmarules_name.text = "pharmas"
    xml_list_pharmarules_text = etree.SubElement(xml_list_pharmarules, "text", type="formattedtext")
    with open(pharmas_rules_file, 'r') as file:
        pharma_rules = file.read()
    xml_list_pharmarules_text.text = pharma_rules


def populate_cybertech_rules(xml_list_cybertechrules):
    xml_list_cybertechrules_name = etree.SubElement(xml_list_cybertechrules, "name", type="string")
    xml_list_cybertechrules_name.text = "cybertechs"
    xml_list_cybertechrules_text = etree.SubElement(xml_list_cybertechrules, "text", type="formattedtext")
    with open(cybertech_rules_file, 'r') as file:
        cybertech_rules = file.read()
    xml_list_cybertechrules_text.text = cybertech_rules


def main():
    xml_root = etree.Element('root', version="2.0")
    generate_xml_structure(xml_root)
    generate_xml_db_file(xml_root)
    generate_xml_def_file()
    generate_module()
    copy_to_Fantasy_Grounds()


if __name__ == '__main__':
    main()