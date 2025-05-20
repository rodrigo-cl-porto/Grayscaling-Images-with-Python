from PIL import Image
import os

def convert_to_grayscale(image_path:str, gray_shades:int=256, method:str='luma') -> None:
    try:

        if not(gray_shades >= 2 and gray_shades <=256):
            return "Error: It's not possible to create an image with {gray_shades} gray shades."

        with Image.open(image_path) as img:

            pixel_map = img.load()
            width, height = img.size

            for i in range(width):
                for j in range(height):
                    R, G, B = img.getpixel((i, j))

                    if method in ['luma', 'luminance']:
                        method = 'luma'
                        gray = int(0.299*R + 0.587*G + 0.114*B)
                    elif method == 'averaging':
                        gray = int((R + G + B)/3)
                    elif method == 'desaturation':
                        gray = int((max(R, G, B) + min(R, G, B))/2)
                    elif method == 'maximum_decomposition':
                        gray = max(R, G, B)
                    elif method == 'minimum_decomposition':
                        gray = min(R, G, B)
                    elif method in ['r', 'red']:
                        method = 'red'
                        gray = R
                    elif method in ['g', 'green']:
                        method = 'green'
                        gray = G
                    elif method in ['b', 'blue']:
                        method = 'blue'
                        gray = B
                    else:
                        return "Error: Method {method} is not valid."
                    
                    conversion_factor = 255 / (gray_shades - 1)
                    shade = int(gray/conversion_factor + 0.5)
                    gray = int(shade * conversion_factor)
                    pixel_map[i, j] = (gray, gray, gray)

            new_image_path = '.'.join(image_path.split('.')[:-1]) + f'_{gray_shades}-{method}-grayscale.png'
            img.save(new_image_path, format="png")

    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    methods = ['luma', 'averaging', 'desaturation', 'maximum_decomposition', 'minimum_decomposition', 'r', 'g', 'b']
    lena = 'images/lena.jpg'
    for method in methods:
        convert_to_grayscale(lena, method=method)
        convert_to_grayscale(lena, gray_shades=2, method=method)