# File Outputter for ChatGPT

## 用途 (Purpose)

本專案是一個簡易的 Python 腳本，可以**一次性將目前資料夾（含所有子目錄）所有檔案內容，格式化匯出到一個檔案**。
常用於將專案原始碼、腳本、設定檔等**自動整理成單一文本**，方便**丟給 ChatGPT 輔助分析、除錯或生成說明**。

---

## 功能特色

- 遞迴列出目前目錄及所有子目錄的檔案內容
- 可排除特定檔案與資料夾（支援萬用字元 `*`）
- 以明確格式標註每個檔案路徑與內容
- 所有內容輸出到單一檔案（`file_output.txt`）
- 自動顯示總檔案數、執行後等待使用者按鍵結束
- 適合大型專案一次匯出全部檔案給 ChatGPT 使用

---

## 使用方式

1. **將 `file_output.py` 複製到你的專案根目錄下**
2. （如需排除檔案，可在 `EXCLUDE_FILES`、`EXCLUDE_DIRS` 調整規則）
3. 在終端機執行：
    ```sh
    python file_output.py
    ```
4. 程式會自動產生 `file_output.txt`，檔案結尾會統計總共幾個檔案
5. 執行結束後會顯示「總共 X 個檔案」，並等待你按任意鍵關閉視窗

---

## 參數說明

- `EXCLUDE_FILES`：**排除的檔案**，可使用萬用字元 `*`（例如 `"*.md"`、`"file_output.*"`）
- `EXCLUDE_DIRS`：**排除的資料夾**（資料夾名稱相符時整個資料夾都不處理）
- 預設會把 Python 腳本自身、壓縮檔等都排除在外

---

## 輸出格式說明

每個檔案會以如下格式標示（方便 ChatGPT 分析）：

```
//=========================================================================================
目錄: /<目前資料夾>/<相對路徑>
<檔案內容>
```

最後一行會是：

```
總共 <N> 個檔案
```

---

## 適用情境

- 專案檔案太多、不想一個一個貼給 ChatGPT
- 需要複雜多檔案結構的內容統一分析
- 快速產生「單一檔案」供 AI 讀取與討論

---

## License

MIT License

---

# English Version

## Purpose

A simple Python script to recursively output the contents of all files (including subdirectories) in the current directory to a single text file. Designed for use cases like providing entire project sources to ChatGPT for analysis, debugging, or documentation generation.

---

## Features

- Recursively lists all files in current directory and subdirectories
- Supports exclude patterns (wildcard `*` for files/folders)
- Outputs every file with a clear header showing its path
- All content is saved to a single file (`file_output.txt`)
- Displays the total number of files at the end, and waits for any key before exit

---

## Usage

1. Copy `file_output.py` to your project root
2. Edit `EXCLUDE_FILES` and `EXCLUDE_DIRS` to match files/folders to skip (wildcard `*` supported)
3. Run in terminal:
    ```sh
    python file_output.py
    ```
4. The script will generate `file_output.txt` with all file contents, and show the total file count at the end
5. After execution, the program waits for you to press any key before exiting

---

## Parameter Explanation

- `EXCLUDE_FILES`: Wildcard-supported patterns to exclude files (e.g. `*.md`, `file_output.*`)
- `EXCLUDE_DIRS`: Folder names to exclude (whole folders will be skipped if names match)

---

## Output Format

Each file will be shown as below (easy for ChatGPT to parse):

```
//=========================================================================================
目錄: /<base_folder>/<relative_path>
<file content>
```

Last line will be:

```
總共 <N> 個檔案
```

---

## Use Cases

- Projects with too many files to paste one-by-one to ChatGPT
- Complex multi-file structures needing batch export for AI analysis
- Fast generation of a single text file for LLM input
