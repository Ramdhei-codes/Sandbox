import os
import curses

def listar_archivos_txt(ruta):
    archivos_txt = [archivo for archivo in os.listdir(ruta) if archivo.endswith(".txt")]
    return archivos_txt

def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    stdscr.clear()

    ruta_actual = os.getcwd()
    archivos_txt_disponibles = listar_archivos_txt(ruta_actual)

    if not archivos_txt_disponibles:
        stdscr.addstr(0, 0, "No hay archivos .txt en la carpeta actual.")
        stdscr.refresh()
        stdscr.getch()
        return

    opcion_seleccionada = 0

    while True:
        stdscr.clear()

        for i, archivo in enumerate(archivos_txt_disponibles):
            if i == opcion_seleccionada:
                stdscr.addstr(i, 0, f"> {archivo}")
            else:
                stdscr.addstr(i, 0, f"  {archivo}")

        stdscr.refresh()

        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and opcion_seleccionada > 0:
            opcion_seleccionada -= 1
        elif tecla == curses.KEY_DOWN and opcion_seleccionada < len(archivos_txt_disponibles) - 1:
            opcion_seleccionada += 1
        elif tecla == ord('\n'):
            break

    archivo_seleccionado = archivos_txt_disponibles[opcion_seleccionada]
    procesar_archivo(archivo_seleccionado)

def procesar_archivo(archivo_seleccionado):
    with open(archivo_seleccionado, 'r') as archivo:
        contenido = archivo.read()
        # Puedes realizar el procesamiento necesario con el contenido del archivo
        print(f"Contenido del archivo {archivo_seleccionado}:\n{contenido}")

if __name__ == "__main__":
    curses.wrapper(main)
