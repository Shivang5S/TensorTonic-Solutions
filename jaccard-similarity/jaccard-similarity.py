def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    if len(set_a) == 0 and len(set_b) == 0:
        return 0.0
    a, b = set(set_a), set(set_b)
    return len(a.intersection(b))/len(a.union(b))