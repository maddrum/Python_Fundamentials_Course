import re

surface_pattern = r'[^\da-zA-Z]+'
core_pattern = r'^([^\da-zA-Z]+)([\d_]+)([A-Za-z]+)([\d_]+)([^\da-zA-Z]+)$'
surface_regex = re.compile(surface_pattern)
core_regex = re.compile(core_pattern)

surface1 = input()
mantle1 = input()
core = input()
mantle2 = input()
surface2 = input()
mantle1 = mantle1.replace('_', "")
mantle2 = mantle2.replace('_', "")
if len(mantle1) == 0:
    mantle1 = 0
if len(mantle2) == 0:
    mantle2 = 0

try:
    mantle1 = int(mantle1)
except:
    print("Invalid")
    exit()
try:
    mantle2 = int(mantle2)
except:
    print("Invalid")
    exit()

surface1_check = surface_regex.search(surface1)
surface2_check = surface_regex.search(surface2)
core_check = core_regex.search(core)
if surface1_check is None or surface2_check is None:
    print("Invalid")
    exit()
len_core = len(core_check.group(3))
print("Valid")
print(len_core)
