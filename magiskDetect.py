import os
import subprocess

# Define the known packages
knownRootAppsPackages = {
    "com.noshufou.android.su",
    "com.noshufou.android.su.elite",
    "com.shanukashen",
    # Add other packages here
}

knownDangerousAppsPackages = {
    "com.koushikdutta.rommanager",
    "com.koushikdutta.rommanager.license",
    # Add other packages here
}

knownRootCloakingPackages = {
    "com.devadvance.rootcloak",
    "com.devadvance.rootcloakplus",
    # Add other packages here
}

# Function to search for known packages in a directory
def search_known_packages(directory):
    found_packages = set()

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

                for package in knownRootAppsPackages:
                    if package in content:
                        found_packages.add(package)
                for package in knownDangerousAppsPackages:
                    if package in content:
                        found_packages.add(package)
                for package in knownRootCloakingPackages:
                    if package in content:
                        found_packages.add(package)

    return found_packages

def print_missing_packages(known_packages, found_packages):
    missing_packages = known_packages - found_packages
    if missing_packages:
        print("Missing Packages:")
        for package in missing_packages:
            print(f" - {package}")

def detect_magisk(directory):
    magisk_detected = False

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

                if "zygote" in content:
                    magisk_detected = True
                    break

    return magisk_detected

def decompile_apk(apk_file, output_dir):
    jadx_path = r'G:\Research\Magisk Proof\Code\jadx-1.4.7\bin\jadx.bat'
    try:
        subprocess.run([jadx_path, "-d", output_dir, apk_file], check=True)
        print(f"APK decompiled successfully to '{output_dir}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error decompiling APK: {e}")
        exit(1)

if __name__ == "__main__":
    apk_file = r'G:\Research\Magisk Proof\Code\AmanaBank.apk'
    output_dir = r'G:\Research\Magisk Proof\Code\Extracted'

    decompile_apk(apk_file, output_dir)

    sources_dir = os.path.join(output_dir, "sources")

    if os.path.exists(sources_dir):
        found_packages = search_known_packages(sources_dir)
        print_missing_packages(knownRootAppsPackages | knownDangerousAppsPackages | knownRootCloakingPackages, found_packages)

        magisk_detected = detect_magisk(sources_dir)
        if magisk_detected:
            print("Magisk detection available")
        else:
            print("Magisk detection is not available")
    else:
        print(f"Directory '{sources_dir}' does not exist.")
