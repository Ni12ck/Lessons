# Список переменных
# Количество участников команд
team1_num = 5
team2_num = 6
# Количество решённых задач
score_1 = 40
score_2 = 42
# Время выполнения задач
team1_time = 2052.512
team2_time = 2153.31451
# Всего задач решено
tasks_total = score_1 + score_2
# Среднее время
time_avg = (team1_time + team2_time) / (score_1 + score_2)

# Результат соревнований
challenge_result = ''

# Условия победы
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:
print('Использование %')
print('В команде Мастера кода участников: %d' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
print()

# Использование format():
print('Использование format()')
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}!'.format(team1_time))
print()

# Использование f-строк
print('Использование f-строк')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')