from PIL import Image
import subprocess
import time
import random
import os

def jump(distance):
    press_time=distance*2.062
    press_time=max(press_time,200)
    press_time=int(press_time)
    point=(random.randint(300,679),random.randint(888,1270))
    cmd='adb shell input swipe {x1} {y1} {x2} {y2} {time}'.format(x1=point[0],y1=point[1],x2=point[0]+random.randint(1,4),y2=point[1]+random.randint(1,4),time=press_time) 
    os.system(cmd)
    return press_time





def find_piece_and_board(img_path):
    img=Image.open(img_path)
    w,h=img.size
    print(w,h)
    img_pixel=img.load()
    start_y=None
    for i in range(int(h/3),int(h*2/3),50):
        first_pixel=img_pixel[0,i]
        for j in range(1,w):
            pixel=img_pixel[j,i]
            if(pixel[0]!=first_pixel[0]or pixel[1]!=first_pixel[1]or pixel[2]!=first_pixel[2]):
                start_y=i-50
                break
        if start_y:
            break
    left=0
    right=0
    piece_y_max=0           
    for i in range(start_y,int(h*2/3)):
        flag=True
        for j in range(int(w/8),int(w*7/8)):  
             pixel=img_pixel[j,i]
             if(50<pixel[0]<60)and (53<pixel[1]<63)and (95<pixel[2]<110):
                 if flag:
                     left=j
                     flag=False
                 right=j
                 piece_y_max=max(i,piece_y_max)
    piece_x=(left+right)//2
    piece_y=piece_y_max-20
    print('棋子所在位置')
    print(piece_x,piece_y)
    if piece_x<w/2:
        board_x_start=piece_x+38
        board_x_end=w
    else:
        board_x_start=0
        board_x_end=piece_x-38
    for i in range(start_y,int(h*2/3)):
        flag=True
        first_pixel=img_pixel[0,i]
        for j in range(board_x_start,board_x_end):
            pixel=img_pixel[j,i]
            if abs(pixel[0]-first_pixel[0])+abs(pixel[1]-first_pixel[1])+abs(pixel[2]-first_pixel[2])>10:
                if flag:
                    left=j
                    right=j
                    flag=False
                else:
                    right=j
        if not flag:
            break
    board_x=(left+right)//2
    top_point=img_pixel[board_x,i]
    print(board_x,i)
    for k in range(i+274,i,-1):
        pixel=img_pixel[board_x,k]
        if abs(pixel[0]-top_point[0])+abs(pixel[1]-top_point[1])+abs(pixel[2]-top_point[2])<10:
            break
    board_y=(i+k)//2
    print('目标所在位置')
    print(board_x,board_y)
    return (piece_x,piece_y),(board_x,board_y)
def get_screenshot():
    process=subprocess.Popen('adb shell screencap -p',shell=True,stdout=subprocess.PIPE)
    screenshot=process.stdout.read()
    screenshot=screenshot.replace(b'\r\r\n',b'\n')
    with open('autojump.png','wb')as f:
        f.write(screenshot)
def run():
    oper=input('请确保手机打开了ADB并且连接了电脑 然后打开跳一跳 并开始游戏后再执行本程序,确定开始？ y/n>>:')
    if oper!='y':
        exit('退出')

    while  True:
        get_screenshot()
        piece,board=find_piece_and_board('autojump.png')
        distance=((piece[0]-board[0])**2+(piece[1]-board[1])**2)**0.5
        print('两个方块的距离')
        print(distance)
        jump(distance)
        time.sleep(random.randrange(1,5))
if __name__=='__main__':
    run()
       
   
