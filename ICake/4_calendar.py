
# merge all overlapping intervals
# assume values are all within the same day, and numbered in ascending order from 0 to 24
class Meeting(object):
    def __init__(self, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime

    def to_string(self):
        return "(%f, %f)" % (self.starttime, self.endtime)


class MeetingOrganizer(object):
    # utility class
    @staticmethod
    def condense_meeting_times(meeting_times):
        """
        :param meeting_times: a list of meeting times
        :return:
        Note: uses a greedy strategy
        using a list of meeting times sorted by start time,
            if start and end time and within the previous entry's start/end times, merge into previous
            if start time is within previous entry's, but end time is after, replace current end time with new end time and remove next entry
            if start time of next entry is after end time of current entry, keep current entry and proceed to next entry
            if reach final entry, stop
        """
        size = len(meeting_times)

        # trivial case
        if size == 1:
            return meeting_times

        sorted_meetings = MeetingOrganizer().sort_meeting_times_starttime(meeting_times)
        merged_meetings = []

        # now merge meetings
        current_size = len(sorted_meetings)
        i = 0
        while i < (current_size-1):
            # next meeting slot is completely within previous slot
            if sorted_meetings[i+1].starttime <= sorted_meetings[i].endtime and sorted_meetings[i+1].endtime <= sorted_meetings[i].endtime:
                # subsume into previous time span by removing the next meeting time
                sorted_meetings.pop \
                    ( i +1)    # don't need to increment i as next element is now the element after the popped element
                current_size = len(sorted_meetings)
            elif sorted_meetings[ i +1].starttime <= sorted_meetings[i].endtime and sorted_meetings[ i +1].endtime > sorted_meetings[i].endtime:
                # if start time of next meeting is within current meeting but end time is after current end time, extend
                # current element's end time to be this later time, and remove next element
                sorted_meetings[i].endtime = sorted_meetings[ i +1].endtime
                sorted_meetings.pop \
                    ( i +1)    # don't need to increment i as next element is now the element after the popped element
                current_size = len(sorted_meetings)
            else:
                # if no overlap, keep current meeting and continue to next meeting
                i += 1
        return sorted_meetings

    @staticmethod
    def sort_meeting_times_starttime(meeting_times):
        """
        takes a list of meeting times
        returns a sorted list by starttime
        """
        return sorted(meeting_times, key= lambda meeting: meeting.starttime)

if __name__ == "__main__":

    mymeetings=[Meeting(9, 12), Meeting(3, 5), Meeting(6, 7), Meeting(3, 9), Meeting(12, 15), Meeting(15.5, 17)]

    condensed = MeetingOrganizer.condense_meeting_times(mymeetings)
    for element in condensed:
        print element.to_string()
