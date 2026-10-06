#!/bin/zsh
set -e
SCRIPT_DIR="${0:A:h}"
STUDY_DIR="${SCRIPT_DIR:h}"
python3 "/home/alfzki/Documents/OSL/.agents/skills/study-assistant/scripts/build_dashboard.py" "$STUDY_DIR"
echo
echo "Dashboard berhasil diperbarui: $SCRIPT_DIR/dashboard.html"
echo "Tekan tombol apa saja untuk menutup..."
read -k 1
