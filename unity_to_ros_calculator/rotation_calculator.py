from scipy.spatial.transform import Rotation as R
import numpy as np
import matplotlib.pyplot as plt

def plot_rotated_axes(ax, r, name=None, offset=(0, 0, 0), scale=1):
    colors = ("#FF6666", "#005533", "#1199EE")  # Colorblind-safe RGB
    loc = np.array([offset, offset])
    for i, (axis, c) in enumerate(zip((ax.xaxis, ax.yaxis, ax.zaxis),
                                      colors)):
        axlabel = axis.axis_name
        axis.set_label_text(axlabel)
        axis.label.set_color(c)
        axis.line.set_color(c)
        axis.set_tick_params(colors=c)
        line = np.zeros((2, 3))
        line[1, i] = scale
        line_rot = r.apply(line)
        line_plot = line_rot + loc
        ax.plot(line_plot[:, 0], line_plot[:, 1], line_plot[:, 2], c)
        text_loc = line[1]*1.2
        text_loc_rot = r.apply(text_loc)
        text_plot = text_loc_rot + loc[0]
        ax.text(*text_plot, axlabel.upper(), color=c,
                va="center", ha="center")
    ax.text(*offset, name, color="k", va="center", ha="center",
            bbox={"fc": "w", "alpha": 0.8, "boxstyle": "circle"})
    
def unity_to_ros(unity_coord):
    # The input unity_coord should be a NumPy array of shape (3,)
    # Convert Unity coordinates (X, Y, Z) to ROS coordinates (X, Y, Z)
    # by applying a rotation.

    #Convert from deg2rad
    
    # Swap the X and Z axes (ROS: X forward, Z up; Unity: X right, Z forward)
    ros_coord_swapped = np.array([unity_coord[2], unity_coord[1], unity_coord[0]])
    
    # Create a rotation object for rotating along the X-axis by -90 degrees
    rotation_x = R.from_euler('x', -90, degrees=True)
    
    # Now apply this rotation to the swapped coordinate
    ros_coord = rotation_x.apply(ros_coord_swapped)

    return ros_coord


if __name__=='__main__':
    # Use following array to give orientation in Unity Coordinate frame [deg]
    orientation_in_unity_deg = np.array([0.964224599, -1.58746422, -0.013700835])

    r0 = R.identity()
    r_sensor = np.array([55.246, -90.955, -0.785])
    r_sensor_ros = unity_to_ros(np.radians(r_sensor))
    print(r_sensor_ros)
    
    ax = plt.figure().add_subplot(projection="3d", proj_type="ortho")
    plot_rotated_axes(ax, r0, name="r0", offset=(0, 0, 0))
    plot_rotated_axes(ax, R.from_euler("xyz", r_sensor_ros), name="r_s", offset=(3, 0, 0))
    _ = ax.annotate(
        "ROS Convention: Identity Rotation\n"
        "Sensor Orientation: Intrinsic Euler Rotation (ZYX)\n",
        xy=(0.6, 0.7), xycoords="axes fraction", ha="left"
    )
    ax.set(xlim=(-1.25, 6.25), ylim=(-1.25, 1.25), zlim=(-1.25, 1.25))
    ax.set(xticks=range(-1, 8), yticks=[-1, 0, 1], zticks=[-1, 0, 1])
    ax.set_aspect("equal", adjustable="box")
    ax.figure.set_size_inches(6, 5)
    plt.tight_layout()
    plt.show()