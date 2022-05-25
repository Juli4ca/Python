s  = None
m = None
h = None
d = None

duration = int(input('Введите время: '))

if duration < 60:
    s = duration
    print(f'{s} сек')
elif 60 <= duration < 3600:
    m = duration // 60
    s = duration % 60
    print(f'{m} мин {s} сек')
elif 3600 <= duration < 86400:
    h = duration // 3600
    m = (duration % 3600) // 60
    s = (duration % 3600) % 60
    print(f'{h} час {m} мин {s} сек')
else:
    d = duration // 86400
    h = (duration % 86400) // 3600
    m = ((duration % 86400) % 3600) // 60
    s = ((duration % 86400) % 3600) % 60
    print(f'{d} дн {h} час {m} мин {s} сек')
