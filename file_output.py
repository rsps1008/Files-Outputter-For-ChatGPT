import os
import fnmatch

EXCLUDE_FILES = ["file_output.*", "*.md", "*.zip"]
EXCLUDE_DIRS = ["META-INF"]

def should_exclude_dir(dirpath):
    for exc in EXCLUDE_DIRS:
        if os.sep + exc + os.sep in dirpath + os.sep or dirpath.endswith(os.sep + exc):
            return True
    return False

def is_exclude_file(filename):
    for pattern in EXCLUDE_FILES:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def main():
    root_dir = os.getcwd()
    base_name = os.path.basename(root_dir)
    output_lines = []
    file_count = 0

    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        if should_exclude_dir(dirpath):
            continue
        for filename in filenames:
            if is_exclude_file(filename):
                continue
            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, root_dir)
            header = "//=========================================================================================\n目錄: /{}/{}".format(base_name, rel_path.replace("\\", "/"))
            output_lines.append(header)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    output_lines.append(content)
            except Exception as e:
                err_msg = f"⚠️ 無法讀取內容: {e}"
                output_lines.append(err_msg)
            output_lines.append("")
            file_count += 1

    # 檔案總數統計（內容最後與畫面最後都印）
    summary = f"總共 {file_count} 個檔案"
    output_lines.append(summary)

    with open("file_output.txt", "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(output_lines))

    print(summary)
    input("按任意鍵離開...")

if __name__ == "__main__":
    main()
