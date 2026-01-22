import cv2


def draw_center_red_box(image_path, box_width_ratio=0.2, box_height_ratio=0.2, output_path=None):
    """
    Otwiera obraz z pliku, rysuje czerwoną ramkę na środku obrazu.

    :param image_path: ścieżka do pliku obrazu
    :param box_width_ratio: szerokość ramki jako ułamek szerokości obrazu (domyślnie 20%)
    :param box_height_ratio: wysokość ramki jako ułamek wysokości obrazu (domyślnie 20%)
    :param output_path: jeśli podany, zapisuje obraz z ramką do pliku
    """
    # Wczytanie obrazu
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Nie udało się wczytać obrazu: {image_path}")

    height, width = img.shape[:2]

    # Wyliczenie rozmiaru ramki w pikselach
    box_width = int(width * box_width_ratio)
    box_height = int(height * box_height_ratio)

    # Wyliczenie współrzędnych narożników prostokąta
    x_center = width // 2
    y_center = height // 2

    x1 = x_center - box_width // 2
    y1 = y_center - box_height // 2
    x2 = x_center + box_width // 2
    y2 = y_center + box_height // 2

    # Rysowanie czerwonej ramki (BGR: (0,0,255))
    cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

    # Zapis lub pokazanie obrazu
    if output_path:
        cv2.imwrite(output_path, img)
        print(f"Obraz zapisany do: {output_path}")
    else:
        cv2.imshow("Image with Red Box", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Przykład użycia:
draw_center_red_box("3d-bialy-czlowiek-w-mile-widziany-pozie-700-139421038.jpg", output_path="zdjecie_z_ramka.jpg")
