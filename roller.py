#!/bin/python2

import random

options = { 
    -1 : '[-]', 
    0  : '[ ]', 
    1  : '[+]' 
    }

ladder = {
    0  : 'Legendary',
    7  : 'Epic',
    6  : 'Fantastic',
    5  : 'Superb',
    4  : 'Great',
    3  : 'Good',
    2  : 'Fair',
    1  : 'Average',
    0  : 'Mediocre',
    -1 : 'Poor',
    -2 : 'Terrible'
    }

counter = 0
outcome = 0

while counter < 4:
    choice = random.choice(options.keys())
    print options[choice], 
    print " ",
    outcome += choice
    counter += 1

print ''

if outcome > -1:
    print '+',

print outcome,

if outcome < -2:
    print 'Beyond Terrible'
elif outcome > 8:
    print 'Beyond Legendary'
else:
    print ladder[outcome]
