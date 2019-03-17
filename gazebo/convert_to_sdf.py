import sys
import numpy as np

def perpendicular_vector(v):
    if v[0] == 0 and v[1] == 0:
        if v[2] == 0:
            # v is Vector(0, 0, 0)
            raise ValueError('zero vector')

        # v is Vector(0, 0, v.z)
        return np.array([0, 1, 0])

    return np.array([-v[1], v[0], 0])

def compute_roll_pitch_yaw(v, px, py, pz):
    yaw = np.arctan2(v[0], -v[1])
    pitch = np.arctan2(np.sqrt(v[0]**2 + v[1]**2), v[2])
    return 0, pitch, yaw

def main():
    if len(sys.argv) != 2:
        print("Usage : python3 {} <filename>".format(sys.argv[0]))
        exit(1)

    filename = sys.argv[1]

    cylinder_model = \
    "    <link name=\"{}\">\n \
        <collision name=\"{}\">\n \
            <pose>{} {} {} {} {} {}</pose>\n \
            <geometry>\n \
            <cylinder>\n \
                <radius>{}</radius>\n \
                <length>{}</length>\n \
            </cylinder>\n \
            </geometry>\n \
        </collision>\n \
        <visual name=\"{}\">\n \
            <pose>{} {} {} {} {} {}</pose>\n \
            <geometry>\n \
            <cylinder>\n \
                <radius>{}</radius>\n \
                <length>{}</length>\n \
            </cylinder>\n \
            </geometry>\n \
            <material>\n \
                <script>\n \
                    <uri>file://media/materials/scripts/gazebo.material</uri>\n \
                    <name>Gazebo/Green</name>\n \
                </script>\n \
            </material>\n \
        </visual>\n \
        </link>\n"

    sphere_model = \
    "    <link name=\"{}\">\n \
        <collision name=\"{}\">\n \
            <pose>{} {} {} {} {} {}</pose>\n \
            <geometry>\n \
            <sphere>\n \
                <radius>{}</radius>\n \
            </sphere>\n \
            </geometry>\n \
        </collision>\n \
        <visual name=\"{}\">\n \
            <pose>{} {} {} {} {} {}</pose>\n \
            <geometry>\n \
            <sphere>\n \
                <radius>{}</radius>\n \
            </sphere>\n \
            </geometry>\n \
            <material>\n \
                <script>\n \
                    <uri>file://media/materials/scripts/gazebo.material</uri>\n \
                    <name>Gazebo/Red</name>\n \
                </script>\n \
            </material>\n \
        </visual>\n \
        </link>\n"

    output = \
    "<?xml version=\"1.0\" ?>\n \
    <sdf version=\"1.6\">\n \
    <model name=\"apple_tree\">\n \
        <static>true</static>\n"

    # Add branches and fruits to model
    with open(filename, "r") as f:
        nb_branches = int(f.readline())
        for i in range(nb_branches):
            line = f.readline()
            # # coords = (px, py, pz, vx, vy, vz, R)
            # coords = line.split()
            # coords = [float(s) for s in coords]
            # link_name = "branche{}".format(i+1)
            # collision_name = "b-c-{}".format(i+1)
            # visual_name = "b-v-{}".format(i+1)
            # # Position
            # x, y, z = coords[0], coords[1], coords[2]
            # # Radius
            # R = coords[6]
            # # Vecteur directeur
            # vx, vy, vz = coords[3], coords[4], coords[5]
            # v = np.array([vx, vy, vz])
            # # Longueur
            # length = np.linalg.norm(v)

            # roll, pitch, yaw = compute_roll_pitch_yaw(v, x, y, z)

            # output += cylinder_model.format(link_name, collision_name, x, y, z, roll, pitch, yaw, R,
            #                              length, visual_name, x, y, z, roll, pitch, yaw, R, length)
        
        # Trunk
        output += cylinder_model.format("b1", "c1", 0.05, 0.05, 1, 0, 0, 0, 0.01,
                                          2, "v1", 0.05, 0.05, 1, 0, 0, 0, 0.01, 2)
        
        
        nb_fruits = int(f.readline())
        for i in range(nb_fruits):
            line = f.readline()
            coords = line.split()
            coords = [float(s) for s in coords]
            link_name = "fruit{}".format(i+1)
            collision_name = "f-c-{}".format(i+1)
            visual_name = "f-v-{}".format(i+1)
            # Position
            x, y, z = coords[0], coords[1], coords[2]
            # Radius
            R = coords[6]
            # Vecteur directeur
            # vx, vy, vz = coords[3], coords[4], coords[5]
            yaw, pitch, roll = 0, 0, 0 # On s'en sert pas pour la sphere
            
            output += sphere_model.format(link_name, collision_name, x, y, z, roll, pitch, yaw, R,
                                         visual_name, x, y, z, roll, pitch, yaw, R)

    # Close model
    output += \
    "  </model>\n \
    </sdf>\n"

    model_path = "/home/loic/.gazebo/models/apple_tree/model.sdf"

    # Writing output to file
    with open(model_path, "w+") as f:
        f.write(output)

if __name__ == "__main__":
    main()