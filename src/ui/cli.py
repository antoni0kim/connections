from importlib.metadata import version

def get_version():
	return version("connection")

def main():
	version = get_version()
	print(f"connection version {version}")