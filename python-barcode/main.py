from barcode import EAN13
from barcode.writer import ImageWriter
num_of_barcode = int(input("How many Barcodes you need?"))
numbers =range(num_of_barcode)
for i in numbers:
    id = input("Give 12-Digit numbers for your barcode id: ")
    my_code = EAN13( id , writer=ImageWriter)
    name = input("Give the name to save barcodes: ")
    my_code.save(name)
