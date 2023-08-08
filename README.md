# CSRSPY

[![PyPI version](https://badge.fury.io/py/csrspy.svg)](https://badge.fury.io/py/csrspy)
[![tests](https://github.com/tayden/csrspy/actions/workflows/tests.yml/badge.svg)](https://github.com/tayden/csrspy/actions/workflows/tests.yml)

*ITRF/NAD83CSRS coordinate transforms in Python.*

## Installation

Install with `pip install csrspy`

## About

CSRSPY provides coordinate transformation utilities to transform coordinates between various ITRF realization and NAD83 (CSRS).
Furthermore, this library provides the ability to transform between reference epochs and between GRS80 ellipsoidal heights and
orthometric heights in CGG2013, CGG2013a, and HT2_2010v70 vertical datums.

CSRSPY is tested for accuracy against official tools from Natural Resources Canada (specifically,
[TRX](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/trx.php) and
[GPS-H](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/gpsh.php)).

If you're hoping to transform LAS/LAZ file coordinates using CSRSPY, check out
[LAS-TRX](https://github.com/HakaiInstitute/LAS-TRX).

## Example Usage

```python
from csrspy import CSRSTransformer
from csrspy.enums import Reference, CoordType, VerticalDatum

transformer = CSRSTransformer(s_ref_frame=Reference.ITRF14, t_ref_frame=Reference.NAD83CSRS,
                              s_coords=CoordType.GEOG, t_coords=CoordType.UTM10,
                              s_epoch=2023.58, t_epoch=2002.0,
                              s_vd=VerticalDatum.GRS80, t_vd=VerticalDatum.CGG2013A)

in_coords = [(-123.365646, 48.428421, 0)]
out_coords = list(transformer(in_coords))

print(out_coords)
# >> [(472952.4353700947, 5363983.41690525, 18.968777521543867)]
```
