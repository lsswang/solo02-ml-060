"""Complete-record independent categorical estimates and a binary pair score."""
import numpy as np

def fit_independent_complete(records):
    data = np.asarray(records, dtype=int)
    if data.ndim != 2 or data.shape[1] != 2 or not len(data):
        raise ValueError("expected complete two-bidder binary records")
    if np.any((data < 0) | (data > 1)):
        raise ValueError("type outside binary domain")
    # Ordinary complete-record estimates, with one pseudo-count per category.
    marginals = np.stack([(np.bincount(data[:, i], minlength=2) + 1)
                          / (len(data) + 2) for i in range(2)])
    joint = np.outer(marginals[0], marginals[1])
    return {"marginals": marginals.tolist(), "joint": joint.tolist()}

def raw_binary_pair_score(parameters, profile):
    a, b = profile
    return parameters[0] * a + parameters[1] * b + parameters[2] * a * b
