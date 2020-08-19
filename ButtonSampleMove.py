from tkinter import*
import tkinter.ttk as ttk

class ButtonSampleMove(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 300, height = 300)
        self.x_y = None
        self.create_widgets()
        self.propagate(False)
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self, text = "button")
        button.place(x = 100, y = 100)
        button.bind("<Button-1>", self.move_start)
        button.bind("<B1-Motion>", self.move_now)
        button.bind("<ButtonRelease-1>", self.move_end)
    
    def move_start(self, event):
        #マウスカーソルの座標取得
        self.start_xy = (event.x_root, event.y_root)
        #位置情報取得
        place_info = event.widget.place_info()
        x = int(place_info['x'])
        y = int(place_info['y'])
        self.x_y = (x,y)

    def move_now(self, event):
        if self.start_xy is None:
            return
        #移動距離を求める
        distance = (event.x_root - self.start_xy[0], event.y_root - self.start_xy[1])
        #再度座標を設定する
        place_info = event.widget.place_info()
        place_info['x'] = self.x_y[0] + distance[0]
        place_info['y'] = self.x_y[1] + distance[1]
        event.widget.place_configure(place_info)

    def move_end(self, event):
        #座標類を初期化
        self.start_xy = None
        self.x_y = None

if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSampleMove")
    master.geometry("300x300")
    ButtonSampleMove(master)
    master.mainloop()

#This is from "https://suzutaka-programming.com/tkinter-ttk-button-bind-motion/"