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
villans = ['000E585F','000FE034','000FE036','0003A147','00164ECA','0010D5D5','00132164','00154454','000E5850','0014F42D','00167E9D','0014F47C','00165183','00168D0B','00159783','0014F479','00167E83','0014F479','0014F476','001689D8','0014F44C','0014F431','000E59E7','0014F42C','00167EC1','000E59E8','000E601F','001532FF','00154A6F','0001CF9C','001607B5','000E584E','0015C64C','0014F47F','0015C642','001745E2','0001CFA2','001607B7','0014F475','001445A7','00167E83','0016AEFA','0015C643','0015C644','0015C645','0015F184','0014F47E','001616F0','0015978E','0009189C','000E584D','00132540','00132541','00133101','00133102','00140D4B','0014F478','0015E908','0015678B','00164A6C','00164EF7','001616EC','00166DFD','001616EF','000E5851','0015F183','0015978F','00159790','001616EE','00159792','0015F182','000FF5E5','000F0B30','0015C690','0015A892','0010AB79','0017AF94','00133F46','0013E313','0001CFA3','0017AF40','0013D83B','0013AFE1','0013AACF','00027FB3','0017AF62','00092c4d','0017AF3F','0009FAFA','00167ECC','00145E6E','00167ED7','0017283A','00167ECC','0009FAFB','00167F02','00145E6E','00167ED7','0017283A','0001CF77','00167ECF','00167EDC','00167EDE','00167ECD','00167F02','00167EDD','00167EE0','00167ED9','00167EE3','0001CF7A','00167ECD','00167ED9','00167EE3','000E585F','000FE034','000FE036','0003A147','000E5861','000E5860','0015A893','00167E64','00159605','00156771','00159604','0015A0C0','00167E8B','0013FE86','000FEB84','00140DB0','00162B3D','00164BCB','001532FE','00167E8B','00157B23','00174BDD','000C938B','00168D0C','00156770','00145E75','0001CF9E','00135B9C','00135BA0','00135BA5','00159606','0001CF7C','001689D4','0015A88E','00167ECE','0014451B','00162948','000F5702','000F5701','0014F47A','0014F42A','0015E911','00101CD3','00144BC4','0007EA2A','0013AFDC','000BAC89','0007EA2C','000E794E','0007EA2D','0007EA2B','001445BB','001445BC','0007EA28','001365B5','00142A22','001710AA','00167EB8','00113246','0010A1F8','0010A1F9','0010A1F7','0010CD73','00157FE0','00165184','0015E908','000EF412','001028C1','00156778','0015C669','000F3D52','000F3D53','000F4401','000F0904','00144BC4','0012BD37','00156788','000F0904','000F3D52','000F3D53','000F4401','001347E0','00135B35','000FC1D0','000EF411','0011D584','0015C653','00135BCF','00145E76','00156782','0015A0BF','00159788','00159789','00164BCC','00167EA6','000E8E95','001040BC','0017283E','0014F480','0001CF80','00102AAD','0015C7BE','0001CF81','00136B11','001183A4','00102AAD','00169DD8','00169DD5','0015C7BF','00162947','00118D61','00164EF2','00164EF8','0014128C','0013215C','0015C680','00145EDB','0015C67F','00156784','00145EDA','0014F44E','00144BC4','00136A20','000CAFF8','001544B8','001544B7','001544B6','001544B9','0001CF9F','000A3D15','0014F481','000A46F4','0015C68F','00167EFF','00167EFD','00167EFE','00102AAE','00145E6F','0001CF7B','00167ED0','00167ED0','0014451A','00167EE6','0017B060']


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
        elif "!villain" in resp:
            if now > claw_time:
                consoleRun("player.placeatme "+random.choice(villains)+"{enter}")
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
            consoleRun("player.placeatme 00168D0C  1{enter}") 
        elif "!borben" in resp:
            consoleRun("player.additem 00032C75  1{enter}") 
        elif "!radroach" in resp:
            consoleRun("player.placeatme 0013215C  1{enter}") 
        elif "!knife" in resp:
            consoleRun("player.additem 0004334 1 {enter}")
        elif "!bark" in resp:
            consoleRun("player.placeatme 0015E910 1{enter}")  
        elif "!ant" in resp:
            consoleRun("player.placeatme 0015E908 1{enter}")               
        elif "!dog" in resp:
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
