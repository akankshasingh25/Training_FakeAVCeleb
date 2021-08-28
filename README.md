# FakeAVCeleb: A Novel Audio-Video Multimodal Deepfake Dataset

![Header](images/teaser.png)

## Overview
FakeAVCeleb is a novel Audio-Video Multimodal Deepfake Detection dataset (FakeAVCeleb), which contains not only deepfake videos but also respective synthesized cloned audios. 


## Access
If you would like to download the FakeAVCeleb dataset, please fill out the [google request form](https://docs.google.com/forms/u/1/d/e/1FAIpQLSfPDd3oV0auqmmWEgCSaTEQ6CGpFeB-ozQJ35x-B_0Xjd93bw/viewform) and, once accepted, we will send you the link to our download script.

If you have not received a response within a week, it is likely that your email is bouncing - please check this before sending repeat requests.

Once, you obtain the download link, please head to the [download section](dataset/README.md). You can also find details about the generation of the dataset there.

## Requirements and Installation


## [Benchmark](TBD)



## Training & Evaluation

### 1. Benchmark
To train and evaluate the model(s) in the paper, run this command:
- train
    ```train
    TBD
    ```
- Unimodal Evaluation
   After train the model, you can evaluate the result. 
    ```eval
    cd ./Unimodal
    python Eval_Headpose.py
    ```
    
- Multimodal Evaluation
  ```eval
    cd ./Ensemble
    python Eval_Xception_pair_softvoting.py
  ```
  
- Multimodal Evaluation
  ```eval
    cd ./Multimodal
    python Eval_Multimodal-2.py
  ```

## Results
Our model achieves the following performance on benchmark:

  
## Citation
If you use the FakeAVCeleb data or code please cite:
```
TBD

```
  
  
## License
The data can be released under the [FakeAVCeleb Request Forms](https://docs.google.com/forms/u/1/d/e/1FAIpQLSfPDd3oV0auqmmWEgCSaTEQ6CGpFeB-ozQJ35x-B_0Xjd93bw/viewform), and the code is released under the MIT license.

Copyright (c) 2021
