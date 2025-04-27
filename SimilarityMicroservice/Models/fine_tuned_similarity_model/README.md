---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:2000
- loss:CosineSimilarityLoss
base_model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
widget:
- source_sentence: — боже, ендрю, — простогнав нікі. метт обвів очима всіх трьох.
  sentences:
  - — спасибі тобі , ніле , за те , що ти такий Звичайний . два твої слова Тільки-но
    принесли мені десять баксів . — Суворо ? і з ким же ти сперечався ?
  - не знаю, хто розповів названимбатькам ендрю про аарона — сам ендрю чи той коп,
    філ хіґґінс, — але названа мати ендрю надіслала ааронові листа.
  - ніл вирушив далі на розвідку, а кевін з аароном залишилися в кімнаті.
- source_sentence: '— Гаразд , — сказав ніл . розуміючи , що тема болюча , він все
    ж таки не втримався : — як думаєш , ендрю закинеться таблетками перед другим таймом
    ? — ні , — похмуро озвався кевін .'
  sentences:
  - Пору від часу вони з цікавістю поглядали на аарона та нікі , але ні про що не
    питали .
  - проблемно , Звичайно , зате досі допомагало залишатися живим .
  - '— добре, — сказав ніл. розуміючи, що тема болюча, він все ж таки не втримався:
    — як думаєш, ендрю закинеться таблетками перед другим таймом? — ні, — похмуро
    озвався кевін.'
- source_sentence: 'ніл це помітив, але не думав, що помітять інші. те, що лиси звернули
    на це увагу і намагаються йому допомогти, його вразило. він зам''явся з відповіддю,
    не знаходячи слів, і зрештою видавив: — ви справді не проти?'
  sentences:
  - ніл спантеличено подивився на обох.
  - — можете переночувати в нас, якщо хочете. якщо вам здається, що… — вона не закінчила,
    але погляд, яким вона обвела кімнату, казав більше за всякі слова.
  - 'ваймака з ними не було — певне, свою частину інтерв''ю він уже відпрацював. помітивши
    рух у коридорі, рене кинула погляд у дверний отвір і посміхнулася нілу: мовляв,
    зрозуміла. після цього він вважав за краще якнайшвидше забратися — не дай боже
    схоплять журналісти. ховатися було особливо ніде, але тут він помітив прочинені
    двері медичного кабінету.'
- source_sentence: — заодно і подивимося. ваймак задоволено кивнув головою.
  sentences:
  - він зізнався матері, що підслухав?
  - здавалося, ніби за вікном настав гелловін — тільки на два місяці раніше, ніж треба.
  - метт переплів свої пальці з її пальцями й міцно їх стиснув.
- source_sentence: 'рішення здавалося простим і очевидним: сьогодні він не повинен
    пропускати прийом таблеток, подобається йому це чи ні, проте «просто» з ендрю
    міньярдом не було ніколи. — мабуть, так, — охоче погодився ендрю.'
  sentences:
  - 'рішення здавалося простим і Явний : сьогодні він не повинен пропускати прийом
    таблеток , подобається йому це чи ні , проте « просто » з ендрю міньярдом не було
    ніколи . — мабуть , так , — охоче погодився Дивак .'
  - нілу подобалося випереджати й обводити довкола пальця захист противника, подобалося
    відчувати викид адреналіну в кров після точного удару по воротах. він любив динаміку,
    тиск, тріумф перемоги. все інше його життя являло собою суцільний бардак, тому
    драйв та чіткі правила гри служили йому необхідною опорою.
  - — що я пропустив ?
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) <!-- at revision 86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'рішення здавалося простим і очевидним: сьогодні він не повинен пропускати прийом таблеток, подобається йому це чи ні, проте «просто» з ендрю міньярдом не було ніколи. — мабуть, так, — охоче погодився ендрю.',
    'рішення здавалося простим і Явний : сьогодні він не повинен пропускати прийом таблеток , подобається йому це чи ні , проте « просто » з ендрю міньярдом не було ніколи . — мабуть , так , — охоче погодився Дивак .',
    '— що я пропустив ?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 2,000 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                         | label                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                          |
  | details | <ul><li>min: 7 tokens</li><li>mean: 46.04 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 46.02 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.39</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                            | sentence_1                                                                                                                                                          | label                           |
  |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
  | <code>— а тепер годі дзявкати, всі слухаємо мене. перед нами постає непросте завдання. почавши з лінії захисту, ваймак пояснив кожному гравцю його прорахунки та похвалив команду за нечисленні вдалі моменти.</code> | <code>— він має рацію, — втрутився ніл перш ніж кевін встиг відповісти.</code>                                                                                      | <code>0.0181818181818181</code> |
  | <code>— навряд чи з мене вийде ця ланка, — зізнався ніл.</code>                                                                                                                                                       | <code>на щастя, стукіт у двері позбавив його необхідності відповідати. ніл почав підійматися, але через ноутбук на колінах забарився, і метт його випередив.</code> | <code>0.0833333333333333</code> |
  | <code>вчора еббі поклала пляшечку з твоїми таблетками в аптечку першої допомоги. щойно залишаєш поле, вони твої.</code>                                                                                               | <code>Напередодні еббі поклала пляшечку з твоїми таблетками в аптечку першої допомоги . Тільки-но залишаєш поле , вони твої .</code>                                | <code>0.2727272727272727</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `tp_size`: 0
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Framework Versions
- Python: 3.12.5
- Sentence Transformers: 4.1.0
- Transformers: 4.51.3
- PyTorch: 2.6.0+cpu
- Accelerate: 1.6.0
- Datasets: 3.5.0
- Tokenizers: 0.21.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->