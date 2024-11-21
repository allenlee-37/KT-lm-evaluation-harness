cd ./
model="openai-chat-completions"
model_args="model=gpt-4o"
# leaderboard_gpqa
# leaderboard_bbh

tasks="leaderboard_gpqa" # leaderboard_bbh_boolean_expressions
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template