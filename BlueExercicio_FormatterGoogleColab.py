# 1. Montar o Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. Instalar o Blue Python Formatter
!pip install blue

# 3. Definir o caminho do arquivo .py no Google Drive
file_path = '/content/drive/xxx/xxxxx/xxxxxxx.py'
backup_path = '/content/drive/xxxx/xxxxxxx/xxxxxxx_backup.py'

# 4. Fazer o backup do arquivo original
import shutil
if os.path.exists(file_path):
    # Copiar o arquivo original para criar o backup
    shutil.copy(file_path, backup_path)
    print(f"\nBackup do arquivo original criado em: {backup_path}")
    
    # 5. Executar o Blue Python Formatter
    !blue --line-length 79 "{file_path}"
    
    print(f"\nArquivo {file_path} foi formatado com Blue.")
else:
    print(f"\nErro: O arquivo {file_path} não foi encontrado.")
