sum = 0
num_tickets = int(input("количество билетов, которые вы хотите приобрести на мероприятие "))
ages = [int(input(f"возраст {i} посетителя: ")) for i in range(1, num_tickets + 1)]
has_error = False
for y in range(0, num_tickets):
    if ages[y] < 0 or ages[y] > 100:
        print('некорректно указан возраст')
        has_error = True
        break
if not has_error:
    for y in range(0, num_tickets):
        if 18 < ages[y] < 25:
            sum += 990
        elif ages[y] >= 25:
            sum += 1390

    if num_tickets >= 3:
        sum *= 0.9  # discount
    print('К оплате:', sum)