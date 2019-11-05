# ------------------------------------------------
# GRAPHING ---------------------------------------
# ------------------------------------------------
class Graph:
    def __init__(self, screen):
        self.screen = screen
        self.framebuf = screen.framebuf
        self.bar_width = 4
        self.graph_height = 60
        self.clear()

    def draw_bar(self, x, y):

        # y value is 0 - 100
        height = int(round(self.graph_height * y / 100))

        self.framebuf.fill_rect(self.bar_width*x, 0, self.bar_width, height, 1)
        self.show()

    def clear(self):
        self.screen.fill(0)
        self.show()

    def show(self):
        self.screen.show()


