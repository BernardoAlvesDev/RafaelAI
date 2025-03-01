import cv2

def process_video(
    input_file='input_video.mp4',
    output_file='output_video.mp4',
    background_present=True,
    show_window=False
):
    """
    Lê o vídeo 'input_file' e gera um vídeo anotado em 'output_file'.
    Se background_present=False, apaga o fundo (frame zerado).
    """
    # Abre o vídeo de entrada
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print(f"Erro: Não foi possível abrir o vídeo {input_file}.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps_input = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define o VideoWriter de saída
    out = cv2.VideoWriter(output_file, fourcc, fps_input, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if not background_present:
            # Apaga totalmente a imagem
            frame = frame * 0

        # Cores e posições de retângulos (placeholder)
        before_occlusion_color = (0, 255, 0)  # Verde
        after_occlusion_color = (0, 0, 255)  # Vermelho

        # Desenha retângulos
        cv2.rectangle(frame, (100, 200), (200, 300), before_occlusion_color, 2)
        cv2.rectangle(frame, (300, 200), (400, 300), after_occlusion_color, 2)

        # Labels
        cv2.putText(frame, "Car: what the AI sees", (100, 190),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, before_occlusion_color, 2)
        cv2.putText(frame, "Car: what the human sees", (300, 190),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, after_occlusion_color, 2)

        # Salva o frame anotado
        out.write(frame)

        if show_window:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def combine_videos(
    file1='output_background_present.mp4',
    file2='output_background_absent.mp4',
    output_file='combined_output.mp4'
):
    """
    Combina dois vídeos lado a lado e salva em output_file.
    """
    cap1 = cv2.VideoCapture(file1)
    cap2 = cv2.VideoCapture(file2)

    if not cap1.isOpened() or not cap2.isOpened():
        print("Erro: Não foi possível abrir um dos vídeos para combinação.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps1 = cap1.get(cv2.CAP_PROP_FPS)
    fps2 = cap2.get(cv2.CAP_PROP_FPS)

    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Usa a altura máxima e soma as larguras
    out_width = width1 + width2
    out_height = max(height1, height2)

    # Idealmente usar uma taxa de FPS que funcione para ambos os vídeos
    out_fps = min(fps1, fps2) if fps1 > 0 and fps2 > 0 else 30

    out = cv2.VideoWriter(output_file, fourcc, out_fps, (out_width, out_height))

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            # Se um dos vídeos terminar, paramos (ou poderíamos inserir tela preta)
            break

        # Ajusta para mesma altura antes de concatenar
        frame1 = cv2.resize(frame1, (width1, out_height))
        frame2 = cv2.resize(frame2, (width2, out_height))

        # Concatena horizontalmente
        combined_frame = cv2.hconcat([frame1, frame2])
        out.write(combined_frame)

    cap1.release()
    cap2.release()
    out.release()


if __name__ == '__main__':
    # Exemplo de uso
    process_video(
        input_file='input_video.mp4',
        output_file='output_background_present.mp4',
        background_present=True,
        show_window=False
    )
    process_video(
        input_file='input_video.mp4',
        output_file='output_background_absent.mp4',
        background_present=False,
        show_window=False
    )
    combine_videos(
        file1='output_background_present.mp4',
        file2='output_background_absent.mp4',
        output_file='combined_output.mp4'
    )
