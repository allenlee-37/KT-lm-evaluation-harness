from datasets import Dataset

def boolq_label_to_text(doc: dict) -> str:
    correct_choice = "예" if doc['label'] == 1 else "아니오"
    return f"""{correct_choice}"""

def copa_doc_to_text(doc: dict) -> str:
    connector = {"원인": " 왜냐하면", "결과": " 그래서"}[doc["question"].strip()]
    system = "다음 전제와 이어지는 보기가 있습니다. 둘 중 더 알맞은 보기를 선택해주세요. 부가 설명 없이 1과 2 중에 선택해주세요."
    text = f"""전제: {doc['premise']} {connector}:\n1.{doc['alternative_1']}\n2.{doc['alternative_2']}"""
    return f"""{system} {text}"""


def copa_doc_to_target(doc: dict) -> str:
    correct_choice = 1 if doc["label"] == 0 else 2
    return f"""{correct_choice}"""


def copa_doc_to_choice(doc: dict) -> list:
    return [f"""{doc["alternative_1"]}""", f"""{doc["alternative_2"]}"""]


def sentineg_doc_to_text(doc: dict):
    system = """다음 문장에 대한 긍부정을 판단해주세요. 긍정일 경우 "1", 부정일 경우 "0"을 선택해주세요."""
    querry = f"""문장: {doc["sentence"]} 긍부정:"""
    return f"{system} {querry}"


def wic_doc_to_text(doc: dict) -> str:
    system = """아래 문제를 보고 두 문장이 같은 뜻으로 쓰였는지 판단해주세요. 같은 뜻이라면 "예", 다른 뜻이라면 "아니오"를 선택해주세요."""
    querry = f"""문장1: {doc["context_1"]}\n문장2: {doc["context_2"]}\n두 문장에서 {doc["word"]}가 같은 뜻으로 쓰였나?"""
    return f"{system} {querry}"

def wic_doc_to_target(doc: dict) -> str:
    correct_choice = "아니오" if doc["label"] == 0 else "예"
    return f"""{correct_choice}"""

def hellaswag_process_doc(doc: Dataset) -> Dataset:
    def preprocessor(dataset):
        ### 시스템 프롬프트 추가
        system = """문장에 이어지는 보기 1,2,3,4 중에 가장 적절한 보기를 선택해주세요."""
        return {
            "query": f"""{system}\n문장: {dataset["context"]}""",
            "choices": [
                dataset["ending_1"],
                dataset["ending_2"],
                dataset["ending_3"],
                dataset["ending_4"],
            ],
            "gold": int(dataset["label"]),
        }

    return doc.map(preprocessor)


def macro_f1_score(items):
    from sklearn.metrics import f1_score

    unzipped_list = list(zip(*items))
    golds = unzipped_list[0]
    preds = unzipped_list[1]
    fscore = f1_score(golds, preds, average="macro")
    return fscore
