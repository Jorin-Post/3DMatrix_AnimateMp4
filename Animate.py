import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, PillowWriter

# Path to ffmpeg.exe if only .gif is needed code can run without following line
plt.rcParams["animation.ffmpeg_path"] = "C:/Windows/FFMpeg/ffmpeg.exe"

metadata = dict(title="Movie", artist="codinglikemad")
# writer = PillowWriter(fps=15, metadata=metadata)                      # PillowWriter = for .gif
writer = FFMpegWriter(fps=15, metadata=metadata)  # FFMpegWriter = for .mp4
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

depth_cube = np.zeros((10, 10, 10), dtype="uint8")
depth_cube[1, :, :] = 0
coller_space = np.where(depth_cube == 1, "lightsalmon", "None")


def func():
    return np.random.randint(1, 9, size=3)


# with writer.saving(fig, "exp3d.gif", 100):
with writer.saving(fig, "exp3d.mp4", 100):
    for tval in range(30):
        val = func()
        # print(val)
        depth_cube[val[0], val[1], val[2]] = 2
        coller_space[val[0], val[1], val[2]] = "lime"
        ax.voxels(depth_cube, facecolors=coller_space, edgecolor="k")
        writer.grab_frame()
        plt.cla()
