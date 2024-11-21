# KT-lm-evaluation-harness branch

This is an branch for KT version lm-evaluation-harness. Version difference in api-based tests (tasks based on logits). Yaml files are adjusted to support `generate_until` and `exact_match` to avoid using `logits` or `log-probs`.

Tasks can be run with sh scripts files for better integrated tests within the team. (errors often happen in logging results and setting fewshots)

> !! Push all adjustements with each respective commit messages

## Updates

### TODO

- integrate BBH yaml files into this repo
- make each sh files
- integrate results files into the repo

#### info

This repo is branched from `LM-Evaluation-Harness 0.4.5 Release`
In case of merging with latest LM-Evaluation-Harness version please inform the repo owner: allenlee-37
