"""Actualiza el índice de un docx con LibreOffice (UNO) y exporta PDF y, opcionalmente, un docx con el índice al día.

Uso: python3 src/u4-t1/actualizar_indice.py entrada.docx salida.pdf [salida.docx]
Hace falta LibreOffice con python3-uno. Sustituye a Word sólo si el laptop no está disponible.
"""
import sys, time, subprocess, uno
from com.sun.star.beans import PropertyValue
def pv(n,v):
    p=PropertyValue(); p.Name=n; p.Value=v; return p
src, pdf = sys.argv[1], sys.argv[2]
proc=subprocess.Popen(["soffice","--headless","--invisible","--norestore","-env:UserInstallation=file:///tmp/lo_u4t1_perfil",'--accept=socket,host=localhost,port=2099;urp;'])
ctx=None
for _ in range(40):
    try:
        local=uno.getComponentContext(); res=local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver",local)
        ctx=res.resolve("uno:socket,host=localhost,port=2099;urp;StarOffice.ComponentContext"); break
    except Exception: time.sleep(0.5)
desk=ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
doc=desk.loadComponentFromURL(uno.systemPathToFileUrl(src),"_blank",0,(pv("Hidden",True),))
idx=doc.getDocumentIndexes()
for i in range(idx.getCount()): idx.getByIndex(i).update()
doc.refresh()
for i in range(idx.getCount()): idx.getByIndex(i).update()
doc.storeToURL(uno.systemPathToFileUrl(pdf),(pv("FilterName","writer_pdf_Export"),))
if len(sys.argv)>3: doc.storeToURL(uno.systemPathToFileUrl(sys.argv[3]),(pv("FilterName","MS Word 2007 XML"),))
print("indices",idx.getCount())
doc.close(True)
try: desk.terminate()
except Exception: pass
proc.wait(timeout=30)
