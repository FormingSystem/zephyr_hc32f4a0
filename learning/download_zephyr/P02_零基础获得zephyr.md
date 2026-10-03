---
id: zephyr-download-notes-02
title: 从零理解：我们到底怎样把 Zephyr 源码下载下来
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2. 从零理解：我们到底怎样把 Zephyr 源码下载下来

下载前先按[本地代理配置](代理配置.md)核对 v2rayN 的 `10808` 混合端口，配置 Git 并测试连接；浏览器下载 ZIP 还需使用系统代理或浏览器代理。

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。当前 HC32 工程请按[项目安装流程](../../project-docs/environment.md)操作；已整理的入门主线见[工程准备大纲](../P01_zephyr_make_project/大纲.md)。

对，这个教学方向更合适。不能直接写“不要用 `sparse-checkout`”，因为一个没接触过 Git 的读者根本不知道 **checkout 是什么、sparse 又是在稀疏什么、它和减少下载量是不是一回事**。

这一部分建议直接改成下面这种写法。

在讨论“怎么少下载一些 Zephyr 内容”之前，需要先理解 Git 下载一个工程时，到底下载了什么。

即使读者从来没有使用过 Git，也应该能够看懂这一节。

------

### 1. 什么是 Git 仓库

Zephyr 的源代码托管在 Git 仓库中。

可以暂时把 Git 仓库理解成：

```
Git 仓库
│
├── 当前版本的源代码
│
│   ├── kernel/
│   ├── drivers/
│   ├── arch/
│   ├── boards/
│   └── ...
│
└── 源代码的历史记录
    │
    ├── 今天修改了什么
    ├── 昨天修改了什么
    ├── 一个月前修改了什么
    ├── 一年前修改了什么
    └── ...
```

也就是说，一个 Git 仓库并不仅仅包含“现在看到的代码”。

它还保存了大量历史版本。

例如 Zephyr 可能经历：

```
commit A
   ↓
commit B
   ↓
commit C
   ↓
commit D
   ↓
...
   ↓
commit N
```

这里的 `commit` 可以暂时理解成：

> 某一次已经保存到 Git 历史中的代码版本。

因此，如果执行最普通的：

```
git clone https://github.com/zephyrproject-rtos/zephyr.git
```

Git 默认不仅会得到当前源码，还会获取这个仓库的历史对象。

官方 `git clone` 的定义就是：把一个已有 Git 仓库复制成本地仓库，并建立对应的远程仓库关系。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

------

## 2.1 `git clone` 是什么

先看最普通的命令：

```
git clone https://github.com/zephyrproject-rtos/zephyr.git
```

一段一段解释。

### 2.1 `git`

```
git
```

表示：

> 调用 Git 程序。

类似于：

```
python
cmake
west
```

都是在调用一个程序。

------

### 2.2 `clone`

```
git clone
```

`clone` 的中文意思可以理解为：

> 克隆。

它做的事情不是简单地“下载一个 ZIP 文件”。

而是：

```
远程 Git 仓库
       │
       │ git clone
       ▼
本地 Git 仓库
```

最终本地通常会出现：

```
zephyr/
│
├── arch/
├── boards/
├── drivers/
├── kernel/
├── ...
│
└── .git/
```

这里有一个非常重要的目录：

```
.git/
```

普通文件：

```
kernel/
drivers/
arch/
```

是我们平时看到和修改的代码。

而：

```
.git/
```

保存 Git 自己管理的数据，例如：

```
提交历史
分支
标签
远程仓库信息
文件对象
版本关系
```

因此可以简单理解为：

```
zephyr/
│
├── 我们工作的源代码
│
└── .git/
       ↓
   Git 自己保存的版本数据库
```

------

## 2.2 为什么完整 `git clone` 可能不是我们想要的

我们只是想学习或者编译一个确定版本的 Zephyr。

例如：

```
Zephyr v4.4.x
```

我们可能根本不关心：

```
2019 年的版本
2020 年的版本
2021 年的版本
……
几年前每一次 commit
```

但是普通：

```
git clone
```

会把 Git 仓库需要的历史对象一起获取。

于是出现一个问题：

```
我们真正需要：

当前教学版本源码
        +
少量必要 Git 信息
```

而不是：

```
当前源码
+
大量历史版本
+
大量和教学无关的历史对象
```

所以第一种优化方式不是删除源码目录。

而是：

> 减少 Git 历史。

------

## 2.3 第一种优化：浅克隆 `--depth`

例如：

```
git clone --depth 1 https://github.com/zephyrproject-rtos/zephyr.git
```

这里增加了：

```
--depth 1
```

------

### 4.1 `depth` 是什么意思

`depth`：

```
深度
```

这里指：

> 下载多少层提交历史。

例如完整仓库：

```
最新版本
   │
   ▼
commit 1000
   │
commit 999
   │
commit 998
   │
...
   │
commit 1
```

正常 clone：

```
把完整历史关系获取下来
```

而：

```
--depth 1
```

可以简单理解成：

```
只保留最靠近当前版本的一层历史
```

例如：

```
远程仓库：

commit 1000  ← 当前版本
commit 999
commit 998
commit 997
...
commit 1


--depth 1


本地：

commit 1000
```

这种 Git 仓库通常叫：

```
shallow clone
```

中文通常称：

> 浅克隆。

Git 官方文档对 `--depth <depth>` 的定义就是创建一个截断历史的 shallow clone。[Git](https://git-scm.com/docs/git-clone.html?utm_source=chatgpt.com)

------

## 2.4 为什么教学环境适合 `--depth 1`

假设我们的目标只是：

```
下载源码
→
配置 Zephyr
→
编译
→
烧录
→
学习驱动
```

通常不需要研究 Zephyr 几年前的提交历史。

因此：

```
git clone --depth 1 ...
```

通常比：

```
git clone ...
```

更符合我们的目的。

两者得到的当前源码基本都是完整的：

```
arch/
boards/
drivers/
kernel/
lib/
soc/
subsys/
...
```

主要差异在于 Git 历史。

可以理解成：

```
普通 clone

源码：★★★★★
历史：★★★★★


--depth 1

源码：★★★★★
历史：★
```

所以这里优化的是：

> Git 历史下载量。

而不是：

> Zephyr 当前源码目录。

------

## 2.5 但我们还没有指定到底要哪个 Zephyr 版本

例如：

```
git clone --depth 1 https://github.com/zephyrproject-rtos/zephyr.git
```

虽然减少了历史，但是它仍然会按照远程仓库默认分支进行克隆。

教学环境通常不应该这样。

因为：

```
今天下载
```

和：

```
半年后下载
```

得到的源码可能发生变化。

教学文档最重要的一件事情就是：

> 固定版本。

例如：

```
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

------

## 2.6 `--branch` 是什么

这里：

```
--branch v4.4.0
```

表示：

> 我们明确指定要获取哪个分支或者标签。

`--branch` 可以简写为：

```
-b
```

所以：

```
git clone --branch v4.4.0 ...
```

和：

```
git clone -b v4.4.0 ...
```

意思相同。

Git 官方 `clone` 文档也说明，`--branch` 可以让 clone 指向指定 branch，也可以指定 tag。[Git](https://git-scm.com/docs/git-clone.html?utm_source=chatgpt.com)

------

## 2.7 什么是 branch

`branch` 就是：

```
分支
```

可以把软件开发想象成：

```
                 ┌── 开发功能 A
                 │
主开发线 ─────────┼── 开发功能 B
                 │
                 └── 修复 Bug
```

Git 可以同时维护不同开发线。

例如：

```
main
release
development
```

都可以是不同 branch。

------

## 2.8 什么是 tag

软件发布正式版本时，经常会给某个 commit 打一个固定标记。

例如：

```
某个 commit
    │
    └── tag: v4.4.0
```

这个 tag 可以理解成：

> 给某个确定版本贴了一个不会随开发继续前进的版本标签。

例如：

```
v4.3.0
v4.3.1
v4.4.0
```

所以教学环境一般更喜欢：

```
--branch v4.4.0
```

而不是：

```
--branch main
```

因为：

```
main
```

会不断变化。

而：

```
v4.4.0
```

指向确定版本。

------

## 2.9 现在把整条命令重新读一遍

```
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

不要把它当成一串魔法命令。

可以逐项翻译。

```
git
│
└── 使用 Git 工具


clone
│
└── 从远程仓库创建一个本地 Git 仓库


--branch v4.4.0
│
└── 我要 v4.4.0 这个确定版本


--depth 1
│
└── 不需要完整 Git 历史，只保留很浅的历史


https://github.com/zephyrproject-rtos/zephyr.git
│
└── Zephyr Git 仓库地址
```

把整句话翻译成中文就是：

> 使用 Git，把 Zephyr 仓库的 v4.4.0 版本克隆到电脑上，但是不要下载完整提交历史，只获取深度为 1 的浅历史。

这才是读者应该真正理解的内容。

------

## 2.10 那么 `sparse-checkout` 又是什么

到这里开始进入另外一个完全不同的问题。

前面的：

```
--depth 1
```

解决的是：

> 历史太多。

而 `sparse-checkout` 主要解决的是：

> 当前仓库里的目录和文件太多，我只想让其中一部分出现在工作目录中。

这是两个完全不同的维度。

------

## 2.11 什么叫 checkout

这是 Git 初学者非常容易困惑的一个单词。

`checkout` 在这里可以简单理解成：

> 把 Git 仓库里的某个版本真正展开成我们可以看到和编辑的文件。

例如 `.git` 中保存 Git 数据：

```
.git/
```

然后 Git 根据某个版本，将文件展开到：

```
kernel/
drivers/
arch/
...
```

这些我们能够：

```
打开
阅读
编辑
编译
```

的文件，组成：

```
working tree
```

中文通常叫：

> 工作树 / 工作目录。

因此：

```
Git 数据库
.git/
    │
    │ checkout
    ▼
工作目录
kernel/
drivers/
arch/
...
```

------

## 2.12 什么叫 sparse

`sparse`：

```
稀疏的
```

因此：

```
sparse-checkout
```

可以理解成：

> 不把仓库里的所有目录都展开到工作目录，只展开我指定的一部分。

例如一个仓库有：

```
project/
├── arch/
├── boards/
├── drivers/
├── kernel/
├── samples/
├── tests/
└── doc/
```

而我只关心：

```
arch/
drivers/
kernel/
```

使用 sparse-checkout 后，工作目录可以只显示：

```
project/
├── arch/
├── drivers/
└── kernel/
```

Git 官方文档把 sparse-checkout 描述为：让工作树只包含用户关注的一部分文件；在 cone mode 下可以按目录指定范围。[Git](https://git-scm.com/docs/sparse-checkout?utm_source=chatgpt.com)

------

## 2.13 一个最简单的 sparse-checkout 示例

这里先不用 Zephyr。

假设有一个仓库：

```
demo/
├── app/
├── driver/
├── docs/
├── test/
└── tools/
```

我们只想看到：

```
app/
driver/
```

可以执行：

```
git sparse-checkout init --cone
```

然后：

```
git sparse-checkout set app driver
```

逐条解释。

------

### `git sparse-checkout`

表示：

> 使用 Git 的 sparse-checkout 功能。

------

### `init`

```
git sparse-checkout init
```

表示：

> 初始化 sparse-checkout 配置。

也就是告诉 Git：

```
从现在开始，这个仓库不是默认把所有目录都放到工作区。
```

------

### `--cone`

```
--cone
```

表示使用比较适合“按目录选择”的 cone 模式。

例如：

```
git sparse-checkout set app driver
```

这种写法就非常直观：

```
我要 app/
我要 driver/
```

官方文档也区分了 cone mode 和 non-cone mode；cone mode 主要按目录选择，而 non-cone mode 可以使用更复杂的类似 gitignore 的模式。[Git](https://git-scm.com/docs/sparse-checkout?utm_source=chatgpt.com)

------

### `set`

```
git sparse-checkout set app driver
```

表示：

> 把 sparse-checkout 的目标目录设置为 app 和 driver。

最后工作目录可能主要看到：

```
app/
driver/
```

------

## 2.14 这里有一个非常容易产生的误解

很多初学者看到：

```
工作目录只剩几个目录
```

会认为：

> 那么其他文件一定没有下载。

不一定。

这是学习 Git 下载优化时非常重要的一点。

单独使用：

```
sparse-checkout
```

主要控制：

> 哪些文件出现在工作树里。

它和：

> 网络到底下载了多少 Git 对象

不是完全同一个问题。

因此：

```
sparse-checkout
```

不能简单等价为：

```
只从服务器下载这些目录。
```

这两个概念一定要分清。

------

## 2.15 用一张图理解三种东西

目前我们已经碰到了三个概念：

```
branch
depth
sparse-checkout
```

它们分别控制完全不同的事情。

```
Git 仓库
│
├── 哪个版本？
│      │
│      └── --branch
│
├── 要多少历史？
│      │
│      └── --depth
│
└── 工作目录显示哪些文件？
       │
       └── sparse-checkout
```

比如：

```
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

表达的是：

```
版本：
v4.4.0

历史：
只要很浅的一层

当前源码：
完整
```

而 sparse-checkout 又是在另外一个维度控制：

```
工作区需要展开哪些目录。
```

------

## 2.16 如果真的希望减少“文件内容”的网络下载呢

Git 还有另外一个概念：

```
partial clone
```

即：

> 部分克隆。

例如：

```
git clone \
    --filter=blob:none \
    https://github.com/zephyrproject-rtos/zephyr.git
```

这里出现：

```
--filter=blob:none
```

------

## 2.17 什么是 blob

Git 内部会把不同数据保存成不同类型的对象。

对于初学者目前只需要知道：

```
blob
```

基本可以理解为：

> 文件内容对象。

比如：

```
main.c
driver.c
README.md
```

它们的文件内容最终会以 Git 对象形式进行管理。

------

## 2.18 `--filter=blob:none` 是什么意思

```
--filter=blob:none
```

大致可以理解为：

> 初始克隆时不要把所有历史文件内容全部下载下来，需要的时候再获取。

Git 官方文档明确说明：

```
--filter=blob:none
```

会过滤 blob，文件内容在需要时再由 Git 获取。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

于是：

```
普通 clone

服务器
  │
  ├── Git 历史关系
  ├── 文件内容
  ├── 文件内容
  ├── 文件内容
  └── ...
        │
        ▼
      本地
```

partial clone 则更像：

```
服务器
  │
  ├── 先给必要的 Git 信息
  │
  └── 某些文件内容暂时保留
          │
          │ 后面真的需要
          ▼
        再下载
```

这与 sparse-checkout 又不是同一个概念。

------

## 2.19 sparse-checkout 和 partial clone 可以组合

例如：

```
git clone \
    --filter=blob:none \
    --sparse \
    https://example.com/project.git
```

Git 官方 `clone` 本身就提供：

```
--sparse
```

以及：

```
--filter=<filter-spec>
```

两个独立选项。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

可以粗略理解：

```
--filter
    ↓
控制服务器初始给我多少 Git 对象

--sparse
    ↓
控制工作目录先展开多少文件
```

两者解决的问题不同。

------

## 2.20 为什么我们暂时不推荐对 Zephyr 主仓库做 sparse-checkout

现在读者终于有足够背景理解这句话了。

原因不是：

> sparse-checkout 不好。

而是：

> Zephyr 本身不是一个几个目录互不相关的简单工程。

Zephyr 构建涉及大量跨目录依赖。

例如：

```
应用程序
   │
   ▼
CMake
   │
   ├── cmake/
   │
   ├── scripts/
   │
   ├── Kconfig
   │
   └── modules
   │
   ▼
Zephyr Kernel
   │
   ├── kernel/
   ├── arch/
   ├── include/
   ├── lib/
   └── subsys/
   │
   ▼
Hardware Description
   │
   ├── boards/
   ├── soc/
   └── dts/
   │
   ▼
Drivers
       └── drivers/
```

初学者很难提前准确回答：

```
我的这个板子编译到底会访问哪些目录？
```

如果一开始就写：

```
git sparse-checkout set \
    kernel \
    drivers \
    arch/arm
```

看起来很精简。

但是可能很快发现：

```
还需要 cmake/
```

补上以后：

```
又需要 scripts/
```

之后：

```
还需要 dts/
```

然后：

```
还需要 include/
soc/
boards/
lib/
subsys/
```

最后可能变成：

```
我们为了节省一点目录，
却花了大量时间维护“到底缺哪个目录”。
```

对于教学环境，这不是很好的收益交换。

------

## 2.21 所以我们真正推荐什么

对于 **Zephyr 主仓库**，推荐：

```
git clone \
    --branch <固定版本> \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

原则是：

```
源码目录：
完整保留

Git 历史：
大幅减少
```

即：

```
              普通 clone       推荐方案

当前源代码        完整             完整

Git 历史          很多             很少

构建兼容性         高               高

初学难度           低               低
```

而不是首先：

```
砍 kernel
砍 drivers
砍 subsys
砍 scripts
砍 cmake
```

------

## 2.22 真正应该大规模裁剪的是“仓库数量”

这里开始进入 Zephyr 与普通单仓库项目最大的区别。

Zephyr 开发环境并不只有：

```
zephyr.git
```

还可能存在很多独立 Git 仓库：

```
zephyr
cmsis
hal_stm32
hal_nxp
hal_nordic
hal_espressif
mbedtls
mcuboot
lvgl
littlefs
...
```

这时候：

```
少下载一个 Zephyr 源码目录
```

和：

```
整个 hal_nxp 仓库都不下载
```

完全不是一个量级的优化思路。

我们的策略因此应该是：

```
第一层：

Zephyr 主仓库
    ↓
源码基本完整保留
    ↓
Git 历史做浅克隆


第二层：

Zephyr 外部模块
    ↓
根据 MCU 和功能需求决定
    ↓
不需要的仓库根本不要下载


第三层：

工具链
    ↓
根据 CPU 架构决定
    ↓
只下载 ARM 工具链
```

这才是“小 Zephyr 环境”的主要设计方法。

------

## 2.23 用 HC32F4A0 举例

例如我们的目标芯片是：

```
HC32F4A0PITB
```

CPU：

```
ARM Cortex-M4F
```

我们首先推导：

```
HC32F4A0
    │
    ▼
ARM Cortex-M4F
    │
    ├── 需要 ARM 架构支持
    │
    ├── 需要 CMSIS
    │
    ├── 需要 HC32 SoC 支持
    │
    ├── 需要 HC32 DDL/HAL
    │
    └── 需要 ARM GCC Toolchain
```

但它完全不需要：

```
STM32 HAL
NXP HAL
Nordic HAL
ESP32 HAL
Renesas HAL
```

所以真正应该优化的是：

```
不要：

Zephyr
+ CMSIS
+ STM32
+ NXP
+ Nordic
+ ESP
+ Renesas
+ ...
```

而是：

```
只要：

Zephyr
+
CMSIS
+
HC32 支持代码
+
ARM Toolchain
```

------

## 2.24 因此最终的下载优化可以分成四层

以后整篇教程都可以沿着这个模型往下讲。

```
              我到底想减少什么？
                     │
        ┌────────────┼─────────────┐
        │            │             │
        ▼            ▼             ▼

     Git 历史      源码目录       外部仓库
        │            │             │
        ▼            ▼             ▼

 --depth 1      sparse-checkout   west manifest
                                      │
                                      ▼
                                只选择必要模块

                                      +
                                      │
                                      ▼

                                  Toolchain
                                      │
                                      ▼
                              只选择目标架构
```

对于我们的教学环境，优先级应该是：

```
优先级 1
固定 Zephyr 版本

        ↓

优先级 2
--depth 1
减少 Git 历史

        ↓

优先级 3
自定义 west manifest
减少外部仓库数量

        ↓

优先级 4
只下载 ARM Toolchain

        ↓

优先级 5
必要时再研究 sparse-checkout / partial clone
```

------

## 2.25 给完全没有 Git 基础读者的一张总结表

| 命令/概念         | 它解决什么问题        | 初学者可以怎样理解                     |
| ----------------- | --------------------- | -------------------------------------- |
| `git clone`       | 获取一个 Git 仓库     | 把远程代码仓库复制到电脑               |
| `--branch`        | 选择版本              | 我要哪个分支/版本标签                  |
| `--depth 1`       | 减少历史              | 当前代码要，但以前很多年的修改记录不要 |
| `checkout`        | 展开代码              | 把 Git 中某个版本变成磁盘上可见的文件  |
| `sparse-checkout` | 减少工作区文件        | 一个仓库中我只想看到部分目录           |
| `--filter`        | 减少初始 Git 对象下载 | 某些文件内容先不拿，用到再获取         |
| `west manifest`   | 控制多个仓库          | 决定 Zephyr 环境到底包含哪些 Git 仓库  |
| Toolchain         | 编译目标 CPU          | Cortex-M4F 就选择 ARM 工具链           |

其中尤其需要记住：

```
--depth
```

和：

```
sparse-checkout
```

并不是同一个东西。

更不是：

```
west manifest
```

。

它们分别处在三层：

```
一个仓库有多少历史
       ↓
    --depth


一个仓库工作区显示多少目录
       ↓
 sparse-checkout


整个 Zephyr Workspace 有多少仓库
       ↓
  west manifest
```

**下一步教学文档就很适合从这里继续进入 `west`：先解释为什么 Zephyr 明明已经下载了 `zephyr.git`，执行 `west update` 却又冒出来几十个 Git 仓库。然后再从“一个 Git 仓库”自然过渡到“west 管理多个 Git 仓库”，这样零 Git 基础的读者也不会突然掉进 `west.yml`、manifest、project 这些概念里。**

[参考资料目录](README.md) · [上一篇](P01_如何下载zephyr.md) · [下一篇](P03_国内如何更快下载zephyr.md)
