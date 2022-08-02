import datetime

import scipy.io as sio
import numpy as np
import arff
import codecs


# @Author : Xie Zexian
# @Description convert arff to mat
# @Time : 2022/8/2 10:28
def arff_to_mat(dataset_name, feature_number):
    print("converting...")

    arff_file = codecs.open(data_name + '/' + data_name + '.arff', 'r', 'UTF-8')
    arff_file = arff.load(arff_file)
    data = arff_file['data']
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][0:feature_number])
        y.append(data[i][feature_number:])
    feature = np.array(x)
    label = np.array(y)
    feature = feature.astype(float)
    label = label.astype(float)
    sio.savemat(dataset_name + '/' + dataset_name + '.mat', {'feature': feature, 'label': label}, do_compression=True)


if __name__ == '__main__':
    '''
    data_name: the name of dataset
    x_number: the number of feature of dataset
    '''
    data_name = 'delicious'
    x_number = 500
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " begin to convert")
    arff_to_mat(data_name, x_number)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " finish!")
