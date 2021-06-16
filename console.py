import socket
import config
sock = socket.socket()
from ahk import AHK
import time
import random
from datetime import datetime, timedelta

weapons = ["001720BC","001720BB","001720BA","001720B9","00176E59","00176E57","00176E55","00174094","00174093","00171B48","00167685","00162C92","001629B6","00162019","00161246","0015FFF4","0015FF5D","0015FE44","0015BA78","0015BA72","0015BA03","0015B38D","0015A47F","0015837B","00157BCA","00156F7C","00156968","001568E6","00155E6D","00155E66","0015430B","001524B3","00151D0C","001519E0","0014F474","0014EB3C","0014EA5A","0014DE1D","0014DDDF","0014DDDE","0014D2AC","0014D2AA","0014D2A7","0014C068","001479B3","00146C79","001465A6","00143FBA","001429E2","001429E1","001429D1","0013F76F","0013E540","0013E4DE","0013D534","0013568B","0013316D","00133058","00130041","0012D852","0012ADB8","00129A44","00127E45","00127C6C","0012701F","001251CD","001251CC","001221C1","00121168","00121154","00121148","0011E46F","0011A8E4","0011A8B9","0011A8A0","00113248","0010BA90","0010A70C","0010A70B","0010A70A","0010A709","00109A0C","00109A0B","00109A0A","00106FEB","00106FEA","00105CF6","00105CF5","001056D3","001056D2","00103B1D","0010108D","000FF576","000FC335","000F82AA","000F7EAE","000F56F6","000F56F5","000F0F04","000F0B12","000F062B","000E9C3B","000E7655","000E6346","000E6064","000E5B17","000E58BB","000E5391","000E393B","000E377A","000E3778","000BA0F3","000E32F4","000E2C86","000E2BFC","000E2BF4","000CE569","000CE549","000CD53A","000CD539","000CD50E","000CD50D","00090A6B","00090A6A","0009073B","00090727","0009071F","000906DF","000906DA","000906CF","0008F21E","0008F21C","0008F21A","0008F218","0008F217","0008F216","0008F215","0008F214","0008F213","0008ED0C","0008ED0B","0008ED0A","0007EA25","0007EA24"]
ammo = ["00176E5C","00176E54","0016AEF9","00166F62","00166B5A","00165E7A","00165E79","001613FF","001613D4","00160C41","00160C40","0015FD42","0015E8EE","0015E8ED","00158313","00158312","00158311","0015830E","0015830D","0015830C","0015830B","00158307","001582E0","001582DF","001582DA","0014F44A","001429CF","00140AA8","00140AA1","00140AA0","00140A9F","00140A9E","0013E44C","0013E44B","0013E449","0013E448","0013E447","0013E446","0013E445","0013E444","0013E443","0013E442","0013E441","0013E440","0013E43F","0013E43E","0013E43D","0013E43C","0013E43B","0013E43A","0013E439","0013E438","0013E437","00121162","00121155","00121150","00121133","0011A207","001003B0","000E86F2","00096C40","0008ED03","0008ED02","0008ECFF","0008ECF5","0007EA27","0007EA26","000615AF","000615A8","00056634","000B8791","0006B53E","0006B53D","0006B53C","00078CC5","00078CC4","00078CC3","00078CC2","00078CC1","0006A80D","0005F706","00047419","00029383","0002937E","00029371","00029364","0002935B","00020799","00020772","00004485","00004241","00004240","001476B0"]
perks = ["00094EB8", "00094EB9", "001361B3", "001361B4", "00165118", "0014609C", "00135F18", "00044CB1", "001377FD", "0010F09E", "00031DD3", "00094EBC", "00031DE1", "00031DD8", "00031DD9", "001656FD", "0014609D", "00146096", "00094EBA", "00031DAB", "00165180", "00031DE3", "00094EBB", "0016581B", "00044CA9", "0016578B", "00165AEC", "00031DE0", "00165816", "00099828", "00138562", "00146099", "0014609B", "001377FE", "00031DA9", "00031DAA", "00165449", "00031DDE", "0014609E", "0010C6CD", "00031DAC", "00031DB5", "00094EC1", "00135EC3", "00137800", "00031DAD", "00031DBC", "00044CA7", "00094EBD", "00165AEF", "00094EBF", "00135EC9", "001651B6", "00031DB1", "00146098", "0014609F", "00031DB2", "00031DC2", "00031DB3", "00031DB4", "00165AF0", "00165447", "00094EC4", "00165182", "0009982D", "00165815", "00031DB7", "00135F75", "00031DBA", "0007B202", "00031DBB", "00099827", "0014609A", "00031DBD", "00146097", "00031DC4", "00044CAF", "00044CB0", "00044CAA", "00031DE5", "00099834", "00031DCC", "00031DC5", "00165789", "00165AE6", "00165181", "00165446", "000E2C49", "000E2C4A"]
villans = ['000E585F','000FE034','000FE036','0003A147','00164ECA','0010D5D5','00132164','00154454','000E5850','0014F42D','00167E9D','0014F47C','00165183','00168D0B','00159783','0014F479','00167E83','0014F479','0014F476','001689D8','0014F44C','0014F431','000E59E7','0014F42C','00167EC1','000E59E8','000E601F','001532FF','00154A6F','0001CF9C','001607B5','000E584E','0015C64C','0014F47F','0015C642','001745E2','0001CFA2','001607B7','0014F475','001445A7','00167E83','0016AEFA','0015C643','0015C644','0015C645','0015F184','0014F47E','001616F0','0015978E','0009189C','000E584D','00132540','00132541','00133101','00133102','00140D4B','0014F478','0015E908','0015678B','00164A6C','00164EF7','001616EC','00166DFD','001616EF','000E5851','0015F183','0015978F','00159790','001616EE','00159792','0015F182','000FF5E5','000F0B30','0015C690','0015A892','0010AB79','0017AF94','00133F46','0013E313','0001CFA3','0017AF40','0013D83B','0013AFE1','0013AACF','00027FB3','0017AF62','00092c4d','0017AF3F','0009FAFA','00167ECC','00145E6E','00167ED7','0017283A','00167ECC','0009FAFB','00167F02','00145E6E','00167ED7','0017283A','0001CF77','00167ECF','00167EDC','00167EDE','00167ECD','00167F02','00167EDD','00167EE0','00167ED9','00167EE3','0001CF7A','00167ECD','00167ED9','00167EE3','000E585F','000FE034','000FE036','0003A147','000E5861','000E5860','0015A893','00167E64','00159605','00156771','00159604','0015A0C0','00167E8B','0013FE86','000FEB84','00140DB0','00162B3D','00164BCB','001532FE','00167E8B','00157B23','00174BDD','000C938B','00168D0C','00156770','00145E75','0001CF9E','00135B9C','00135BA0','00135BA5','00159606','0001CF7C','001689D4','0015A88E','00167ECE','0014451B','00162948','000F5702','000F5701','0014F47A','0014F42A','0015E911','00101CD3','00144BC4','0007EA2A','0013AFDC','000BAC89','0007EA2C','000E794E','0007EA2D','0007EA2B','001445BB','001445BC','0007EA28','001365B5','00142A22','001710AA','00167EB8','00113246','0010A1F8','0010A1F9','0010A1F7','0010CD73','00157FE0','00165184','0015E908','000EF412','001028C1','00156778','0015C669','000F3D52','000F3D53','000F4401','000F0904','00144BC4','0012BD37','00156788','000F0904','000F3D52','000F3D53','000F4401','001347E0','00135B35','000FC1D0','000EF411','0011D584','0015C653','00135BCF','00145E76','00156782','0015A0BF','00159788','00159789','00164BCC','00167EA6','000E8E95','001040BC','0017283E','0014F480','0001CF80','00102AAD','0015C7BE','0001CF81','00136B11','001183A4','00102AAD','00169DD8','00169DD5','0015C7BF','00162947','00118D61','00164EF2','00164EF8','0014128C','0013215C','0015C680','00145EDB','0015C67F','00156784','00145EDA','0014F44E','00144BC4','00136A20','000CAFF8','001544B8','001544B7','001544B6','001544B9','0001CF9F','000A3D15','0014F481','000A46F4','0015C68F','00167EFF','00167EFD','00167EFE','00102AAE','00145E6F','0001CF7B','00167ED0','00167ED0','0014451A','00167EE6','0017B060']
base = ['0007f8e1','00080771','000810e9','00084206','0008cd23','0008cd27','0008d0e7','0008d0e9','0008d0eb','0008d749','0008f0ba','0008f13a','00092bd2','000941dc','000a41a3','000a59ae','000a59b0','000a59e6','000acd6b','000b8fa0','000ccfc8','000cd22c','000cd22d','000cd22e','000cd22f','000cd230','000cd231','000ce88c','000cef3b','000d71b6','000d7f57','000da729','000e07d3','000e07d4','000e07d5','000e27e5','000e27e6','000e2881','000e2886','000e2c93','000e2c94','000e2dce','000e2dcf','000e2f82','000e2f83','000e2f84','00164605','000e2f85','000e32a2','000e32aa','000e5299','000e5518','000e5958','000e595b','000e595c','000e5e4f','000e5f17','000e5f36','000e604c','000e604f','000e60ef','000e60f0','000e60f1','000e6675','000e7c1b','000e84a2','000e8992','000e8993','000e8994','000e8d1a','000e8f69','000e8f6b','000e8f6c','000e8f6d','000e8f96','000ec7a1','000ec7a3','000ece21','000ed4e2','000ed4e9','000ed50d','000edc34','000eddcf','000eddd0','000ee688','000ef3aa','000ef3ab','000ef468','000efb25','000efb26','000f04ad','000f05e2','000f0b31','000f1095','000f1863','000f1864','000f271c','000f2746','000f3b86','000f3bce','000f3bf8','000f43d5','000f47a9','000f47aa','000f47ab','000f47ac','000f512d','000f52ab','000f56f7','000f56f8','000f56f9','000f56fa','000f56fb','000f56fc','000f56fd','000f56fe','000f56ff','000f5700','000f624e','000f624f','000f6250','000f6251','000f6252','000f6370','000f6371','000f8298','000f839a','000f839b','000f839c','000f839d','000f839e','000f83a2','000f889a','000f889b','000fa749','000fa877','000fea1d','000feb3c','000fed41','000fed42','000fed43','000ff1b8','000ff262','000ff264','000ff265','000ff803','001010b7','00101c9b','00101c9d','00103869','00103dfd','00104310','00104311','00104312','00104313','00104314','00104315','001043d1','00104c0c','00104c67','00104c6c','00104c78','00104c7c','00104c7c','00104c7f','00104e84','0010588d','0010596b','0010596c','0010596d','00106623','0010a6fe','0010af1b','0010c0be','0010c67d','0010c67e','0010c680','0010c681','0010c682','0010c683','0010c6dd','0010c6ea','0010c6f3','0010c6f4','0010c6f5','0010c6f6','0010c6f7','0010c6f9','0010c6fa','0010c760','0010c761','0010c762','00116c62','0010c764','0010c767','0010c769','0010d23d','0010d4e7','0010d4e8','0010d4e9','0010d4ea','0010d4eb','0010d4ec','0010e037','0010eb2b','0010f700','0010fa83','0010fd2f','0010fd30','0010fd31','00110d89','0011253e','00112640','00112641','00112642','0011324d','0011324e','00113456','00113647','00113648','00113649','001158b2','00115c38','001164f9','0015e110','001164fc','00116580','00116597','00116892','0011689c','00116a50','00116b3f','00116b40','00116e22','00117e11','00118374','00118e71','0011904e','0011baee','0011e496','0011e496','0011e4c2','0011e4fc','0011e6b6','0011e752','0011eb5b','0011ebdd','0011f862','0011f90f','0011f9b8','0011f9b9','0011f9ba','0011f9be','0011f9d0','0011fb7c','0011fbc3','0011fc07','0011fc9d','00120172','00120183','001206fc','00120dcc','00120dcd','00120dce','00121fef','001228db','00122b95','00122b97','00122b99','00123c91','00123cc6','0012411c','001252bf','001258b3','001258e0','00126d47','00127dcc','0012ac9e','0012ac9f','0012aca0','0012b512','0012b513','0012b514','0012b515','0012b515','0012baae','0013002d','001300a6','001300a7','001300a8','001300a9','001300aa','001300e2','001300ed','001300ee','001300f0','00130bb9','00131f77','00133955','00133956','00133957','00133958','00133fdd','001347d9','00134972','00134985','001364c7','001364c8','00136fd3','00137121','00137123','0013721e','00137acf','00139b8b','0013a5fe','0013a7eb','0013d6a1','0013d6a2','0013d6a4','0013d6a7','0013d831','0013d834','0013e307','0013e4d6','0013e4d7','0013e5b9','0013ec2c','0013ec2d','0013ec2e','0013ec2f','0013f323','0013f70d','0013fe78','0013fe79','0013fe79','0013fe7a','00140e53','00140e60','00140e6b','00140e6d','00140e70','001413bd','001413c2','001428ed','00144f32','00145f8a','00147404','00147405','00148a32','00148c26','0014e83c','0014edbe','0014efb2','0014f279','001544b5','001547bb','001558d7','00155a03','00157c8d','0015882b','0015968a','00159a9c','0015a028','0015a245','0015a359','0015d78f','0015e9e6','0015ec2c','0015f072','00160800','0016192c','0016192d','00161eb2','001630cd','00163369','0016336b','0016336c','00164604','001694e0','001694e2','00171b38']
#ref = ['001164fa','0007f8c0','00080770','000834c0','000840c8','00084204','00084207','00084226','0008cd24','0008cd28','0008d501','0008d74c','0008e447','0008e44c','0008e44d','0008f0b8','0009649b','00096bce','00099cfe','00099d00','000a41db','000acd6b','000b8fa6','000ccfcd','000cd22b','000ce94e','000cef3c','000d6f51','000d7036','000d7037','000d71b7','000d7f59','000e07d7','000e07d8','000e07db','000e2807','000e2808','000e2809','000e280f','000e2882','000e2883','000e288c','000e2dbf','000e2f3f','000e2f86','000e2f87','000e2f88','000e2f89','000e32a3','000e32a9','000e3488','000e529a','000e5517','000e5a68','000e5a69','000e5e50','000e5e51','000e6105','000e61a2','000e61a3','000e6822','000e6825','000e684b','000e686e','000e689a','000e7c1c','000e84a4','000e8f64','000e8f65','000e8f66','000e8f67','000e8f68','000ec7b8','000ed4dd','000eea78','000ef3ad','000ef3e9','000efb27','000efb28','000efb4e','000efb52','000f0678','000f0a3f','000f0a48','000f0b33','000f1866','000f18bd','000f2def','000f2eaa','000f36ea', '000f3b8b','000f3bd5','000f3bf9','000f3dd0','000f43d7','000f47ae','000f47af','000f47b0','000f47b1','000f5143','000f52b0','000f53aa','000f5704','000f570a','000f570b','000f570d','000f570e','000f570f','000f5710','000f5711','000f5712','000f6253','000f6254','000f6255','000f6256','000f6257','000f6283','000f6372','000f6373','000f829a','000f83a3','000f83a4','000f83a5','000f83a6','000f83aa','000f83ab','000f889c', '000f889d','000f8b13','000fab0b','000fb327','000fbc4b','000fe245','000fea1e','000ff1b9','000ff267','000ff268','000ff269','000ff26a','000ff26b','000ff26c','001010cb','00101ca0','00103dfe','00104318','00104319','0010431a','0010431b','00104893','00104a39','00104c0f','00104c68','00104c6d','00104c79','00104c7d','00104c7d','00104c80','00104e85','0010588e','00106515','00106516','0010651a','00106616','00106d79','00107af5','0010b908','0010c0bf','0010c6de','0010c6eb','0010d4ee','0010d4ef', '0010d4f0','0010d4f1','0010d4f2','0010d8df','0010d8e0','0010d8e1','0010d8e2','0010d8e3','0010d8e5','0010d8e6','0010d8e7','0010d8e8','0010d8e9','0010d8ea','0010d8eb','0010e0ce','0010eb29','0010f701','0010fa82','0010fd33','0010fd34','0011118d','00112471','0011253f','0011267a','0011267b','0011267c','00112dc9','001132ca','0011365d','0011365e','0011365f','00115c5f','00115c60','00115f07','00116598','00116838','0011683a','00116840','00116894','0011689d','00116a52','00117e10','00117e7a','00118343','001185d4','0011904f','001199a4','0011baf0','0011e497','0011e4fb','0011e6b9','0011eb8e','0011ebdc','0011ed50','0011f87a','0011f9bf','0011f9c0','0011f9c1','0011f9c2','0011fb7b','0011fbbd','0011fbc4','0011fc9e','001206fe','00120dd7','00120dd8','00120dd9','00120dda','00121ff0','001228ef','001229ba','00122b98','00123c8c','00123cc7','00124aea','001258d1','001258d2','00125c1a','001271d7','00127212','00127dd7','00127ecb','0012b4a8','0012d6e2','0012fcb2','0012fcb3','0012fcb4','0012fcb4','0012fcd2','0012fcd6','001300f2','001300f5','00130b99','00131e7b','00131f78','00133043','00133044','00133047','00133959','0013395a','0013395c''00134830','00134973','001349b6','00134b9c','00134d03','00134d05','00134db4','00135f19','001364c4','001364c5','00136a1f','001370c9','00137122','00137124','00137125','0013721f','001376e7','00137a9d','00137ad0','0013bf5b','0013d830','0013d832','0013e30a','0013e5bb','0013ec00','0013ec01','0013ef04','0013ef05','0013ef09','0013ef0a','0013f31b','0013f70e','0013fe89', '0013fe89','0013fe8a','0013feab','00140da7','00140da9','00140dac','00140e54','00140e6c','00140e6e','00140e71','00140e73','001413bf','001413c3','00144f33','00148c27','0014e83d','0014edbf','0014f27a','00151ee0','00152e90','0015362b','0015362c','00154612','001558d8','00155a04','00157c8f','0015882c','0015968b','00159aa2','0015a246','0015a373','0015a82c','0015bc9e','0015d782','0015e9eb','00160801','00161969','00161988','00161eb1','00163364','00163367','001656da','00171b39','001732cf','001732d0','001732d1','00174983','001770e6','00179357','0017935f']

    

def consoleRun(string):
    ahk = AHK()
    win = ahk.find_window(title=b'Fallout: New Vegas')  # Find the opened window
    win.activate()                                      # give the window Focus  
    ahk.key_press('~')                                  # open the console
    time.sleep(0.5)                                     # Pause for half a second just so it doesnt start typing before the console is open
    ahk.send_event(string, 1)                           # Type the string, passed from the if below
    time.sleep(0.5)                                     # Sleep again to make sure its finished typing
    ahk.send_event('~',1)                               # Close the console (THIS DOESNT ALWAYS WORK)

def main():
    server = 'irc.chat.twitch.tv'
    port = 6667

    sock.connect((server, port))
    sock.send(f"PASS {config.token}\n".encode('utf-8'))
    sock.send(f"NICK {config.nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {config.channel}\n".encode('utf-8'))
    base_time = datetime.now()- timedelta(seconds=60)
    size_time = datetime.now()- timedelta(seconds=60)
    speed_time = datetime.now()- timedelta(seconds=60)
    god_time = datetime.now()- timedelta(seconds=60)
    villain_time = datetime.now()- timedelta(seconds=60)
    level_time = datetime.now()- timedelta(seconds=60)
    brute_time = datetime.now()- timedelta(seconds=60)
    while True:
        now = datetime.now()
        resp = sock.recv(2048).decode('utf-8')
        print(resp)
        if "!god" in resp:
            if now > god_time:
                print("god")
                #consoleRun("tgm {enter}")
                god_time = now + timedelta(seconds=10)
        elif "!friend" in resp:
            if now > base_time:
                consoleRun("player.placeatme "+random.choice(base)+"{enter}")
                base_time = now + timedelta(seconds=10)
        elif "!foe" in resp:
            if now > villain_time:
                consoleRun("player.placeatme "+random.choice(villans)+"{enter}")
                villain_time = now + timedelta(seconds=30)
        elif "!brute" in resp:
            if now > brute_time:
                consoleRun("player.placeatme 00027FB3 1{enter}")
                brute_time = now + timedelta(minutes=30)
        elif "!level" in resp:
            if now > level_time:
                consoleRun("advlevel {enter}")
                level_time = now + timedelta(seconds=10)
        elif "!roach" in resp:
            consoleRun("player.placeatme 00168D0C  1{enter}") 
        elif "!borben" in resp:
            consoleRun("player.additem 00032C75  1{enter}") 
        elif "!knife" in resp:
            consoleRun("player.additem 0004334 1 {enter}")
        elif "!bark" in resp:
            consoleRun("player.placeatme 0015E910 1{enter}")  
        elif "!ant" in resp:
            consoleRun("player.placeatme 0015E908 1{enter}")           
        elif "!face" in resp:
            consoleRun("showplasticsurgeonmenu {enter}")   
        elif "!speed" in resp:
            if now > speed_time:
                consoleRun("player.setav speedmult "+str(random.randint(50,200))+"{enter}")  
                speed_time = now + timedelta(seconds=30)
        elif "!size" in resp:
            if now > size_time:
                consoleRun("player.setscale "+str(random.randint(5,50)/10)+"{enter}")
                size_time = now + timedelta(seconds=120)  
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
