# 數獨求解器 (numpy)
本專案是一個使用 `numpy` 的簡單數獨求解與檢查程式。包含求解器、基本 I/O 工具，以及多次運行記錄輸出功能。英文說明位於 `README.md`，中文說明在本檔案。

## 功能
- 從 `sudoku.txt` 載入數獨題目（若檔案不存在則隨機生成）。
- 使用回溯法檢查並嘗試解題。
- 結果會儲存在 `sudoku_results.txt`。

## 需求
- Python 3.8+
- 參考 `requirements.txt` 安裝相依套件。

## 使用方法
1. 準備 `sudoku.txt`（9x9，空格分隔，0 表示空格），若無則會隨機生成。
2. 執行：

```powershell
python sudoku_solver.py
```

遵循互動提示選擇執行次數與是否從上次結果繼續。

輸出預設寫入 `sudoku_results.txt`。`.gitignore` 已將 `bot.py`、結果檔和臨時檔排除。