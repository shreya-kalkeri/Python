from datetime import datetime, timedelta

YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
YourWorkingHours = ['9:00', '20:00']

YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
YourCoWorkersWorkingHours = ['10:00', '18:30']

def find_free_time_intervals(calendar, working_hours):
    #Record the earliestStartTime
    work_start = working_hours[0]
    #Record the latestEndTime
    work_end = working_hours[1]

    free_time = []

    for i in range(len(calendar)):
        #for the first element of the list 
        if i == 0:
            #if first meetingStartTime is not equal to your earliestStartTime
            #then record [earliestStartTime,meetingStartTime] as free time
            if calendar[i][0] != work_start:
                temp_list = [work_start, calendar[i][0]]
                free_time.append(temp_list)

        #for the last element of the list
        elif i == (len(calendar) - 1):
            #if last meetingEndTime is not equal to your latestEndTime
            #then record [meetingEndTime,latestEndTime] as free time
            if calendar[i][1] != work_end:
                temp_list = [calendar[i][1], work_end]
                free_time.append(temp_list)

        #for the middle elements of the list 
        else:
            #record the previous and the next slot
            previous_slot = calendar[i - 1]
            next_slot = calendar[i + 1]

            #if there are no continuous meeting schedules
            #then record the difference of currentStartTime and previousEndTime meetings as free time
            if calendar[i][0] != previous_slot[1]:
                temp_list = [previous_slot[1], calendar[i][0]]
                free_time.append(temp_list)

            #if there are no continuous meeting schedules
            #then record the difference of currentEndTime and nextStartTime meetings as free time
            if calendar[i][1] != next_slot[0]:
                temp_list = [calendar[i][1], next_slot[0]]
                free_time.append(temp_list)

    return free_time

#print(find_free_time_intervals(YourCalendar, YourWorkingHours))
#print(find_free_time_intervals(YourCoWorkersCalendar, YourCoWorkersWorkingHours))

def find_common_free_time(calendar1, working_hours1, calendar2, working_hours2):
    free_time1 = find_free_time_intervals(calendar1, working_hours1)
    free_time2 = find_free_time_intervals(calendar2, working_hours2)

    common_free_time = []

    for slot1 in free_time1:
        for slot2 in free_time2:
            start_time = max(slot1[0], slot2[0])
            end_time = min(slot1[1], slot2[1])
            if start_time < end_time:
                common_free_time.append([start_time, end_time])

    return common_free_time

print(find_common_free_time(YourCalendar, YourWorkingHours, YourCoWorkersCalendar, YourCoWorkersWorkingHours))

#> Worst Case Time Complexity : O(N^2)
#> N is the number of meeting slots in each calender. 
#> In worst case, to compute free time we might need to compare 'Your calender's' each time slot with 'co-worker's' calender's each slot, 
#  for which we need to traverse through 2 'for' loops.
#>Hence making time complexity O(n^2)

#> Worst Case Space Complexity : O(N^2)
#> N is the number of meeting slots in each calender. 
#> In the worst case, all the time slots of 'Your calender' and your 'co-worker's' calender might be free.
#> There might be a need to assign free slot for each calender slot.
#> Hence there might be a need to record all slots as free.