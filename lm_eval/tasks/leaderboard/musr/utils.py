import ast
import datasets

def doc_to_choice(doc):
    """
    Convert a doc to a choice.
    """
    return ast.literal_eval(doc["choices"])

# 명확한 질문 전달을 위한 프롬프트 수정
DOC_TO_TEXT = "Please answer the following question with (a), (b), (c), (d) \n\nNarrative: {narrative}\n\n" "Question: {question}\n\n" "Choices: {choices}\n\n" "Answer: "

def doc_to_text(doc):
    """
    Convert a doc to text.
    """
    choices = ""
    for i, choice in enumerate(ast.literal_eval(doc["choices"])):
        choices += f"({chr(i+97)}) - {choice}\n" # 정답 인덱싱 추가

    text = DOC_TO_TEXT.format(
        narrative=doc["narrative"], question=doc["question"], choices=choices
    )
    return text

# 정답 보내주는 부분 추가
def get_answer(doc):
    # 1~4까지의 인덱스를 a~d로 변환
    return f"({chr(doc['answer_index']+96)})"