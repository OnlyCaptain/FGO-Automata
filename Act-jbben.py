from core.Automata import Automata
import time
import sys
# bb = Automata("./assets/cn/Free-ep.png", "./assets/eg-sp5.png", (0, 0))
bb = Automata("./assets/cn/Act-ep.png", "./assets/eg-sp6.png", (0, 0))
apple = 0
if len(sys.argv) >= 2:
    apple = int(sys.argv[1])
# bb.set_apples(2, "silver")
bb.set_apples(apple, "silver")
print("apple = "+str(apple))

# if (apple == 0):


while True:
    bb.quick_start()
    # time.sleep(5)
    # BATTLE 1
    bb.select_servant_skill(1)
    bb.select_servant_skill(2)
    bb.select_servant_skill(4)
    bb.select_servant_skill(5, 1)
    bb.select_servant_skill(6, 1)
    bb.select_servant_skill(9, 1)
    bb.select_cards([6])
    # BATTLE 2
    bb.select_servant_skill(8, 1)
    bb.select_servant_skill(3)
    bb.select_cards([6])
    # BATTLE 3
    bb.select_servant_skill(7)
    bb.select_master_skill(2, 1)
    bb.select_cards([6])
    # FINISH
    bb.finish_battle()