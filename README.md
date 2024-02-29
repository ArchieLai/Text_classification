# Text_classification

## TextCNN
* Implementation of [Yoon Kim. Convolutional Neural Networks for Sentence Classification. 2014](https://arxiv.org/abs/1408.5882)
### Credits
This implementation is based on the work of [gitE0Z9](https://github.com/gitE0Z9/pytorch-implementations/tree/main). I have made the following modifications:
1. Use a pre-trained model (glove-twitter-25) to generate word embeddings instead of passing word indices into an embedding layer inside the model.
2. Modify model structure.

### Dataset
* Movie Reviews: 
https://www.cs.cornell.edu/people/pabo/movie-review-data/

### Requirements
python version: 3.9.13  
pytorch version: 2.1.2