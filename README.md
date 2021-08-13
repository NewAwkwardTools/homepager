# Homepager

![](resources/Pics/Screenshot\ 2021-08-13\ at\ 15-05-46\ HomePage.png)

一个简洁的首页生成器

A simple homepage generator.

目前正在开发中..

Under developing now...

# Dependency

* Python 3.6+
* Python library
    * toml
* [titlegetter](https://github.com/WeepingDogel/TitleGetter)

# Installation

By git:
```
$ git clone https://github.com/NewAwkwardTools/homepager.git
```

By [aur](https://aur.archlinux.org/packages/homepager/)
```
$ yay -S homepager
```

# Usage

At first, you need to create a `*.txt` file and add the urls you want.

For example:

```bash
vim list.txt 
```

```txt
https://www.runoob.com/
https://zh.wikipedia.org/zh/Wikipedia:%E9%A6%96%E9%A1%B5
https://wiki.archlinux.org/
https://weepingdogel.github.io/
https://github.com/
https://blog.lilydjwg.me/
https://liolok.com/zhs/
https://esonhugh.me/
https://blog.piggy.moe/
https://blog.atri.tk/
https://9bie.org/
https://blog.yuuta.moe/
https://xueya.me/
https://farseerfc.me/ 
https://prism-break.org/zh-CN/
```

If you are an Arch Linux user who has installed it by aur, just execute this on a terminal.

```bash
homepager -i list.txt
```

Wait for a while, there will be a directory named `public/`.


**If you've installed it by git, then you need to keep your shell in the directory `homepager`.**

```bash
cd homepager
```

You need to execute it manully, and the `python` should be typed in front.

```
python homepager -i list.txt
```

After minutes or seconds, there will also be a directory named `public/` in the directory named `homepager/`.

## Notice

1. It's not necessary to name after the  `*.txt` file as `list.txt`, but you should know its location.

2. It's still on the testing stage, there are some problems and bugs we haven't seen. You can post an issue or pull requests.
