from core.Automata import Automata
import time
bb = Automata("assets/Qp5.png", "assets/eg-sp4.png", (0, 0))

bb.set_apples(3, "silver")

while bb.counts > 0:
    bb.quick_start()
    time.sleep(2)
    # BATTLE 1
    bb.select_servant_skill(4)
    bb.select_servant_skill(5, 1)
    bb.select_servant_skill(6, 1)
    bb.select_servant_skill(7)
    bb.select_servant_skill(8, 1)
    bb.select_servant_skill(9, 1)
    bb.select_servant_skill(1)
    bb.select_cards([6])
    # BATTLE 2
    bb.select_cards([6])
    # BATTLE 3
    bb.select_cards([6])
    # FINISH
    bb.finish_battle()