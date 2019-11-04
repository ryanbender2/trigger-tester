"""Return dictionary of results of trigger test

This class will be doing the bulk of the work as of 
actually processing data. This class is meant to be
used in a loop. 

This class takes in one record in at a time,
runs the record through each trigger, and
returns the results.

"""


class Triggers():
    """
    Trigger tester

    """
    
    
    def __init__(self):
        None
    
    
    def test(self, record):
        """Tests record against trigger
        
        :param record: client record
        :type record: dict
        
        :returns: results
        :rtype: dict
        
        """
        
        None