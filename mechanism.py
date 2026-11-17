"""Known-value allocation; no truthfulness constraints are imposed here."""
import numpy as np

def clairvoyant_rule(values):
    values = np.asarray(values, dtype=float)
    allocations, payments = [], []
    for a in range(2):
        for b in range(2):
            v = values[np.arange(2), [a, b]]
            winners = v == v.max()
            x = winners.astype(float) / winners.sum()
            allocations.append(x.tolist())
            payments.append((x * v).tolist())
    return {"allocations": allocations, "payments": payments}

def outcome(rule, profile):
    index = 2 * profile[0] + profile[1]
    return {"allocation": list(rule["allocations"][index]),
            "payment": list(rule["payments"][index])}

def revenue(rule, joint):
    return float(np.asarray(joint).reshape(4)
                 @ np.asarray(rule["payments"]).sum(axis=1))
