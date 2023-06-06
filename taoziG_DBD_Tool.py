import os
import tkinter
import tkinter.messagebox

UserData = os.getenv("LOCALAPPDATA")

Steam_path = UserData+r"\DeadByDaylight\Saved\Config\WindowsClient"

Epic_path = UserData+r"\DeadByDaylight\Saved\Config\EGS"

vsync_true = "bUseVSync=True"

vsync_false = "bUseVSync=False"

config_add =('''

[/script/engine.engine]
bSmoothFrameRate=false
MinSmoothedFrameRate=5
MaxSmoothedFrameRate=120
bUseVSync=false
''')
#
#
#
def Unlock(file_path):
    if not os.path.exists(file_path):
        tkinter.messagebox.showinfo("提示","不存在你选择的版本，若首次安装游戏请启动一次后再解锁")
        return
    # 禁用VSync
    file_setting = file_path+r"\GameUserSettings.ini"
    with open(file_setting,'r',encoding='UTF-8') as file:
        data_temp = file.read()
        data = data_temp.replace(vsync_true,vsync_false)
    with open(file_setting,'w',encoding='UTF-8') as file:
        file.write(data)
    # 解锁帧率
    file_config = file_path+r"\Engine.ini"
    with open(file_config,'r',encoding='UTF-8') as file:
        if config_add in file.read():
            tkinter.messagebox.showinfo("提示","你已解锁过本版本")
            return
    with open(file_config,'a',encoding='UTF-8') as file:
        file.write(config_add)
        tkinter.messagebox.showinfo("提示","解锁成功")
# 图形化界面
menu = tkinter.Tk()
menu.title("taoziGの黎明杀机FPS解锁工具")
menu.geometry("400x100")
menu.resizable(0,0)

use_steam_button = tkinter.Button(menu, text="Steam解锁", command=lambda:Unlock(Steam_path))
use_steam_button.pack()

use_epic_button = tkinter.Button(menu, text="Epic解锁", command=lambda:Unlock(Epic_path))
use_epic_button.pack()
menu.mainloop()
