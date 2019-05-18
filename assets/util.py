import pickle


# 序列化
def serialize(filename, data):
    with open('%s.pkl' % filename, 'wb') as f:
        pickle.dump(data, f)


# 反序列化
def unserialize(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
