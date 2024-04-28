import sys
import os

class Atom:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

def calculate_bounding_box_volume(atoms):
    min_x = min(atom.x for atom in atoms)
    max_x = max(atom.x for atom in atoms)
    min_y = min(atom.y for atom in atoms)
    max_y = max(atom.y for atom in atoms)
    min_z = min(atom.z for atom in atoms)
    max_z = max(atom.z for atom in atoms)
    volume = (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
    return volume

def main(filename):
    atoms = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('ATOM'):
                parts = line.split()
                x, y, z = map(float, parts[5:8])
                atoms.append(Atom(x, y, z))
    
    bounding_box_volume = calculate_bounding_box_volume(atoms)
    file_name = os.path.basename(filename)
    print(f"Bounding box volume for {file_name}:\t{bounding_box_volume}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python findbbox.py molecule.pdbqt")
        sys.exit(1)
    main(sys.argv[1])

