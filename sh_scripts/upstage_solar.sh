cd ./
model="hf"
model_args="pretrained=upstage/SOLAR-10.7B-Instruct-v1.0" # pretrained=upstage/SOLAR-10.7B-v1.0 
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