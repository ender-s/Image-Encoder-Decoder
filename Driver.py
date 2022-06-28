import os
import base64
from Encoder import Encoder
from Decoder import Decoder

class Driver:
    def __init__(self, args):
        self.operation = args.operation
        self.input = args.input
        self.output = args.output
        self.use_base64 = args.use_base64

        if os.path.exists(self.output):
            raise Exception(f"Path {self.output} already exists!")

        self.encoder = Encoder()
        self.decoder = Decoder()

    def start_execution(self):
        if self.operation == 'encode':
            self.execute_encode_operation()
        else:
            self.execute_decode_operation()

    def execute_decode_operation(self):
        decoded = self.decoder.decode(self.input)
        if self.use_base64:
            mode = 'wb'
            data_to_be_written = base64.b64decode(decoded)

        else:
            mode = 'wb'
            try:
                data_to_be_written = decoded.encode("utf-8")
            except:
                mode = 'w'
                data_to_be_written = decoded

        with open(self.output, mode) as f:
            f.write(data_to_be_written)


    def execute_encode_operation(self):
        with open(self.input, 'rb') as f:
            binary_input_data = f.read()

        if self.use_base64:
            input_data = base64.b64encode(binary_input_data).decode('utf-8')
        else:
            input_data = binary_input_data.decode('utf-8')

        self.encoder.encode(input_data, self.output)
        
        