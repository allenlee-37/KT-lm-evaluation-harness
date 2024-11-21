# KT-lm-evaluation-harness branch

This is an branch for KT version lm-evaluation-harness. Version difference in api-based tests (tasks based on logits). Yaml files are adjusted to support `generate_until` and `exact_match` to avoid using `logits` or `log-probs`.

Tasks can be run with sh scripts files for better integrated tests within the team. (errors often happen in logging results and setting fewshots)
