---
title: 'Overview of open and commercially usable LLMs'
date: '2023-07-11'
summary: "New models are coming out every day. Here's an overview that can aid in selecting one for commercial use."
author: 'Yorick van Pelt'
---


This page contains an overview of source-available LLMs. Weights have been released for all of these models, but in some cases, restrictions apply to the usage of the weights. Several of these models can be tested at [https://chat.lmsys.org/](https://chat.lmsys.org/)

The legal situation of copyrighting LLM weights is unclear (in Europe and the US), but source code definitely falls under copyright protection.

## Omissions

- In general, our investigation has centered on commercially usable models. There are a lot of fine-tuned llamas that have been omitted, but they are generally not that different.
- **Unaligned chat/instruct models**: not a big research focus, as they are all based on llama. However, they may be useful in case you're hitting “Sorry, as an AI language model..” a lot.

## Various Restrictions

The Models section uses various tags for usage restrictions:

- **Non-commercial** means the weights have been released under a license that prohibits commercial use.
- **No-Evil** means the weights have been released under a license that prohibits use for illegal or unethical activities. There are two licenses in wide use.
    - **The Together license** Includes some examples of misuse.
        
        Using the model to generate content that is cruel to individuals is a misuse of this model. This includes, but is not limited to:
        
        - Generating fake news, misinformation, or propaganda
        - Promoting hate speech, discrimination, or violence against individuals or groups
        - Impersonating individuals or organizations without their consent
        - Engaging in cyberbullying or harassment
        - Defamatory content
        - Spamming or scamming
        - Sharing confidential or sensitive information without proper authorization
        - Violating the terms of use of the model or the data used to train it
        - Creating automated bots for malicious purposes such as spreading malware, phishing scams, or spamming
        
    - **The RAIL license**: [License - a Hugging Face Space by bigscience](https://huggingface.co/spaces/bigscience/license)
        
    
    While this is (hopefully) not a problem for your intended use, it's good to keep this restriction in mind, and don't consider the model fully open.

<!-- comment
How to generate:
- notion: export as markdown + csv
- pandoc -i Models\ 1f4e7a77004c4aed97864b551b9a00c4.csv -f csv -t gfm | wl-copy
- clean up links
-->
    
# Model list


| Name                      | Tags           | Trained    | Based on              | Company              | Date       | Dataset                                 | Params            |
|---------------------------|----------------|------------|-----------------------|----------------------|------------|-----------------------------------------|-------------------|
| GPT-2                     |                | Completion |                       | OpenAI               | 2019/02/14 |                                         | 1.5B              |
| gpt-j-6b                  |                | Completion |                       | EleutherAI           | 2021/05/01 | The Pile                                | 6B                |
| GPT-NeoX-20B              |                | Completion |                       | EleutherAI           | 2022/04/14 | The Pile                                | 20B               |
| BLOOM                     | No-Evil        | Completion |                       | BigScience           | 2022/07/06 |                                         | 176B              |
| flan-t5                   |                | Completion |                       | Google               | 2022/10/20 |                                         | 11B, 3B           |
| RWKV-4-pile               |                | Completion |                       |                      | 2022/10/22 | The Pile                                |                   |
| Llama                     | Non-commercial | Completion |                       | Meta                 | 2023/02/24 |                                         | 13B, 33B, 65B, 7B |
| oasst-pythia-12b          |                | Assistant  | Pythia                | LAION                | 2023/03/07 | openassistant/oasst1                    | 12B               |
| Dolly                     |                | Instruct   | Pythia                | Databricks           | 2023/03/24 | databricks-dolly-15k                    | 12B, 3B, 6B, 7B   |
| Cerebras-GPT-13B          |                | Completion |                       | Cerebras             | 2023/03/28 | The Pile                                | 13B               |
| Vicuna                    | Non-commercial | Chat       | Llama                 | LMSYS                | 2023/03/30 | ShareGPT                                | 13B, 7B           |
| GPT-NeoXT-Chat-Base-20B   | No-Evil        | Chat       | GPT-NeoX-20B          | Together             | 2023/03/30 |                                         |                   |
| RWKV-4-raven              |                | Chat       | RWKV-4-pile           | BlinkDL              | 2023/04/01 | ShareGPT                                | 1.5B, 14B, 3B, 7B |
| Koala                     | Non-commercial | Chat       | Llama                 | Berkeley AI Research | 2023/04/03 |                                         | 13B, 7B           |
| Pythia                    |                | Completion | GPT-NeoX-20B          | EleutherAI           | 2023/04/03 | The Pile                                |                   |
| gpt4all-j                 |                | Chat       | gpt-j-6b              | Nomic                | 2023/04/12 | databricks-dolly-15k, ShareGPT          | 6B                |
| Fastchat-T5-3b-v1.0       |                | Chat       | flan-t5               | LMSYS                | 2023/05/01 | ShareGPT                                | 3B                |
| StarCoder                 |                | Code       |                       |                      | 2023/05/03 | The Stack                               | 16B               |
| MPT-7B-storywriter-65k+   |                | Completion | MPT-7B                | MosaicML             | 2023/05/05 |                                         | 7B                |
| MPT-7B-Instruct           |                | Instruct   | MPT-7B                | MosaicML             | 2023/05/05 | databricks-dolly-15k, Anthropic/hh-rlhf | 7B                |
| MPT-7B-Chat               |                | Chat       | MPT-7B                | MosaicML             | 2023/05/05 |                                         | 7B                |
| MPT-7B                    |                | Completion |                       | MosaicML             | 2023/05/05 |                                         | 7B                |
| RedPajama-INCITE-Chat     | No-Evil        | Chat       | RedPajama-INCITE-Base | Together             | 2023/05/05 | RedPajama                               | 3B, 7B            |
| RedPajama-INCITE-Instruct | No-Evil        | Instruct   | RedPajama-INCITE-Base | Together             | 2023/05/05 | RedPajama                               | 3B, 7B            |
| RedPajama-INCITE-Base     | No-Evil        | Completion |                       | Together             | 2023/05/05 | RedPajama                               | 3B, 7B            |
| StarCoderPlus             | No-Evil        | Completion | StarCoder             | bigcode              | 2023/05/08 | RefinedWeb                              | 16B               |
| Falcon-rw                 |                | Completion |                       | TII UAE              | 2023/06/05 | RefinedWeb                              | 1B, 7B            |
| Falcon-Instruct           |                | Chat       | Falcon                | TII UAE              | 2023/06/05 |                                         | 40B, 7B           |
| Falcon                    |                | Completion |                       | TII UAE              | 2023/06/05 |                                         | 40B, 7B           |
| StarChat-β                | No-Evil        | Chat       | StarCoderPlus         | Huggingface          | 2023/06/07 | openassistant/oasst1                    | 16B               |

# Datasets

| Name                 | Group      |
|----------------------|------------|
| The Pile             | EleutherAI |
| ShareGPT             |            |
| RedPajama            | Together   |
| databricks-dolly-15k | Databricks |
| Anthropic/hh-rlhf    |            |
| openassistant/oasst1 | LAION      |
| RefinedWeb           | TII UAE    |
| The Stack            | bigcode    |

# Groups

| Name                        | Tags           | URL                             |
|-----------------------------|----------------|---------------------------------|
| EleutherAI                  | Research group | https://www.eleuther.ai/        |
| Google                      |                | https://ai.googleblog.com/      |
| Meta                        |                | https://ai.facebook.com/        |
| Cerebras                    |                | https://www.cerebras.net/       |
| LMSYS                       | Research group | https://lmsys.org/              |
| Nomic                       |                | https://nomic.ai/               |
| OpenAI                      |                | https://openai.com/             |
| Together                    |                | https://www.together.xyz/       |
| Databricks                  |                | https://www.databricks.com/     |
| MosaicML                    |                | https://www.mosaicml.com/       |
| Berkeley AI Research (BAIR) | Research group | https://bair.berkeley.edu/blog/ |
| BigScience                  |                |                                 |
| LAION                       |                |                                 |
| BlinkDL                     |                |                                 |
| TII UAE                     |                |                                 |
| Huggingface                 |                |                                 |
| bigcode                     |                |                                 |
