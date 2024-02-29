from selenium import webdriver
import os
import pyautogui
import time
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


# metodos
def isValid(filepath):
    extension = os.path.splitext(filepath)

    if extension[1] != ".zip" or extension[1] != ".rar" or extension[1] != ".7z":
        return True
    else:
        return False


def mandarArchivo(archivo):
    try:
        upload_input = wait.until(EC.presence_of_element_located((By.NAME, 'file')))
        upload_input.send_keys(archivo)
    except Exception as e:
        print(f"Unable to upload:\n\n\n{e}")


def upload(archivo, directorio):
    mandarArchivo(archivo)

    # verifica si ya existe el archivo en libgen
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, 'file-input-submit'),
                'already exists in '
            )
        )
        print(f"El archivo: '{archivo}' ya existe!")
        shutil.move(archivo, uploaded_folder)
        driver.find_element(By.LINK_TEXT, 'upload a file').click()
        return

    except:
        print(f"archivo pasa exitosamente! {file_path}")

    """
    wait.until(EC.presence_of_element_located((By.ID, 'progress_text')))

    try:
        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, 'progress_text'),
                'Uploading has been started...'
            )
        )
    except Exception as e:
        print(e)

    """
    # sirve para poner el nombre del pdf, hacer click en "amazon.com" y darle al fetch
    dir_archivo = os.path.join(directorio)
    nombre_file = os.listdir(dir_archivo)
    print(nombre_file)


"""
    isbn_input = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.NAME, "metadata_query")))
    isbn_input.send_keys(f"{nombre_file[0]}")

    select = Select(driver.find_element(By.NAME, "metadata_source"))
    select.select_by_visible_text("Amazon.com")

    fetch_button = driver.find_element(By.NAME, "fetch_metadata")
    fetch_button.click()

    # le da a submit
    submit_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit')))
    submit_input.click()

    print("Uploaded!")

    shutil.move(archivo, uploaded_folder)

    driver.find_element(By.LINK_TEXT, 'Go to the upload page').click()
"""


def verificarISBN(file_dir):
    for archivo in os.listdir(file_dir):
        full_path = os.path.join(file_dir, archivo)
        directory_name = os.path.join(file_dir)

        if os.path.isdir(full_path):
            verificarISBN(full_path)
        else:
            file_name = os.listdir(file_dir)[0].split(".")[0]
            if len(file_name) != 10:
                os.rename(full_path, f"{directory_name}.{os.listdir(file_dir)[0].split('.')[1]}")
            else:
                print(f"Esta en ISBN-10 con el nombre de: {file_name}")


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)

    folder_path = os.path.join(base_path, 'to_upload')
    uploaded_folder = os.path.join(base_path, 'uploaded')

    verificarISBN(folder_path)

    username = 'genesis'
    password = 'upload'

    chrome_options = Options()

    # ruta del driver
    driver_path = r'C:\Users\carlo\Desktop\chrome-headless-shell.exe'

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 1200)

    url = f'http://library.bz/main/upload/'

    driver.get(url)

    time.sleep(1)

    # Enviar el nombre de usuario y la contraseña
    pyautogui.write('genesis')
    pyautogui.press('tab')
    pyautogui.write('upload')
    pyautogui.press('enter')

    for file in os.listdir(folder_path):
        if not os.path.isdir(os.path.join(folder_path, file)):
            file_path = os.path.join(folder_path, file)

            if isValid(file_path):
                upload(file_path, folder_path)

                # driver.quit()
            else:
                print("archivo no valido")


        else:
            print(f"Directorio{file}")

    # bucle que recorre los archivos
