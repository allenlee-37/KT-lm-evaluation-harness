import random
import re

import datasets


def preprocess(text): # 텍스트 정리
    if text is None:
        return " "
    text = text.strip()
    text = text.replace(" [title]", ". ")
    text = re.sub("\\[.*?\\]", "", text)
    text = text.replace("  ", " ")
    return text


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        choices = [
            preprocess(doc["Incorrect Answer 1"]), # 텍스트 정리가 된 보기들
            preprocess(doc["Incorrect Answer 2"]),
            preprocess(doc["Incorrect Answer 3"]),
            preprocess(doc["Correct Answer"]),
        ]

        random.shuffle(choices) # 보기들을 섞음
        correct_answer_index = choices.index(preprocess(doc["Correct Answer"])) # 정답의 인덱스 찾기

        out_doc = { # 최종 데이터셋 딕셔너리 형태로 반환
            "choice1": choices[0],
            "choice2": choices[1],
            "choice3": choices[2],
            "choice4": choices[3],
            "answer": f"({chr(65 + correct_answer_index)})",
            "answer_str": f"{chr(65 + correct_answer_index)}", # 정답은 문자열로 나옴 (A, B, C, D)
        }
        return out_doc

    return dataset.map(_process_doc) # 데이터셋에 매핑
