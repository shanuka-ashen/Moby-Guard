import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import shutil


def apkToJava(apk_file, java_dir):
    # Use absolute paths for jadx.bat and APK file
    jadx_path = os.path.join(os.path.dirname(__file__), 'jadx.bat')
    apk_path = os.path.join(os.path.dirname(__file__), apk_file)
    
    try:
        subprocess.run([jadx_path, '-d', java_dir, apk_path], check=True, shell=True)
        print(f"APK converted to Java successfully - '{java_dir}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting APK to Java: {e}")
        exit(1)
        
        
def apkTooldecompile(apk_file, decompiled_path):  
    apk_tool = os.path.join(os.path.dirname(__file__), 'apktool.jar')
    apk_path = os.path.join(os.path.dirname(__file__), apk_file )

    if os.path.exists(decompiled_path):
        # If it exists, forcefully remove the directory and its contents
        shutil.rmtree(decompiled_path)
    
    try:
        subprocess.run([apk_tool, 'd', apk_path], check=True, shell=True)
        print(f"APK decompiled successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error decompiling APK: {e}")
        exit(1)
        

def apkToolBuild(decompiled_path):  
    apk_tool = os.path.join(os.path.dirname(__file__), 'apktool.jar')
    #folder_selected = filedialog.askdirectory(title=decompiled_path)
    
    try:
        subprocess.run(['java', '-jar', apk_tool, 'b', '-f', '--use-aapt2', '-o', 'build.apk', decompiled_path], check=True, shell=True)
        print(f"APK build successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error building APK: {e}")
        exit(1)        

def apkZipAlignAndSigned(apk_file, output_apk_path, final_apk_name):
    zipalign_command = [
        '.\zipalign',
        '-p', '4',  # 4-byte alignment is recommended
        apk_file,
        output_apk_path
    ]
    subprocess.run(zipalign_command, check=True)

    sign_command = [
        'java.exe',
        '-jar',
        'apksigner.jar', 'sign',
        '--key', 'key.pk8',
        '--cert', 'certificate.pem',
        '--v4-signing-enabled', 'false',
        '--out', 
        output_apk_path,
        output_apk_path
    ]
    subprocess.run(sign_command, check=True)

    shutil.move(output_apk_path, final_apk_name)
    print(f'APK signed and zipaligned successfully. Output APK saved as: {final_apk_name}')


def apkPathVerifier(decompiled_path):

        def find_example_smali(decompiled_path):
            for root, dirs, files in os.walk(decompiled_path):
                if os.path.basename(root).startswith('smali'):
                    for sub_dir in dirs:
                        sub_dir_path = os.path.join(root, sub_dir)
                        for dir_root, _, dir_files in os.walk(sub_dir_path):
                            for file_name in dir_files:
                                if file_name.startswith('FirstFragment.') and file_name.endswith('smali'):
                                    return os.path.join(dir_root)
            return None

        result = find_example_smali(decompiled_path)

        if result:
            print(f'Found the file at: {result}')
            return result
        else:
            print('No file found.')
            return result    


def smaliFixRoot(smali_solution, smali_code):
    try:
        # Read content from the smali_solution file
        with open(smali_solution, 'r') as file1:
            smali_solution_content = file1.read()

        # Read content from the smali_code file
        with open(smali_code, 'r') as file2:
            smali_code_content = file2.read()

        # Append content of the smali_solution file to the smali_code file
        merged_content = smali_code_content + '\n' + smali_solution_content

        # Write the merged content back to the smali_code file
        with open(smali_code, 'w') as file2:
            file2.write(merged_content)

        print("smali fixation addedd successfully.")

    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print("An error occurred:", str(e))    


def smaliFixIntegrity(smali_solution, smali_code, integrityFragment, smali_code_directory):
    try:
        # Read content from the smali_solution file
        with open(smali_solution, 'r') as file1:
            smali_solution_content = file1.read()

        # Read content from the smali_code file
        with open(smali_code, 'r') as file2:
            smali_code_content = file2.read()

        # Append content of the smali_solution file to the smali_code file
        merged_content = smali_code_content + '\n' + smali_solution_content

        # Write the merged content back to the smali_code file
        with open(smali_code, 'w') as file2:
            file2.write(merged_content)

        shutil.copy(integrityFragment, smali_code_directory)    

        print("smali fixation addedd successfully.")

    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print("An error occurred:", str(e))                    



        

if __name__ == "__main__":
    apk_file = "SignatureDetectorOriginal.apk"
    decompiled_path = "SignatureDetectorOriginal"
    output_apk_path = 'zipalignedAPK.apk'
    final_apk_name = 'final.apk'
    build_name = 'build.apk'
    fragmentFile = 'FirstFragment.smali'
    integrityFragment = 'FirstFragment$4.smali'
    magisk_solution = "magiskDetect.txt"
    integrity_solution = 'integritycheck.txt'
    

    apkTooldecompile(apk_file, decompiled_path) 

    smali_code_directory = apkPathVerifier(decompiled_path)
    smali_code = os.path.join(smali_code_directory, fragmentFile)
    
    #smaliFixIntegrity(integrity_solution, smali_code, integrityFragment, smali_code_directory)

    apkToolBuild(decompiled_path)
    apkZipAlignAndSigned('build.apk', output_apk_path, final_apk_name)















    #java_dir = os.path.join(os.path.dirname(__file__), "output")  # Specify the output directory
    # if len(sys.argv) < 2:
        # print("Usage: python script.py <COMMAND> [<APK_FILE> <DECOMPILED_PATH> <OUTPUT_DIR>]")
        # sys.exit(1)

    # command = sys.argv[1]
    # commands = {
        # "apkToJava": apkToJava,
        # "apkTooldecompile": apkTooldecompile,
        # "apkToolBuild": apkToolBuild
    
    
