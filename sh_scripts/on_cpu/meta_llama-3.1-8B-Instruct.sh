cd ../
model="hf"
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct"
tasks="leaderboard_gpqa"

lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size 1 \
    --log_samples \
    --apply_chat_template \
    --limit 10 \
    --device cpu