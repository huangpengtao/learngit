http://yongbingchen.github.io/blog/2015/03/27/config-gerrit-server-behind-apache-https-reverse-proxy/

'$site_path'/etc/gerrit.config 
[httpd]
  	listenUrl = proxy-http://127.0.0.1:8081/r/

httpd config is
<VirtualHost *:8082>
    ServerName localhost

    ProxyRequests Off
    ProxyVia Off
    ProxyPreserveHost On

    <Proxy *>
          Order deny,allow
          Allow from all
    </Proxy>
  <Location "/login/">
  AuthType Basic
  AuthName "Gerrit Code Review"
  AuthBasicProvider file
  AuthUserFile /usr/local/apache/passwd/passwords
 Require valid-user
 </Location>
ProxyPass / http://localhost:8081/




gerrit.config is

[gerrit]
        basePath = git
        canonicalWebUrl = http://localhost:8081/
[database]
        type = mysql
        hostname = localhost
        database = reviewdb
        username = gerrit
[auth]
        type = HTTP
[sendemail]
        smtpServer = localhost
        smtpUser = gerrit
[container]
        user = gerrit
        javaHome = /usr/lib/jvm/java-1.6.0-openjdk-1.6.0.0.x86_64/jre
[sshd]
        listenAddress = *:29418
[httpd]
        listenUrl = proxy-http://*:8081/
[cache]
        directory = cache
        
        
        
        
http://hacklog.tumblr.com/post/104627701707/gerrit-apache-reverse-proxy-http-auth-with-anon
sudo apt-get install apache2 apache2-utils
sudo apt-get install mysql-server
sudo apt-get install git
sudo apt-get install sendmail mailutils

[gerrit]
  basePath = git
  canonicalWebUrl = http:///gerrit/
[database]
  type = mysql
  hostname = localhost
  database = reviewdb
  username = gerrit2
[index]
  type = LUCENE
[auth]
  type = HTTP
  loginUrl = http:///gerrit/login/
[sendemail]
  smtpServer = localhost
[container]
  user = gerrit2
  javaHome = /usr/lib/jvm/java-7-openjdk-amd64/jre
[sshd]
  listenAddress = *:29418
[httpd]
  listenUrl = http://localhost:8080/gerrit/
[cache]
  directory = cache
  sudo touch /etc/apache2/passwords
sudo htpasswd /etc/apache2/passwords 
/etc/hostname

127.0.0.1 localhost
127.0.0.1 gerrit
  


http://dachary.org/?p=1716
http://codexc.com/blog/2014/09/how-to-installation-and-configuration-gerrit-v2-10-with-github-oauth/
apt-get install gitweb
mkdir ~/gerrit/
wget https://gerrit-releases.storage.googleapis.com/gerrit-2.10-rc0.war

CREATE USER 'gerrit'@'localhost' IDENTIFIED BY 'yourpassword';
CREATE DATABASE reviewdb;
GRANT ALL ON reviewdb.* TO 'gerrit'@'localhost';
FLUSH PRIVILEGES;
exit;
java -jar gerrit*.war init -d ~/gerrit/

Database server type           [H2/?]: mysql
atabase name                  [reviewdb]:
Database username              [gerrit2]: gerrit
gerrit2's password             : yourpassword
Authentication method          [OPENID/?]: http
Get username from custom HTTP header [y/N]? y
Behind reverse proxy           [y/N]? y
Proxy uses SSL (https://)      [y/N]? n
anonical URL                  [http://review.probam.net/]: https://your-domain.com/
java -jar gerrit*.war reindex

