# python-mysql-s2i

1. Create a new project to play in.

`oc new-project python-mysql`

2. Start ephemeral MySQL pod via a template and note generated username, password and dbname

`oc new-app mysql-ephemeral --name mysql`

3. Create a python pod via s2i that connects to MySQL 

`oc new-app https://github.com/magik8paul/python-mysql-s2i.git --name pymyapp -e MYSQL_HOST=<your mysql app name> -e MYSQL_DATABASE=<from above> -e MYSQL_USER=<from above> -e MYSQL_PASSWORD=<from above>`

If python outputs 'apples' 'bananas' 'cherries', then you have a functioning multi-pod app!
