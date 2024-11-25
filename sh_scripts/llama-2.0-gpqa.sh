cd ../
model="hf"
model_args="pretrained=/vfroot/n22-model/f6e12a6705dc47f5af9f2b6bce90e0d4/93/40/e3564e474cf19dfb7e2fc364fe61/llama3.1-pro16-0827-Inst-nc-chat_241016"
tasks="leaderboard_gpqa"

CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template