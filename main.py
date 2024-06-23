from functools import reduce
from sys import argv

from redeal import *

with open(argv[1]) as f: contents = f.read().strip().split('\n')

predeal = {
    "N": contents.pop(0), 
    "E": contents.pop(0), 
    "S": contents.pop(0), 
    "W": contents.pop(0), 
}

restrictions = {
    "N": eval('Shape("' + contents
        .pop(0)
        .replace(' ','')
        .replace('+','") + Shape("')
        .replace('-','") - Shape("') + '")'), 
    "E": eval('Shape("' + contents
        .pop(0)
        .replace(' ','')
        .replace('+','") + Shape("')
        .replace('-','") - Shape("') + '")'), 
    "S": eval('Shape("' + contents
        .pop(0)
        .replace(' ','')
        .replace('+','") + Shape("')
        .replace('-','") - Shape("') + '")'), 
    "W": eval('Shape("' + contents
        .pop(0)
        .replace(' ','')
        .replace('+','") + Shape("')
        .replace('-','") - Shape("') + '")'), 
}

ranges = {
    "N": reduce(lambda x, y: x + y, 
          [[int(_)] if '-' not in _ else 
          list(range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)) 
          for _ in contents.pop(0).split(' ')]), 
    "E": reduce(lambda x, y: x + y, 
          [[int(_)] if '-' not in _ else 
          list(range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)) 
          for _ in contents.pop(0).split(' ')]), 
    "S": reduce(lambda x, y: x + y, 
          [[int(_)] if '-' not in _ else 
          list(range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)) 
          for _ in contents.pop(0).split(' ')]), 
    "W": reduce(lambda x, y: x + y, 
          [[int(_)] if '-' not in _ else 
          list(range(int(_.split('-')[0]), int(_.split('-')[1]) + 1)) 
          for _ in contents.pop(0).split(' ')]), 
}

def accept(deal):
    if not restrictions['N'](deal.north): return False
    if not restrictions['E'](deal.east): return False
    if not restrictions['S'](deal.south): return False
    if not restrictions['W'](deal.west): return False
    if deal.north.hcp not in ranges['N']: return False
    if deal.east.hcp not in ranges['E']: return False
    if deal.south.hcp not in ranges['S']: return False
    if deal.west.hcp not in ranges['W']: return False
    return True

dealer = Deal.prepare()

inp = []
for i in range(100):
    deal = dealer(accept)
    deal.set_str_style('pbn')
    print(deal)
