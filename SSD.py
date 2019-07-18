import numpy as np
from PIL import Image


def my_ssd(left_image, right_image, kernel, max_offset,compostion):
    left_image = Image.open(left_image).convert('L')
    left = np.asarray(left_image)
    right_image = Image.open(right_image).convert('L')
    right = np.asarray(right_image)
    w, h = right_image.size
    depth = np.zeros((w, h), np.uint8)
    depth.shape = h, w
    kernel_half = int(kernel/2)
    offset_adjust = 255 / max_offset
    for i in range(0,len(compostion)):
        for j in range(0, len(compostion[i])):
            if compostion[i][j][0]<(h-kernel_half)& kernel_half < compostion[i][j][0]& compostion[i][j][1]<(w-kernel_half)& kernel_half < compostion[i][j][1]:
                ssd_reserved = 65534
                best_offset = 0
                for offset in range(max_offset):
                    ssd = 0
                    for v in range(-kernel_half, kernel_half):
                        for u in range(-kernel_half, kernel_half):
                            ssd_temp = int(left[(compostion[i][j][0] + v), (compostion[i][j][1] + u)]) - int(right[(compostion[i][j][0] + v), ((compostion[i][j][1] + u) - offset)])
                            ssd += ssd_temp * ssd_temp
                    if ssd < ssd_reserved:
                        ssd_reserved = ssd
                        best_offset = offset
                depth[compostion[i][j][0], compostion[i][j][1]] = best_offset * offset_adjust

    Image.fromarray(depth).save('depth.png')
