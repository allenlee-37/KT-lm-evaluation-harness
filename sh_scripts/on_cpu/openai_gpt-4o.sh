cd ./
model="openai-chat-completions"
model_args="model=gpt-4o"
tasks="bbh_cot_fewshot_boolean_expressions"
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template \
    --limit 5