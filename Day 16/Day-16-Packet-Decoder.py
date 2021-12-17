

class Packet():
    def __init__(self):
        self.binary = self.convertHextoBin()
        
    def convertHextoBin(self):
        with open("Day-16-Input.txt") as file:
            input = file.read()
        conversion = ''.join(f'{int(char, 16):04b}' for char in input)
        return conversion
