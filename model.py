from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
X = ['As U.S. budget fight looms, Republicans flip t...	']




def fake_news_det(X):
    model = load_model("saved_model/model.h5")  # Ensure the path uses forward slashes or a raw string
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X)
    maxlen = 1000
    X = tokenizer.texts_to_sequences(X)
    X = pad_sequences(X, maxlen=maxlen)
    prediction = (model.predict(X) >= 0.5).astype(int)
    if prediction[0][0] == 1:
        return True
    else:
        return False

# print(fake_news_det(X))



