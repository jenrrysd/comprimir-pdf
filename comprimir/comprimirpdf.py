import os
import subprocess, webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox

def comprimir_pdf():
    # Seleccionar archivo PDF de entrada
    input_pdf = filedialog.askopenfilename(
        title="Selecciona el PDF a comprimir",
        filetypes=[("Solo Archivos PDF", "*.pdf")]
    )
    
    if not input_pdf:
        return  # El usuario canceló

    # Obtener la ruta del archivo original
    directorio = os.path.dirname(input_pdf)

    nombre_base = os.path.splitext(os.path.basename(input_pdf))[0]  # Obtener nombre sin extensión
    extension = os.path.splitext(input_pdf)[1]  # Obtener extensión (.pdf)

    # Generar nombre de salida manteniendo el original y agregando "_copia"
    output_pdf = os.path.join(directorio, f"{nombre_base}_copia{extension}")

    # Ejecutar Ghostscript
    try:
        subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            "-dPDFSETTINGS=/ebook",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_pdf}",
            input_pdf
        ], check=True)
        messagebox.showinfo(
            "Éxito",
            f"PDF comprimido como:\n{output_pdf}"
        )
    except subprocess.CalledProcessError:
        messagebox.showerror(
            "Error",
            "Falló la compresión. Verifica que Ghostscript esté instalado."
        )
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "Ghostscript no está instalado.\nInstálalo con 'sudo apt install ghostscript'."
        )

# Abrir web
def abrir_web():
    webbrowser.open("https://dextre.xyz")

# Configuración de la ventana
root = tk.Tk()
root.title("Compresor de PDF")
root.geometry("400x200")

# Botón para seleccionar y comprimir PDF
btn = tk.Button(
    root,
    text="Seleccionar PDF y Comprimir",
    command=comprimir_pdf,
    font=("Arial", 12),
    padx=20,
    pady=10
)
btn.pack(expand=True)

# mensaje de la aplicación
etiqueta = tk.Label(
    root,
    text="Esta aplicación reduce un 60% \n del peso original del documento",
    font=("Arial", 9),
    fg="black",
    pady=10
)
etiqueta.pack()

# creditos al final de la ventana
footer = tk.Label(
    root,
    text="Creado por: Jenrry Soto Dextre \n Web: https://dextre.xyz",
    font=("Arial", 8),
    fg="gray",
    cursor="hand2"
)
footer.pack

# Cambia de color al pasar el mouse sobre el enlace
footer.bind("<Enter>", lambda e: footer.config(fg="black"))
footer.bind("<Leave>", lambda e: footer.config(fg="gray"))

footer.pack(side="bottom", pady=10)
footer.bind("<Button-1>", lambda e: abrir_web())

root.mainloop()
