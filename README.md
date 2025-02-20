# Image Compressor

This Python script allows you to compress images in a specified folder. It uses the `Pillow` library to handle image compression and supports common image formats such as `.png`, `.jpg`, `.jpeg`, and `.webp`. The compressed images are saved in a separate folder.

## Features

- **Compress Images**: The script compresses images and saves them in a designated output folder.
- **Customizable Compression**: You can specify the output image format (e.g., `webp`, `jpeg`) and the compression quality.
- **Batch Processing**: The script processes all images in a specified folder at once.

### Libraries Used
- `Pillow`: For image manipulation and compression.
- `os`: For creating and managing folders.

## Requirements
### Prerequisites
1. Python 3.x installed on your system.

To run this script, you need to have Python installed on your computer. The project includes a virtual environment (`venv`) with all the required dependencies pre-installed. If you prefer to install the dependencies manually, you can use the `requirements.txt` file.

## How to Use

1. **Clone the Repository**: First, clone this repository to your local machine.

    ```bash
    git clone https://github.com/saadrafi/Batch_Image_Compress_In_Folder.git
    cd Batch_Image_Compress_In_Folder
    ```

2. **Set Up the Virtual Environment**:
   - If you want to use the provided virtual environment, activate it:
     - On **Windows**:
       ```bash
       .\imagecompressenv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source imagecompressenv\bin\activate
       ```
   - If you prefer to install the dependencies manually, skip this step and proceed to the next one.

3. **Install Dependencies (Optional)**: If you are not using the virtual environment, install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script**: Execute the script using Python.

    ```bash
    python compress_images_of_folder.py
    ```

5. **Enter the Folder Path**: When prompted, enter the path to the folder containing the images you want to compress.

    ```bash
    Enter the folder path containing images to compress: /path/to/your/images
    ```

6. **View the Results**: The script will create a folder named `compressed_images` in the same directory as the script. The compressed images will be saved in this folder.

## Customization

- **Change Output Format**: You can change the format of the compressed images by modifying the `type` parameter in the `compress_images_in_folder` function.

    ```python
    compress_images_in_folder(folder_name, type="jpeg")
    ```

- **Adjust Compression Quality**: You can adjust the quality of the compressed images by modifying the `quality` parameter in the `compress_images_in_folder` function.

    ```python
    compress_images_in_folder(folder_name, quality=70)
    ```

## Running on Different Computers

To run this script on a different computer, follow these steps:

1. **Install Python**: Ensure that Python is installed on the computer. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone the repository to the new computer.

    ```bash
    git clone https://github.com/saadrafi/Batch_Image_Compress_In_Folder.git
    cd Batch_Image_Compress_In_Folder
    ```

3. **Set Up the Virtual Environment**:
   - If you want to use the provided virtual environment, activate it:
     - On **Windows**:
       ```bash
       .\imagecompressenv\Scripts\activate
       ```
     - On **macOS/Linux**:
       ```bash
       source imagecompressenv\bin\activate
       ```
   - If you prefer to install the dependencies manually, skip this step and proceed to the next one.

4. **Install Dependencies (Optional)**: If you are not using the virtual environment, install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Script**: Execute the script using Python.

    ```bash
    python compress_images_of_folder.py
    ```

6. **Enter the Folder Path**: When prompted, enter the path to the folder containing the images you want to compress.

    ```bash
    Enter the folder path containing images to compress: /path/to/your/images
    ```

## Example Output

```bash
Enter the folder path containing images to compress: /path/to/your/images
Compressed image1.png and saved to compressed_images/image1.webp
Compressed image2.jpg and saved to compressed_images/image2.webp
```

---

## Notes
- Ensure the folder path you provide contains valid image files (e.g., `.png`, `.jpg`, `.jpeg`, `.webp`).
- The compression quality can be adjusted in the `compress_images_in_folder` function by modifying the `quality` parameter.
- If the folder does not contain any valid images, the script will not produce any output.

---
---

### Notes on Virtual Environments

- The virtual environment (`venv`) included in this project is pre-configured with all the necessary dependencies. Activating it ensures that the script runs in an isolated environment with the correct versions of the libraries.
- If you prefer not to use the virtual environment, you can install the dependencies globally using `pip install -r requirements.txt`.
- If you create a new virtual environment, make sure to install the dependencies using `pip install -r requirements.txt`.

---

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any contributions, whether they are bug fixes, new features, or improvements to the documentation.

## Support

If you encounter any issues or have any questions, please open an issue on the GitHub repository.

---

Enjoy using the Image Compressor! If you find it useful,  consider giving it a ⭐ on GitHub.
