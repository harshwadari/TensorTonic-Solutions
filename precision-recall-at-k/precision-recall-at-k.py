def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    topk = recommended[:k]
    count = 0
    for item in relevant:
        if item in topk:
            count += 1
    pre = abs(count/k)
    recal = abs(count/len(relevant))
    return [pre,recal]
    