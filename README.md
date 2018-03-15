# CRF-DATA-PREPARE
a tool used to translate data from brat to crf trainning data set

## Usage

Labeling and export the data file from brat

Put the two files(*.ann and *.txt) to '''data_brat''' dir

Edit the config.ini file under config/,such as below
```shell
[brat_files]
data.ann = data.txt
data1.ann = data1.txt
```


## Run

After the files from brat prepared.go to the root path of CRF-DATA-PREPARE and run:
```shell
python3 main.py
```

## Result

After then,if you could see this info as below,that means file convert successful.
```shell
Convert complete 2 files

Process finished with exit code 0
```

The trainning file should be saved under ref_data/

## Todo
You could use these trainning set to continue to train your model using 
[Chinese Relation Extraction by biGRU with Character and Sentence Attentions](https://github.com/crownpku/Information-Extraction-Chinese/tree/master/NER_IDCNN_CRF).

