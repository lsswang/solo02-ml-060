import json
from pathlib import Path
import latent
import mechanism

if __name__ == "__main__":
    cases = json.loads((Path(__file__).parent / "fixtures/cases.json").read_text())
    model = latent.fit_independent_complete(cases["ordinary_complete_records"])
    rule = mechanism.clairvoyant_rule(cases["values"])
    print(json.dumps({"model": model, "rule": rule,
                      "revenue": mechanism.revenue(rule, model["joint"])}, indent=2))
