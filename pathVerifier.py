import os

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
            #print(f'Found the file at: {result}')
            return result
        else:
            print('No file found.')
            return result    

if __name__ == "__main__":

    decompiled_path = "SignatureDetectorOriginal"
    file = 'FirstFragment.smali'

    print(apkPathVerifier(decompiled_path))
    #print(os.path.join(apkPathVerifier(decompiled_path), file))

