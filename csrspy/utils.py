import logging
from datetime import date
from typing import TypeVar

import pyproj.sync

T = TypeVar("T")

logger = logging.getLogger(__name__)


def date_to_decimal_year(d: date) -> float:
    """
    Convert a date object to a decimal year representation.

    Args:
        d (date): The date to convert.

    Returns:
        float: The decimal year representation of the input date.
    """
    year_part = d - date(d.year, 1, 1)
    year_length = date(d.year + 1, 1, 1) - date(d.year, 1, 1)
    return d.year + year_part / year_length


def sync_missing_grid_files():
    """
    Synchronize missing PROJ grid files for the Canada area of use.

    This function checks for missing grid files and downloads them from the PROJ
    endpoint if necessary. It uses the pyproj library to manage the synchronization.
    """
    target_directory = pyproj.sync.get_user_data_dir(True)
    endpoint = pyproj.sync.get_proj_endpoint()
    grids = pyproj.sync.get_transform_grid_list(area_of_use="Canada")

    if len(grids):
        logger.info("Syncing PROJ grid files.")

    for grid in grids:
        filename = grid["properties"]["name"]
        pyproj.sync._download_resource_file(
            file_url=f"{endpoint}/{filename}",
            short_name=filename,
            directory=target_directory,
            sha256=grid["properties"]["sha256sum"],
        )
