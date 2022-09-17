from core.Automata import Automata
import time
import sys
bb = Automata("assets/swimsuit22-ep.png", "assets/swimsuit22-sp.png", "assets/swimsuit22-sp-bak.png", (0, 0))
apple = 0
if len(sys.argv) >= 2:
    apple = int(sys.argv[1])
# bb.set_apples(2, "silver")
bb.set_apples(apple, "gold")
print("apple = ", (apple))

while True:
    bb.quick_start()
    # BATTLE 1
    bb.wait_attack()
    # bb.select_servant_skill(4)
    bb.select_servant_skill(2,2)
    bb.select_servant_skill(3,2)
    bb.select_servant_skill(8,2)
    bb.select_servant_skill(9,2)
    bb.select_cards([7])
    # BATTLE 2
    bb.select_servant_skill(1)
    bb.select_cards([7])
    # BATTLE 3
    bb.select_servant_skill(7)
    bb.select_servant_skill(6)
    bb.select_cards([7])
    # FINISH
    bb.finish_battle()