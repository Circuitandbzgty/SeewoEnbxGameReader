file_path = input("Please enter the XML file path: ")

with open(file_path, 'r') as file:
    xml_content = file.read()

def extract_tags(xml_content, tag_name):
    start_tag = '<' + tag_name + '>'
    end_tag = '</' + tag_name + '>'
    results = []
    start_index = xml_content.find(start_tag)
    
    while start_index != -1:
        start_index += len(start_tag)
        end_index = xml_content.find(end_tag, start_index)
        if end_index == -1:
            break
        tag_content = xml_content[start_index:end_index]
        results.append(tag_content)
        start_index = xml_content.find(start_tag, end_index)
    
    return results

# 提取TextMatchConfig标签中的内容
match_contents = extract_tags(xml_content, 'TextMatchConfig')

for match in match_contents:
    matchitem_name = extract_tags(match, 'MatchItems')
    for matchitems_name in matchitem_name:
        textmatchitem_name = extract_tags(matchitems_name, 'TextMatchItem')
    for matchtexts_names in textmatchitem_name:
        text_names = extract_tags(matchtexts_names, 'Text')
        matchtext_names = extract_tags(matchtexts_names, 'MatchText')
        print(f"{text_names}: {matchtext_names}")
