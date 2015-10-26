
from revd.prototype import reverse_dict_lookup
# from nose import with_setup

dictionary = {}

dictionary['pandiculation'] = 'to stretch oneself, typically after waking up'
dictionary['bigot'] = 'a person holding firm convictions'
dictionary['sizeable'] = 'of considerable size'


passcnt = 0
failcnt = 0

# options
verbose = True

for word in dictionary:
    if reverse_dict_lookup(dictionary[word]) == word:
        passcnt = passcnt + 1
    else:
        failcnt = failcnt + 1
        if verbose: print 'Failed at', dictionary[word], ': got ',\
                          reverse_dict_lookup(dictionary[word]), ' expected', word



print 'Cases Passed: ', passcnt
print 'Cases Failed: ', failcnt


