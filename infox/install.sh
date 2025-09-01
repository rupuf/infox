#!/data/data/com.termux/files/usr/bin/bash
set -e

PREFIX_DIR="$PREFIX"
SHARE_DIR="$PREFIX_DIR/share/infox"
BIN_FILE="$PREFIX_DIR/bin/infox"

echo "[*] Installing dependencies..."
pkg install -y python >/dev/null 2>&1 || true
pip install -q requests phonenumbers || true

echo "[*] Placing files..."
mkdir -p "$SHARE_DIR"
cp -f infox.py "$SHARE_DIR/infox.py"
cp -f logo.txt "$SHARE_DIR/logo.txt"
chmod +x "$SHARE_DIR/infox.py"

echo "[*] Creating launcher: infox"
cat > "$BIN_FILE" << 'LAUNCH'
#!/data/data/com.termux/files/usr/bin/bash
python "$PREFIX/share/infox/infox.py"
LAUNCH
chmod +x "$BIN_FILE"

echo "[✓] Installation complete! Run: infox"
