

class Task(object):
    def __init__(self, name, description, start_date=None, end_date=None, percent_complete=0.0):
        self._name = name 
        self._description = description
        self._start_date = start_date
        self._end_date = end_date
        self._percent_complete = percent_complete * 1.0

    ''' --- Properties ---'''
    @property
    def name(self):
        return self._name 
    @property 
    def description(self):
        return self._description 
    @property
    def start_date(self):
        return self._start_date 
    @property
    def end_date(self):
        return self._end_date
    @property
    def duration(self):
        return self.end_date - self.start_date
    @property
    def percent_complete(self):
        return self._percent_complete
    @percent_complete.setter
    def percent_complete(self, percent_complete):
        if percent_complete < 0 or percent_complete > 100:
            raise ValueError('Percentage must be between 0 and 100, inclusive. For 100%, pass 100')
        self._percent_complete = percent_complete * 1.0

    ''' --- Magic Methods --- '''
    def __str__(self):
        return '{}({} : {} : from {} to {})'.format(self.__class__.__name__
                                                    ,self.name
                                                    ,self.description
                                                    ,self.start_date
                                                    ,self.end_date)

    def __hash__(self):
        return hash(self.name)