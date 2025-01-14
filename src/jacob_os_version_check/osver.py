def get_os_pretty_name():
          with open('/etc/os-release','r') as file:
                  for line in file:
                          if line.startswith('PRETTY_NAME'):
                                  return line.split("=")[1].strip().strip('"')
          return None


