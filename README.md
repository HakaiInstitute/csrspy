# CSRSPY

[![PyPI version](https://badge.fury.io/py/csrspy.svg)](https://badge.fury.io/py/csrspy)
[![tests](https://github.com/tayden/csrspy/actions/workflows/tests.yml/badge.svg)](https://github.com/tayden/csrspy/actions/workflows/tests.yml)

*ITRF/NAD83CSRS coordinate transforms in Python.*

## Table of Contents

1. [Installation](#installation)
2. [About](#about)
3. [Usage](#usage)
    - [Basic Example](#basic-example)
    - [Advanced Usage](#advanced-usage)
4. [API Reference](#api-reference)
5. [Developer Guide](#developer-guide)
    - [Setting Up the Development Environment](#setting-up-the-development-environment)
    - [Running Tests](#running-tests)
    - [Updating the Library](#updating-the-library)
    - [Publishing to PyPI](#publishing-to-pypi)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

Install with pip:

```bash
pip install csrspy
```

## About

CSRSPY provides coordinate transformation utilities to transform coordinates between
various ITRF realization and NAD83 (CSRS).
Furthermore, this library provides the ability to transform between reference epochs and
between GRS80 ellipsoidal heights and
orthometric heights in CGG2013, CGG2013a, and HT2_2010v70 vertical datums.

CSRSPY is tested for accuracy against official tools from Natural Resources Canada (
specifically,
[TRX](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/trx.php) and
[GPS-H](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/gpsh.php)).

If you're hoping to transform LAS/LAZ file coordinates using CSRSPY, check out
[LAS-TRX](https://github.com/HakaiInstitute/LAS-TRX).

## Usage

### Basic Example

Here's a simple example of how to use CSRSPY to transform coordinates:

```python
from csrspy import CSRSTransformer
from csrspy.enums import Reference, CoordType, VerticalDatum

transformer = CSRSTransformer(s_ref_frame=Reference.ITRF14,
                              t_ref_frame=Reference.NAD83CSRS,
                              s_coords=CoordType.GEOG, t_coords=CoordType.UTM10,
                              s_epoch=2023.58, t_epoch=2002.0,
                              s_vd=VerticalDatum.GRS80, t_vd=VerticalDatum.CGG2013A)

in_coords = [(-123.365646, 48.428421, 0)]
out_coords = list(transformer(in_coords))
print(out_coords)  # Output: [(472952.4353700947, 5363983.41690525, 18.968777523406512)]
```

### Advanced Usage

CSRSPY supports various coordinate types, reference frames, and vertical datums. Here's
an example of a more complex transformation:

```python
from csrspy import CSRSTransformer
from csrspy.enums import Reference, CoordType, VerticalDatum

transformer = CSRSTransformer(
    s_ref_frame=Reference.ITRF14,
    t_ref_frame=Reference.NAD83CSRS,
    s_coords=CoordType.GEOG,
    t_coords=CoordType.UTM10,
    s_epoch=2002,
    t_epoch=2010,
    s_vd=VerticalDatum.GRS80,
    t_vd=VerticalDatum.HT2_2010v70
)

in_coords = [(-123.365646, 48.428421, 0)]
out_coords = list(transformer(in_coords))
print(out_coords)  # Output: [(472952.3385926245, 5363983.279823124, 18.81151352316209)]
```

## API Reference

### CSRSTransformer

The main class for performing coordinate transformations.

```python
# CSRSTransformer(
#    s_ref_frame: Reference | str,
#    t_ref_frame: Reference | str,
#    s_coords: CoordType | str,
#    t_coords: CoordType | str,
#    s_epoch: float,
#    t_epoch: float,
#    s_vd: VerticalDatum | str = VerticalDatum.GRS80,
#    t_vd: VerticalDatum | str = VerticalDatum.GRS80,
#    epoch_shift_grid: str = "ca_nrc_NAD83v70VG.tif"
# )
```

#### Parameters:

- `s_ref_frame`: Source reference frame
- `t_ref_frame`: Target reference frame
- `s_coords`: Source coordinate type
- `t_coords`: Target coordinate type
- `s_epoch`: Source epoch in decimal year format
- `t_epoch`: Target epoch in decimal year format
- `s_vd`: Source vertical datum
- `t_vd`: Target vertical datum
- `epoch_shift_grid`: Name of the proj grid file used for epoch transformations

### Enums

- `Reference`: Enumeration of supported reference frames
- `CoordType`: Enumeration of supported coordinate types
- `VerticalDatum`: Enumeration of supported vertical datums

## Utility Functions

CSRSPY provides some utility functions to assist with common tasks:

### date_to_decimal_year

Converts a date object to a decimal year representation.

```python
from datetime import date
from csrspy.utils import date_to_decimal_year

d = date(2023, 6, 15)
decimal_year = date_to_decimal_year(d)
print(decimal_year)  # Output: 2023.4520547945206
```

### sync_missing_grid_files

Synchronizes missing PROJ grid files for the Canada area of use. This function should be
called to ensure all necessary grid files are downloaded before using the
`CSRSTransformer` class.

```python
from csrspy.utils import sync_missing_grid_files

sync_missing_grid_files()
```

This function will download any missing grid files required for transformations in the
Canada area. It uses the pyproj library to manage the synchronization process.

## Developer Guide

### Setting Up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/tayden/csrspy.git
   cd csrspy
   ```

2. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Activate the virtual environment:
   ```bash
   poetry shell
   ```

### Running Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

To run tests across multiple Python versions, use tox:

```bash
poetry run tox
```

### Updating the Library

1. Make your changes in the appropriate files.
2. Update tests if necessary.
3. Run the tests to ensure everything is working.
4. Update the version number in `pyproject.toml`.
5. Commit your changes and push to the repository.

### Publishing to PyPI

1. Ensure all tests pass and the version number is updated.
2. Create a new tag with the version number:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```

3. The GitHub Action will automatically build and publish the package to PyPI when a new
   tag is pushed.

## Contributing

Contributions to CSRSPY are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Make your changes and ensure all tests pass.
5. Submit a pull request with a clear description of your changes.

## License

CSRSPY is released under the [MIT License](https://opensource.org/licenses/MIT).
