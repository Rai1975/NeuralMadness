import json

file_path = r'PATH/TO/FILE'

# File to read JSON file of conversation corpus
def read_json():
    lines = []
    with open(file_path, 'r+') as file:
       counter = 0
       for line in file:
        lines.append(json.loads(line.strip()))
        counter += 1
        if(counter == 5):
           break

    return lines

# Organizing them by conversation
def extract_conversations(corpus_json):
    convos = {}

    for utterance in corpus_json:
        if utterance.get('conversation_id') in convos.keys():
            conversation = convos[utterance.get('conversation_id')]
            if utterance.get('speaker') in conversation.keys():
               conversation[utterance.get('speaker')].append(utterance.get('text'))
            else:
               conversation[utterance.get('speaker')] = [utterance.get('text')]
        else:
            convos[utterance.get('conversation_id')] = {utterance.get('speaker'): [utterance.get('text')]}

    return convos


json_obj = read_json()
convos = extract_conversations(json_obj)

print(convos)


