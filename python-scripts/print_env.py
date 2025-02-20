import subprocess

try:
    from mmengine.utils.dl_utils import collect_env
except ImportError:
    subprocess.run(["pip", "install", "mmengine"])
    from mmengine.utils.dl_utils import collect_env


def print_env():
    for name, val in collect_env().items():
        print(f"{name}: {val}")


print_env()
