from transformers import pipeline
nlp = pipeline("question-answering")

data=""
try:
    with open('/data/bert/info.txt', 'r') as file:
        data = file.read().replace('\n', '')
except:
    print('create a dataset ')
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script.
"""+data


def respond(question):
    resp = nlp(question=question, context=context)
    return resp['answer']