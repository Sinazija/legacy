from pathlib import Path
import sys
import shutil
from .normalize import normalize


JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
}
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item is dir:
            if item not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        ful_name = folder / item.name
        if not ext:
            OTHER.append(ful_name)
        else:
            try:
                conteiner = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                conteiner.append(ful_name)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(ful_name)


def hand_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder/normalize(filename.name))


def hand_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder/normalize(filename.name))


def hand_archiv(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_file = target_folder / \
        normalize(filename.name.replace(filename.suffix, ''))
    folder_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_file.resolve()))
    except shutil.ReadError:
        folder_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')


def main(folder: Path) -> None:
    scan(folder)
    for file in JPEG_IMAGES:
        hand_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        hand_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        hand_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        hand_media(file, folder / 'images' / 'SVG')
    for file in AVI_VIDEO:
        hand_media(file, folder / 'video' / 'AVI')
    for file in MP4_VIDEO:
        hand_media(file, folder / 'video' / 'MP4')
    for file in MOV_VIDEO:
        hand_media(file, folder / 'video' / 'MOV')
    for file in MKV_VIDEO:
        hand_media(file, folder / 'video' / 'MKV')
    for file in DOC_DOCUMENTS:
        hand_media(file, folder / 'video' / 'DOC')
    for file in TXT_DOCUMENTS:
        hand_media(file, folder / 'video' / 'TXT')
    for file in PDF_DOCUMENTS:
        hand_media(file, folder / 'video' / 'PDF')
    for file in XLSX_DOCUMENTS:
        hand_media(file, folder / 'video' / 'XLSX')
    for file in PPTX_DOCUMENTS:
        hand_media(file, folder / 'video' / 'PPTX')
    for file in MP3_AUDIO:
        hand_media(file, folder / 'audio' / 'MP3')
    for file in OGG_AUDIO:
        hand_media(file, folder / 'audio' / 'OGG')
    for file in WAV_AUDIO:
        hand_media(file, folder / 'audio' / 'WAV')
    for file in AMR_AUDIO:
        hand_media(file, folder / 'audio' / 'AMR')

    for file in OTHER:
        hand_media(file, folder / 'OTHER')
    for file in ZIP_ARCHIVES:
        hand_media(file, folder / 'archives' / 'ZIP')
    for file in GZ_ARCHIVES:
        hand_media(file, folder / 'archives' / 'GZ')
    for file in TAR_ARCHIVES:
        hand_media(file, folder / 'archives' / 'TAR')

    for folder in FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan)
