# KT-lm-evaluation-harness

---

**KT 내부 LM 모델 테스트용 lm-eval-harness 수정 버전**

This is an branch for KT version lm-evaluation-harness. Version difference in api-based tests (tasks based on logits). Yaml files are adjusted to support `generate_until` and `exact_match` to avoid using `logits` or `log-probs`.

Tasks can be run with sh scripts files for better integrated tests within the team. (errors often happen in logging results and setting fewshots)

> !! Push all adjustements with each respective commit messages

**_변경사항 📣_**

- [2024/11] Ko-winogrande task 추가 (KT 내부 벤치마크).
- GPT API 호출을 위해 exact-match 형태로 변환됨. (logprobability 방식 사용하지 않을 것)

## TODO

- [2024/11] lm>tasks>BBH의 평가방식을 exact match 및 generate until로 수정
- [2024/11] lm-eval-harness 지원하지 않는 벤치마크 추가
- [2024/11] sh scripts 추가 필요

| Model          | model                                                                                                                         | model_args              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| llama 1.0      | /vfroot/n22-model/f6e12a6705dc47f5af9f2b6bce90e0d4/93/40/e3564e474cf19dfb7e2fc364fe61/llama3.1-pro16-0827-Inst_241016         | hf                      |
| llama 2.0      | /vfroot/n22-model/f6e12a6705dc47f5af9f2b6bce90e0d4/93/40/e3564e474cf19dfb7e2fc364fe61/llama3.1-pro16-0827-Inst-nc-chat_241016 | hf                      |
| llama 3.1 8b   | pretrained=meta-llama/Llama-3.1-8B-Instruct                                                                                   | hf                      |
| midm2.0-8b     | /vfroot/n22-largeai/studio/Midm-bitext-S-Chat/midm-bitext-s-chat-200                                                          | hf                      |
| gpt4o          | model=gpt-4o                                                                                                                  | openai-chat-completions |
| solar instruct | pretrained=upstage/SOLAR-10.7B-Instruct-v1.0                                                                                  | hf                      |
| Exaone         | pretrained=LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct0                                                                              | hf                      |

#### info

This repo is branched from `LM-Evaluation-Harness 0.4.5 Release`
In case of merging with latest LM-Evaluation-Harness version please inform the repo owner: allenlee-37
