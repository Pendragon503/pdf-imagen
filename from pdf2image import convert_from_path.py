import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os

def select_pdf():
    # Abrir el diálogo para seleccionar el archivo PDF
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        pdf_label.config(text=f"Archivo seleccionado: {os.path.basename(pdf_path)}")
        return pdf_path
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo PDF.")

def select_output_folder():
    # Abrir el diálogo para seleccionar la carpeta de destino
    output_folder = filedialog.askdirectory()
    if output_folder:
        folder_label.config(text=f"Carpeta seleccionada: {output_folder}")
        return output_folder
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta de salida.")

def convert_pdf_to_images():
    pdf_path = select_pdf()
    output_folder = select_output_folder()

    if pdf_path and output_folder:
        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image_path = os.path.join(output_folder, f"page_{i + 1}.png")
                image.save(image_path, "PNG")
            messagebox.showinfo("Éxito", f"Conversión completada. Las imágenes se guardaron en {output_folder}.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al convertir el PDF: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de PDF a Imágenes PNG")
root.geometry("400x200")

# Etiquetas y botones
pdf_label = tk.Label(root, text="Selecciona un archivo PDF", pady=10)
pdf_label.pack()

select_pdf_button = tk.Button(root, text="Seleccionar PDF", command=select_pdf)
select_pdf_button.pack()

folder_label = tk.Label(root, text="Selecciona una carpeta de salida", pady=10)
folder_label.pack()

select_folder_button = tk.Button(root, text="Seleccionar Carpeta de Salida", command=select_output_folder)
select_folder_button.pack()

convert_button = tk.Button(root, text="Convertir PDF a Imágenes", command=convert_pdf_to_images, pady=10)
convert_button.pack()

root.mainloop()
