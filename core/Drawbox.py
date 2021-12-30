from os import close
import time
import random
from core import util, crds
from core.Dynamica import Dynamica

class Drawbox():
    def __init__(self, ckp: str, sft=(0, 0)): 
        self.shifts = sft
        self.checkpoint = ckp

    def quick_start(self, advance=True):
        """ Quick Start
        Select the default `checkpoint`, `support` and start the battle.

        Parameters
        ----------
            advance: bool, optional
        Set to `True` if you want to enable `advance support selection`, `False` to use the normal support selection.
        By default, it is `False`

        """
        self.select_checkpoint()
        self.draw()

    # pre-battle related
    def select_checkpoint(self, ckp: str = None):
        self.wait(self.checkpoint)
        if ckp is None:
            ckp = self.checkpoint
        coordinates = util.get_crd(util.get_sh(self.shifts), ckp)
        self.tap(coordinates[0], 100)
        time.sleep(0.2)
        print("[INFO] Checkpoint selected.")
    
    def draw(self):
        # 循环抽池子
        while True:
            # while not util.standby(util.get_sh(self.shifts), crds.IMAGE["switchbox"]) and not util.standby(util.get_sh(self.shifts), crds.IMAGE["emailfull"]):
            while not util.standby(util.get_sh(self.shifts), crds.IMAGE["switchbox"]):
                self.tap(crds.DRAW)
            if util.standby(util.get_sh(self.shifts), crds.IMAGE["switchbox"]):
                self.switchBox()
            # if util.standby(util.get_sh(self.shifts), crds.IMAGE["emailfull"]):
            #     self.emailClear()

    def switchBox(self):
        # 换池子
        time.sleep(0.3)
        coordinates = util.get_crd(util.get_sh(self.shifts), crds.IMAGE["switchbox"])
        self.tap(coordinates[0], 100)
        time.sleep(0.2)
        coordinates = util.get_crd(util.get_sh(self.shifts), crds.IMAGE["execute"])
        self.tap(coordinates[0], 100)
        time.sleep(1)
        coordinates = util.get_crd(util.get_sh(self.shifts), crds.IMAGE["close2"])
        self.tap(coordinates[0], 100)
        time.sleep(0.2)
        print("[INFO] Gift box reseted.")

        # raise Exception("Gift box empty!")

    def emailClear(self):
        # 处理邮箱
        raise Exception("Email box full!")


    def tap(self, crd: (int, int), i: int = 10, j: int = 10):
        x = crd[0] + self.shifts[0]
        y = crd[1] + self.shifts[1]
        util.tap(util.shifter((x, y), i, j))

    def swipe(self, org: (int, int), tar: (int, int), delay, sfts: (int, int) = (10, 10)):
        original = (org[0] + self.shifts[0], org[1] + self.shifts[1])
        target = (tar[0] + self.shifts[0], tar[1] + self.shifts[1])
        util.swipe(
            util.shifter(original, sfts[0], sfts[1]),
            util.shifter(target, sfts[0], sfts[1]),
            delay)

    def wait(self, pic: str):
        while not util.standby(util.get_sh(self.shifts), pic):
            time.sleep(0.2)

    def aquire_screenshot(self):
        """ aquire screenshot
        Returns
        -------
            str
        Path of the screenshot image
        """
        return util.get_sh(self.shifts)

    def __str__(self):
        return ("Checkpoint: " + self.checkpoint + "\n" +
                "Support: " + self.support + "\n" +
                "Shift: " + str(self.shifts))
