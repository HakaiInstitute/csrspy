"""Factories for coordinate transformations.

This module provides abstract base classes and concrete implementations for
creating coordinate transformation factories. The factories are used to
generate PROJ strings for various types of transformations, such as Helmert
transformations and vertical grid shifts. Each factory can be used to create
a Transformer object that can perform coordinate transformations based on the
defined PROJ strings.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from pyproj import Transformer

from csrspy.enums import Reference, VerticalDatum


class Factory(ABC):
    """Abstract base class for transformation factories.

    This class defines the interface for creating transformation factories that
    provide a PROJ string for coordinate transformations. Subclasses should
    implement the proj_str property to return the appropriate PROJ string for
    the specific transformation type.

    Attributes:
        proj_str (str): The PROJ string for the transformation.

    Raises:
        NotImplementedError: If the proj_str property is not implemented by a subclass.

    """

    @property
    @abstractmethod
    def proj_str(self) -> str:
        """Returns the PROJ string for the transformation.

        This property should be implemented by subclasses to provide the
        appropriate PROJ string for the specific transformation type.
        """
        raise NotImplementedError

    @property
    def transformer(self) -> Transformer:
        """Returns a Transformer object based on the PROJ string.

        This method creates a Transformer instance using the PROJ string defined
        in the proj_str property. It allows for easy transformation of coordinates
        using the defined transformation parameters.

        Returns:
            Transformer: A Transformer object initialized with the PROJ string.

        """
        return Transformer.from_pipeline(self.proj_str)


@dataclass(frozen=True)
class HelmertFactory(Factory):
    """Factory for creating Helmert transformations.

    This factory provides the PROJ string for Helmert transformations based on
    the specified Helmert parameters. It supports various reference frames
    such as NAD83CSRS, ITRF88, ITRF89, ITRF90, ITRF91, ITRF92, ITRF93, ITRF94,
    ITRF96, ITRF97, ITRF00, ITRF05, ITRF08, ITRF14, and ITRF20.

    Attributes:
        x (float): X translation in meters.
        dx (float): X translation uncertainty in meters.
        y (float): Y translation in meters.
        dy (float): Y translation uncertainty in meters.
        z (float): Z translation in meters.
        dz (float): Z translation uncertainty in meters.
        rx (float): X rotation in milliarcseconds.
        drx (float): X rotation uncertainty in milliarcseconds.
        ry (float): Y rotation in milliarcseconds.
        dry (float): Y rotation uncertainty in milliarcseconds.
        rz (float): Z rotation in milliarcseconds.
        drz (float): Z rotation uncertainty in milliarcseconds.
        s (float): Scale difference in parts per million.
        ds (float): Scale difference uncertainty in parts per million.
        itrf_epoch (float): ITRF epoch year, default is 2010.

    Raises:
        KeyError: If the reference frame is not recognized.
    Usage:
        helmert = HelmertFactory.from_ref_frame(Reference.ITRF14)
        print(helmert.proj_str)

    """

    x: float
    dx: float
    y: float
    dy: float
    z: float
    dz: float
    rx: float
    drx: float
    ry: float
    dry: float
    rz: float
    drz: float
    s: float
    ds: float
    itrf_epoch: float = 2010

    @property
    def proj_str(self) -> str:
        """Returns the PROJ string for Helmert transformation.

        The string is constructed based on the Helmert parameters.

        Returns:
            str: The PROJ string for the Helmert transformation.

        """
        return (
            f"proj=helmert convention=position_vector t_epoch={self.itrf_epoch:.3f} "
            f"x={self.x:.8f} dx={self.dx:.8f} "
            f"y={self.y:.8f} dy={self.dy:.8f} "
            f"z={self.z:.8f} dz={self.dz:.8f} "
            f"rx={self.rx * 1e-3:.8f} drx={self.drx * 1e-3:.8f} "
            f"ry={self.ry * 1e-3:.8f} dry={self.dry * 1e-3:.8f} "
            f"rz={self.rz * 1e-3:.8f} drz={self.drz * 1e-3:.8f} "
            f"s={self.s * 1e-3:.8f} ds={self.ds * 1e-3:.8f}"
        )

    @classmethod
    def from_ref_frame(cls, ref_frame: Reference | str) -> HelmertFactory:
        """Create a Helmert transformation based on the reference frame.

        Args:
            ref_frame (Reference | str): The reference frame for which to create the transformation.

        Returns:
            HelmertFactory: An instance of HelmertFactory with the parameters for the specified reference frame.

        Raises:
            KeyError: If the reference frame is not recognized.

        """
        if ref_frame == Reference.NAD83CSRS:
            return cls(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2010)

        if ref_frame == Reference.ITRF88:
            return cls(
                0.97300,
                0.00000,
                -1.90720,
                0.00000,
                -0.42090,
                0.00000,
                -26.58160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                -7.40000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF89:
            return cls(
                0.96800,
                0.00000,
                -1.94320,
                0.00000,
                -0.44490,
                0.00000,
                -26.48160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                -4.30000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF90:
            return cls(
                0.97300,
                0.00000,
                -1.91920,
                0.00000,
                -0.48290,
                0.00000,
                -26.48160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                -0.90000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF91:
            return cls(
                0.97100,
                0.00000,
                -1.92320,
                0.00000,
                -0.49890,
                0.00000,
                -26.48160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                -0.60000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF92:
            return cls(
                0.98300,
                0.00000,
                -1.90920,
                0.00000,
                -0.50490,
                0.00000,
                -26.48160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                0.80000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF93:
            return cls(
                1.04880,
                0.00290,
                -1.91100,
                -0.00040,
                -0.51550,
                -0.00080,
                -23.67160,
                0.05680,
                3.37990,
                0.93230,
                -11.38920,
                -0.01840,
                -0.40000,
                0.00000,
                2010,
            )

        if ref_frame in {Reference.ITRF94, Reference.ITRF96}:
            return cls(
                0.99100,
                0.00000,
                -1.90720,
                0.00000,
                -0.51290,
                0.00000,
                -26.48160,
                -0.05320,
                -0.00010,
                0.74230,
                -11.24920,
                0.03160,
                0.00000,
                0.00000,
                2010,
            )

        if ref_frame == Reference.ITRF97:
            return cls(
                0.99790,
                0.00069,
                -1.90871,
                -0.00010,
                -0.47877,
                0.00186,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -11.19206,
                0.03133,
                -3.43109,
                -0.19201,
                2010,
            )

        if ref_frame == Reference.ITRF00:
            return cls(
                1.00460,
                0.00069,
                -1.91041,
                -0.00070,
                -0.51547,
                0.00046,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -10.93206,
                0.05133,
                -1.75109,
                -0.18201,
                2010,
            )

        if ref_frame == Reference.ITRF05:
            return cls(
                1.00270,
                0.00049,
                -1.91021,
                -0.00060,
                -0.53927,
                -0.00134,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -10.93206,
                0.05133,
                -0.55109,
                -0.10201,
                2010,
            )

        if ref_frame == Reference.ITRF08:
            return cls(
                1.00370,
                0.00079,
                -1.91111,
                -0.00060,
                -0.54397,
                -0.00134,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -10.93206,
                0.05133,
                0.38891,
                -0.10201,
                2010,
            )

        if ref_frame == Reference.ITRF14:
            return cls(
                1.00530,
                0.00079,
                -1.90921,
                -0.00060,
                -0.54157,
                -0.00144,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -10.93206,
                0.05133,
                0.36891,
                -0.07201,
                2010,
            )

        if ref_frame == Reference.ITRF20:
            return cls(
                1.00390,
                0.00079,
                -1.90961,
                -0.00070,
                -0.54117,
                -0.00124,
                -26.78138,
                -0.06667,
                0.42027,
                0.75744,
                -10.93206,
                0.05133,
                -0.05109,
                -0.07201,
                2010,
            )

        raise KeyError(ref_frame)


@dataclass(frozen=True)
class VerticalGridShiftFactory(Factory):
    """Factory for creating vertical grid shift transformations.

    This factory provides the PROJ string for vertical grid shifts based on the
    specified vertical datum. It supports different vertical datums such as
    CGG2013A, CGG2013, and HT2_2010v70.

    Attributes:
        grid_shift (VerticalDatum): The vertical datum for the grid shift.

    Raises:
        KeyError: If the grid shift type is not recognized.

    """

    grid_shift: VerticalDatum

    @property
    def grid_shift_file(self) -> str:
        """Returns the grid shift file name based on the vertical datum.

        The file names are predefined for each vertical datum.

        Raises:
            KeyError: If the grid shift is not recognized.

        Returns:
            str: The file name of the grid shift.

        """
        if self.grid_shift == VerticalDatum.CGG2013A:
            return "ca_nrc_CGG2013an83.tif"
        if self.grid_shift == VerticalDatum.CGG2013:
            return "ca_nrc_CGG2013n83.tif"
        if self.grid_shift == VerticalDatum.HT2_2010v70:
            return "ca_nrc_HT2_2010v70.tif"
        err_msg = f"Unknown grid shift type: {self.grid_shift}"
        raise KeyError(err_msg)

    @property
    def proj_str(self) -> str:
        """Returns the PROJ string for vertical grid shift transformation.

        The string is constructed based on the grid shift type.

        Returns:
            str: The PROJ string for the vertical grid shift transformation.

        """
        if self.grid_shift is VerticalDatum.GRS80:
            return "+proj=noop"
        return f"+inv +proj=vgridshift +grids={self.grid_shift_file} +multiplier=1"
