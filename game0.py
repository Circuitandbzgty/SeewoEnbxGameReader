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

# 提取JudgeConfig标签中的内容
judge_contents = extract_tags(xml_content, 'JudgeConfig')

for judge in judge_contents:
    judgeitem_name = extract_tags(judge, 'JudgeItem')
    for judgeitem_names in judgeitem_name:
        text_names = extract_tags(judgeitem_names, 'Text')
        answer_names = extract_tags(judgeitem_names, 'Answer')
        print(f"{text_names}: {answer_names}")
