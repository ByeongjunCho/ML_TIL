# Word embeddings
* 단어를 벡터로 표현하는 것을 말한다.  
* One hot vector == 희소 벡터(sparse representation)로 단어를 표현할 수 있다.  
* Dense Representation(밀집 표현) : 벡터 차원을 단어들의 갯수(클래스의 수)로 하지 않고 실수를 이용해 벡터를 표현하는 방법  
* 밀집 벡터(dense vector)의 형태로 표현하는 방법을 **워드 임베딩(Word Embedding)** 이라고 한다.  

tf.keras.layers.Embedding(  
    input_dim, output_dim, embeddings_initializer='uniform',  
    embeddings_regularizer=None, activity_regularizer=None,  
    embeddings_constraint=None, mask_zero=False, input_length=None, **kwargs  
)  

**input_dim** : 단어 집합의 크기, 즉 총 단어의 개수  
**output_dim** : 임베딩 벡터의 출력 차원. 결과로 나오는 임베딩 벡터의 크기  
**input_length** : 입력 시퀀스의 길이(입력되는 단어 벡터의 dim) `지정하지 않으면 입력으로 지정`  

**Input shape** : 2D tensor with shape: `(batch_size, input_length)`  
**Output shape** : 3D tensor with shape: `(batch_size, input_length, output_dim)`  

# 전처리(Preprocessing)
**Tokenizer() :** 토큰화와 정수 인코딩(단어에 대한 인덱싱)을 위해 keras에서 제공하는 Tokenizer를 사용한다.  
