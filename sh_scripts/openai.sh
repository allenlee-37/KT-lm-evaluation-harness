cd ./
model="openai-chat-completions"
model_args="model=gpt-4o"
tasks="kmmlu_direct_agricultural_sciences"

lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path results \
    --batch_size auto \
    --log_samples \
    --apply_chat_template \
    --limit 10
