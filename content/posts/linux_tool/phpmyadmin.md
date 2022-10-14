---
title: phpmyadmin
date: 2018-03-19T11:03:39
categories: [tool]
---

# phpmyadmin

```sh
docker run --restart=unless-stopped --name pmd -d -p 33060:80 phpmyadmin/phpmyadmin:4.7

docker exec -it pmd sh

vi /etc/phpmyadmin/config.user.inc.php

supervisorctl restart all
```

/etc/phpmyadmin/config.user.inc.php
```php
<?php

// vi /etc/phpmyadmin/config.user.inc.php

$cfg['Servers'] = [];

$cfg['Servers'][1] = [
    'auth_type'       => 'cookie',
    'connect_type'    => 'tcp',
    'compress'        => false,
    'AllowNoPassword' => true,
    'host'            => '139.196.x.x',
    'user'            => 'root',
];

$cfg['Servers'][] = [
    'auth_type'       => 'config',
    'connect_type'    => 'tcp',
    'compress'        => false,
    'AllowNoPassword' => true,
    'host'            => 'x.x.x.x', // 本机
    'user'            => 'root',
    'password'        => 'xxxx',
];
```
