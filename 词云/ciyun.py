from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import chardet
import jieba


with open("love.txt") as fp:
    text = fp.read()
    cut = jieba.cut(text)
    print(cut)
    #text1 = text.decode(type["unicode"])
    #print(text)
    mask = np.array(image.open("love.png"))
    wordcloud = WordCloud(
        mask=mask
    ).generate(','.join(cut))
    image_produce = wordcloud.to_image()
    image_produce.show()