# Tensorflow2-generative-model-collections(궁금한거 만드는중....)

* [hwalusklee github](https://github.com/hwalsuklee/tensorflow-generative-model-collections)를 참고하여 작성하였습니다.



## BEGAN

* 논문에 나와있는 대로 generator 입력을 Zd와 Zg 두개를 사용하니까 학습이 안됨(논문 이해를 잘못한거 같음. 혹은 구조를 잘못 구성해서 그런듯)
* discriminator의 loss는 1차 `norm`이다. 참고로 했던 github의 2차 `norm`으로 했다가 잘 안되서 1차로 바꾸니 학습속도가 빨라짐
* Generator과 Discriminator의 구조가 deep하지 않아서 그런지 몇가지 숫자는 깔끔하게 나오지 않은 것 같다.

![BEGAN_imagemnist_began](.\BEGAN_imagemnist_began.gif)

* 이미지의 변화도 많지 않음(M_global 파라미터는 계속 감소함. M_global 변수를 저장하지 못함. 집 컴퓨터로 학습한거라 다시하기 귀찮)
* batch_size = 64, epoch=50으로 학습



* epoch=1

![image_at_epoch_0001](.\BEGAN_image\image_at_epoch_0001.png)

* epoch=50(더 선명해지고 구분이 쉬워진거 말고는 차이가 없는듯?)

![image_at_epoch_0050](.\BEGAN_image\image_at_epoch_0050.png)