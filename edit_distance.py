import np


def edit_distance(pred, label, normalize=False):
    if pred == label:
        return 0

    L1, L2 = len(pred), len(label)
    pred, label = [int(t) for t in pred], [int(t) for t in label]
    M = np.zeros((L1+1, L2+1))
    for i in range(L1 + 1):
        M[i, 0] = i
    for j in range(L2 + 1):
        M[0, j] = j

    for i in range(1, L1+1):
        for j in range(1, L2+1):
            t1, t2 = pred[i-1], label[j-1]
            M[i, j] = min(M[i-1, j-1] + (t1!=t2), M[i-1, j]+1, M[i, j-1]+1,)
    if normalize:
        return M[L1, L2] / len(label)
    return M[L1, L2]
