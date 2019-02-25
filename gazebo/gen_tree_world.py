import numpy as np
import sys

if (len(sys.argv) != 5):
	print("Usage: python3 ScriptGenerateTree.py <col_space> <row_space> <nb_rows> <nb_cols>")
	exit(1)

col_space = float(sys.argv[1])
row_space = float(sys.argv[2])
nb_rows = int(sys.argv[3])
nb_cols = int(sys.argv[4])

x_coord = np.arange(-nb_cols * col_space / 2, nb_cols * col_space / 2, col_space)
y_coord = np.arange(-nb_rows * row_space / 2, nb_rows * row_space / 2, row_space)

# Modèle d'abre
tree ="     <model name=\"tree{}\">\n \
        <include>\n \
            <static>true</static>\n \
            <uri>model://apple_tree</uri>\n \
            <pose>{} {} 0 0 0 0</pose>\n \
            <box>\n \
                <size>10 10 1</size>\n \
            </box>\n \
        </include>\n \
    </model>\n"

output = "<?xml version=\"1.0\" ?>\n \
<sdf version=\"1.6\">\n \
  <world name=\"default\">\n \
\n \
    <!-- A global light source -->\n \
    <include>\n \
      <uri>model://sun</uri>\n \
    </include>\n \
\n \
    <!-- A ground plane -->\n \
    <include>\n \
      <uri>model://ground_plane</uri>\n \
    </include>\n"

# Compteur pour le nom des arbres
i_tree = 0

# Adding trees
for x in x_coord:
	for y in y_coord:
		x_offset = np.random.ranf() - 0.5
		y_offset = np.random.ranf() - 0.5
		output += tree.format(i_tree, x + x_offset, y + y_offset)
		i_tree += 1

output += "  </world>\n \
</sdf>"

# Writing output to file
with open("tree-world.world", "w+") as f:
	f.write(output)
