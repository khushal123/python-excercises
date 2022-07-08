input = [['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
         ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'], [
             'Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
         ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
         ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia',
             'Sam', 'Sachin', 'Desmond', 'Kapil'],
         ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam']]


def get_daily_participents(participent_list):
    common_items = set.intersection(*map(set, participent_list))
    return list(common_items)


def get_once_participents(participent_list):
    once_participent_list = []
    one_d_list = sum(participent_list, [])
    participent_count_dict = {}
    for participent in one_d_list:
        participent_count_dict[participent] = 1 if participent_count_dict.get(
            participent, None) is None else participent_count_dict.get(participent) + 1
    for participent in participent_count_dict:
        if participent_count_dict.get(participent, None) == 1:
            once_participent_list.append(participent)
    return once_participent_list


def get_first_day_participents(participent_list):
    day_one_participents = participent_list[0]
    subsequent_days_list = sum(participent_list[1:], [])
    first_day_only = []
    for participent in day_one_participents:
        if participent not in subsequent_days_list:
            first_day_only.append(participent)
    return first_day_only


print(get_daily_participents(participent_list=input))
print(get_once_participents(participent_list=input))
print(get_first_day_participents(participent_list=input))
