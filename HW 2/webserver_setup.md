1. Log into lightsail instance 
2. Install apache by running: 
``` 
    sudo apt update 
    sudo apt install apache2 -y

```
3. Open the apache configuration file and edit the port:

```
    sudo nano /etc/apache2/ports.conf
    Listen 80 -> Listen 8008
```

4. Then, edit the recommended vh file:
``` 
    sudo nano /etc/apache2/sites-enabled/000-default.conf
```

5. Then, open LightSail management in AWS and go to Networking > Firewall and add a rule for port 8008

6. Go to the root and create the file comp370_hw2.txt:
```
    cd /var/www/html
    sudo nano comp370_hw2.txt
        # write some text in the file and save
```

7. Restart ubuntu server:
```
    sudo systemctl restart apache2
```

8. Then, access webpage by going to (for my public IP):
```
    http://3.96.172.118:8008/comp370_hw2.txt
```