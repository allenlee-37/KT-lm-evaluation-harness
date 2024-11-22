import string


def doc_to_text(doc):
    doc_to_text = f"What is the correct answer to this question? Please do not add any explanation, just give me the correct answer between options (A-Z).  {doc['question']}\n"

    for i in range(len(doc["options"])):
        # () 감쌀 수 있게 수정
        doc_to_text += f"({string.ascii_uppercase[i]}). {doc['options'][i]}\n"

    doc_to_text += "Answer:"
    return doc_to_text


def doc_to_choice(doc):
    # () 감쌀 수 있게 수정
    return [f"({string.ascii_uppercase[i]})" for i in range(len(doc["options"]))]
