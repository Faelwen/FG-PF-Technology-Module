#-
# Extract information and place in csv file
#-

from bs4 import BeautifulSoup
import re
import csv

htmlfile = "html/Armor.html"
cvsfile = "csv/Armor.csv"

def main():
    pass

if __name__ == '__main__':
    with open(htmlfile, encoding="utf-8") as inputfile:
        html_content = inputfile.read()
    my_soup = BeautifulSoup(html_content)
    items = my_soup.find_all("p", "stat-block-title")
    all_elements = list()

    for item in items:
        next_element = item
        item_elements = list()
        item_elements.append(item)

        while True:
            next_element = next_element.next_sibling
            if next_element == '\n':
                pass
            elif next_element == None:
                break
            elif next_element.has_attr("class") and (next_element["class"][0] == "stat-block-title"):
                break
            else:
                for match in next_element.findAll('a'):
                    match.replace_with_children()
                item_elements.append(next_element)
        all_elements.append(item_elements)

    all_elements_formated = list()
    for element in all_elements:
        name = ""
        stats = ""
        reqs = ""
        desc = ""
        details = ""
        crafting_flag = False
        for tag in element:
            if crafting_flag:
                if reqs != "":
                    reqs += ", " + tag.get_text().lower()
                else:
                    reqs += tag.get_text()
            else:
                if ((tag.has_attr("class") and tag["class"][0] == "stat-block") or (tag.name == 'p' and not tag.has_attr("class"))):
                    tag.attrs = dict()
                    desc += str(tag)
                elif tag.has_attr("class") and tag["class"][0] == "stat-block-1":
                    details += "; " + tag.get_text()

            if tag.has_attr("class") and tag["class"][0] == "stat-block-title":
                name = tag.get_text().lower().capitalize()
                print(name)
            if tag.has_attr("class") and tag["class"][0] == "stat-block-breaker":
                crafting_flag = True
        item_contents = dict()
        item_contents["Name"] = name
        item_contents["Description"] = desc
        item_contents["Details"] = details
        item_contents["Construction"] = reqs
        extract_info = re.search('Price\s(.*?);', details)
        if extract_info != None:
            item_contents["Price"] = extract_info.groups()[0].replace(',','').lower()
        else:
            item_contents["Price"] = "Varies"
        all_elements_formated.append(item_contents)

    with open(cvsfile, 'w', newline='', encoding='utf-8') as cvsw:
        writer = csv.writer(cvsw, delimiter ='\t', quotechar='"')
        for item in all_elements_formated:
            row = list()
            row.append(item["Name"])
            row.append(item["Price"])
            row.append(item["Description"])
            row.append(item["Construction"])
            writer.writerow(row)