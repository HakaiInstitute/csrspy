# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CSRSPY is a Python library for coordinate transformations between ITRF realizations and NAD83 (CSRS). It handles coordinate type conversions, epoch transformations, and vertical datum shifts for the Canada area of use.

## Development Commands

### Dependencies and Environment
- **Install dependencies**: `uv sync`
- **Install with dev dependencies**: `uv sync --extra dev`
- **Activate virtual environment**: `source .venv/bin/activate`
- **Sync PROJ grid files**: `pyproj sync --area-of-use=Canada` (required before running tests)

### Testing
- **Run tests**: `uv run pytest`
- **Run tests across Python versions**: `uv run tox`
- **Individual test**: `uv run pytest tests/test_main.py::test_function_name`

### Code Quality
- **Lint code**: `uv run ruff check`
- **Format code**: `uv run ruff format`

### Build and Publish
- **Build package**: `uv build`
- **Publish**: Done via GitHub Actions when tags are pushed

## Architecture

### Core Components

**CSRSTransformer** (`main.py`): Main transformation class that orchestrates coordinate transformations by composing multiple transformation steps. Uses a strategy pattern with `_ToNAD83` and `_FromNAD83` classes.

**Transformation Pipeline**: All transformations go through NAD83(CSRS) as an intermediate step:
1. Input coordinates → ECEF GRS80 (cartesian)
2. ECEF GRS80 → NAD83(CSRS) via Helmert transform
3. Epoch transformation (if needed) using deformation grids
4. Convert back to geographic coordinates
5. Vertical datum shift (ellipsoidal ↔ orthometric heights)
6. Final coordinate type conversion

**HelmertFactory** (`factories.py`): Creates Helmert transformations with predefined parameters for each ITRF realization. Parameters are hardcoded from official sources.

**VerticalGridShiftFactory** (`factories.py`): Handles vertical datum transformations using PROJ grid files (CGG2013, CGG2013A, HT2_2010v70).

### Key Design Patterns

- **Factory Pattern**: Used for creating transformers with predefined parameters
- **Strategy Pattern**: `_ToNAD83` vs `_FromNAD83` handle forward/inverse transformations
- **Pipeline Pattern**: Transformations are chained in sequence using pyproj transformers

### Dependencies

- **pyproj**: Core transformation engine and PROJ grid file management
- **uv**: Dependency management and packaging
- **pytest**: Testing framework
- **tox**: Multi-version testing
- **ruff**: Linting and formatting

## Important Notes

### PROJ Grid Files
Grid files for Canada must be synchronized before running transformations or tests. This is automatically done in tox but must be run manually during development.

### Coordinate System Validation
The library enforces compatibility rules between reference frames and vertical datums (e.g., ITRF frames must use GRS80 ellipsoid).

### Testing Strategy
Tests use parametrized test cases with reference values from official NRCan tools (TRX and GPS-H) to ensure accuracy.