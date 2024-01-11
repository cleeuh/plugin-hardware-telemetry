import subprocess
import time
import json
import argparse
import re

from waggle.plugin import Plugin

# For Server: "iperf3 -s -p 7575"
stream_def = {"sender": "upload", "receiver": "download"}

def sanitize_input(user_input):
    sanitized_input = re.sub(r'[^a-zA-Z0-9.\- "\']', '', user_input)
    return sanitized_input

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stderr:
        return result.stderr
    else:
        return result.stdout

def main():        
    with Plugin() as plugin:
        print(run_cmd("uptime"))
        print(run_cmd("cat /proc/meminfo"))
        print(run_cmd("paste <(cat /sys/class/thermal/thermal_zone*/type) <(cat /sys/class/thermal/thermal_zone*/temp)"))
        print(run_cmd('cat /sys/devices/system/cpu/cpufreq/cpuload/cpu_usage'))
        print(run_cmd('ls /dev/'))
        print(run_cmd('ls /'))
        print(run_cmd('cat /dev/constraint_cpu_freq'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Hardware Telemetry',
                    description='Gathers the device\'s statistics such at cpu load, network speeds, etc.',
                    epilog='')
    parser.add_argument('--rate', dest='rate', default='',
                    help='Set the polling rate')
    args = parser.parse_args()
    
    # cmd = sanitize_input(args.cmd)
    main()
