
import os
import logging
import dotenv

dotenv.load_dotenv()

FORMAT_STRING = '''

%(asctime)s | %(levelname)s | 
%(filename)s | %(message)s

'''.replace('\n', '').strip()

DATA_FORMAT_STRING = '''

%d/%m/%Y %H:%M:%S
'''.replace('\n', '').strip()


opts = {
	'filename': 'app.log',
#	'level': logging.WARNING,
	'level': int(os.getenv('DEBUG_LEVEL') or 0),
	'format': FORMAT_STRING,
	'datefmt': DATA_FORMAT_STRING
}
logging.basicConfig(**opts)

logging.debug('mensagem de DEBUG')
logging.info('mensagem de INFO')
logging.warning('mensagem de WARNING')
logging.error('mensagem de ERROR')
logging.critical('mensagem de CRITICAL')