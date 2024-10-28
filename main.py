# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:
#
# Использование %:
#
# Переменные: количество участников первой команды (team1_num).
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
#
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
#
# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
# Переменные: исход соревнования (challenge_result).
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


def winner() -> str:

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'


print('количество участников первой команды %(team1_num)s' % {'team1_num': team1_num})
print('В команде Мастера кода участников: %(team2_num)s' % {'team2_num': team2_num})

print('Команда Волшебники данных решила задач: {score_1}'.format(score_1=score_1))
print('Волшебники данных решили задачи за: {team1_time}'.format(team1_time=team1_time))

print(f'Команды решили: {score_1} и {score_2} задач')
print(f'Результат битвы: {winner()}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time + team2_time) / 2} секунды на задачу!.')
