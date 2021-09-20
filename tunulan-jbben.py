from core.Automata import Automata
import time
import sys
bb = Automata("assets/cn/tunvlang2-ep.png", "assets/tunvlang-sp.png", (0, 0))
apple = 0
if len(sys.argv) >= 2:
    apple = int(sys.argv[1])
# bb.set_apples(2, "silver")
bb.set_apples(apple, "gold")
print("apple = ", (apple))

while True:
    bb.quick_start()
    # time.sleep(5)
    # BATTLE 1
    bb.wait_attack()
    bb.select_servant_skill(1)
    bb.select_servant_skill(4)
    bb.select_servant_skill(5,1)
    bb.select_servant_skill(6, 1)
    bb.select_servant_skill(7)
    bb.select_servant_skill(8,1)
    bb.select_servant_skill(9, 1)
    bb.select_cards([6])
    # BATTLE 2
    bb.select_servant_skill(2, color=2)
    bb.select_servant_skill(3)
    bb.select_master_skill(3, 3, 1)
    bb.select_servant_skill(7)
    bb.select_servant_skill(8,1)
    bb.select_cards([6])
    # BATTLE 3
    bb.select_servant_skill(9, 1)
    bb.select_master_skill(1)
    bb.select_cards([6])
    # FINISH
    bb.finish_battle()