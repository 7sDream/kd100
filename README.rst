kd100.py
========

I'm a small script that help you get express package information use kuaidi100.com api.

Install
=======

..  code:: bash

    $ pip install kd100

Usage
=====

``kd100``: normal use, type code in shell, return info.

``kd100 -c code``: ``-c`` means code, specified express code.

``kd100 -c code -o filename``: ``-o`` means output, specified output filename.

``kd100 -c code -o filename -p company_name``: ``-p`` means company, specified the express company name, useful when auto guess is error.

Type ``kd100 -h`` for more help.

Example
=======

..  code:: bash

    yourname@computer:~$ kd100
    Input your express code: <Your code>
    Possible company: zhongtong, kuayue, yuantong, zhaijisong, shengfengwuliu
    Try zhongtong ...Done
    code: <Your  code>         company: zhongtong       is checked: 0
    =================================================================
            time         |                  content
    -----------------------------------------------------------------
     2015-08-16 17:40:28 | first content
    -----------------------------------------------------------------
     2015-08-16 17:02:32 | some content
    -----------------------------------------------------------------
    ...
    -----------------------------------------------------------------
     2015-08-13 20:41:27 | last content
    =================================================================

..  image:: http://ww4.sinaimg.cn/large/88e401f0gw1evjtouw9hgj20m20cnjyl.jpg

Changelog
=========

- v0.0.4

  - remove third party module dependencies.
  - add ``-p`` option to specified company.

- v0.0.2

  - kuaidi100 webside change the rule, need special header referer when send query

- v0.0.1

  - first version, with base function.

LICENSE
=======

MIT.
