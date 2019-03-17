import pickle


# 序列化
def serialize(fileName,data):
    with open('%s.pkl'%fileName, 'wb') as f:
        pickle.dump(data, f)

# 反序列化
def unserialize(fileName):
    with open('%s.pkl'%fileName, 'rb') as f:
        return pickle.load(f)