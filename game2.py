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

# 提取Classify标签中的内容
classify_contents = extract_tags(xml_content, 'ClassifyConfig')

# 遍历Classify标签内容并提取Items中的Name标签内容
for classify in classify_contents:
    classify_name = extract_tags(classify, 'Name')[0]
    items_names = extract_tags(classify, 'Items')
    for item_names in items_names:
        item_names = extract_tags(item_names, 'Name')
        print(f"{classify_name}: {item_names}")