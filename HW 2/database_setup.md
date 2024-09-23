1. Log into Lightsail instance

2. Install MariaDB:
```
    sudo apt update
    sudo apt install mariadb-server -y
```

3. Edit MariaDB config file to run on port 6002
```
    sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
        under [mysqld], add 
        port = 6002
        bind-address = 0.0.0.0 # allows connection from any IP address
```
4. Start the server:
```
    sudo systemctl start mariadb
    sudo systemctl enable mariadb       
```

5. Security protocol that GPT recommended:
```
    sudo mysql_secure_installation
        Set a root password: Yes (set a strong password).
        Remove anonymous users: Yes.
        Disallow root login remotely: Yes.
        Remove test database: Yes.
        Reload privilege tables: Yes.
```
6. Login to MariaDB as root user and create the database:
```
    CREATE DATABASE comp370_test;
```
7. Add user with password:
```
    CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
    GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';
    FLUSH PRIVILEGES;
    EXIT;
```
8. Make sure MariaDB is running on 6002 and use DBeaver to test if user is accessible:
```
    to view ports:
    netstat -tln

    in DBeaver:
    jdbc:mariadb://3.96.172.118:6002/comp370_test
        Run test connection, if successful add the database
```

