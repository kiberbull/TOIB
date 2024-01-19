# Практическое задание №2
##  Создать пользователя super-{ФИО}, наделить его привилегиями суперпользователя
    sudo adduser super-duryagin
    sudo usermod -aG sudo super-duryagin

##  Зайти под созданным пользователем и создать группу group-{группа}
    su - super-duryagin
    Password: 

## Создание группы BBMO-01-23 и добавление суперпользователя в нее
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$ sudo groupadd BBMO-02-23
    [sudo] password for super-duryagin: 

## Добавить пользователя super-{ФИО} в группу group-{группа}
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$ sudo usermod -aG BBMO-02-23 super-duryagin

## Продемонстрировать наличие пользователя в группе
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$ cat /etc/group | grep super-duryagin
    sudo:x:27:parallels,super-duryagin
    super-duryagin:x:1001:
    BBMO-02-23:x:1002:super-duryagin

## Создать пользователя user-{ФИО}, добавить его в группу group-{группа}
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$    sudo adduser user-duryagin
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$    sudo usermod -aG BBMO-02-23 user-duryagin

## Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod) пользователя user-{ФИО} по созданию и удалению файлов в домашнем каталоге пользователя super-{ФИО}
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$    chmod 770 /home/super-duryagin
    
    ┌──(super-duryagin㉿kali-linux-2021-3)-[~]
    └─$    sudo usermod -aG super-duryagin user-duryagin

