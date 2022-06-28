import cv2
import io
import numpy as np
from Helper import Helper

class Decoder:
    def read_pixel_matrix(self, path):
        return np.asarray(cv2.imread(path))

    def write_pixel_matrix_as_image(self, path, matrix):
        cv2.imwrite(path, matrix)

    def detect_different_color_intensity_values(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        # n x m matrix
        
        color_intensity_values = []
        
        for i in range(n): # row loop
            for j in range(m): # column loop
                pixel = matrix[i][j]
                for k in range(len(pixel)):
                    color_intensity_value = pixel[k]
                    if not color_intensity_value in color_intensity_values:
                        color_intensity_values.append(color_intensity_value)
        
        color_intensity_values.sort()
        return color_intensity_values

    def resolve_data(self, matrix, map):
        n = len(matrix)
        m = len(matrix[0])
        # n x m matrix
                
        data_io = io.StringIO()
        
        base_n = len(map.keys())
        
        additional_space = base_n // 3
        if base_n % 3 != 0:
            additional_space += 1
        
        
        for i in range(n):
            for j in range(m):
                if (i*m + j) < additional_space:
                    continue
                
                pixel = matrix[i][j]
                number_str = ""

                for k in range(len(pixel)):
                    number = int(pixel[k])
                    number_value = map[number]
                    number_str += str(number_value)

                number_str = self.reverse_str(number_str)
                try:
                    decimal = Helper.base_n_to_decimal(base_n, number_str)
                    data_io.write(chr(decimal))
                except:
                    data_io.write(chr(0))
                    
        
        return data_io.getvalue()

    def reverse_str(self, input):
        result = ''
        counter = len(input) - 1
        while counter >= 0:
            result += input[counter]
            counter -= 1
        
        return result

    def generate_map(self, color_intensity_values):
        n = len(color_intensity_values)
        map = {}
        for index in range(n):
            map[color_intensity_values[index]] = index
        return map
    
    def decode(self, path):
        matrix = self.read_pixel_matrix(path)
        color_intensity_values = self.detect_different_color_intensity_values(matrix)
        return self.resolve_data(matrix, self.generate_map(color_intensity_values))
