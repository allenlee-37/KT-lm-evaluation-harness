cd ./
model="hf"
# meta-llama/Llama-3.1-8B-Instruct
model_args="pretrained=meta-llama/Llama-3.1-8B-Instruct" 
tasks="bbh_cot_fewshot_boolean_expressions"
lm_eval --model $model \
    --model_args $model_args \
    --tasks $tasks \
    --output_path output \
    --batch_size auto \
    --log_samples \
    --apply_chat_template \
    --limit 10 \
    --device cpu # 이건 mac 용도: 서버의 경우 삭제 필요