import os
import requests
import platform
import subprocess
from ftplib import FTP
from zipfile import ZipFile

def download_client(ftp_server_ip):
	ftp = FTP(ftp_server_ip)
	ftp.login()

	with open('client.php', 'wb') as fp:
		ftp.retrbinary('RETR CLIENT.PHP', fp.write)

	ftp.quit()

def install_server(ftp_server_ip):
	OS: str = platform.system()
	DISTRO: str = platform.release()
	DISTRO_VERSION: str = platform.version()

	if OS == 'Windows':
		pass

	elif OS == 'Linux':
		pass

	elif OS == 'MacOS':
		pass
