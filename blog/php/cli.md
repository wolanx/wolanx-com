---
title: php cli类
date: 2018-03-22 16:39:22
tags:
  - php
---

# cli类

```php
<?php

/**
 * 命令行获取参数
 * create by 赵煜杰
 * lastmodify 2015年3月27日 14:42:36
 * use A: php test.php --stdin="true"
 * use B: php test.php --environ="online" --check="true"
 */
class cli_param
{
    /**
     * @param boolean $stdin
     * true 支持手动输入
     * false 不合法直接退出
     */
    public $stdin;
    public $filename;

    public function __construct($filename = 'here', $stdin = false)
    {
        $this->start();
        $this->filename = $filename;
        $this->stdin = $stdin;
    }

    public function get($arr)
    {
        $return = [];
        /** @var array $longopts */
        $longopts = ['stdin:'];
        foreach ($arr as $k => $v) {
            $longopts[] = $k . ':';
        }
        $opts = getopt('', $longopts);
        if (isset($opts['stdin']) && $opts['stdin'] == "true") {
            $this->stdin = true;
        }
        unset($opts['stdin']);
        if (count($opts) != count($arr)) {
            foreach (array_keys($arr) as $v) {
                $opts[$v] = isset($opts[$v]) ? $opts[$v] : '';
            }
        }
        foreach ($opts as $k => $v) {
            if (!in_array($v, $arr[$k]['param'])) {
                if ($this->stdin) {
                    echo $arr[$k]['desc'] . "\n";
                    fwrite(STDOUT, "Enter Field '{$k}': ");
                    $get = trim(fgets(STDIN));
                    while (!in_array($get, $arr[$k]['param'])) {
                        if (isset($arr[$k]['desc'])) {
                            fwrite(STDOUT, "{$arr[$k]['desc']},\nit maybe in (" . implode(',', $arr[$k]['param']) . "): ");
                        } else {
                            fwrite(STDOUT, "Your Field '{$k}' is error,\nit maybe in (" . implode(',', $arr[$k]['param']) . "): ");
                        }
                        $get = trim(fgets(STDIN));
                    }
                    $return[$k] = $get;
                } else {
                    echo "Parameter is error: Field '{$k}' not in (" . implode(',', $arr[$k]['param']) . ")\n";
                    $this->end();
                }
            } else {
                $return[$k] = $v;
            }
        }

        return $return;
    }

    public function start()
    {
        echo "Log from '" . $this->filename . "'\n";
        echo "\n" . str_repeat('=', 79) . "\n";
    }

    public function end()
    {
        echo str_repeat('=', 79) . "\n\n";
        exit;
    }
}
```

## cli类 使用

```php
<?php
$arr = [
    'environ' => [
        'desc'  => 'descdescdescdescdesc',
        'param' => ['online', 'offline'],
    ],
    'check'   => [
        'desc'  => 'descdescdescdescdesc',
        'param' => ['true', 'false'],
    ],
];
$a = (new cli_param(__FILE__, true))->get($arr);
print_r($a);
```