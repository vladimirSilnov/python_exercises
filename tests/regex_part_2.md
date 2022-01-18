# Регулярные выражения. Часть 2

Тест [Регулярные выражения. Часть 2](https://goo.gl/forms/ltuOAO62yLlZkEmm1)

## question 1

Какой результат будет выведен в последней строке?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

m = re.match('(\d+).+(\S+)', line)

print(m.groups())
```

Правильный ответ:
```python
('100', '1')
```

### Объяснение

Такой результат в данном случае из-за того, что ```.+``` захватывает максимальное количество символов - по умолчанию ```+``` жадный.

Поэтому во вторые скобки попала 1 - это последний символ строки. Само выражение описывает всю строку:
```python
In [7]: line = '100    aabb.cc10.7000    DYNAMIC     Gi0/1'

In [8]: m = re.match('(\d+).+(\S+)', line)

In [9]: m.group()
Out[9]: '100    aabb.cc10.7000    DYNAMIC     Gi0/1'

In [10]: m.groups()
Out[10]: ('100', '1')
```

## question 2

Какой результат будет выведен в последней строке?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

m = re.match('(\d+).+?(\S+)', line)

print(m.groups())
```

Правильный ответ:
```python
('100', 'aabb.cc10.7000')
```

### Объяснение

Этот вариант отличается от предыдущего тем, что для ```.+``` отключена жадность - то есть сюда попадет самые короткий вариант, который описывает выражение.

Но ```\S+``` - жадное выражение. Поэтому сюда попадут все символы до первого пробела - весь MAC-адрес
```python
In [11]: line = '100    aabb.cc10.7000    DYNAMIC     Gi0/1'

In [12]: m = re.match('(\d+).+?(\S+)', line)

In [13]: m.group()
Out[13]: '100    aabb.cc10.7000'

In [14]: m.groups()
Out[14]: ('100', 'aabb.cc10.7000')
```

## question 3

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

m = re.search('(\d+) +[a-f0-9.] +\w+ +(\S+)', line)

if m:
    print(m.groups())
else:
    print(None)
```

Правильный ответ:
```python
None
```

### Объяснение

После квадратных скобок нет символа повторения, поэтому регулярное выражение не соответствует строке
```python
In [13]: line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

In [14]: m = re.search('(\d+) +[a-f0-9.] +\w+ +(\S+)', line)

In [15]: if m:
    ...:     print(m.groups())
    ...: else:
    ...:     print(None)
    ...:
None

```

## question 4

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

m = re.search('(\d+) +([a-f0-9.])+ +\w+ +(\S+)', line)

if m:
    print(m.groups())
else:
    print(None)
```

Правильный ответ:
```python
('100', '0', 'Gi0/1')
```

### Объяснение

```([a-f0-9.])+``` тут плюс стоит после круглых скобок. Поэтому во вторую группу попадает только последний символ из MAC-адреса.

То есть в группу будут попадать по очереди символы в MAC-адресе. Но запомнится в итоге последний:
```python
In [17]: line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

In [18]: m = re.search('(\d+) +([a-f0-9.])+ +\w+ +(\S+)', line)

In [19]: if m:
    ...:     print(m.groups())
    ...: else:
    ...:     print(None)
    ...:
('100', '0', 'Gi0/1')

In [20]: m.group()
Out[20]: '100     aabb.cc10.7000    DYNAMIC     Gi0/1'
```


## question 5

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'
m = re.search('([0-9a-f]+\.)+', line)
if m:
    print(m.groups())
else:
    print(None)

```

Правильный ответ:
```python
('cc10.',)
```

### Объяснение

Выражение описывает подстроку ```aabb.cc10.```, но в группу попадет только вторая часть MAC-адреса.

Тут нюанс в методе groupS: group - покажет что вообще совпадение - это первые две части мака.
Но, groups выдает то, что попало в скобки и запомнилось.
А попали в скобки обе части, сначала первая, потом вторая.

Соответственно, последняя которую запомнили скобки - была вторая часть
```python
In [21]: line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

In [22]: m = re.search('([0-9a-f]+\.)+', line)

In [23]: if m:
    ...:     print(m.groups())
    ...: else:
    ...:     print(None)
    ...:
('cc10.',)

In [24]: m.group()
Out[24]: 'aabb.cc10.'

```

## question 6

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
table = '''
100     aabb.cc10.7000    DYNAMIC     Gi0/1
200     aacc.cc10.7000    DYNAMIC     Gi0/2
100     aadd.cc10.1400    DYNAMIC     Gi0/3
100     aadd.ee10.1400    DYNAMIC     Gi0/4
'''

print(re.findall('\d{3} +[a-f0-9.]+', table))
```


Правильный ответ:
```python
['100     aabb.cc10.7000', '200     aacc.cc10.7000', '100     aadd.cc10.1400', '100     aadd.ee10.1400']
```

### Объяснение

Метод findall ищет все совпадения с регулярным выражением в строке и возвращает их в виде списка
```python
In [30]: table = '''
    ...: 100     aabb.cc10.7000    DYNAMIC     Gi0/1
    ...: 200     aacc.cc10.7000    DYNAMIC     Gi0/2
    ...: 100     aadd.cc10.1400    DYNAMIC     Gi0/3
    ...: 100     aadd.ee10.1400    DYNAMIC     Gi0/4
    ...: '''

In [31]: print(re.findall('\d{3} +[a-f0-9.]+', table))
['100     aabb.cc10.7000', '200     aacc.cc10.7000', '100     aadd.cc10.1400', '100     aadd.ee10.1400']
```



## question 7

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
table = '''
100     aabb.cc10.7000    DYNAMIC     Gi0/1
200     aacc.cc10.7000    DYNAMIC     Gi0/2
100     aadd.cc10.1400    DYNAMIC     Gi0/3
100     aadd.ee10.1400    DYNAMIC     Gi0/4
'''

print(re.findall('(\d{3}) +[a-f0-9.]+', table))
```

Правильный ответ:
```python
['100', '200', '100', '100']
```

### Объяснение

findall возвращает все строки, которые совпали с выражением. Но, если в регулярном выражении есть группы, findall возвращает только то,что попало в группы (выражения в скобках)
```python
In [33]: table = '''
    ...: 100     aabb.cc10.7000    DYNAMIC     Gi0/1
    ...: 200     aacc.cc10.7000    DYNAMIC     Gi0/2
    ...: 100     aadd.cc10.1400    DYNAMIC     Gi0/3
    ...: 100     aadd.ee10.1400    DYNAMIC     Gi0/4
    ...: '''

In [34]: print(re.findall('(\d{3}) +[a-f0-9.]+', table))
['100', '200', '100', '100']
```


## question 8

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
table = '''
100     aabb.cc10.7000    DYNAMIC     Gi0/1
200     aacc.cc10.7000    DYNAMIC     Gi0/2
100     aadd.cc10.1400    DYNAMIC     Gi0/3
100     aadd.ee10.1400    DYNAMIC     Gi0/4
'''

print(re.findall('(\d{3}) +((?:[a-f0-9.]+)+) +\w+ +([\w\/]+)', table))
```

Правильный ответ:
```python
[('100', 'aabb.cc10.7000', 'Gi0/1'), ('200', 'aacc.cc10.7000', 'Gi0/2'), ('100', 'aadd.cc10.1400', 'Gi0/3'), ('100', 'aadd.ee10.1400', 'Gi0/4')]
```

### Объяснение

Тут еще один нюанс метода findall: если выражение в скобках было одно, как в прошлом задании, возвращается список строк.
Если же групп в регулярном выражении несколько, возвращается список кортежей:
```python
In [28]: table = '''
    ...: 100    aabb.cc10.7000    DYNAMIC     Gi0/1
    ...: 200    aacc.cc10.7000    DYNAMIC     Gi0/2
    ...: 100    aadd.cc10.1400    DYNAMIC     Gi0/3
    ...: 100    aadd.ee10.1400    DYNAMIC     Gi0/4
    ...: '''

In [29]: print(re.findall('(\d{3}) +((?:[a-f0-9.]+)+) +\w+ +([\w\/]+)', table))
[('100', 'aabb.cc10.7000', 'Gi0/1'), ('200', 'aacc.cc10.7000', 'Gi0/2'), ('100', 'aadd.cc10.1400', 'Gi0/3'), ('100', 'aadd.ee10.1400', 'Gi0/4')]
```

Кроме того, тут используется синтаксис ```(?:[a-f0-9.]+)```:
* ```?:``` внутри группы означает, что не надо запоминать то, что совпадет с выражением в скобках. Что скобки тут нужны только чтобы сгруппировать символы и указать, что они должны повторяться. Это называется noncapturing group. То есть группа, которая не запоминает результат

Если убрать ```?:``` в выражении, результат будет таким:
```python
In [31]: print(re.findall('(\d{3}) +(([a-f0-9.]+)+) +\w+ +([\w\/]+)', table))
[('100', 'aabb.cc10.7000', 'aabb.cc10.7000', 'Gi0/1'), ('200', 'aacc.cc10.7000', 'aacc.cc10.7000', 'Gi0/2'), ('100', 'aadd.cc10.1400', 'aadd.cc10.1400', 'Gi0/3'), ('100', 'aadd.ee10.1400', 'aadd.ee10.1400', 'Gi0/4')]
```

MAC-адрес повторяется два раза.

Это значит, что можно было написать такое выражение, чтобы описать нужные элементы:
```python
In [32]: print(re.findall('(\d{3}) +([a-f0-9.]+) +\w+ +([\w\/]+)', table))
[('100', 'aabb.cc10.7000', 'Gi0/1'), ('200', 'aacc.cc10.7000', 'Gi0/2'), ('100', 'aadd.cc10.1400', 'Gi0/3'), ('100', 'aadd.ee10.1400', 'Gi0/4')]
```


## question 9

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

m = re.search('(?P<vlan>\d)+ +(?P<mac>\S+) +\w+ +(?P<port>\S+)', line)

print(m.groupdict())
```

Правильный ответ:
```python
{'vlan': '0', 'mac': 'aabb.cc10.7000', 'port': 'Gi0/1'}
```

### Объяснение

Выражение эквивалентно такому ```(\d)+ +(\S+) +\w+ +(\S+)```, только используются именованные группы.

Также надо обратить внимание, что первый плюс стоит после скобок, поэтому в первую группу попадет одна цифра, а не весь номер влан.

Аналогичный пример с нумерованными группами:
```python
In [34]: line = '100    aabb.cc10.7000    DYNAMIC     Gi0/1'

In [35]: m = re.search('(\d)+ +(\S+) +\w+ +(\S+)', line)

In [36]: m.groups()
Out[36]: ('0', 'aabb.cc10.7000', 'Gi0/1')
```

И с именованными, как в задании
```python
In [37]: line = '100    aabb.cc10.7000    DYNAMIC     Gi0/1'

In [38]: m = re.search('(?P<vlan>\d)+ +(?P<mac>\S+) +\w+ +(?P<port>\S+)', line)

In [39]: m.groups()
Out[39]: ('0', 'aabb.cc10.7000', 'Gi0/1')

In [40]: m.groupdict()
Out[40]: {'mac': 'aabb.cc10.7000', 'port': 'Gi0/1', 'vlan': '0'}
```


## question 10

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

regex = re.compile('(?P<vlan>\d+) +(?P<mac>\S+) +\w+ +(?P<port>\S+)')

m = regex.search(line)

print(m.groups())
```

Правильный ответ:
```python
('100', 'aabb.cc10.7000', 'Gi0/1')
```

### Объяснение

Это задание на два момента: вспомнить синтаксис, который используется при компиляции регулярного выражения.

И то, что несмотря на то, что в выражении используются именованные группы, по методу groups() будут доступны результаты, как и в случае когда используются нумерованные группы
```python
In [42]: line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

In [43]: regex = re.compile('(?P<vlan>\d+) +(?P<mac>\S+) +\w+ +(?P<port>\S+)')

In [44]: m = regex.search(line)

In [45]: print(m.groups())
('100', 'aabb.cc10.7000', 'Gi0/1')
```


## question 11

Какой результат будет выведен на стандартный поток вывода в последнем выражении?
```python
line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

regex = re.compile('(?P<vlan>\d+) +(?P<mac>\S+) +\w+ +(?P<port>\S+)')

m = regex.search(line)

print(m.group())
```

Правильный ответ:
```python
100     aabb.cc10.7000    DYNAMIC     Gi0/1
```

### Объяснение

Метод group возвращает строку, которая соответствует регулярному выражению
```python
In [48]: line = '100     aabb.cc10.7000    DYNAMIC     Gi0/1'

In [49]: regex = re.compile('(?P<vlan>\d+) +(?P<mac>\S+) +\w+ +(?P<port>\S+)')

In [50]: m = regex.search(line)

In [51]: print(m.group())
100     aabb.cc10.7000    DYNAMIC     Gi0/1
```
