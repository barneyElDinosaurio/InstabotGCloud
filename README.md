## InstagranBotConsole
This
## Requirements
`Python2.7` minimum
A working Instagram account

## Usage


| Parameter            | Type|                Description                           |        Default value             |                 Example value                   |
|:--------------------:|:---:|:----------------------------------------------------:|:--------------------------------:|:-----------------------------------------------:|
| login                | str | your instagram username                              |                                  | python_god                                      |
| password             | str | your instagram password                              |                                  | python_god_password                             |
| like_per_day         | int | how many likes the bot does in 1 day                 | 1000                             | 500                                             |
| media_max_like       | int | don't like if media has more than ... likes          | 0                                | 100                                             |
| media_min_like       | int | don't like if media has less than ... likes          | 0                                | 5                                               |
| follow_per_day       | int | how many users to follow in 1 day                    | 0                                | 100                                             |
| follow_time          | int | how many times passes before the  bot unfollows a followed user (sec) | 5 * 60 * 60     | 60 * 60                                         |
| unfollow_per_day     | int | how many user unfollows the bot does in day          | 0                                | 100                                             |
| comments_per_day     | int | how many comments the bot writes in a day            | 0                                | 50                                              |
| tag_list             | list| list of tag the bot uses                             | ['cat', 'car', 'dog']            | ['moto', 'girl', 'python']                      |
| tag_blacklist        | list| list of tags the bot refuses to like                 | []                               | ['rain', 'thunderstorm']                        |
| user_blacklist       | dict| don't like posts from certain users                  | {}                               | {'hellokitty':'', 'hellokitty3':''}             |
| max_like_for_one_tag | int | bot get 21 media from one tag, how many use by row   | 5                                | 10                                              |
| unfollow_break_min   | int | Minimum seconds for unfollow break pause             | 15                               | 30                                              |
| unfollow_break_max   | int | Maximum seconds for unfollow break pause             | 30                               | 60                                              |
| log_mod              | int | logging mod                                          | 0                                | 0 log to console, 1 log to file, 2 no log.      |
| proxy             | string | Access instagram through a proxy server              |                                  | Without authentication: proxy:port, example: 10.10.1.10:3128, with authentication: user:password@proxy:port, example: user:password@10.10.1.10:3128 |

####2) Seteo de likes y unlikes:
######Be careful, Si intentas hacer mas de 1000 likes en el dia la cuenta podra ser BANEADA!!
like_per_day=1000
```

## How to install and run:
1) Download and install `Python 2.7` to your computer.

2) Download ZIP an extract

3) Double click in install_libraries.pyc, these execute a python script installing requests module(This is just the first time).

4) Double click in instabotico.pyc

5)Uso interno
RECOMENDACIONES DE USO:
likes por dia = 1000
maximo likes por TAG = 50
seguir por dia = 300
dejar de seguir cada dia = 300

MODOS
modo = 0 : hace un loop en 24 horas para llegar a cumplir las metricas asignadas
modo = 1 : en este el robot compara el numero de personas seguidas con el numero de seguidores
para saber en q momento dejar de seguir o empezar a seguir en masa.
modo = 2 :es como el modo 0 pero deja de seguir a los q no te siguen

## Tested on:

Ubuntu 15.10 wily - 2.7.10

