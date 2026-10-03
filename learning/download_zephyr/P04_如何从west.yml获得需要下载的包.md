---
id: zephyr-download-notes-04
title: west.yml 解析与模块下载
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第4章\_west.yml\_解析与模块下载

本章操作终端统一为 **MSYS2 UCRT64 Bash**，主机仍是 Windows x64。独立下载实验使用 `~/zephyr-download-lab`；路径、工具准备和当前 HC32 集成工程的区别见[环境与目录约定](环境与目录约定.md)。下文保留的版本、模块名和仓库地址示例须结合实际清单核对。

下载前先按[本地代理配置](代理配置.md)核对 v2rayN 的 `10808` 混合端口，配置 Git 并测试连接；浏览器下载 ZIP 还需使用系统代理或浏览器代理。

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。当前 HC32 工程请按[项目安装流程](../../project-docs/environment.md)操作；已整理的入门主线见[工程准备大纲](../P01_zephyr_make_project/大纲.md)。

**本章目录**

- [4.1 读取版本与解压位置](#section-4-1)
- [4.2 拼出真实仓库地址](#section-4-2)
- [4.3 按架构与厂商筛选依赖](#section-4-3)
- [4.4 在 UCRT64 中搜索实际源码](#section-4-4)
- [4.5 按功能验证模块集合](#section-4-5)
- [4.6 记录并复用下载结果](#section-4-6)


前面我们已经确定了一个原则：

> **第一阶段先获取“能编译的源码”，不要求先拥有完整 Git 仓库。**

现在真正的问题就变成了：

```text
我已经下载了 zephyr.zip

但是 Zephyr 不是只有一个仓库。

那么：
    还缺哪些仓库？
    去哪里下载？
    下载哪个版本？
    解压到哪里？
    哪些根本不用下载？
```

Zephyr 官方本身支持“不使用 west”的工作方式，只是这时额外仓库需要开发者自己获取，并把模块位置告诉构建系统。官方也明确说明，这实际上就是手工完成 west 原本替你做的工作。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/without-west.html?utm_source=chatgpt.com)

所以这一章最重要的文件就是：

```text
zephyr/west.yml
```

------

<a id="section-4-1"></a>

## 4.1\_读取版本与解压位置

先从一个 project 描述建立名称、revision 与 path 的关系。

### 4.1.1\_先理解\_west.yml\_是什么

拿到 Zephyr ZIP 后，在源码根目录通常可以找到：

```text
zephyr/
├── arch/
├── boards/
├── drivers/
├── kernel/
├── modules/
├── scripts/
├── soc/
├── subsys/
├── west.yml       ← 现在重点看这个
└── ...
```

`west.yml` 是一个 YAML 文本文件。

不要因为它里面内容很多就觉得复杂。

对现在这个阶段，可以把它理解成：

> **Zephyr 官方提供的一张“外部仓库依赖清单”。**

Zephyr 自己的源码已经在：

```text
zephyr/
```

里面。

但是有很多东西并不放在 Zephyr 主仓库，例如：

```text
ARM CMSIS

STM32 HAL
Nordic HAL
NXP HAL

LittleFS
FatFS

mbedTLS

MCUboot

OpenAMP
```

它们分别是独立 Git 仓库。

`west.yml` 的作用之一，就是告诉 west：

```text
这个仓库叫什么？
从哪里下载？
下载哪个版本？
放在哪里？
```

west 官方也把 manifest 定义为管理 workspace 中多个 Git repository 的 YAML 文件。[GitHub](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/develop/west/basics.rst?utm_source=chatgpt.com)

------

### 4.1.2\_先看一个最简单的项目描述

实际 `west.yml` 中会看到类似内容：

```text
projects:

  - name: cmsis_6
    repo-path: CMSIS_6
    revision: 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
    path: modules/hal/cmsis_6
```

初学者不要直接跳过去。

我们逐行解释。

------

#### (1)\_name\_这个项目叫什么

```text
name: cmsis_6
```

意思是：

```text
west 内部给这个项目起的名字
```

这里叫：

```text
cmsis_6
```

它不是磁盘路径，也不一定就是 GitHub 仓库的真实名字。

只是 west 用来识别这个项目的名称。

例如以后：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west update cmsis_6
```

其中的：

```text
cmsis_6
```

就是这个：

```text
name:
```

------

### 4.1.3\_revision\_到底下载哪个版本

下一行：

```text
revision: 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
```

这个长字符串：

```text
1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
```

是一个 Git commit ID。

可以把它理解成：

> Zephyr 要求 CMSIS_6 必须处于这个确定的源码版本。

这非常重要。

假如我们自己跑去 CMSIS 仓库点击：

```text
main
→
Download ZIP
```

那是不严谨的。

因为：

```text
Zephyr 要的 CMSIS 版本
```

可能是：

```text
三个月前的某个 commit
```

而当前：

```text
CMSIS main
```

已经发展到另外一个版本。

于是可能出现：

```text
Zephyr源码：版本 A

CMSIS源码：版本 B

两边接口不匹配
```

然后编译报一些看起来莫名其妙的错误。

所以：

> **不要随便下载外部模块最新版。**

应该按照：

```text
revision:
```

指定的版本下载。

------

### 4.1.4\_为什么\_commit\_ID\_特别适合我们的\_ZIP\_方案

GitHub 不仅可以下载：

```text
branch ZIP
tag ZIP
```

还可以直接下载：

```text
指定 commit 的 ZIP
```

GitHub 官方明确支持 branch、tag 和具体 commit 的源码快照，而且 ZIP 不包含完整 Git 历史。[GitHub Docs](https://docs.github.com/ko/repositories/working-with-files/using-files/downloading-source-code-archives?utm_source=chatgpt.com)

假设：

```text
仓库：

https://github.com/zephyrproject-rtos/CMSIS_6
```

commit：

```text
1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
```

那么 ZIP 可以直接对应到这个 commit。

其形式是：

```text
https://github.com/zephyrproject-rtos/CMSIS_6/archive/1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8.zip
```

这样有一个很大的优点：

```text
不是：

今天的 CMSIS main


而是：

Zephyr 明确要求的 CMSIS commit
```

对于教学环境和公司 SDK，这种方式比下载 `main.zip` 更可靠。

------

### 4.1.5\_path\_解压以后放在哪里

继续看：

```text
path: modules/hal/cmsis_6
```

意思不是：

> CMSIS 仓库里面有这个目录。

而是：

> 在 Zephyr workspace 中，这个仓库应该位于这个位置。

例如 workspace：

```text
~/zephyr-download-lab/
```

那么：

```text
path: modules/hal/cmsis_6
```

最终就是：

```text
~/zephyr-download-lab/
└── modules/
    └── hal/
        └── cmsis_6/
```

所以 ZIP 下载以后，不能随便扔到：

```text
Downloads\
```

然后就认为环境完整了。

应该整理成：

```text
workspace/
│
├── zephyr/
│
└── modules/
    └── hal/
        └── cmsis_6/
```

------

### 4.1.6\_ZIP\_解压后为什么经常多一层目录

例如下载：

```text
CMSIS_6-1c1840af7a7e....zip
```

解压以后可能得到：

```text
CMSIS_6-1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8/
├── CMSIS/
├── Device/
├── LICENSE
└── ...
```

但是我们需要的是：

```text
modules/
└── hal/
    └── cmsis_6/
        ├── CMSIS/
        ├── Device/
        └── ...
```

所以需要把：

```text
CMSIS_6-1c184.../
```

重命名或者移动为：

```text
cmsis_6/
```

最终不要变成：

```text
modules/hal/cmsis_6/
└── CMSIS_6-1c184.../
    └── CMSIS/
```

这种多套了一层目录的形式。

正确：

```text
modules/hal/cmsis_6/
├── CMSIS/
└── ...
```

错误：

```text
modules/hal/cmsis_6/
└── CMSIS_6-xxxxx/
    └── CMSIS/
```

这是以后非常常见的环境搭建错误。

------

<a id="section-4-2"></a>

## 4.2\_拼出真实仓库地址

继续读取 remote、url-base 和 repo-path，避免把清单名称误当成仓库地址。

### 4.2.1\_repo-path\_真实\_Git\_仓库不一定和\_name\_一样

再来看：

```text
- name: cmsis_6
  repo-path: CMSIS_6
```

为什么有：

```text
name = cmsis_6
```

同时又有：

```text
repo-path = CMSIS_6
```

因为：

```text
west 内部项目名称
```

和：

```text
远程服务器上的 Git 仓库名称
```

可以不一样。

这里：

```text
west 名称：

cmsis_6
```

而 GitHub 仓库实际叫：

```text
CMSIS_6
```

所以：

```text
repo-path: CMSIS_6
```

就是告诉 west：

> 真正去远程服务器找 `CMSIS_6` 这个 repository。

------

### 4.2.2\_那么\_GitHub\_前面的地址从哪里来

继续往 `west.yml` 上面看，会看到：

```text
remotes:

  - name: upstream
    url-base: https://github.com/zephyrproject-rtos
```

这里定义了一个：

```text
remote
```

。

暂时可以理解为：

> 给一个 Git 服务器地址起个简称。

例如：

```text
name: upstream
```

就是给：

```text
https://github.com/zephyrproject-rtos
```

起名：

```text
upstream
```

这样后面就不用反复写完整 GitHub URL。

------

### 4.2.3\_url-base\_是仓库地址的公共部分

例如：

```text
url-base: https://github.com/zephyrproject-rtos
```

而 CMSIS：

```text
repo-path: CMSIS_6
```

把两部分拼起来：

```text
url-base
+
repo-path
```

就是：

```text
https://github.com/zephyrproject-rtos
+
CMSIS_6
```

最终：

```text
https://github.com/zephyrproject-rtos/CMSIS_6
```

这就是实际 GitHub repository。

------

### 4.2.4\_如果没有\_repo-path\_怎么办

有些 project 只有：

```text
- name: fatfs
  revision: xxxxx
  path: modules/fs/fatfs
```

却没有：

```text
repo-path:
```

这时通常：

```text
repository 名称
=
name
```

因此：

```text
name = fatfs
```

对应：

```text
https://github.com/zephyrproject-rtos/fatfs
```

可以理解为：

```text
如果 repo-path 存在：
    使用 repo-path

如果 repo-path 不存在：
    使用 name
```

------

### 4.2.5\_defaults.remote\_又是什么

实际 Zephyr `west.yml` 顶部还会看到类似：

```text
defaults:
  remote: upstream
```

意思是：

> 如果某个 project 自己没有特别声明使用哪个 remote，就默认使用 `upstream`。

例如：

```text
defaults:
  remote: upstream

remotes:
  - name: upstream
    url-base: https://github.com/zephyrproject-rtos
```

然后：

```text
- name: cmsis_6
  repo-path: CMSIS_6
```

虽然它没有写：

```text
remote: upstream
```

实际上继承了：

```text
defaults.remote
```

所以还是从：

```text
https://github.com/zephyrproject-rtos
```

下载。

------

### 4.2.6\_到这里我们已经可以手工解析一个\_project

例如：

```text
defaults:
  remote: upstream

remotes:
  - name: upstream
    url-base: https://github.com/zephyrproject-rtos

projects:

  - name: cmsis_6
    repo-path: CMSIS_6
    revision: 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
    path: modules/hal/cmsis_6
```

我们自己就能得到下面四个信息：

| 项目        | 得到的内容                   |
| ----------- | ---------------------------- |
| west 项目名 | `cmsis_6`                    |
| GitHub 仓库 | `zephyrproject-rtos/CMSIS_6` |
| 源码版本    | `1c1840af...`                |
| 本地目录    | `modules/hal/cmsis_6`        |

因此整个动作就变成：

```text
找到项目
    ↓
找到 URL
    ↓
找到 revision
    ↓
下载该 revision 的 ZIP
    ↓
解压
    ↓
放到 path 指定的位置
```

这就是我们人工替代：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west update cmsis_6
```

所做的事情。

------

<a id="section-4-3"></a>

## 4.3\_按架构与厂商筛选依赖

先核对 CPU 架构和 CMSIS，再判断厂商 HAL 是内置还是独立仓库。

### 4.3.1\_但是\_west.yml\_中有几十个项目\_我们难道一个个下载

不是。

这是这一章最重要的地方。

`west.yml` 表示的是：

> **Zephyr 能够使用的完整外部项目集合。**

不是：

> **你的 HC32F4A0 工程必须使用的全部项目。**

例如当前 upstream Zephyr manifest 中包含：

```text
CMSIS
FatFS
LittleFS
mbedTLS
MCUboot
各种厂商 HAL
测试工具
BabbleSim
……
```

当前 upstream manifest 本身还通过 `group-filter` 默认禁用了 babblesim、optional、testing 等组。[GitHub](https://github.com/zephyrproject-rtos/zephyr/blob/main/west.yml?utm_source=chatgpt.com)

所以看到：

```text
projects:
    一大堆项目
```

不能得出：

```text
这些都要下载。
```

我们的真正目标是：

> **从这张“大菜单”里找出当前板卡和当前功能真正要吃的东西。**

------

### 4.3.2\_第一层筛选\_先看\_CPU\_架构

对于我们的目标：

```text
HC32F4A0PITB
```

首先不要考虑 SPI、UART、I2C。

先看 CPU：

```text
HC32F4A0
    ↓
ARM Cortex-M4F
```

于是已经可以推导出：

```text
需要 ARM Cortex-M 架构支持
```

Zephyr 从 4.2 开始，Cortex-M board/SoC 构建正式要求 `CMSIS_6`；CMSIS 5 仍主要用于旧 HAL 兼容，而 Cortex-M 新架构代码应使用 CMSIS 6。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/hardware/arch/arm_cortex_m.html?utm_source=chatgpt.com)

因此，如果我们的 Zephyr 基线是：

```text
Zephyr >= 4.2
```

对于 Cortex-M4F：

```text
cmsis_6
```

基本可以直接进入“基础下载集合”。

于是第一个依赖出现：

```text
HC32F4A0
    ↓
Cortex-M4F
    ↓
CMSIS_6
```

------

### 4.3.3\_注意\_CMSIS\_和\_CMSIS\_6\_不是一回事

现在 upstream manifest 中同时存在：

```text
cmsis
```

以及：

```text
cmsis_6
```

例如：

```text
- name: cmsis
  path: modules/hal/cmsis

- name: cmsis_6
  repo-path: CMSIS_6
  path: modules/hal/cmsis_6
```

Zephyr 官方 Cortex-M 文档解释得很清楚：

```text
CMSIS 5
    ↓
主要保留给旧 Vendor HAL 兼容

CMSIS 6
    ↓
新的 Cortex-M architecture headers
```


所以对我们的 HC32 环境不能简单写：

```text
Cortex-M → 下载 cmsis
```

应该写：

```text
Zephyr 4.2+
Cortex-M
    ↓
优先确定 cmsis_6

如果 HC32 DDL/HAL 本身还引用 CMSIS 5
    ↓
可能还要额外保留 cmsis
```

这就体现出：

> **依赖不仅由 CPU 决定，还要继续看 Vendor HAL。**

------

### 4.3.4\_第二层筛选\_HC32\_HAL\_到底在哪里

现在进入真正和芯片厂商相关的部分。

对于一个 MCU，Zephyr 通常需要：

```text
Zephyr 通用驱动
        │
        ▼
SoC 支持层
        │
        ▼
Vendor HAL / LL / DDL
        │
        ▼
MCU 寄存器
```

例如 STM32 会有：

```text
hal_stm32
```

Nordic 会有：

```text
hal_nordic
```

NXP 会有：

```text
hal_nxp
```

对于我们的 HC32F4A0，需要检查：

```text
HC32 DDL 到底放在哪里？
```

这里存在两种情况。

------

### 4.3.5\_情况一\_HC32\_DDL\_已经放在\_Zephyr\_主\_ZIP\_中

例如我们自己的 Zephyr fork：

```text
zephyr/
├── soc/
│   └── hdsc/
│       └── hc32f4a0/
│
├── boards/
│   └── ...
│
└── drivers/
```

同时 DDL 也直接被我们纳入：

```text
zephyr/soc/...
```

或者：

```text
zephyr/drivers/...
```

那么：

```text
HC32 DDL
```

就已经随着：

```text
zephyr.zip
```

下载完成。

这种情况下不需要另外寻找：

```text
hal_hc32.zip
```

。

------

### 4.3.6\_情况二\_HC32\_DDL\_是独立仓库

另外一种更标准的模块化方式可能是：

```text
workspace/
├── zephyr/
│
└── modules/
    └── hal/
        └── hc32/
```

那么在 manifest 中应该存在类似：

```text
- name: hal_hc32
  revision: xxxxxxxxx
  path: modules/hal/hc32
```

这时：

```text
hal_hc32
```

就是第二个必须下载的外部模块。

因此不能因为：

```text
芯片叫 HC32
```

就主观假设一定存在：

```text
hal_hc32
```

。

应该先检查：

```text
我们的 Zephyr port 是怎样组织的。
```

------

<a id="section-4-4"></a>

## 4.4\_在\_UCRT64\_中搜索实际源码

用文本搜索验证清单与源码布局，进一步区分 west 项目和构建模块。

### 4.4.1\_怎么快速搜索\_west.yml\_有没有\_HC32

在 UCRT64 Bash 中进入下载实验的 Zephyr 目录。若检查的是当前集成工程，则从该工程根目录运行搜索；本工程的活动清单为 `project-west.yml`，上游 `west.yml` 只作对照。

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
cd "$HOME/zephyr-download-lab/zephyr"
```

执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
grep -ni -- "hc32" ./west.yml
```

这条命令逐项解释。

```text
grep
```

是 UCRT64 中的文本搜索工具。这里 `-n` 显示行号，`-i` 忽略大小写，`--` 结束选项；无匹配时退出码为 1。

作用类似：

```text
在一个文件里面搜索某个关键词
```

：

```text
./west.yml
```

意思是：

```text
搜索 west.yml
```

：

```text
"hc32"
```

意思是：

```text
查找字符串 hc32
```

。

如果输出类似：

```text
name: hal_hc32
path: modules/hal/hc32
```

那么说明 manifest 中确实存在 HC32 独立仓库。

如果完全没有输出，则继续检查我们自己的 HC32 port 是否直接包含 HAL。

------

### 4.4.2\_搜索整个\_Zephyr\_源码中的\_HC32

Bash：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；保留管道以说明两个工具的分工。
find . -type d \( -name .git -o -name build -o -name .venv \) -prune -o -type f -print0 |
    xargs -0 -r grep -nHiI -- "HC32F4A0"
```

这里：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
find .
```

负责从当前目录出发：

```text
遍历目录中的文件与子目录
```

。

```text
find . 的默认递归遍历
```

意思是：

```text
递归进入所有子目录
```

。

```text
-type f
```

表示：

```text
只看文件
```

。

中间的：

```text
|
```

叫管道。`-print0` 与 `xargs -0` 用 NUL 字符传递文件名，路径含空格时仍能正确分隔；`-r` 避免没有文件时启动 grep，`-H` 始终显示文件名，`-i` 忽略大小写，`-I` 跳过二进制文件。命令还通过 `-prune` 跳过 `.git`、`build`、`.venv`。

表示：

> 把左边找到的所有文件交给右边继续处理。

然后：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
xargs -0 -r grep -nHiI -- "HC32F4A0"
```

就在这些文件里面寻找：

```text
HC32F4A0
```

。

于是整条命令的中文意思就是：

> 递归找到 Zephyr 目录中的所有文件，然后搜索其中哪些文件包含 `HC32F4A0`。

------

### 4.4.3\_为什么这个搜索很有价值

假设找到：

```text
soc/hdsc/hc32f4a0/Kconfig.soc
soc/hdsc/hc32f4a0/CMakeLists.txt
soc/hdsc/hc32f4a0/soc.c
```

打开：

```text
CMakeLists.txt
```

可能会看到：

```text
zephyr_include_directories(...)
zephyr_sources(...)
```

或者引用：

```text
ZEPHYR_HAL_HC32_MODULE_DIR
```

如果出现类似：

```text
ZEPHYR_xxx_MODULE_DIR
```

通常意味着：

> 这里期望存在某个 Zephyr external module。

这时候就继续反向找：

```text
xxx
```

对应哪个 `west.yml project`。

------

### 4.4.4\_什么叫\_ZEPHYR\_<MODULE>\_MODULE\_DIR

当 Zephyr 识别到 external module 时，会为模块建立相应路径信息。

例如模块：

```text
cmsis_6
```

可能对应构建系统中的模块目录配置。

不要把：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west project
```

和：

```text
Zephyr module
```

当成完全相同的概念。

官方特别强调：

> west project 是 west 管理的 Git repository；Zephyr module 是 Zephyr 构建系统可以加载的外部项目，两者不是同一个概念。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/modules.html?utm_source=chatgpt.com)

典型 Module 中会存在：

```text
zephyr/
└── module.yml
```

。

所以下载一个 ZIP 后，还可以检查：

```text
modules/hal/hc32/
└── zephyr/
    └── module.yml
```

如果存在：

```text
zephyr/module.yml
```

就很明确：

> 这是一个 Zephyr Module。

------

<a id="section-4-5"></a>

## 4.5\_按功能验证模块集合

功能决定额外依赖，配置阶段用于检验集合是否完整，并显式说明模块路径。

### 4.5.1\_第三层筛选\_功能决定额外模块

现在我们的基础平台可能已经缩小到：

```text
Zephyr
+
CMSIS_6
+
HC32 HAL
```

但是工程功能还会继续增加依赖。

例如你启用了文件系统。

可能出现：

```text
CONFIG_FILE_SYSTEM=y
CONFIG_FILE_SYSTEM_LITTLEFS=y
```

那么就可能需要：

```text
littlefs
```

。

如果启用了：

```text
FAT filesystem
```

可能需要：

```text
fatfs
```

。

如果启用了 TLS：

```text
TLS
HTTPS
MQTT TLS
```

可能需要：

```text
mbedtls
```

。

如果启用了 Bootloader：

```text
MCUboot
```

可能需要：

```text
mcuboot
```

。

所以依赖关系不是：

```text
芯片
    ↓
一次性决定全部模块
```

而是：

```text
硬件平台
    │
    ├── CPU Architecture
    ├── Vendor HAL
    └── SoC Support

+

软件功能
    │
    ├── File System
    ├── Crypto
    ├── Bootloader
    ├── Network
    └── GUI

=
最终下载集合
```

------

### 4.5.2\_我们应该建立一个\_最小基础环境

对于目前 HC32F4A0 教学环境，第一阶段不要启用复杂功能。

例如只要求：

```text
Kernel

GPIO

UART

SPI

I2C

Timer

Shell
```

那么环境先收敛为：

```text
Zephyr 主源码
        +
CMSIS_6
        +
HC32 DDL/HAL
        +
ARM Toolchain
```

然后编译。

成功以后再增加：

```text
LittleFS
```

或者：

```text
mbedTLS
```

。

这种方式非常适合教学，因为学生会清楚看到：

```text
我增加了什么功能
        ↓
为什么多了一个依赖
        ↓
这个依赖从哪里下载
```

而不是第一次：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west update
```

就把几十个 repository 全部拉下来。

------

### 4.5.3\_一个非常重要的技巧\_先让配置阶段告诉我们缺什么

人工筛选时不必要求自己第一次就把所有依赖猜正确。

我们的策略可以是：

```text
先准备我们明确知道的最小集合
        ↓
运行 CMake 配置
        ↓
观察缺少什么
        ↓
增加对应模块
        ↓
重新配置
```

例如当前只有：

```text
zephyr/
modules/hal/cmsis_6/
```

。

执行配置后出现：

```text
某 HC32 HAL module not found
```

那就说明：

```text
HC32 HAL
```

还需要单独添加。

这不是失败。

这实际上是：

> **利用 Zephyr 构建系统验证我们的依赖分析是否完整。**

------

### 4.5.4\_不使用\_west\_时\_Zephyr\_怎么知道\_Modules\_在哪里

官方支持手动指定：

```text
ZEPHYR_MODULES
```

。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/without-west.html?utm_source=chatgpt.com)

假设：

```text
~/zephyr-download-lab/
├── zephyr/
└── modules/
    └── hal/
        ├── cmsis_6/
        └── hc32/
```

那么可以在 CMake 配置阶段告诉 Zephyr：

```text
我有哪些 external modules。
```

概念上，以下是附加到 `cmake` 命令的一个参数片段，当前目录为下载实验根目录。`cygpath -m` 转成 Windows 路径；双引号确保分号由 CMake 解析，不被 Bash 当成命令分隔：

```text
"-DZEPHYR_MODULES=$(cygpath -m "$PWD/modules/hal/cmsis_6");$(cygpath -m "$PWD/modules/hal/hc32")"
```

Windows 上建议这里统一使用：

```text
/
```

而不是：

```text
\
```

避免某些 CMake 转义问题。

------

### 4.5.5\_ZEPHYR\_MODULES\_每一段是什么意思

例如：

```text
"-DZEPHYR_MODULES=$(cygpath -m "$PWD/modules/hal/cmsis_6");$(cygpath -m "$PWD/modules/hal/hc32")"
```

首先：

```text
-D
```

是：

> 给 CMake 定义一个变量。

变量名：

```text
ZEPHYR_MODULES
```

值：

```text
盘符:/实际实验目录/modules/hal/cmsis_6
;
盘符:/实际实验目录/modules/hal/hc32
```

其中：

```text
;
```

是 CMake list 的分隔符。

也就是说：

```text
module 1 = cmsis_6

module 2 = hc32
```

。

Zephyr 官方说明，在不使用 west 时，`ZEPHYR_MODULES` 中每个目录都需要满足 Module 的目录要求，例如包含 `zephyr/module.yml`，或者对应的 Zephyr CMake/Kconfig 文件。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/modules.html?utm_source=chatgpt.com)

------

### 4.5.6\_不过\_CMSIS\_6\_是否一定要手工放进\_ZEPHYR\_MODULES

这里教学文档应该稍微严谨一点。

不能机械地认为：

```text
west.yml 里面的所有 project
=
全部都必须写进 ZEPHYR_MODULES
```

。

因为：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west project
```

不一定都是：

```text
Zephyr module
```

。

比如某些项目可能只是：

```text
工具
测试程序
脚本
模拟器
```

。

所以判断一个下载仓库是否应该进入：

```text
ZEPHYR_MODULES
```

最直接的方法之一就是检查：

```text
<project>/
└── zephyr/
    └── module.yml
```

。

------

<a id="section-4-6"></a>

## 4.6\_记录并复用下载结果

把手工筛选流程落实到版本、下载清单和摘要，保留与 west 自动流程的对应关系。

### 4.6.1\_现在我们可以定义一套真正可执行的人工筛选流程

假设我们下载了：

```text
Zephyr 固定版本 ZIP
```

目标是：

```text
HC32F4A0PITB
Cortex-M4F
```

实际判断链应该是：

```text
Zephyr ZIP
    │
    ▼
读取 west.yml
    │
    ▼
确定 CPU Architecture
    │
    └── Cortex-M4F
            │
            ▼
          CMSIS_6
    │
    ▼
确定 Vendor
    │
    └── HC32
            │
            ▼
     HC32 HAL 是否独立仓库？
          │
        ┌─┴─┐
        │   │
       是   否
        │   │
        ▼   ▼
下载 HAL   已包含在 zephyr ZIP
    │
    ▼
检查工程功能
    │
    ├── LittleFS？
    ├── TLS？
    ├── MCUboot？
    └── 其它？
    │
    ▼
补对应 ZIP
    │
    ▼
CMake 配置验证
    │
    ▼
缺什么再补什么
```

这才是“小环境下载”的核心算法。

------

### 4.6.2\_给教学环境建立\_download-manifest.yml

我强烈建议不要只靠教学文档记录这些东西。

我们自己再创建一个非常简单的：

```text
download-manifest.yml
```

它不是 west 必需文件。

它是：

> **我们这套教学环境自己的下载锁定文件。**

例如：

```yaml
environment:
  name: hc32f4a0-zephyr-learning
  zephyr_version: vX.Y.Z

sources:

  zephyr:
    repository: zephyrproject-rtos/zephyr
    revision: vX.Y.Z
    type: zip
    path: zephyr

  cmsis_6:
    repository: zephyrproject-rtos/CMSIS_6
    revision: 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
    type: zip
    path: modules/hal/cmsis_6

  hal_hc32:
    repository: our-company/hal_hc32
    revision: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    type: zip
    path: modules/hal/hc32

toolchain:

  architecture: arm
  toolchain: arm-zephyr-eabi
  sdk_version: 1.0.1
```

这样学生根本不用第一次就理解整个 upstream `west.yml`。

他们只需要理解：

```text
west.yml
    ↓
官方完整依赖数据库

download-manifest.yml
    ↓
我们从里面筛选出来的教学环境依赖
```

------

### 4.6.3\_为什么最好记录\_commit\_而不是只记录\_ZIP\_文件名

例如：

```text
cmsis6.zip
```

这个名字几乎没有信息。

半年后根本不知道：

```text
它到底是哪一个版本？
```

更好的名字应该类似：

```text
CMSIS_6-1c1840af7a7e757d.zip
```

再在：

```text
download-manifest.yml
```

保存完整 commit。

这样即使完全没有 `.git`：

```text
我们的环境仍然是可追溯的。
```

这对于以后：

```text
问题定位
版本升级
CI
团队环境统一
```

都很重要。

------

### 4.6.4\_还可以进一步保存\_SHA256

这里要区分两种东西：

```text
Git commit SHA
```

和：

```text
ZIP SHA256
```

不是一回事。

例如：

```text
cmsis_6:
  revision: 1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8
  sha256: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

：

```text
revision
```

用于表示：

> 源代码版本。

：

```text
sha256
```

用于表示：

> 我实际拿到的压缩文件有没有损坏或者被替换。

不过需要注意，GitHub 官方说明：源码 archive 的**文件内容**在固定 commit 下具有稳定性，但压缩参数本身未来可能变化，因此同一 commit 后来重新生成的 ZIP 字节级内容不一定永远完全相同。[GitHub Docs](https://docs.github.com/en/enterprise-cloud@latest/repositories/working-with-files/using-files/downloading-source-code-archives?utm_source=chatgpt.com)

所以：

```text
commit ID
```

才是我们最重要的源码身份。

SHA256 更多适合：

```text
验证我们公司内部保存的这一份下载包。
```

------

### 4.6.5\_最后再回来看\_west\_官方是怎么做的

到这里学生就不会觉得：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west update
```

是一句魔法命令了。

它大致是在自动完成：

```text
读取 west.yml

解析：
    remote
    repo-path
    revision
    path

        ↓

获得 Git 仓库

        ↓

checkout 到 revision

        ↓

放到 path

        ↓

Zephyr build system
识别这些 module
```

而我们现在做的是：

```text
读取 west.yml

        ↓

人工选择：
只要 HC32 真正需要的

        ↓

根据 revision
下载 ZIP

        ↓

解压到 path

        ↓

通过 ZEPHYR_MODULES
告诉 Zephyr
```

两条路径最终目标是一样的：

```text
构建系统获得正确版本的源码。
```

区别只是：

```text
官方完整 west workspace

强调：
自动化 Git 管理


我们的 Mini ZIP Environment

强调：
下载少
网络依赖低
源码优先
Git 延后
目标芯片专用
```

------

### 4.6.6\_对\_HC32F4A0\_当前可以先得到这样的结论

如果我们的 Zephyr 基线是现代 4.x，尤其 4.2 及以后，那么 Cortex-M4F 基础层首先应该考虑 `CMSIS_6`。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/hardware/arch/arm_cortex_m.html?utm_source=chatgpt.com)

因此第一版教学环境可以先设计成：

```text
HC32F4A0 Zephyr Mini Environment
│
├── zephyr/
│       Zephyr 固定版本 ZIP
│
├── modules/
│   └── hal/
│       ├── cmsis_6/
│       │       Cortex-M 必需
│       │
│       └── hc32/
│               如果 HC32 HAL 是独立 module
│
├── sdk/
│       Zephyr SDK Minimal
│
└── toolchain/
        arm-zephyr-eabi
```

如果你的 HC32 DDL 已经直接包含在自己的：

```text
zephyr_hc32f4a0
```

源码树中，则进一步简化为：

```text
Zephyr HC32 fork ZIP
+
CMSIS_6 ZIP
+
Minimal SDK
+
arm-zephyr-eabi
```

**下一节我们正好可以继续往下写《Zephyr SDK 和 ARM 交叉编译器到底是什么，以及为什么 HC32F4A0 只需要下载 `arm-zephyr-eabi`》**。这样源码依赖讲完之后，自然进入工具链下载，而且同样可以完全按“零基础但不是 C 小白”的方式，把 GCC、binutils、sysroot、host tools、Zephyr SDK 之间的关系一次讲清楚。

[参考资料目录](README.md) · [上一篇](P03_国内如何更快下载zephyr.md) · [下一篇](P05_SDK和交叉编译器下载说明.md)
