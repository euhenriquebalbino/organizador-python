import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"],
    "planilhas": [".csv", ".xlsx", ".xls", ".ods"],
    "documentos": [".doc", ".docx", ".txt", ".rtf", ".odt"],
    "apresentações": [".ppt", ".pptx", ".odp"],
    "pdfs": [".pdf"],
    "videos": [".mp4", ".mov", ".mkv", ".avi", ".wmv", ".flv", ".webm"],
    "audios": [".mp3", ".wav", ".flac", ".aac", ".wma", ".ogg", ".m4a"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "executáveis": [".exe", ".msi", ".bat", ".sh", ".apk", ".jar"],
    "codigo_fonte": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".ts", ".php", ".rb", ".go", ".cs"],
    "bancos_de_dados": [".sql", ".db", ".sqlite", ".mdb", ".accdb"],
    "modelos_3d": [".obj", ".fbx", ".stl", ".3ds", ".dae", ".blend"],
    "fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "sistemas": [".iso", ".img", ".vmdk", ".vdi"],
    "scripts": [".ps1", ".vbs", ".cmd", ".reg"],
    "logs": [".log"],
    "configuracoes": [".ini", ".cfg", ".yaml", ".yml", ".json", ".xml"],
    "livros_digitais": [".epub", ".mobi", ".azw3", ".cbz", ".cbr"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")