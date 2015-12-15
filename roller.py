#!/bin/python2

import random

options = { 
    -1 : '[-]', 
    0  : '[  ]', 
    1  : '[+]' 
    }

options_color = { 
    -1 : '\033[40m\033[1;31m - \033[1;m', 
    0  : '\033[40m\033[1;30m   \033[0;m', 
    1  : '\033[40m\033[1;32m + \033[1;m' 
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
print ''

while counter < 4:
    choice = random.choice(options.keys())
    print options[choice], 
    print " ",
    outcome += choice
    counter += 1

print ''
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

print ''
