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

