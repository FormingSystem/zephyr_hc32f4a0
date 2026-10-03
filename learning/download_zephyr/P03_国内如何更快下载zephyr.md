---
id: zephyr-download-notes-03
title: ZIP 下载与 Git 元数据接入
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第3章\_ZIP\_下载与\_Git\_元数据接入

本章操作终端统一为 **MSYS2 UCRT64 Bash**，主机仍是 Windows x64。独立下载实验使用 `~/zephyr-download-lab`；路径、工具准备和当前 HC32 集成工程的区别见[环境与目录约定](环境与目录约定.md)。下文保留的版本、模块名和仓库地址示例须结合实际清单核对。

下载前先按[本地代理配置](代理配置.md)核对 v2rayN 的 `10808` 混合端口，配置 Git 并测试连接；浏览器下载 ZIP 还需使用系统代理或浏览器代理。

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。当前 HC32 工程请按[项目安装流程](../../project-docs/environment.md)操作；已整理的入门主线见[工程准备大纲](../P01_zephyr_make_project/大纲.md)。

**本章目录**

- [3.1 先用固定版本的 ZIP 取得源码](#section-3-1)
- [3.2 按清单补齐模块](#section-3-2)
- [3.3 准备工具链与构建入口](#section-3-3)
- [3.4 按需补充 Git 元数据](#section-3-4)
- [3.5 把元数据接回源码目录](#section-3-5)
- [3.6 逐步扩展历史](#section-3-6)
- [3.7 保存可复用的下载环境](#section-3-7)


对于国内访问 GitHub 不稳定的场景，本专题把 Zephyr 环境搭建明确设计成：

> **源码下载与 Git 历史下载解耦。先用浏览器 ZIP 快速获得“能编译的源码环境”，Git 版本数据库以后需要时再按需补。**

这和传统的“先 `git clone`，再 `west update`”思路完全不同。

<a id="section-3-1"></a>

## 3.1\_先用固定版本的\_ZIP\_取得源码

先明确 ZIP 包含什么、缺少什么，再选择固定版本和独立目录。

### 3.1.1\_为什么要把\_源码\_和\_Git\_分开

很多初学者容易认为：

```text
Git 仓库 = 源代码
```

实际上不是。

一个 Git 工程大致有两部分：

```text
zephyr/
│
├── arch/
├── boards/
├── drivers/
├── kernel/
├── soc/
├── subsys/
├── ...
│
└── .git/
```

其中：

```text
arch/
drivers/
kernel/
...
```

才是我们真正拿来：

```text
阅读
修改
编译
```

的源码。

而：

```text
.git/
```

是 Git 自己的数据库，其中保存：

```text
commit
tree
blob
branch
tag
remote
历史版本
```

所以理论上：

```text
没有 .git
```

并不会导致：

```text
C/C++ 源代码无法编译。
```

Git 是源码管理工具，不是 C 编译器。

------

### 3.1.2\_GitHub\_的\_Download\_ZIP\_得到的是什么

在 GitHub 页面：

```text
Code
  ↓
Download ZIP
```

得到的是：

> 某一个版本的源代码快照。

比如：

```text
zephyr/
├── arch/
├── boards/
├── drivers/
├── kernel/
├── scripts/
├── soc/
├── subsys/
└── west.yml
```

但是不会包含：

```text
.git/
```

所以它不能直接执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git log
git diff
git status
git fetch
git pull
```

因为 Git 不知道：

```text
这些文件来自哪个 commit
它们以前是什么样
远程仓库在哪里
当前 HEAD 是什么
```

但它完全可以用来：

```text
阅读 Zephyr
配置 Board
编译 Zephyr
开发驱动
```

Zephyr 官方也明确支持**不使用 west/Git 进行构建**；这种情况下外部 module 需要自己提供，并通过 `ZEPHYR_MODULES` 等方式告诉构建系统它们的位置。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/without-west.html?utm_source=chatgpt.com)

------

### 3.1.3\_我们推荐的下载模型

教学环境可以设计成四个阶段：

```text
阶段 1
下载源码 ZIP
    │
    ▼
立即拥有完整源码

阶段 2
下载目标 MCU 必需 Module ZIP
    │
    ▼
CMSIS / Vendor HAL

阶段 3
下载目标 CPU 工具链
    │
    ▼
arm-zephyr-eabi

阶段 4
以后真正需要 Git 功能时
    │
    ▼
再补最少量 Git Metadata
```

于是最开始根本不需要：

```text
git clone zephyr
west update 全仓库
完整 Git 历史
```

------

### 3.1.4\_第一步\_不要直接下载\_main\_的\_ZIP

GitHub 上确实可以：

```text
Code → Download ZIP
```

但这里有一个教学上非常重要的问题。

如果当前页面是：

```text
main
```

那么你今天下载：

```text
main.zip
```

和半年以后下载：

```text
main.zip
```

内容可能完全不同。

所以教学环境一定应该固定版本。

例如：

```text
Zephyr v4.x.x
```

然后进入对应：

```text
Tags
或者
Releases
```

选择固定版本。

再执行：

```text
Code
→
Download ZIP
```

这样我们下载的是：

```text
固定版本源码快照
```

而不是：

```text
不断变化的 main
```

------

### 3.1.5\_下载之后\_可以先完全不管\_Git

假设下载：

```text
zephyr-vX.Y.Z.zip
```

解压：

```text
~/zephyr-download-lab/
└── zephyr/
    ├── arch/
    ├── boards/
    ├── drivers/
    ├── kernel/
    ├── soc/
    ├── scripts/
    ├── subsys/
    └── west.yml
```

此时：

```text
~/zephyr-download-lab/zephyr/.git
```

根本不存在。

这没有问题。

我们的第一目标不是：

```text
git status 能不能执行
```

而是：

```text
源码是否完整
依赖是否完整
编译器是否完整
能否编译目标 MCU
```

------

<a id="section-3-2"></a>

## 3.2\_按清单补齐模块

主源码就位后，依照匹配版本的清单补充 CMSIS 与厂商 HAL。

### 3.2.1\_第二步\_根据\_MCU\_决定还要下载什么

例如目标芯片型号：

```text
HC32F4A0PITB
```

CPU：

```text
ARM Cortex-M4F
```

那么先推导：

```text
HC32F4A0
    │
    ▼
ARM Cortex-M4F
    │
    ├── Zephyr ARM 架构代码
    │
    ├── CMSIS
    │
    ├── HC32 SoC 支持
    │
    ├── HC32 DDL/HAL
    │
    └── ARM Toolchain
```

这里：

```text
Zephyr ARM 架构代码
```

已经包含在刚才的：

```text
zephyr.zip
```

里面。

接下来主要找：

```text
CMSIS
HC32 HAL/DDL
```

------

> 批注：
>
> 1. 怎么知道是CMSIS？有什么说法吗？是怎么把CMSIS和芯片型号绑定的？这里解释清楚
> 2. HC32 HAL/DDL 为什么是这个？也解释清楚，无论是行业传统还是说芯片公司自己的出产物啥的，你都要这里解释清楚，完成逻辑闭环

### 3.2.2\_怎么知道\_Zephyr\_需要哪个版本的\_CMSIS

不要凭感觉下载最新版 CMSIS。

打开：

```text
zephyr/west.yml
```

这个文件很重要。

它本质上是在告诉 west：

> 当前 Zephyr 版本还依赖哪些其他 Git 仓库，以及这些仓库应该处于什么版本。

里面会看到类似：

```text
- name: cmsis
  revision: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  path: modules/hal/cmsis
```

这里：

```text
name: cmsis
```

表示项目名字。

```text
revision:
```

表示：

> Zephyr 要求的 CMSIS 精确版本。

可能是：

```text
tag
branch
commit SHA
```

而：

```text
path: modules/hal/cmsis
```

告诉我们：

> CMSIS 最终应该放在哪里。

所以即使完全不用 west，也可以人工按照这份表下载。

------

### 3.2.3\_手工下载\_CMSIS\_ZIP

假设 `west.yml` 指定：

```text
cmsis
revision = ABCDEF123456...
```

那么进入 CMSIS 对应 GitHub 仓库。

切换到：

```text
ABCDEF123456...
```

对应 commit。

然后：

```text
Code
→
Download ZIP
```

解压。

最后整理目录：

```text
~/zephyr-download-lab/
│
├── zephyr/
│
└── modules/
    └── hal/
        └── cmsis/
```

这里目录最好与：

```text
path: modules/hal/cmsis
```

保持一致。

这样以后即使重新引入 west，也比较容易迁移。

------

### 3.2.4\_HC32\_HAL\_也是同样处理

假设我们的 HC32 支持单独存在：

```text
hal_hc32
```

同样：

```text
GitHub
→
固定 commit/tag
→
Download ZIP
```

然后：

```text
~/zephyr-download-lab/
│
├── zephyr/
│
└── modules/
    └── hal/
        ├── cmsis/
        └── hc32/
```

最终我们只下载：

```text
Zephyr
CMSIS
HC32 HAL
```

完全没有：

```text
STM32 HAL
NXP HAL
Nordic HAL
Espressif HAL
Renesas HAL
...
```

------

### 3.2.5\_这实际上已经实现\_人工\_west\_update

官方：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west update
```

做的事情可以粗略理解为：

```text
读取 west.yml
     │
     ▼
找到项目
     │
     ▼
找到 revision
     │
     ▼
下载 Git 仓库
     │
     ▼
放到指定 path
```

我们现在人工做的是：

```text
读取 west.yml
     │
     ▼
找到需要的项目
     │
     ▼
找到 revision
     │
     ▼
浏览器 Download ZIP
     │
     ▼
解压到指定 path
```

结果对于：

```text
编译器
```

而言没有本质区别。

编译器关心的是：

```text
文件在不在
路径对不对
版本兼不兼容
```

它不关心这些文件是不是通过：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone
```

得到的。

------

<a id="section-3-3"></a>

## 3.3\_准备工具链与构建入口

模块准备只是构建条件的一部分，还需要 SDK、主机工具和实际存在的板级移植。

### 3.3.1\_第三步\_工具链也直接下载压缩包

这一点现在 Zephyr SDK 非常适合。

Zephyr SDK 1.0.1 官方 Release 已经把：

```text
完整 SDK
Minimal SDK
各个架构工具链
```

拆开提供。

例如 Windows x86-64 可以单独获得：

```text
zephyr-sdk-1.0.1_windows-x86_64_minimal.7z
```

以及：

```text
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

也就是说我们完全没有必要下载：

```text
RISC-V
Xtensa
x86
ARC
AArch64
...
```

HC32F4A0 是 Cortex-M4F，只需要：

```text
arm-zephyr-eabi
```

即可。官方 SDK Release 确实提供独立的 `arm-zephyr-eabi` Windows/Linux/macOS 工具链包。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/releases?utm_source=chatgpt.com)

------

### 3.3.2\_为什么还需要\_Minimal\_SDK

Zephyr SDK 不只是 GCC。

它还有：

```text
Host Tools
CMake integration
OpenOCD 等辅助工具
SDK metadata
```

官方现在把 bundle 分成：

```text
GNU
LLVM
Minimal
```

其中：

```text
minimal
```

包含 Host Tools，但不预装目标 CPU Toolchain。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html?utm_source=chatgpt.com)

因此对于我们的环境：

```text
Minimal SDK
+
arm-zephyr-eabi
```

是非常合理的组合。

即：

```text
Zephyr 开发环境
│
├── Zephyr ZIP
├── CMSIS ZIP
├── HC32 HAL ZIP
│
└── Zephyr SDK
    ├── Minimal Host Tools
    └── arm-zephyr-eabi
```

这已经非常接近真正意义上的：

> HC32F4A0 专用 Zephyr 小环境。

------

### 3.3.3\_这时候完全可以开始编译

这时候目录可能是：

```text
~/zephyr-download-lab/
│
├── zephyr/
│
├── modules/
│   └── hal/
│       ├── cmsis/
│       └── hc32/
│
├── sdk/
│   └── zephyr-sdk-1.0.1/
│
├── app/
│
└── build/
```

没有：

```text
.git
```

也没有：

```text
.west
```

一样能够编译。

官方明确给出了不用 west 的构建形式：

```text
cmake -B build -GNinja "-DZEPHYR_MODULES=module1;module2" app
ninja -C build
```


以下仍是独立教学目录的构建示例：从 `~/zephyr-download-lab` 执行，先按 P06 设置 Python 和 SDK。只有 `zephyr/` 已包含 HC32 移植、两个模块及 `app/` 已准备好时才适用；官方原版 ZIP 不会自动包含本项目的板级支持。当前集成工程直接使用 `python scripts/project_env.py build`。

Bash 中必须给带分号的整个 `-D` 参数加引号；`cygpath -m` 将目录换成 Windows CMake 能读取的盘符加正斜杠形式。

例如概念上：

```bash
cmake \
    -B build \
    -GNinja \
    -DBOARD=uyup_rpi_a/hc32f4a0pitb \
    "-DZEPHYR_MODULES=$(cygpath -m "$PWD/modules/hal/cmsis");$(cygpath -m "$PWD/modules/hal/hc32")" \
    app

cmake --build build
```

所以：

> **Git 可以完全延后。**

------

<a id="section-3-4"></a>

## 3.4\_按需补充\_Git\_元数据

先说明何时需要 Git，再理解临时仓库和各个减量参数。

### 3.4.1\_那什么时候才需要\_Git

当你开始需要这些能力：

```text
git status
git diff
git log
git blame
查看某次修改
和官方版本比较
以后 fetch 新版本
```

才需要：

```text
.git
```

那么问题就变成：

> 我已经有 ZIP 源码了，能不能不要重新完整 clone，而只给它补 Git 数据？

可以。

而且这恰恰可以利用：

```text
partial clone
```

。

------

### 3.4.2\_最重要的方案\_ZIP\_源码\_+\_Blobless\_Git\_Metadata

这是我最推荐写进教学文档的高级方案。

假设现在：

```text
~/zephyr-download-lab/zephyr/
```

已经是我们从 ZIP 解压出来的完整源码。

我们不想重新 clone 一份源码。

只想补：

```text
commit
tree
branch
tag
remote
```

等 Git 信息。

但是不希望大量下载历史文件内容。

这时候使用：

```text
--filter=blob:none
```

。

Git 官方称之为：

```text
blobless partial clone
```

GitHub 也支持这种方式。GitHub 的说明是：`--filter=blob:none` 会先获取 commit/tree，而文件内容 blob 在真正需要时再获取。[Git](https://git-scm.com/docs/git-clone.html?utm_source=chatgpt.com)

------

### 3.4.3\_什么叫\_blob

Git 内部大致有：

```text
commit
tree
blob
```

可以暂时理解：

```text
commit
=
一次版本记录

tree
=
目录结构

blob
=
真正的文件内容
```

而通常占空间比较大的恰恰是：

```text
blob
```

。

所以：

```text
--filter=blob:none
```

的意思大致就是：

> Git 历史结构我要，但是历史文件内容先不要。

Git 真正需要某个文件内容时，再从服务器拿。

------

### 3.4.4\_已经有\_ZIP\_后\_推荐使用临时\_Metadata\_仓库

假设我们已经有：

```text
~/zephyr-download-lab/zephyr
```

不要直接在里面做完整 clone。

另外建立一个临时目录：

```text
~/zephyr-download-lab/git-meta
```

先在实验根目录核对 ZIP 的标签或提交；`vX.Y.Z` 是待替换的版本占位符，必须与 ZIP 对应，再执行：

```bash
# 当前位置：~/zephyr-download-lab；以下续行符为 Bash 的反斜杠。
git clone \
    --filter=blob:none \
    --no-checkout \
    --depth 1 \
    --branch vX.Y.Z \
    https://github.com/zephyrproject-rtos/zephyr.git \
    git-meta
```

这条命令值得逐项解释。

------

### 3.4.5\_filter=blob:none

```text
不要立即下载文件内容 blob。
```

我们已经有 ZIP 源码了。

所以没必要再通过 Git 下载一遍相同源码。

------

### 3.4.6\_no-checkout

普通：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone
```

最后还会进行：

```text
checkout
```

即把 Git 中的源码展开到工作目录。

但是：

```text
我们已经有源码。
```

所以不希望 Git 又 checkout 一份。

于是使用：

```text
--no-checkout
```

意思是：

> 只建立 Git 仓库数据，不创建工作区文件。

GitHub 也专门展示过 `--filter=blob:none --no-checkout` 的组合用法。[The GitHub Blog](https://github.blog/open-source/git/bring-your-monorepo-down-to-size-with-sparse-checkout/?utm_source=chatgpt.com)

------

### 3.4.7\_depth\_1

这里进一步限制：

```text
历史 commit 深度 = 1
```

所以我们开始甚至连完整：

```text
commit 历史
```

都不要。

只拿当前版本附近最少的信息。

------

### 3.4.8\_整条命令的中文含义

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --filter=blob:none \
    --no-checkout \
    --depth 1 \
    --branch vX.Y.Z \
    https://github.com/zephyrproject-rtos/zephyr.git \
    git-meta
```

翻译就是：

> 给我建立 Zephyr vX.Y.Z 的 Git 仓库，但是不要 checkout 文件，不要下载历史文件 blob，只需要深度 1 的最少版本信息，并把这些 Git 数据先放到 `git-meta`。

注意：

这时候真正使用 GitHub 网络传输的内容已经比普通：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone
```

少很多。

------

<a id="section-3-5"></a>

## 3.5\_把元数据接回源码目录

保留原有文件，依次移动元数据、建立索引并检查版本对应关系。

### 3.5.1\_然后把.git\_接到\_ZIP\_源码上

临时目录中：

```text
git-meta/
└── .git/
```

真正有价值的是：

```text
.git/
```

而我们的源码已经在：

```text
zephyr/
```

。

因此概念上就是：

```text
git-meta/.git
        │
        │ 搬过去
        ▼
zephyr/.git
```

变成：

```text
zephyr/
│
├── .git/
├── arch/
├── boards/
├── drivers/
├── kernel/
└── ...
```

然后删除空的：

```text
git-meta
```

即可。

------

### 3.5.2\_UCRT64\_Bash\_接入示例

假设：

```text
~/zephyr-download-lab/
├── zephyr/
└── git-meta/
```

可以：

```bash
# 当前位置：~/zephyr-download-lab；先确认 ZIP 与 git-meta 是同一版本。
test -d ./git-meta/.git && test -d ./zephyr && test ! -e ./zephyr/.git &&
    mv -- ./git-meta/.git ./zephyr/.git
```

然后：

```bash
# 仅在上一条 mv 成功后执行；非空目录会保留并报错。
rmdir -- ./git-meta
```

进入：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
cd ./zephyr
```

------

### 3.5.3\_还需要做一件事\_建立\_Git\_Index

我们现在虽然有：

```text
.git
```

也有：

```text
源码
```

但是这两者刚刚才组合起来。

执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git reset --mixed HEAD
```

注意：

```text
--mixed
```

非常重要。

它会：

```text
根据 HEAD 建立 Git index
```

但不会覆盖当前工作区文件。

可以粗略理解：

```text
HEAD 中记录的文件
        │
        ▼
建立 index
        │
        X
不重新 checkout
        │
        ▼
保留 ZIP 文件
```

这正符合我们的目的。

------

### 3.5.4\_然后检查

执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git status
```

理想状态应该类似：

```text
On branch ...
nothing to commit, working tree clean
```

或者 tag 场景是 detached HEAD。

如果出现：

```text
几万个 modified
```

那不要继续。

通常说明：

```text
ZIP 版本和 Git HEAD 不一致
```

或者：

```text
下载了错误 tag
```

或者：

```text
源码被修改过
```

也可能涉及：

```text
换行符配置
```

。

------

### 3.5.5\_这时候\_git\_diff\_会怎么样

现在非常有意思。

`.git` 中没有所有历史 blob。

所以执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git status
```

通常并不一定需要下载所有历史文件。

但如果执行：

```text
git diff drivers/spi/spi_xxx.c
```

Git 要知道：

```text
原始 spi_xxx.c 是什么
```

才能和：

```text
当前 spi_xxx.c
```

进行比较。

如果那个原始 blob 本地没有，Git 就会：

```text
访问 GitHub
     │
     ▼
只获取需要的 blob
     │
     ▼
完成 diff
```

这就是 partial clone 的价值。

GitHub 也明确说明：在 blobless clone 中，`git diff`、`git blame` 等真正需要文件内容的操作，会按需下载缺失 blob。[The GitHub Blog](https://github.blog/open-source/git/get-up-to-speed-with-partial-clone-and-shallow-clone/?utm_source=chatgpt.com)

所以你的需求基本可以实现为：

```text
不使用 Git
    ↓
0 Git 网络开销


需要 status
    ↓
只有少量 metadata


需要 diff 某个文件
    ↓
只拉那个文件需要的 blob


需要更多历史
    ↓
再继续 fetch
```

------

<a id="section-3-6"></a>

## 3.6\_逐步扩展历史

在小请求和初次获取成功后，再根据需求加深历史，并评估完整下载的成本。

### 3.6.1\_后面想看最近\_50\_次提交怎么办

一开始：

```text
--depth 1
```

只有很浅历史。

以后想增加：

```text
最近 50 层
```

可以：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git fetch --deepen=50 --filter=blob:none
```

意思：

```text
把 commit 历史再向过去扩展 50 层
```

但是仍然：

```text
历史文件 blob 按需获取
```

。

------

### 3.6.2\_如果以后真的想把完整历史补回来

可以继续：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git fetch --unshallow --filter=blob:none
```

这时：

```text
commit/tree 历史
```

会逐步变完整。

但是：

```text
blob
```

仍然可以保持 partial clone 模式。

因此不存在：

> 第一天就必须在“没有 Git”和“完整 Git 仓库”之间二选一。

完全可以逐步成长：

```text
Level 0

ZIP
没有 Git
        ↓


Level 1

ZIP
+
depth 1 Git metadata
        ↓


Level 2

更多 commit
+
blob 按需下载
        ↓


Level 3

完整 commit 历史
+
blob 按需下载
        ↓


Level 4

如果真的需要
完整 Git 仓库
```

------

### 3.6.3\_这比一开始\_git\_clone\_--depth\_1\_更符合国内网络场景

比如一个学生第一天只是要：

```text
搭环境
编译 hello_world
运行 HC32
```

传统路线：

```text
git clone
    ↓
GitHub 网络慢
    ↓
失败
    ↓
重试
    ↓
west update
    ↓
再下载几十个仓库
    ↓
再次失败
```

这非常影响教学。

我们的路线：

```text
浏览器 / 下载工具
下载固定 ZIP
        ↓
解压
        ↓
下载 CMSIS ZIP
        ↓
下载 HC32 ZIP
        ↓
下载 ARM Toolchain 7z
        ↓
直接编译
```

Git 完全不是第一天的阻塞项。

------

<a id="section-3-7"></a>

## 3.7\_保存可复用的下载环境

把源码、版本记录和两条下载路线收束为后续可复查的教学环境。

### 3.7.1\_对\_Zephyr\_教学环境\_我建议最终这样定义

例如一个：

```text
HC32F4A0 Zephyr Learning Kit
```

下载目录甚至可以做成：

```text
downloads/
│
├── source/
│   ├── zephyr-vX.Y.Z.zip
│   ├── cmsis-xxxxxxxx.zip
│   └── hal_hc32-xxxxxxxx.zip
│
├── sdk/
│   ├── zephyr-sdk-minimal.7z
│   └── arm-zephyr-eabi.7z
│
└── SHA256SUMS.txt
```

然后安装之后：

```text
workspace/
│
├── zephyr/
│
├── modules/
│   └── hal/
│       ├── cmsis/
│       └── hc32/
│
├── sdk/
│
├── app/
└── build/
```

第一天：

```text
完全没有 .git
```

。

------

### 3.7.2\_还应该保存一个版本清单

这是这种方案非常重要的一步。

因为我们没有 Git 自动帮忙记录 revision。

所以教学包应该提供：

```text
versions.yml
```

例如：

```text
zephyr:
  version: vX.Y.Z
  source: zephyrproject-rtos/zephyr

cmsis:
  revision: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  path: modules/hal/cmsis

hal_hc32:
  revision: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  path: modules/hal/hc32

sdk:
  version: 1.0.1

toolchain:
  name: arm-zephyr-eabi
```

最好再保存：

```text
SHA256
```

。

这样即使完全没有 Git：

```text
这个环境到底用了什么
```

仍然是明确可追溯的。

------

### 3.7.3\_Git\_ZIP\_模式真正的代价是什么

这个方案也不是没有代价。

最重要的是：

```text
ZIP 本身没有 Git identity
```

所以一定要额外记录：

```text
Zephyr tag
CMSIS commit
HC32 commit
SDK version
```

另外：

```text
Download ZIP
```

也不会自动替你处理 Zephyr 所有外部 module。

你必须自己根据：

```text
west.yml
```

决定下载哪些依赖。

这恰恰又符合我们这个教程的目的：

> 教会开发者理解依赖，而不是让 `west update` 把所有东西黑盒式拉下来。

------

### 3.7.4\_我建议最终教程采用\_双轨制

这是我认为非常适合正式教学材料的结构。

#### (1)\_快速开发模式

```text
Download ZIP
        ↓
固定 Zephyr Version
        ↓
人工读取 west.yml
        ↓
下载需要的 Module ZIP
        ↓
下载 Minimal SDK
        ↓
下载 ARM Toolchain
        ↓
直接开始编译
```

特点：

```text
不依赖 GitHub Git 协议稳定性
不下载 Git 历史
不下载无关 MCU 仓库
最快进入开发
```

##### 1)\_Git\_增强模式

真正需要 Git 时：

```text
现有 ZIP 源码
        +
--filter=blob:none
--no-checkout
--depth 1
        ↓
补最小 Git Metadata
        ↓
git status
        ↓
git diff 时按需取 blob
        ↓
需要历史时再 deepen
```

这条路径在技术上是合理的：Git 的 partial clone 就是为了把暂时不需要的对象留在远端，并在以后需要时 demand-fetch。[Git](https://git-scm.com/docs/partial-clone/2.48.0.html?utm_source=chatgpt.com)

**所以这份教程完全可以把 `git clone` 从“Zephyr 环境搭建的必经步骤”降级成“以后需要版本管理时才启用的增强能力”。第一阶段只要求：源码快照正确、Module 版本正确、工具链正确、能编译。**

而且我建议我们下一节直接继续写成 **《从 `west.yml` 判断 HC32F4A0 到底需要下载哪些 ZIP》**。这一节会真正解决“小环境如何自动/人工筛选依赖”的核心问题。

[参考资料目录](README.md) · [上一篇](P02_零基础获得zephyr.md) · [下一篇](P04_如何从west.yml获得需要下载的包.md)
