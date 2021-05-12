#apt install nodejs npm
#npm install -g --unsafe-perm node-red
#node-red -port 6006
#snap install node-red
python -m spacy download en_core_web_sm
yes y | pip uninstall torch tochvision
yes y | pip install --pre torch -f https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
python download_glue_data.py --data_dir='glue_data' --tasks='MRPC'
git clone https://github.com/huggingface/transformers.git
cd transformers
pip install -e .
cd ..
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I love you'))"


