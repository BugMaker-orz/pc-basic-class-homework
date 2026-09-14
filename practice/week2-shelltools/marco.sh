MARCO_DIR=""
marco() { MARCO_DIR="$PWD"; echo "saved: $MARCO_DIR"; }
polo() { [ -n "$MARCO_DIR" ] && cd "$MARCO_DIR" && echo "cd to $PWD" || echo "no marco saved"; }
