 the detailed progress of OpenStack installations and configurations triggered by devstack
devstack/localrc
SCREEN_LOGDIR=$DEST/logs/screen  // log files of individual OpenStack /opt/stack/logs/screen/*.log
LOGFILE=/opt/stack/logs/stack.sh.log
VERBOSE=True

https://gerrit.googlecode.com/files/gerrit-2.2.2.war
https://gerrit-releases.storage.googleapis.com/index.html
https://gerrit-review.googlesource.com/Documentation/install-quick.html
http://download.opensuse.org/repositories/OBS:/Server:/2.5/images/iso/
http://download.opensuse.org/repositories/OBS:/Server:/2.5/SLE_11_SP3/

获取文件：obs-server.x86_64.install.iso  安装完成后root用户的密码为opensuse
rcsshd start

sudo mysql -uroot -pff

CREATE USER 'ff'@'localhost' IDENTIFIED BY 'secret';
CREATE DATABASE reviewdb;
ALTER DATABASE reviewdb charset=latin1;
GRANT ALL ON reviewdb.* TO 'ff'@'localhost';
FLUSH PRIVILEGES;


Either run CreateSchema from the command line:

java -jar gerrit.war --cat extra/GerritServer.properties_example >GerritServer.properties
edit GerritServer.properties
java -jar gerrit.war CreateSchema

MySQL:

java -jar gerrit.war --cat sql/index_generic.sql | mysql reviewdb -u gerrit2 -p
java -jar gerrit.war --cat sql/mysql_nextval.sql | mysql reviewdb -u gerrit2 -p
Co

# java -jar gerrit-2.8.war init -d /etc/gerrit/

*** Gerrit Code Review 2.8
***

Create '/etc/gerrit'           [Y/n]? y

*** Git Repositories
***

Location of Git repositories   [git]:

*** SQL Database
***

Database server type           [h2]: mysql

Gerrit Code Review is not shipped with MySQL Connector/J 5.1.21
**  This library is required for your configuration. **
Download and install it now [Y/n]? y
Downloading http://repo2.maven.org/maven2/mysql/mysql-connector-java/5.1.21/mysql-connector-java-5.1.21.jar ... OK
Checksum mysql-connector-java-5.1.21.jar OK
Server hostname                [localhost]:
Server port                    [(mysql default)]:
Database name                  [reviewdb]: gerritdb
Database username              [root]: gerrituser
gerrituser's password          :
              confirm password :

*** User Authentication
***

Authentication method          [OPENID/?]: http
Get username from custom HTTP header [y/N]? n
SSO logout URL                 :

*** Email Delivery
***

SMTP server hostname           [localhost]: smtp.googlemail.com
SMTP server port               [(default)]: 587
SMTP encryption                [NONE/?]: tls
SMTP username                  [root]: gerrit@thstack.com
review@thstack.com's password  :
              confirm password :

*** Container Process
***

Run as                         [root]:
Java runtime                   [/usr/lib/jvm/java-6-openjdk-amd64/jre]:
Copy gerrit-2.8.war to /etc/gerrit/bin/gerrit.war [Y/n]? y
Copying gerrit-2.8.war to /etc/gerrit/bin/gerrit.war

*** SSH Daemon
***

Listen on address              [*]:
Listen on port                 [29418]:

Gerrit Code Review is not shipped with Bouncy Castle Crypto v144
  If available, Gerrit can take advantage of features
  in the library, but will also function without it.
Download and install it now [Y/n]? y
Downloading http://www.bouncycastle.org/download/bcprov-jdk16-144.jar ... OK
Checksum bcprov-jdk16-144.jar OK
Generating SSH host key ... rsa... dsa... done

*** HTTP Daemon
***

Behind reverse proxy           [y/N]? y
Proxy uses SSL (https://)      [y/N]? n
Subdirectory on proxy server   [/]:
Listen on address              [*]:
Listen on port                 [8081]: 8082
Canonical URL                  [http://www.thstack.com/]: http://review.thstack.com/

*** Plugins
***

Install plugin reviewnotes version v2.8 [y/N]? y
Install plugin download-commands version v2.8 [y/N]? y
Install plugin replication version v2.8 [y/N]? y
Install plugin commit-message-length-validator version v2.8 [y/N]? y

Initialized /etc/gerrit
Executing /etc/gerrit/bin/gerrit.sh start
Starting Gerrit Code Review: OK
Waiting for server on review.thstack.com:80 ... OK
Opening http://review.thstack.com/#/admin/projects/ ...FAILED
Open Gerrit with a JavaScript capable browser:

http://review.thstack.com/#/admin/projects/

Gerrit 启动脚本

cp /etc/gerrit/bin/gerrit.sh /etc/init.d/gerrit
vim /etc/init.d/gerrit
GERRIT_SITE=/etc/gerrit/       # 在代码 47 行增加
sudo update-rc.d gerrit defaults 21
service gerrit restart
创建 htpasswd.conf 文件，并添加 admin 用户、密码到文件中

# touch /etc/gerrit/etc/htpasswd.conf
# htpasswd /etc/gerrit/etc/htpasswd.conf admin
  New password: 
  Re-type new password: 
  Adding password for user admin
  在浏览器 url 输入：http://review.thstack.com/，
  
  確認有否安裝 java：

java -version

如未有安裝，可輸入以下指令：

sudo apt-get install default-jdk

至於 SQL Database，這筆記會以 MySQL 作例子：

sudo apt-get install mysql-server

當然，也請先安裝 Git，那麼到了設定的時候會比較清楚。

1. 設定 MySQL Gerrit 帳號

登入 MySQL 後運行以下 SQL：

CREATE USER ‘gerrit2′@’localhost’ IDENTIFIED BY ‘password’;

CREATE DATABASE reviewdb;

ALTER DATABASE reviewdb charset=latin1;

GRANT ALL ON reviewdb.* TO ‘gerrit2′@’localhost’;

FLUSH PRIVILEGES;

2. 在 Ubuntu 安裝 Gerrit
依照所需設定 Gerrit 就可以了。內容跟筆記設定一樣，如：

basePath = /var/git

canonicalWebUrl = http://your-aws-hostname:8080/

Database:

type = mysql

hostname = localhost

database = reviewdb

username =  gerrit2

password = password

安裝完畢後設定 git config:

git config -f /var/gerrit/etc/gerrit.config gerrit.canonicalWebUrl
在 AWS 的 Security Group 增加兩條 TCP Rules: 8080, 29418



  gerrit2@host:~$ git config -f ~/gerrit_testsite/etc/gerrit.config gerrit.canonicalWebUrl
  gerrit2@host:~$ git config -f ~/gerrit_testsite/etc/gerrit.config --add http.proxy http://proxy:8080
  gerrit2@host:~$ git config -f ~/gerrit_testsite/etc/gerrit.config --add http.proxyUsername username
  gerrit2@host:~$ git config -f ~/gerrit_testsite/etc/gerrit.config --add http.proxyPassword password



vi  ~/gerrit_example/etc/gerrit.config
## wget --no-cookies \
--no-check-certificate \
--header "Cookie: oraclelicense=accept-securebackup-cookie" \
"http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm" \
-O /opt/jdk-8-linux-x64.rpm
## yum install /opt/jdk-8-linux-x64.rpm
configure the JAVA package using alternatives as in:

## JDK_DIRS=($(ls -d /usr/java/jdk*))
## JDK_VER=${JDK_DIRS[@]:(-1)}

## alternatives --install /usr/bin/java java /usr/java/"${JDK_VER##*/}"/jre/bin/java 20000
## alternatives --install /usr/bin/jar jar /usr/java/"${JDK_VER##*/}"/bin/jar 20000
## alternatives --install /usr/bin/javac javac /usr/java/"${JDK_VER##*/}"/bin/javac 20000
## alternatives --install /usr/bin/javaws javaws /usr/java/"${JDK_VER##*/}"/jre/bin/javaws 20000
## alternatives --set java /usr/java/"${JDK_VER##*/}"/jre/bin/java
## alternatives --set javaws /usr/java/"${JDK_VER##*/}"/jre/bin/javaws
## alternatives --set javac /usr/java/"${JDK_VER##*/}"/bin/javac
## alternatives --set jar /usr/java/"${JDK_VER##*/}"/bin/jar

## yum install mariadb mariadb-server mysql
Once installed, edit its server configuration file in /etc/my.cnf.d/server.cnf and add the following:

## vim /etc/my.cnf.d/server.cnf

[mysqld]
#log-bin=mysql-bin
#binlog_format=mixed
bind-address = 127.0.0.1
## systemctl restart mariadb
## systemctl status mariadb
## systemctl enable mariadb
## yum install httpd httpd-tools openssl mod_ssl
Add the following to /etc/httpd/conf.d/options.conf

## vim /etc/httpd/conf.d/options.conf

TraceEnable off
## mysql_secure_installation

Enter current password for root (enter for none): ENTER
Set root password? [Y/n] Y
Remove anonymous users? [Y/n] Y
Disallow root login remotely? [Y/n] Y
Remove test database and access to it? [Y/n] Y
Reload privilege tables now? [Y/n] Y
## mysql -u root -p
MariaDB> create database gerritdb;
MariaDB> grant all on gerritdb.* to gerrit@localhost identified by 'secret';

## useradd -m gerrit2
## su - gerrit2
## java -jar gerrit.war init -d /home/gerrit2/review_site
fill the questions asked by the wizard, for example:

Location of Git repositories   [git]: 
Database server type           [mysql]: 
Server hostname                [localhost]: 
Server port                    [(mysql default)]: 
Database name                  [gerritdb]: 
Database username              [gerrit]: 
Change gerrit's password       [y/N]? n 
Type                           [LUCENE/?]: 
Authentication method          [HTTP/?]: 
Get username from custom HTTP header [y/N]?  
SSO logout URL                 : 
Install Verified label         [y/N]? 
SMTP server hostname           [localhost]: 
SMTP server port               [(default)]: 
SMTP encryption                [NONE/?]: 
SMTP username                  : 
Run as                         [gerrit2]: 
Java runtime                   [/usr/java/jdk1.8.0_25/jre]: 
Upgrade /home/gerrit2/review_site/bin/gerrit.war [Y/n]? 
Copying gerrit.war to /home/gerrit2/review_site/bin/gerrit.war
Listen on address              [*]: 
Listen on port                 [29418]: 
Behind reverse proxy           [Y/n]? 
Proxy uses SSL (https://)      [y/N]? 
Subdirectory on proxy server   [/gerrit/]: 
Listen on address              [*]: 
Listen on port                 [8081]: 
Canonical URL                  [http://vs377.rosehosting.com/gerrit/]: 
Install plugin commit-message-length-validator version v2.9.1 [y/N]? 
Install plugin download-commands version v2.9.1 [y/N]? 
Install plugin replication version v2.9.1 [y/N]? 
Install plugin reviewnotes version v2.9.1 [y/N]? 
Install plugin singleusergroup version v2.9.1 [y/N]? 

Initialized /home/gerrit2/review_site
## java -jar gerrit.war reindex -d /home/gerrit2/review_site
and start the gerrit using the command below:

## /home/gerrit2/review_site/bin/gerrit.sh start

## Disable Signature
ServerSignature Off

## Disable Banner
ServerTokens Prod
## vim /etc/httpd/conf.d/vhosts.conf

# Load my vhosts
IncludeOptional vhosts.d/*.conf
## mkdir /etc/httpd/vhosts.d
Restart Apache and add it to automatically start on your system start-up using:

## systemctl restart httpd
## systemctl status httpd
## systemctl enable httpd
 

APACHE PROXY TO GERRIT
## vim /etc/httpd/vhosts.d/gerrit.conf

<VirtualHost your_ip_address:80>
    ServerName your_hostname

    ProxyRequests Off
    ProxyVia Off
    ProxyPreserveHost On

    <Proxy *>
		Order deny,allow
		Allow from all
    </Proxy>

    <Location /gerrit/login/>
		AuthType Basic
		AuthName "Gerrit Code Review"
		Require valid-user
		AuthUserFile '/etc/httpd/gerrit.htpasswd'
    </Location>

    AllowEncodedSlashes On
    ProxyPass /gerrit/ http://your_ip_address:8081/gerrit/
</VirtualHost>
create user using htpasswd

## htpasswd -c /etc/httpd/gerrit.htpasswd admin
New password: 
Re-type new password: 
Adding password for user admin
restart apache using

## systemctl restart httpd
