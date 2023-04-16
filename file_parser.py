import sys
from pathlib import Path


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


if __name__ is '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video mov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")
    print(f"documents doc: {DOC_DOCUMENTS}")
    print(f"documents txt: {TXT_DOCUMENTS}")
    print(f"documents pdf: {PDF_DOCUMENTS}")
    print(f"documents xlsx: {XLSX_DOCUMENTS}")
    print(f"documents pptx: {PPTX_DOCUMENTS}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio wav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")
    print(f"ARCHIVES zip: {ZIP_ARCHIVES}")
    print(f"ARCHIVES gz: {GZ_ARCHIVES}")
    print(f"ARCHIVES tar: {TAR_ARCHIVES}")
    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
