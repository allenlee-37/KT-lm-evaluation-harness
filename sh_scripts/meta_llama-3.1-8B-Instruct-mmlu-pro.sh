cd ../

model="hf"
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct"
tasks="leaderboard_mmlu_pro"
CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template