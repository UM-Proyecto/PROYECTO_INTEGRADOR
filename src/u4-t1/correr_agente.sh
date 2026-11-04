#!/usr/bin/env bash
# Corre una etapa del agente de la wiki con el prompt mejorado y guarda la evidencia.
# Uso: src/u4-t1/correr_agente.sh <nn> <etapa> ["texto extra para la línea ETAPA"]
#
# Agente: Claude Code (claude -p, modelo Opus) con un directorio de configuración aislado
# (CLAUDE_CONFIG_DIR con sólo las credenciales): no carga instrucciones personales, memoria,
# hooks ni servidores MCP. Puede leer y editar archivos de la carpeta y correr python3 y
# comandos de lectura; no puede hacer commits ni usar la red.
# La primera corrida se intentó con Codex y se cortó por falta de cuota
# (docs/u4-t1/evidencia/corridas/00_codex_sin_cuota).
set -euo pipefail
cd "$(dirname "$0")/../.."
NN=$1; ETAPA=$2; EXTRA=${3:-}
D=docs/u4-t1/evidencia/corridas/$NN; mkdir -p "$D"
{ cat docs/u4-t1/prompts/prompt_mejorado.md; echo; echo "ETAPA: $ETAPA $EXTRA"; } > "$D/prompt.txt"
{ date -Iseconds; git rev-parse HEAD; } > "$D/inicio.txt"
set +e
CLAUDE_CONFIG_DIR="$HOME/.cache/claude-home-u4t1" claude -p --model opus --strict-mcp-config \
  --permission-mode acceptEdits \
  --allowedTools "Read Edit Write Glob Grep Bash(python3:*) Bash(ls:*) Bash(cat:*) Bash(head:*) Bash(tail:*) Bash(wc:*) Bash(grep:*) Bash(find:*) Bash(sha256sum:*) Bash(git status:*) Bash(git diff:*) Bash(git log:*)" \
  --disallowedTools "Bash(git commit:*) Bash(git push:*) Bash(git add:*) Bash(curl:*) Bash(wget:*) WebFetch WebSearch" \
  --output-format stream-json --verbose < "$D/prompt.txt" | tee "$D/transcripcion.jsonl" | python3 -u -c '
import sys,json
for l in sys.stdin:
    try: e=json.loads(l)
    except Exception: continue
    if e.get("type")=="assistant":
        for c in e["message"].get("content",[]):
            if c.get("type")=="text": print("·", c["text"][:200].replace("\n"," "))
            elif c.get("type")=="tool_use": print("  >", c["name"], json.dumps(c["input"],ensure_ascii=False)[:150])
    elif e.get("type")=="result":
        open(sys.argv[1],"w").write(e.get("result") or "")
        print("RESULTADO:", e.get("subtype"), "turnos", e.get("num_turns"), "costo_usd", e.get("total_cost_usd"))
' "$D/respuesta.md"
RC=${PIPESTATUS[0]}
set -e
{ echo "exit=$RC"; date -Iseconds; git status --short; } > "$D/fin.txt"
echo "CORRIDA $NN TERMINADA exit=$RC"
