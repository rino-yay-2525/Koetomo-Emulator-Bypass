import frida
import sys

package_name = "meetscom.s"

jscode = """
setImmediate(function(){
    console.log("script start");
    Java.perform(function(){
        console.log("start")
    
        var EmulatorDetector = Java.use("meetscom.s.utility.EmulatorDetector");
        EmulatorDetector.isAndroidSDKEmulator.implementation = function(){
            console.log("isAndroidSDKEmulator")
            return false;
        }
    
        var EmulatorDetector = Java.use("meetscom.s.utility.EmulatorDetector");
        EmulatorDetector.isBluestacks.implementation = function(){
            console.log("isBluestacks")
            return false;
        }
    
        var EmulatorDetector = Java.use("meetscom.s.utility.EmulatorDetector");
        EmulatorDetector.isNoxAppPlayer.implementation = function(){
            console.log("isNoxAppPlayer")
            return false;
        }
    
    });
});
"""

device = frida.get_usb_device()
pid = None
for a in device.enumerate_applications():
    if a.identifier == package_name:
        pid = a.pid
        break

process = device.attach(pid)
script = process.create_script(jscode)
print(f"\nSTART: {package_name}\n")

script.load()
sys.stdin.read()
