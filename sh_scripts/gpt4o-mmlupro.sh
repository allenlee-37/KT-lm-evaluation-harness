<<<<<<< HEAD
cd ../
model="openai-chat-completions"
model_args="model=gpt-4o"
tasks="leaderboard_mmlu_pro"
=======
model="openai-chat-completions"
model_args="model=gpt-4o"
tasks="leaderboard_mmlu_pro"

>>>>>>> 5e2067fe4bf5575d4af88ebd3a3678a260640fbf
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template