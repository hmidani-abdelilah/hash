import os , click, hashlib
from click_help_colors import HelpColorsGroup, HelpColorsCommand

@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
) #main command
def main():
   print("program running ...")
"""
@click.group() #main command
def main():
   print("program running ...")
"""
# subCommands

@main.command() # affiliation to the main command
@click.argument('sha1') #argument for sha1 algorithm
def sha_1(sha1):
   # the help is displayed using the multiline comment
   """SHA1 hashing"""
   hash_object = hashlib.sha1(sha1.encode())
   hash_object = hash_object.hexdigest()
   click.echo(click.style(f"{hash_object}",fg='red'))

@main.command() # affiliation to the main command
@click.argument('md5') #argument for md5 algorithm
def md5(md5):
   # the help is displayed using the multiline comment
   """MD5 hashing"""
   hash_object = hashlib.md5(md5.encode())
   hash_object = hash_object.hexdigest()
   click.echo(click.style(f"{hash_object}",fg='green'))

@main.command() # affiliation to the main command
@click.argument('sha256') #argument for sha256 algorithm
# the help is displayed using the multiline comment
def sha_256(sha256):
   """256 hashing"""
   hash_object = hashlib.sha256(sha256.encode())
   hash_object = hash_object.hexdigest()
   click.echo(click.style(f"{hash_object}",fg='yellow'))

@main.command() # affiliation to the main command
@click.argument('sha384') #argument for sha384 algorithm
# the help is displayed using the multiline comment
def sha_384(sha384):
   """384 hashing"""
   hash_object = hashlib.sha384(sha384.encode())
   hash_object = hash_object.hexdigest()
   click.echo(click.style(f"{hash_object}",fg='blue'))

@main.command() # affiliation to the main command
@click.argument('sha512') #argument for sha512 algorithm
# the help is displayed using the multiline comment
def sha_512(sha512):
   """512 hashing"""
   hash_object = hashlib.sha512(sha512.encode())
   hash_object = hash_object.hexdigest()
   click.echo(click.style(f"{hash_object}",fg='cyan'))

if __name__ == '__main__':
   os.system('clear')
   main()