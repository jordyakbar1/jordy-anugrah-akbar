import random

class Robot:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.defense_mode = False

    def attack_enemy(self, enemy):
        # Menghitung akurasi serangan
        attack_accuracy = random.randint(1, 100)
        if attack_accuracy <= 80:  # 80% chance to hit
            damage = self.attack
            if enemy.defense_mode:
                damage //= 2  # Damage reduced by half if in defense mode
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} menyerang {enemy.name} tetapi meleset!")

    def regen_health(self):
        regen_amount = random.randint(5, 15)
        self.hp += regen_amount
        print(f"{self.name} meregenerasi {regen_amount} HP!")

    def is_alive(self):
        return self.hp > 0

    def defend(self):
        self.defense_mode = True
        print(f"{self.name} masuk ke mode pertahanan!")

    def reset_defense(self):
        self.defense_mode = False

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def start_game(self):
        print("Permainan dimulai!")
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round} ==========================================================")
            print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]")
            print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]")

            # Robot 1 memilih aksi
            action1 = self.player_action(self.robot1)
            if action1 == 1:  # Attack
                self.robot1.attack_enemy(self.robot2)
            elif action1 == 2:  # Defense
                self.robot1.defend()
            elif action1 == 3:  # Giveup
                print(f"{self.robot1.name} menyerah! {self.robot2.name} menang!")
                return

            if not self.robot2.is_alive():
                print(f"{self.robot2.name} telah kalah! {self.robot1.name} menang!")
                return

            # Robot 2 memilih aksi
            action2 = self.player_action(self.robot2)
            if action2 == 1:  # Attack
                self.robot2.attack_enemy(self.robot1)
            elif action2 == 2:  # Defense
                self.robot2.defend()
            elif action2 == 3:  # Giveup
                print(f"{self.robot2.name} menyerah! {self.robot1.name} menang!")
                return

            if not self.robot1.is_alive():
                print(f"{self.robot1.name} telah kalah! {self.robot2.name} menang!")
                return

            # Reset defense mode for both robots
            self.robot1.reset_defense()
            self.robot2.reset_defense()

            self.round += 1

    def player_action(self, robot):
        while True:
            print(f"\n1. Attack     2. Defense     3. Giveup")
            action = input(f"{robot.name}, pilih aksi: ")
            if action in ['1', '2', '3']:
                return int(action)
            else:
                print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

def main():
    print("Selamat datang di permainan pertarungan Robot!")
    
    # Input untuk Robot 1
    name1 = input("Masukkan nama Robot 1: ")
    attack1 = int(input("Masukkan nilai serangan Robot 1: "))
    hp1 = int(input("Masukkan HP Robot 1: "))
    
    # Input untuk Robot 2
    name2 = input("Masukkan nama Robot 2: ")
    attack2 = int(input("Masukkan nilai serangan Robot 2: "))
    hp2 = int(input("Masukkan HP Robot 2: "))
    
    # Membuat objek Robot
    robot1 = Robot(name1, attack1, hp1)
    robot2 = Robot(name2, attack2, hp2)

    # Memulai permainan
    game = Game(robot1, robot2)
    game.start_game()

if __name__ == "__main__":
    main()