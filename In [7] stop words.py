import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words("russian")

# и, в, во, не, что, он, на, я, с, со, как, 
# а, то, все, чтоб, без, будто, впрочем, хорошо, 
# свою, этой, перед, иногда, лучше, чуть, том, нельзя, 
# такой, им, более, всегда, конечно, всю, между и другие

def DeleteStopWords(text: str):
    res = ""
    stop_words = set(stopwords)
    for word in text:
        if word not in stop_words:
            res = res + " " + word
    return res
