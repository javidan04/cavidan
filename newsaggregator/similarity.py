import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def find_similarity(one_news, others, other_ids):
    df = pd.DataFrame({'texts': others})
    df["ids"] = other_ids


    tfidf = TfidfVectorizer()
    mx_tf = tfidf.fit_transform(others)
    new_entry = tfidf.transform([one_news])
    sdf = pd.DataFrame.sparse.from_spmatrix(mx_tf)
    cosine_similarity(mx_tf)

    new_entry = tfidf.transform([one_news])
    pd.DataFrame.sparse.from_spmatrix(new_entry)

    cosine_similarities = cosine_similarity(new_entry, mx_tf).flatten()

    df['cos_similarities'] = cosine_similarities
    # df = df.sort_values(by=['cos_similarities'], ascending=[0])
    return df