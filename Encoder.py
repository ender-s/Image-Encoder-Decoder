import cv2
import numpy as np
import random
from Helper import Helper

# 256 different ascii codes.
# each pixel consists of 3 color intensity values (1 for R, 1 for G, and 1 for B). --> 3-digit number
# (color intensity value --> an integer value ranging from 0 to 255)
# at least 7 different color intensity values to represent at least 256 different ascii codes (6**3 = 216, 7**3 = 343)
# thus, we will work on base-7 number system
# choose 7 random different color intensity value, sort them in ascending order
# map each of them to numbers from 0 to 6 (since we work on base-7)
# since color intensity values are chosen randomly, the same input yields so many different image outputs.
# decoder can resolve each one of them correctly since it will read all different color intensity values and sort them in ascending order
# just before mapping them to numbers from 0 to 6

class Encoder:
    def __init__(self):
        self.BASE = 7

    def encode(self, data, image_output_path):
        additional_space = self.BASE // 3
        if self.BASE % 3 != 0:
            additional_space += 1
        
        size = len(data) + additional_space # additional space for allocating space to introduce all color intensity values
        n, m = Helper.find_two_closest_factors(size, random_order = True)
        color_intensity_values = Helper.choose_different_random_numbers(0, 255, self.BASE, sorted = True)
        
        intensity_values_to_be_shuffled = color_intensity_values.copy()
        random.shuffle(intensity_values_to_be_shuffled)
        
        cont_flag = True
        i, j, k = 0, 0, 0
        index = i*m*k + j*k + k
        
        matrix = np.zeros((n, m, 3))
        
        while cont_flag and i < n:
            j = 0
            while cont_flag and j < m:
                k = 0
                while cont_flag and k < 3:
                    index = i*m*3 + j*3 + k
                    if index >= self.BASE:
                        cont_flag = False
                        remainder = self.BASE % 3
                        if remainder != 0:
                            for k in range(remainder, 3):
                                matrix[i][j][k] = random.choice(color_intensity_values)
                        continue

                    matrix[i][j][k] = intensity_values_to_be_shuffled[index]
                    
                    k += 1
                j += 1
            i += 1

        counter = 0
        for i in range(n):
            for j in range(m):
                if (i*m + j) < additional_space:
                    continue
                current_char = data[counter]
                encoded = Helper.decimal_to_base_n(self.BASE, ord(current_char))

                for k in range(3):
                    matrix[i][j][2 - k] = color_intensity_values[int(encoded[k])]
                
                counter += 1
        
        cv2.imwrite(image_output_path, matrix)
 