import re

atomic_masses = {
    "H": 1.008,
    "O": 15.999,
    "S": 32.066,
    "Na": 22.990,
    "Cl": 35.453,
    "K": 39.098,
}


def molecular_mass(molecule):

    atoms = re.findall(r"([A-Za-z]+)(\d*)", molecule)
    mass = sum(
        atomic_masses[atom] * (int(count) if count else 1) for atom, count in atoms
    )
    return mass


molecules = ["H2-S-O4", "H2-O", "Na-Cl", "H-Cl", "K-Cl"]

molar_masses = sorted(
    ((mol, molecular_mass(mol)) for mol in molecules), key=lambda x: x[1]
)

for mol, mass in molar_masses:
    print(f"{mol.ljust(10)} {mass:.3f}")
