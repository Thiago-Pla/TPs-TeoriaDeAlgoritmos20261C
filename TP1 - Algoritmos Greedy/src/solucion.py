def planificar_videos(videos):
    videos_ordenados = sorted(videos, key=lambda x: x[1], reverse=True)
    tiempo_scaloni = 0
    tiempo_total= 0
    for s_i, a_i in videos_ordenados:
        tiempo_scaloni += s_i
        tiempo_fin_ayudante = tiempo_scaloni + a_i
        tiempo_total = max(tiempo_fin_ayudante, tiempo_total)
    return videos_ordenados, tiempo_total


def main():
    videos = []
    ruta_archivo = "archivo..."
    with open(ruta_archivo, 'r') as archivo:
        next(archivo)
        for linea in archivo:
            s_i, a_i = map(int, linea.strip().split(','))
            videos.append((s_i, a_i))
    orden_optimo, tiempo_total = planificar_videos(videos)

    print(f"Orden de videos: {orden_optimo}")
    print(f"Tiempo total: {tiempo_total}")

if __name__ == '__main__':
    main()