import subprocess
import os
import shutil

def sign_apk(input_apk, output_apk):
    # Zipalign the signed APK
    zipalign_command = [
        '.\zipalign',
        '-p', '4',  # 4-byte alignment is recommended
        input_apk,
        output_apk_path
    ]
    subprocess.run(zipalign_command, check=True)


    # Sign the APK using jarsigner tool

    sign_command = [
        'java.exe',
        '-jar',
        'apksigner.jar', 'sign',
        '--key', 'apkeasytool.pk8',
        '--cert', 'apkeasytool.pem',
        '--v4-signing-enabled', 'false',
        '--out', 
        output_apk_path,
        output_apk_path
    ]
    subprocess.run(sign_command, check=True)



# Example usage
input_apk_path = 'Amana.apk'  # Path to the APK you want to sign and zipalign
output_apk_path = 'zipalignedAPK.apk'  # Path where the signed and aligned APK will be saved
final_apk_name = 'final.apk'

sign_apk(input_apk_path, output_apk_path)
#os.rename(output_apk_path, 'final.apk')
shutil.move(output_apk_path, final_apk_name)

print(f'APK signed and zipaligned successfully. Output APK saved as: {final_apk_name}')
