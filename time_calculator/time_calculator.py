

def addition(t1, t2):
    
    d0, h0, m0 = (0,0,0)
    h1, m1 = t1 # tuple1
    h2, m2 = t2 # tuple2

    m0 += m1 + m2
    while m0 >= 60:
        m0 -= 60
        h0 += 1

    h0 += h1 + h2
    while h0 >= 24:
        h0 -= 24
        d0 += 1

    return d0, h0, m0


def convert2time(time):
    
    ftime = ''

    days, halfday, hours, minutes = time
    minutes = str(minutes)

    minutes = '0' + minutes if len(minutes) == 1 else minutes

    ftime = f'{hours}:{minutes} {halfday}'

    return ftime


def convertto24(hm, halfday):
    '''
    it converts the 12h format to 24h
    '''
    hours, minutes = hm.split(':')
    hours = int(hours)
    minutes = int(minutes)

    if (halfday == 'PM' and hours < 12):
        hours += 12
    
    elif (halfday == 'AM' and hours == 12):
        hours -= 12
        
    return hours, minutes


def convertto12(hours, minutes):
    '''
    it converts the 24h format to 12h
    '''
    ftime = ''

    if hours > 12:
        hours -= 12
        halfday = 'PM'
    elif hours == 12:
        halfday = 'PM'
    elif hours == 0:
        hours += 12
        halfday = 'AM'
    else:
        halfday = 'AM'

    if minutes < 10:
        minutes = '0' + str(minutes)

    ftime = f'{hours}:{minutes} {halfday}'

    return ftime


def addtoweekday(days, weekday):

    weekday_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    wdn = weekday_list.index(weekday)

    wdn += days
    while wdn >= 7:
        wdn -= 7

    weekday = weekday_list[wdn]

    return f', {weekday.capitalize()}'


def add_time(start, duration, weekday=''):
    weekday = weekday.lower()
    addhours , addminutes = duration.split(':')
    elements = start.split()

    # print(f'{start} , {duration}\n') #test

    hours, minutes = convertto24(elements[0], elements[1].upper())

    t1 = (hours, minutes)
    t2 = (int(addhours), int(addminutes))

    t0 = addition(t1,t2)

    days, hours, minutes = t0

    ftime = convertto12(hours, minutes)

    if days == 1:
        fdays = ' (next day)'
    elif days > 1:
        fdays = f' ({days} days later)'
    else:
        fdays = ''

    if weekday:
        weekday = addtoweekday(days, weekday)

    added_time = f'{ftime}{weekday}{fdays}\n'

    return added_time


