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
    print("the length of composition is ",len(compostion) )
    temp_string = "the size of image is: row={} and column={}."
    print(temp_string.format(h , w))
    temp_mean = np.zeros(len(compostion))
    temp_var = np.zeros(len(compostion))
    temp_depth = []
    for i in range(0,len(compostion)-8):
        temp_depth.append([])
        print(len(compostion[i]))
        for j in range(0, len(compostion[i])):
            if compostion[i][j][0]<(h-kernel_half)and kernel_half < compostion[i][j][0]and compostion[i][j][1]<(w-kernel_half)and kernel_half < compostion[i][j][1]:
                #print("test")
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
                temp_depth[i].append([])
                temp_depth[i][j] = best_offset
        # print(temp_depth[i])
        temp_mean[i] = np.mean(temp_depth[i])
        temp_var[i] = np.var(temp_depth[i])
        print(temp_mean[i])
        print(temp_var[i])
    print("The code is before writing image.")
    Image.fromarray(depth).save('depth.png')
    print("very thing is done.")
    return [temp_mean, temp_var]

