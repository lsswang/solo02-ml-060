# Latent values and allocation rules

Python 3.11 with NumPy and SciPy. Run `python demo.py` in this folder.

`latent.fit_independent_complete` estimates two independent binary categorical
variables from complete type records. `raw_binary_pair_score` supplies a small
three-coordinate log-linear score primitive, without a likelihood or fitter.
`mechanism.clairvoyant_rule` allocates one item to a highest known value and
charges that value, splitting exact ties. This is a known-value allocation
tool; it does not implement truthful direct reporting.

Profile order for the small existing rule representation is 00,01,10,11.
All values and payments are synthetic mathematical quantities.
