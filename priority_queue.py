
from collections import OrderedDict


class Job(object):
    JOB_KEYS = ['command', 'priority']

    def __init__(self, job_dict: dict):

        if not isinstance(job_dict, dict):
            raise ValueError(f"Expected dict, got {type(job_dict)}")

        if not type(job_dict['command']) is str:
            raise ValueError(f"Expected str, got {type(job_dict['command'])}")

        if not type(job_dict['priority']) is int:
            raise ValueError(f"Expected str, got {type(job_dict['priority'])}")

        unsupported = [key for key in job_dict if key not in self.JOB_KEYS]
        if unsupported:
            raise RuntimeError(f"Job contains unsupported '{unsupported}' keys")

        priority = job_dict['priority']
        if not (0 <= priority <= 10):
            raise ValueError('Invalid priority: {}'.format(priority))
        self.priority = priority

        command = job_dict['command']
        self.command = command


class PriorityQueue(object):
    """
    Simple Priority Queue
    add(job) takes a dictionary with
    """
    def __init__(self):
        self._queue = OrderedDict({})

    def __str__(self):
        output = ''
        for prio, jobs, in sorted(self._queue.items()):
            output += '\nPriority: {}'.format(prio)
            for job in jobs:
                output += '\nCommand: {}'.format(job.command)
            output += '\n'
        return output

    def is_empty(self):
        return len(self._queue) == 0

    def add(self, job_dict: dict):
        """ Adds job to queue list and also adds to the dictionary
        to better sort jobs with same priority.
        :param job: eg-
        {"command": "batcherapp -f -p /YYZ/some/path166", "priority": 1}
        """
        job = Job(job_dict)
        if job.priority in self._queue:
            self._queue[job.priority].append(job)
        else:
            self._queue[job.priority] = [job]


if __name__ == '__main__':

    q = PriorityQueue()
    q.add({"command": "batcherapp -f -p /XYZ/some/path123", "priority": 1})
    q.add({"command": "batcherapp -f -p /XZY/some/path321", "priority": 9})
    q.add({"command": "batcherapp -f -p /YYZ/some/path111", "priority": 3})
    q.add({"command": "batcherapp -f -p /YYZ/some/path621", "priority": 3})
    q.add({"command": "batcherapp -f -p /YYZ/some/path221", "priority": 4})
    q.add({"command": "batcherapp -f -p /YYZ/some/path166", "priority": 1})
    q.add({"command": "batcherapp -f -p /YVZ/some/path144", "priority": 6})
    print(q)


