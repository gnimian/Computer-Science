import subprocess as sp
#pid = sp.Popen(['mpv', '--really-quiet', 'van_halen-DanceTheNightAway.mp3'])
pid = sp.Popen(['vlc', '--intf','dummy', 'van_halen-DanceTheNightAway.mp3'])

#stop the song
pid.send_signal(sp.signal.SIGTERM)