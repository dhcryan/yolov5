# 2023-1 기계학습 Team project


<img src="킥라니.png" width="800">

## 1. Folder Tree
- ```data/```
    - ```sleep/```
        - this is the data folder for the processed sample-based Sleep-EDF cassette portion.
        - **sleep_edf_process.py**: the processing file for sleep-edf (using multiprocess package for parallel programming)
        - for downloading the Sleep-EDF data, please refere to https://www.physionet.org/content/sleep-edfx/1.0.0/
- ```log/```, ```pre-trained/```
    - this two folders stores the automatically generated running logs and pre-trained models
- **model.py**
    - this file contains all the backbone and Base models for running the experiments

- ```run_sleep/```
    - **model_sleep.py**: This file inherit the Base model and other model utility functions from **model.py** and support the sleep staging task
    - **run_sleep.py**: This is the entry of sleep stagin task, specifiying the data loader and other initialization steps.
    - **utils_sleep.py**: This file provides the data split and loading files.

## 2. How to run the code
- for sleep staging
``` python
cd ./dg_selfstudy
python data/sleep/sleep_edf_process.py
python run_sleep/util_sleep.py
python run_sleep/model_sleep.py
python run_sleep/run_sleep.py --model dev --cuda 0 --epochs 50
```
- for speech
``` python
cd ./dg_selfstudy
# python data/sleep/sleep_edf_process.py
python run_speech/model.py
python run_speech/util_sleep.py
python run_speech/model_sleep.py
python run_speech/run_sleep.py --model dev --cuda 0 --epochs 50
```

## 3. Result
- https://wandb.ai/dilab_ajou/train/reports/---Vmlldzo0NTUyOTAw
- https://wandb.ai/dilab_ajou/train/reports/FINAL-REPORT--Vmlldzo0NTUyOTYz

## 4. Citation
```bibtex
@inproceedings{yolov5,
    github = https://github.com/ultralytics/yolov5
}
```