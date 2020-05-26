# ssh internet 

This page is to include some tutorial for setup ssh to the internet.

1. https://imadelhanafi.com/posts/jetson_nano_setup/

2. https://www.chenhuijing.com/blog/tunnelling-services-for-exposing-localhost-to-the-web/

3. https://dev.to/giorgosk/expose-your-local-web-server-to-the-world-using-localhost-run-or-serveo-net-l83


## command

1. ssh -R 80:localhost:8888 ssh.localhost.run : use to setup a website so other member can connect through the website

Note: Seem like serveo.net is down now, need to use other serivce 



## Graphical interface

In the host machine

```
vim /etc/ssh/sshd_config
```

modify the settings as follows

```
X11Forwarding yes 
X11DisplayOffset 10
```

The on the laptop

```
ssh -X
```

