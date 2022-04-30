import faiss
import numpy as np

FAISS_INDEX_PATH = '/home/yoloxiao/project/graduation/image_search/data/index_flat.index'


def faiss_add(id, hash):
    index = faiss.read_index_binary(FAISS_INDEX_PATH)
    faiss_key = np.array([id]).astype('int64')
    faiss_data = np.array([int(hash[i:i+2], 16)
                           for i in range(0, len(hash), 2)]).astype('uint8')
    faiss_data = faiss_data.reshape(1, len(faiss_data))
    index.add_with_ids(faiss_data, faiss_key)
    faiss.write_index_binary(index, FAISS_INDEX_PATH)
    index.display()


def faiss_search(hash, radius):
    index = faiss.read_index_binary(FAISS_INDEX_PATH)
    index.display()
    faiss_query = np.array([int(hash[i:i+2], 16)
                           for i in range(0, len(hash), 2)]).astype('uint8')
    faiss_query = faiss_query.reshape(1, len(faiss_query))
    L, D, I = index.range_search(faiss_query, radius)
    id = list(map(int, I[L[0]:L[-1]]))
    dis = list(D[L[0]:L[-1]])
    return id, dis
