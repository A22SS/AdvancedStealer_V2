import ctypes
import uuid
import psutil
import time

class EvasionTools:
    @staticmethod
    def is_sandbox():
        checks = [
            lambda: 'VMware' not in ctypes.windll.kernel32.GetComputerNameA(),
            lambda: uuid.getnode() != 0,
            lambda: psutil.cpu_count() > 1,
            lambda: psutil.cpu_freq().max > 1000,
            lambda: psutil.disk_usage('/').total > 20*1024**3,
            lambda: time.sleep(0.1) < 0.09,
        ]
        return all(check() for check in checks)

evasion = EvasionTools()
