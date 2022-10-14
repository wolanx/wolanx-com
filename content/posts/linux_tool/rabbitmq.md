---
title: rabbitmq
date: 2018-12-28T10:15:36+08:00
categories: [linux]
---

## rabbitmq

```shell
docker pull rabbitmq:3.7.8

docker run -d --name rabbitmq-1 rabbitmq:3.7.8

docker run -d --name rabbitmq -p 5671:5671 -p 5672:5672 -p 4368:4368 -p 25672:25672 -p 15671:15671 -p 15672:15672 rabbitmq:management

docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq:3.7.8-management
http://0.0.0.0:15672
guest/guest
```

## demo
```php
<?php

namespace app\console\controllers;

use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;
use yii\console\Controller;

class QueueController extends Controller
{

    public function actionIn($n = 1)
    {
        $connection = new AMQPStreamConnection('172.16.30.123', 5672, 'guest', 'guest');
        $channel    = $connection->channel();

        // if not exist
        $channel->queue_declare('hello', false, false, false, false);

        $msg = 'hello_' . date('H_i_s');
        $msg = new AMQPMessage($msg);
        $channel->basic_publish($msg, '', 'hello');

        echo "Send: {$msg->body}\n";
        $channel->close();
        $connection->close();
    }

    public function actionExec()
    {
        $connection = new AMQPStreamConnection('172.16.30.123', 5672, 'guest', 'guest');
        $channel    = $connection->channel();

        // if not exist
        $channel->queue_declare('hello', false, false, false, false);

        echo "Start\n";
        $callback = function ($msg) use ($channel) {
            /** @var AMQPMessage $msg */
            echo "Get: {$msg->body}\n";

            // ack
            $delivery_tag = $msg->delivery_info['delivery_tag'];
            $channel->basic_ack($delivery_tag);
        };

        $channel->basic_consume('hello', '', false, false, false, false, $callback);

        while (count($channel->callbacks)) {
            $channel->wait();
        }
    }

}
```
