import pprint

pprint.pprint([{"bin": bin(i), "hex": hex(i), "oct": oct(i), "dec": i} for i in range(16)])
