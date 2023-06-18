import subprocess


def detectDarkModeGnome():
    '''Detects dark mode in GNOME'''
    getArgs = ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme']
    currentTheme = subprocess.run(
        getArgs, capture_output=True
    ).stdout.decode("utf-8").strip().strip("'")

    darkIndicator = '-dark'
    if currentTheme.endswith(darkIndicator):
        return True
    return False

isDarkMode = detectDarkModeGnome()
print(isDarkMode)
