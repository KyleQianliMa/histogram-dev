from __future__ import print_function

#!/usr/bin/env python
# Copyright (c) 2005 Timothy M. Kelley all rights reserved

import ARCSTest.utilities as utilities

target = "histogram"   # name of package being tested

log = utilities.picklog(target)

def runTests(**kwds):

    # do not alter the next statement, or py_test.py may not work 
    testmods = [
        "DictAttCont",
        "StdvectorDataset",
        "Axis",
        "DatasetContainer",
        "Histogram"# <eol>
        ]  # list of strings, one per module
    
    allPassed = True
    records = {}

    for mod in testmods:
        exec('from histogramTest_{0!s} import run'.format(mod))
        utilities.preReport(log, mod, "")
        passed = run()
        if passed:
            records[mod] = 'PASSED'
        else:
            records[mod] = 'FAILED'
        utilities.postReport(log, mod, "", passed)
        allPassed = allPassed and passed

    if allPassed:
        log("All Python tests of {0!s} PASSED".format(target))
    else:
        log("Some/all Python tests of {0!s} FAILED".format(target))

    _summarize(records)

    return allPassed


def _summarize(records):
    print('*'*80)
    print("Test summary:")
    for key in records.keys():
        print("Test of {0!s} {1!s}".format(key, records[key]))
    print("End of test")
    return


if __name__ == '__main__':
    import journal
    journal.info(target).activate()
    journal.debug(target).activate()
    runTests()


# version
__id__ = "$Id$"

# End of file
