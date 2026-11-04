#!/usr/bin/env bash
# Corre una etapa del agente (Codex) con el prompt mejorado y guarda la evidencia.
# Uso: evidencia/correr.sh <nn> <etapa> ["texto extra para la línea ETAPA"]
# CODEX_HOME aislado: sólo credenciales, sin instrucciones personales ni hooks.
set -euo pipefail
cd "$(dirname "$0")/.."
NN=$1; ETAPA=$2; EXTRA=${3:-}
D=evidencia/corridas/$NN; mkdir -p "$D"
{ cat prompts/prompt_mejorado.md; echo; echo "ETAPA: $ETAPA $EXTRA"; } > "$D/prompt.txt"
date -Iseconds > "$D/inicio.txt"; git rev-parse HEAD >> "$D/inicio.txt"
CODEX_HOME=/home/adminodoo/informes/bi-integrador/.codex-home-u4t1 codex exec -C "$PWD" -s workspace-write \
  --json -o "$D/respuesta.md" - < "$D/prompt.txt" | tee "$D/transcripcion.jsonl" | python3 -u -c '
import sys,json
for l in sys.stdin:
    try: e=json.loads(l)
    except Exception: continue
    it=e.get("item",{})
    if e.get("type")=="item.completed" and it.get("type") in ("agent_message","command_execution","file_change"):
        print("·", it.get("type"), (it.get("text") or it.get("command") or str(it.get("changes")))[:160])
'
echo "exit=${PIPESTATUS[0]}" > "$D/fin.txt"; date -Iseconds >> "$D/fin.txt"
git status --short >> "$D/fin.txt"
echo "CORRIDA $NN TERMINADA"
