# Recreate the chart from the provided image as a clean timeline and a summary table.
# (No seaborn; separate plots; no explicit colors.)

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Data reconstructed from the image (unverified; based on labels shown)
data = [
    {"Giai đoạn": "Thứ ba", "Bắt đầu": 1730, "Kết thúc": 1830, "Khoảng thời gian": "1730–1830", "Số năm": 100},
    {"Giai đoạn": "Thứ tư", "Bắt đầu": 1830, "Kết thúc": 1890, "Khoảng thời gian": "1830–1890", "Số năm": 60},
    {"Giai đoạn": "Thứ năm", "Bắt đầu": 1890, "Kết thúc": 1929, "Khoảng thời gian": "1890–1929", "Số năm": 39},  # 1929-1890 = 39 (often rounded ~40)
    {"Giai đoạn": "Thứ sáu", "Bắt đầu": 1929, "Kết thúc": 1955, "Khoảng thời gian": "1929–1955", "Số năm": 26},   # 1955-1929 = 26 (often ~25)
]

df = pd.DataFrame(data)
df["Số năm (xấp xỉ)"] = [100, 60, 40, 25]

# Display the table for interactive viewing
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("Bảng giai đoạn Kondratieff (tái dựng)", df)

# --- Plot 1: Timeline (horizontal bar chart) ---
fig1, ax1 = plt.subplots(figsize=(10, 4.5))
ypos = list(range(len(df)))
lefts = df["Bắt đầu"].tolist()
widths = (df["Kết thúc"] - df["Bắt đầu"]).tolist()

for y, left, width, label in zip(ypos, lefts, widths, df["Giai đoạn"] + " (" + df["Khoảng thời gian"] + ")"):
    ax1.barh(y, width, left=left, align="center")
    # annotate approximate years near the center of each bar
    ax1.text(left + width/2, y, f"{int(width)} năm", va="center", ha="center")

ax1.set_yticks(ypos, df["Giai đoạn"] + " (" + df["Khoảng thời gian"] + ")")
ax1.set_xlabel("Năm")
ax1.set_title("Các giai đoạn công nghiệp & Sóng Kondratieff (tái dựng từ ảnh)")
ax1.grid(axis="x", linestyle="--", alpha=0.5)
fig1.tight_layout()
timeline_path = "/mnt/data/kondratieff_timeline.png"
fig1.savefig(timeline_path, dpi=200)

# --- Plot 2: Summary table as a figure ---
fig2, ax2 = plt.subplots(figsize=(9, 2.8))
ax2.axis("off")
summary_cols = ["Giai đoạn", "Khoảng thời gian", "Bắt đầu", "Kết thúc", "Số năm", "Số năm (xấp xỉ)"]
table = ax2.table(cellText=df[summary_cols].values,
                  colLabels=summary_cols,
                  loc="center")
table.auto_set_font_size(False)
table.set_fontsize(9.5)
table.scale(1, 1.6)
ax2.set_title("Tóm tắt các giai đoạn (tái dựng)", pad=12)
fig2.tight_layout()
table_path = "/mnt/data/kondratieff_table.png"
fig2.savefig(table_path, dpi=200)

timeline_path, table_path
