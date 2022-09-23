from typing import List, Dict, Set
import textwrap
from plasmapy.utils.decorators import modify_docstring

_classification_categories = {
    "lepton",
    "antilepton",
    "fermion",
    "boson",
    "antibaryon",
    "baryon",
    "neutrino",
    "antineutrino",
    "matter",
    "antimatter",
    "stable",
    "unstable",
    "charged",
    "uncharged",
}

_periodic_table_categories = {
    "nonmetal",
    "metal",
    "alkali metal",
    "alkaline earth metal",
    "metalloid",
    "transition metal",
    "post-transition metal",
    "halogen",
    "noble gas",
    "actinide",
    "lanthanide",
}

_atomic_property_categories = {"element", "isotope", "ion"}

_specific_particle_categories = {"electron", "positron", "proton", "neutron"}

valid_categories = (
    _periodic_table_categories
    | _classification_categories
    | _atomic_property_categories
    | _specific_particle_categories
)


class _SetFormatter:
    """
    ABCD
    """
    def __init__(self, set: Set[str], indentation = 5):
        self.set = sorted(set)
        self.str = ""
        self.indentation =indentation
        for i, element in enumerate(self.set):
            if i == len(self.set) - 1:
                self.str += f"and ``'{element}'``."
            else:
                self.str += f"``'{element}'``, "

    def __format__(self, format_spec) -> str:
        tab = '\t'
        return f"\n{tab*self.indentation}".join(textwrap.wrap(self.str, 72))

class Classy:
    """
        A class for an individual particle or antiparticle.

        Parameters
        ----------
        argument : |particle-like|
            A string representing a particle, element, isotope, or ion; an
            integer representing the atomic number of an element; or a
            |Particle|.

        mass_numb : integer, optional, |keyword-only|
            The mass number of an isotope.

        Z : integer, optional, |keyword-only|
            The |charge number| of an ion or neutral atom.

        Raises
        ------
        `TypeError`
            For when any of the arguments or keywords is not of the required
            type.

        `~plasmapy.particles.exceptions.InvalidParticleError`
            Raised when the particle input does not correspond to a valid
            particle or is contradictory.

        `~plasmapy.particles.exceptions.InvalidElementError`
            For when an attribute is being accessed that requires
            information about an element, but the particle is not an
            element, isotope, or ion.

        `~plasmapy.particles.exceptions.InvalidIsotopeError`
            For when an attribute is being accessed that requires
            information about an isotope or nuclide, but the particle is not
            an isotope (or an ion of an isotope).

        `~plasmapy.particles.exceptions.ChargeError`
            For when either the
            `~plasmapy.particles.particle_class.Particle.charge` or
            `~plasmapy.particles.particle_class.Particle.charge_number`
            attributes is being accessed but the charge information for the
            particle is not available.

        `~plasmapy.particles.exceptions.ParticleError`
            Raised for attempts at converting a
            |Particle| object to a `bool`.

        See Also
        --------
        ~plasmapy.particles.particle_class.CustomParticle
        ~plasmapy.particles.particle_class.DimensionlessParticle
        ~plasmapy.particles.particle_collections.ParticleList
        ~plasmapy.particles.particle_class.valid_categories

        Notes
        -----
        Valid particle categories include:
        {valid_categories}


        Examples
        --------
        Particles may be defined using a wide variety of aliases:

        >>> proton = Particle('p+')
        >>> electron = Particle('e-')
        >>> neutron = Particle('neutron')
        >>> deuteron = Particle('D', Z=1)
        >>> triton = Particle('T+')
        >>> alpha = Particle('He', mass_numb=4, Z=2)
        >>> positron = Particle('positron')
        >>> hydrogen = Particle(1)  # atomic number

        The `~plasmapy.particles.particle_class.Particle.symbol` attribute
        returns the particle's symbol in the standard form.

        >>> positron.symbol
        'e+'

        The `~plasmapy.particles.particle_class.Particle.element`,
        `~plasmapy.particles.particle_class.Particle.isotope`, and
        `~plasmapy.particles.particle_class.Particle.ionic_symbol` attributes
        provide the symbols for each of these different types of particles.

        >>> proton.element
        'H'
        >>> alpha.isotope
        'He-4'
        >>> deuteron.ionic_symbol
        'D 1+'

        The `~plasmapy.particles.particle_class.Particle.ionic_symbol`
        attribute works for neutral atoms if charge information is available.

        >>> deuterium = Particle("D", Z=0)
        >>> deuterium.ionic_symbol
        'D 0+'

        If the particle doesn't belong to one of those categories, then
        these attributes are `None`.

        >>> positron.element is None
        True

        The attributes of a |Particle| instance may be used to test whether
        or not a particle is an element, isotope, or ion.

        >>> True if positron.element else False
        False
        >>> True if deuterium.isotope else False
        True
        >>> True if Particle('alpha').is_ion else False
        True

        Many of the attributes provide physical properties of a particle.

        >>> electron.charge_number
        -1
        >>> proton.spin
        0.5
        >>> alpha.atomic_number
        2
        >>> deuteron.mass_number
        2
        >>> deuteron.binding_energy.to('MeV')
        <Quantity 2.224... MeV>
        >>> alpha.charge
        <Quantity 3.20435...e-19 C>
        >>> neutron.half_life
        <Quantity 881.5 s>
        >>> Particle('C-14').half_life.to(u.year)
        <Quantity 5730. yr>
        >>> deuteron.electron_number
        0
        >>> alpha.neutron_number
        2

        If a |Particle| instance represents an elementary particle, then
        the unary ``~`` (invert) operator may be used to return the
        particle's antiparticle.

        >>> ~positron
        Particle("e-")

        A |Particle| instance may be used as the first argument to
        |Particle|.

        >>> iron = Particle('Fe')
        >>> iron == Particle(iron)
        True
        >>> Particle(iron, mass_numb=56, Z=6)
        Particle("Fe-56 6+")

        If the previously constructed |Particle| instance represents an
        element, then the ``Z`` and ``mass_numb`` arguments may be used to
        specify an ion or isotope.

        >>> iron = Particle('Fe')
        >>> Particle(iron, Z=1)
        Particle("Fe 1+")
        >>> Particle(iron, mass_numb=56)
        Particle("Fe-56")

        Adding particles together will create a
        `~plasmapy.particles.particle_collections.ParticleList`, which is
        a list-like collection of particles.

        >>> proton + 2 * electron
        ParticleList(['p+', 'e-', 'e-'])

        The ``>`` operator can be used with |Particle| and/or
        `~plasmapy.particles.particle_collections.ParticleList` objects to
        return the nuclear reaction energy.

        >>> deuteron + triton > alpha + neutron
        <Quantity 2.81810898e-12 J>

        The `~plasmapy.particles.particle_class.Particle.categories` attribute
        and `~plasmapy.particles.particle_class.Particle.is_category` method
        may be used to find and test particle membership in categories.


        Please refer to
        `~plasmapy.particles.particle_class.Particle.is_category` for more
        details, including a list of all valid particle categories.

        """

    __doc__ = __doc__.format(valid_categories=_SetFormatter(set=valid_categories))


print(Classy.__doc__)




