import random

MAX_HP = 100  # константа для значения максимального здоровья игроков
LOW_HP_CMP = 35  # значение низкого показателя здоровья Компьютера; если здоровья столько или меньше, то вероятность исцеления увеличивается
ACT_RANGE = [0, 60]  # границы для интервала выбора действия
BOUNDS = [20, 40]  # разделители внутри интервала выбора действия
BOUNDS_WEAK_CMP = [15, 30]  # разделители внутри интервала выбора действия с повышенной вероятностью исцеления
DMG_WEAK_RANGE = [18, 25]  # границы интервала урона для атаки с небольшим диапазоном
DMG_STRONG_RANGE = [10, 35]  # границы интервала урона для атаки с большим диапазоном
HEAL_RANGE = [18, 25]  # границы интервала единиц здоровья для исцеления


class Player(object):  # класс для объекта игрока

    def __init__(self, name, is_cmp):  # конструктор класса
        self.HP = MAX_HP  # установка максимального значения здоровья
        self.name = name  # установка имени
        self.is_computer = is_cmp  # устанвка свойства "является Компьютером"

    def get_hp(self):
        return self.HP

    def get_name(self):
        return self.name

    def act(self, enemy):  # функия действия
        act_choice = random.randint(*ACT_RANGE)  # получение случайного значения из интервала выбора действия

        atk_1_bound = BOUNDS[0]  # установка разделителей внутри интервала выбора действия
        atk_2_bound = BOUNDS[1]
        if self.is_computer and self.HP <= LOW_HP_CMP:  # анализ свойства "является Компьютером" и количества здоровья
            atk_1_bound = BOUNDS_WEAK_CMP[0]  # установка разделителей с повышенной вероятностью исцеления
            atk_2_bound = BOUNDS_WEAK_CMP[1]

        if act_choice <= atk_1_bound:  # определение действия
            return self.atk_weak(enemy)  # возвращение сообщения об атаке с небольшим диапазоном урона
        if atk_1_bound < act_choice <= atk_2_bound:
            return self.atk_strong(enemy)  # возвращение сообщения об атаке с большим диапазоном урона
        if atk_2_bound < act_choice:
            return self.heal()  # возвращение сообщения об исцелении

    def atk_weak(self, enemy):  # функция атаки с небольшим диапазоном урона
        dmg = random.randint(*DMG_WEAK_RANGE)
        damage_line = enemy.get_damage(dmg)
        return self.name + " attacked " + enemy.name + "; " + damage_line

    def atk_strong(self, enemy):  # функция атаки с большим диапазоном урона
        dmg = random.randint(*DMG_STRONG_RANGE)
        damage_line = enemy.get_damage(dmg)
        return self.name + " attacked " + enemy.name + "; " + damage_line

    def heal(self):  # функция исцеления
        heal = random.randint(*HEAL_RANGE)
        if self.HP + heal > MAX_HP:  # проверка, не превышается ли максимальное значение здоровья
            heal = MAX_HP - self.HP
        self.HP += heal
        heal_line = self.name + " healed himself"
        if self.HP < MAX_HP:
            heal_line += " by " + str(heal) + " points"
        return heal_line

    def get_damage(self, dmg):  # функция получения урона
        if self.HP - dmg <= 0:  # проверка, не понижается ли здоровье меньше 0
            dmg = self.HP
        self.HP -= dmg
        return self.name + " lost " + str(dmg) + "HP"


def who_is_alive(player1, player2):     # проверка, кто из игроков жив
    if player1.get_hp() == 0 and player2.get_hp() > 0:
        return player2.get_name()
    elif player1.get_hp() > 0 and player2.get_hp() == 0:
        return player1.get_name()
    return "Both or none"


pl = Player("Player", False)  # создание Игрока
cmp = Player("Computer", True)  # создание Компьютера
while pl.get_hp() > 0 and cmp.get_hp() > 0:  # пока здоровье игроков больше нуля, продолжаем игру
    player_choice = random.randint(0, 1)  # случайное значение для выбора очередности хода
    if player_choice == 0:  # ход Игрока
        input("Your turn. Press Enter")
        print(pl.act(cmp))
    else:
        print(cmp.act(pl))  # ход Компьютера
    print(pl.get_name() + ": " + str(pl.get_hp()) + " HP | " + cmp.get_name() + ": " + str(
        cmp.get_hp()) + " HP")  # вывод количества здоровья для каждого из игроков
    print("------------------")
print("Game over! Winner: " + who_is_alive(pl, cmp))
