from cudatext import *

""" on every "Show fat menu" comamnd call - CudaText gains ~50MB in memory
"""

class Command:
    def __init__(self):
        self.h_menu = None

    def show_fat_menu(self):
        if self.h_menu is None:
            self.h_menu = menu_proc(0, MENU_CREATE)

        menu_proc(self.h_menu, MENU_CLEAR)

        large_str = '?'*50_000_000
        fat_lambda = lambda *args, **vargs: print(large_str[:3])

        menu_proc(self.h_menu, MENU_ADD, command=fat_lambda, caption='Caption')

        menu_proc(self.h_menu, MENU_SHOW)


