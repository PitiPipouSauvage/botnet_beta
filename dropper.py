import os
import requests
import platform
import subprocess
from ftplib import FTP
from zipfile import ZipFile

def download_client(ftp_server_ip):
	ftp = FTP(ftp_server_ip)
	ftp.login()

	with open('client.py', 'wb') as fp:
		ftp.retrbinary('RETR CLIENT.PY', fp.write)

	ftp.quit()

def install_server(ftp_server_ip):
	OS: str = platform.system()
	DISTRO: str = platform.release()
	DISTRO_VERSION: str = platform.version()

	if OS == 'Windows':
		download_client(ftp_server_ip)
		os.system('python client.py')

	elif OS == 'Linux' or OS == 'MacOS':
		download_client(ftp_server_ip)
		os.system('python3 client.py')
