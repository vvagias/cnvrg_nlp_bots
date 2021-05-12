# NLP in Production Demo

## PyTorch, Huggingface, BERT NLP bot Project 

### AS seen on May 2021 cnvrg Webinar 


The spirit of BERT is to pre-train the language representations and then to fine-tune the deep bi-directional representations on a wide range of tasks with minimal task-dependent parameters, and achieves state-of-the-art results. In this tutorial, we will focus on fine-tuning with the pre-trained BERT model to classify semantically equivalent sentence pairs on MRPC task.

This webinar assumes you have selected one of the many models and fine tuned it based on your data. 

#TODO
-add screenshots and video of webinar. 


## Workspace
main jupyter notebook from the demo has code to explore. 
Also check out the notebooks in the transformers git repo that get's cloned automatically when you start a workspace. see the prerun.sh for details on automating what happens when a workspace launches. 

## Flow
Automate deployment and use data drift to trigger updates to your bot

## Deployment
Deployment is done in the serving section. 
serve.py will deploy the question answering bot 

### Example 

qa-bot 
```
curl -X POST \
    https://bert-qa-bot-.......8 \
-H 'Cnvrg-Api-Key: ...............' \
-H 'Content-Type: application/json' \
-d '{"input_params": "what is the meaning of this"}'
```



## Application

app.py and app2.py provide a way of creating a chat interface

```
    some_questions = [
        "what is cnvrg.io",
        "How many pretrained models are available in 🤗 Transformers?",
        "What does 🤗 Transformers provide?",
        "🤗 Transformers provides interoperability between which frameworks?",
    ]
```



## References
### transformer fine tunning
https://huggingface.co/transformers/custom_datasets.html#fine-tuning-with-native-pytorch-tensorflow

### pytorch tutorial
https://pytorch.org/tutorials/intermediate/dynamic_quantization_bert_tutorial.html

### huggingface transformers github
https://github.com/huggingface/transformers

### book corpus
https://github.com/huggingface/datasets/tree/master/datasets/bookcorpus

### install transformers from source 
https://huggingface.co/transformers/installation.html#installing-from-source

