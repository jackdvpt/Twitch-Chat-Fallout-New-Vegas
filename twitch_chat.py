import socket

def twitch_setup(sock):
    server = 'irc.chat.twitch.tv'
    port = 6667
    nickname = 'jacksbots'
    token = 'oauth:YOURTOKEN'
    channel = '#jackdvpt'
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    
  
