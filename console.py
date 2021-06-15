import socket
sock = socket.socket()
from emoji import demojize
from ahk import AHK
import time
import random
from datetime import datetime, timedelta

weapons = ["001720BC","001720BB","001720BA","001720B9","00176E59","00176E57","00176E55","00174094","00174093","00171B48","00167685","00162C92","001629B6","00162019","00161246","0015FFF4","0015FF5D","0015FE44","0015BA78","0015BA72","0015BA03","0015B38D","0015A47F","0015837B","00157BCA","00156F7C","00156968","001568E6","00155E6D","00155E66","0015430B","001524B3","00151D0C","001519E0","0014F474","0014EB3C","0014EA5A","0014DE1D","0014DDDF","0014DDDE","0014D2AC","0014D2AA","0014D2A7","0014C068","001479B3","00146C79","001465A6","00143FBA","001429E2","001429E1","001429D1","0013F76F","0013E540","0013E4DE","0013D534","0013568B","0013316D","00133058","00130041","0012D852","0012ADB8","00129A44","00127E45","00127C6C","0012701F","001251CD","001251CC","001221C1","00121168","00121154","00121148","0011E46F","0011A8E4","0011A8B9","0011A8A0","00113248","0010BA90","0010A70C","0010A70B","0010A70A","0010A709","00109A0C","00109A0B","00109A0A","00106FEB","00106FEA","00105CF6","00105CF5","001056D3","001056D2","00103B1D","0010108D","000FF576","000FC335","000F82AA","000F7EAE","000F56F6","000F56F5","000F0F04","000F0B12","000F062B","000E9C3B","000E7655","000E6346","000E6064","000E5B17","000E58BB","000E5391","000E393B","000E377A","000E3778","000BA0F3","000E32F4","000E2C86","000E2BFC","000E2BF4","000CE569","000CE549","000CD53A","000CD539","000CD50E","000CD50D","00090A6B","00090A6A","0009073B","00090727","0009071F","000906DF","000906DA","000906CF","0008F21E","0008F21C","0008F21A","0008F218","0008F217","0008F216","0008F215","0008F214","0008F213","0008ED0C","0008ED0B","0008ED0A","0007EA25","0007EA24"]
ammo = ["00176E5C","00176E54","0016AEF9","00166F62","00166B5A","00165E7A","00165E79","001613FF","001613D4","00160C41","00160C40","0015FD42","0015E8EE","0015E8ED","00158313","00158312","00158311","0015830E","0015830D","0015830C","0015830B","00158307","001582E0","001582DF","001582DA","0014F44A","001429CF","00140AA8","00140AA1","00140AA0","00140A9F","00140A9E","0013E44C","0013E44B","0013E449","0013E448","0013E447","0013E446","0013E445","0013E444","0013E443","0013E442","0013E441","0013E440","0013E43F","0013E43E","0013E43D","0013E43C","0013E43B","0013E43A","0013E439","0013E438","0013E437","00121162","00121155","00121150","00121133","0011A207","001003B0","000E86F2","00096C40","0008ED03","0008ED02","0008ECFF","0008ECF5","0007EA27","0007EA26","000615AF","000615A8","00056634","000B8791","0006B53E","0006B53D","0006B53C","00078CC5","00078CC4","00078CC3","00078CC2","00078CC1","0006A80D","0005F706","00047419","00029383","0002937E","00029371","00029364","0002935B","00020799","00020772","00004485","00004241","00004240","001476B0"]
perks = ["00094EB8", "00094EB9", "001361B3", "001361B4", "00165118", "0014609C", "00135F18", "00044CB1", "001377FD", "0010F09E", "00031DD3", "00094EBC", "00031DE1", "00031DD8", "00031DD9", "001656FD", "0014609D", "00146096", "00094EBA", "00031DAB", "00165180", "00031DE3", "00094EBB", "0016581B", "00044CA9", "0016578B", "00165AEC", "00031DE0", "00165816", "00099828", "00138562", "00146099", "0014609B", "001377FE", "00031DA9", "00031DAA", "00165449", "00031DDE", "0014609E", "0010C6CD", "00031DAC", "00031DB5", "00094EC1", "00135EC3", "00137800", "00031DAD", "00031DBC", "00044CA7", "00094EBD", "00165AEF", "00094EBF", "00135EC9", "001651B6", "00031DB1", "00146098", "0014609F", "00031DB2", "00031DC2", "00031DB3", "00031DB4", "00165AF0", "00165447", "00094EC4", "00165182", "0009982D", "00165815", "00031DB7", "00135F75", "00031DBA", "0007B202", "00031DBB", "00099827", "0014609A", "00031DBD", "00146097", "00031DC4", "00044CAF", "00044CB0", "00044CAA", "00031DE5", "00099834", "00031DCC", "00031DC5", "00165789", "00165AE6", "00165181", "00165446", "000E2C49", "000E2C4A"]

def consoleRun(string):
    ahk = AHK()
    win = ahk.find_window(title=b'Fallout: New Vegas') # Find the opened window
    win.activate()    
    ahk.key_press('~')  # Send keys, as if typed (performs ahk string escapes)
    time.sleep(0.5)
    ahk.send_event(string, 1)        # Give the window focus
    time.sleep(0.5)
    ahk.send_event('~',1)

def main():
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'jacksbots'
    token = 'oauth:YOURTOKEN'
    channel = '#jackdvpt'

    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    god_time = datetime.now()- timedelta(seconds=60)
    claw_time = datetime.now()- timedelta(seconds=60)
    level_time = datetime.now()- timedelta(seconds=60)
    gun_time =datetime.now()- timedelta(seconds=60)
    ammo_time = datetime.now()- timedelta(seconds=60)
    super_time = datetime.now()- timedelta(seconds=60)
    while True:
        now = datetime.now()
        resp = sock.recv(2048).decode('utf-8')
        print(resp)
        if "!god" in resp:
            if now > god_time:
                print("god")
                #consoleRun("tgm {enter}")
                god_time = now + timedelta(seconds=10)
        elif "!claw" in resp:
            if now > claw_time:
                print("claw")
                consoleRun("player.placeatme 1CF9A 1{enter}")
                claw_time = now + timedelta(seconds=30)
        elif "!brute" in resp:
            if now > super_time:
                print("claw")
                consoleRun("player.placeatme 00027FB3 1{enter}")
                super_time = now + timedelta(minutes=30)
        elif "!level" in resp:
            if now > level_time:
                print("level up")
                consoleRun("advlevel {enter}")
                level_time = now + timedelta(seconds=10)
        elif "!roach" in resp:
            print("New Dog")
            consoleRun("player.placeatme 00168D0C  1{enter}") 
        elif "!borben" in resp:
            print("New Dog")
            consoleRun("player.additem 00032C75  1{enter}") 
        elif "!radroach" in resp:
            print("New Dog")
            consoleRun("player.placeatme 0013215C  1{enter}") 
        elif "!knife" in resp:
            consoleRun("player.additem 0004334 1 {enter}")
        elif "!bark" in resp:
            print("New Dog")
            consoleRun("player.placeatme 0015E910 1{enter}")  
        elif "!ant" in resp:
            print("New Dog")
            consoleRun("player.placeatme 0015E908 1{enter}")               
        elif "!dog" in resp:
            print("New Dog")
            consoleRun("player.placeatme 0015C690 1{enter}")         
        elif "!gun" in resp:
            print("New Gun")
            consoleRun("player.additem "+random.choice(weapons)+" 1 {enter}")
        elif "!be" in resp:
            print("New gender droppin")
            consoleRun("sexchange {enter}")
        elif "!ammo" in resp:
            print("New Ammo")
            consoleRun("player.additem "+random.choice(ammo)+" 10 {enter}")
        elif "!perk" in resp:
            print("New Perk")
            if perks:
                cur_perk = random.choice(perks)
                perks.remove(cur_perk)
                consoleRun("player.addperk "+cur_perk+"{enter}")
            else:
                print("outta perks")
if __name__ == "__main__":
    main()