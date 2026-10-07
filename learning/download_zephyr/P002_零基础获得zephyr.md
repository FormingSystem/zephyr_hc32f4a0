---
id: zephyr-download-notes-02
title: Git 下载基础与减量方法
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第2章\_Git\_下载基础与减量方法

当前型号与依赖依据统一见[准备专题 P004 的 4.1 节](../P01_zephyr_make_project/环境与依赖导航.md#chip-selection)，完整下载和核验见[准备专题 P004 的 4.2.2、4.2.3 节](../P01_zephyr_make_project/环境与依赖导航.md#section-4-2)。实装芯片先用丝印/BOM/手册确认；CMSIS_6 版本来自当前 Zephyr 清单，HC32 HAL 来自配套移植指定的 hal_xhsc 快照。当前官方清单没有 hal_xhsc，AN386 编译示例也不需要它。下文其他模块名称与布局示例不能替代这条实际操作路线。

本章操作终端统一为 **MSYS2 UCRT64 Bash**，主机仍是 Windows x64。独立下载实验使用 `~/zephyr-download-lab`；路径、工具准备和当前 HC32 集成工程的区别见[环境与目录约定](环境与目录约定.md)。下文保留的版本、模块名和仓库地址示例须结合实际清单核对。

下载前先按[本地代理配置](代理配置.md)核对 v2rayN 的 `10808` 混合端口，配置 Git 并测试连接；浏览器下载 ZIP 还需使用系统代理或浏览器代理。

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。从零操作请按[工程准备大纲](../P01_zephyr_make_project/大纲.md)，使用 `G:\zephyr_practice\zephyr-main`；下文的其他目录布局是方案说明，不能直接当作主线已存在的文件。

**本章目录**

- [2.1 认识仓库与克隆](#section-2-1)
- [2.2 选择历史深度和版本](#section-2-2)
- [2.3 理解检出与稀疏工作区](#section-3-1)
- [2.4 按需取得文件对象](#section-3-2)
- [2.5 选择适合实验的下载策略](#section-4-1)

在选择下载优化方法前，需要先理解 Git 的几个基本动作。不能直接记住“不要用 `sparse-checkout`”，而不清楚 **checkout 是什么、sparse 又是在稀疏什么、它和减少下载量是不是一回事**。

本章沿着仓库、克隆、版本、检出和文件对象的顺序逐项说明。

在讨论“怎么少下载一些 Zephyr 内容”之前，需要先理解 Git 下载一个工程时，到底下载了什么。

即使读者从来没有使用过 Git，也应该能够看懂这一节。

<a id="section-2-1"></a>

## 2.1\_认识仓库与克隆

先认识 Git 仓库中保存的内容，再看 clone 为什么可能产生较大的下载量。

### 2.1.1\_什么是\_Git\_仓库

Zephyr 的源代码托管在 Git 仓库中。

可以暂时把 Git 仓库理解成：

```text
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

```text
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

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone https://github.com/zephyrproject-rtos/zephyr.git
```

Git 默认不仅会得到当前源码，还会获取这个仓库的历史对象。

官方 `git clone` 的定义就是：把一个已有 Git 仓库复制成本地仓库，并建立对应的远程仓库关系。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

### 2.1.2\_git\_clone\_是什么

先看最普通的命令：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone https://github.com/zephyrproject-rtos/zephyr.git
```

一段一段解释。

#### (1)\_git

```text
git
```

表示：

> 调用 Git 程序。

类似于：

```text
python
cmake
west
```

都是在调用一个程序。

#### (2)\_clone

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone
```

`clone` 的中文意思可以理解为：

> 克隆。

它做的事情不是简单地“下载一个 ZIP 文件”。

而是：

```text
远程 Git 仓库
       │
       │ git clone
       ▼
本地 Git 仓库
```

最终本地通常会出现：

```text
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

```text
.git/
```

普通文件：

```text
kernel/
drivers/
arch/
```

是我们平时看到和修改的代码。

而：

```text
.git/
```

保存 Git 自己管理的数据，例如：

```text
提交历史
分支
标签
远程仓库信息
文件对象
版本关系
```

因此可以简单理解为：

```text
zephyr/
│
├── 我们工作的源代码
│
└── .git/
       ↓
   Git 自己保存的版本数据库
```

### 2.1.3\_为什么完整\_git\_clone\_可能不是我们想要的

我们只是想学习或者编译一个确定版本的 Zephyr。

例如：

```text
Zephyr v4.4.x
```

我们可能根本不关心：

```text
2019 年的版本
2020 年的版本
2021 年的版本
……
几年前每一次 commit
```

但是普通：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone
```

会把 Git 仓库需要的历史对象一起获取。

于是出现一个问题：

```text
我们真正需要：

当前教学版本源码
        +
少量必要 Git 信息
```

而不是：

```text
当前源码
+
大量历史版本
+
大量和教学无关的历史对象
```

所以第一种优化方式不是删除源码目录。

而是：

> 减少 Git 历史。

<a id="section-2-2"></a>

## 2.2\_选择历史深度和版本

浅克隆控制历史深度；分支和标签决定取得哪个版本，两者分别说明。

### 2.2.1\_第一种优化\_浅克隆\_--depth

例如：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone --depth 1 https://github.com/zephyrproject-rtos/zephyr.git
```

这里增加了：

```text
--depth 1
```

#### (1)\_depth\_是什么意思

`depth`：

```text
深度
```

这里指：

> 下载多少层提交历史。

例如完整仓库：

```text
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

```text
把完整历史关系获取下来
```

而：

```text
--depth 1
```

可以简单理解成：

```text
只保留最靠近当前版本的一层历史
```

例如：

```text
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

```text
shallow clone
```

中文通常称：

> 浅克隆。

Git 官方文档对 `--depth <depth>` 的定义就是创建一个截断历史的 shallow clone。[Git](https://git-scm.com/docs/git-clone.html?utm_source=chatgpt.com)

### 2.2.2\_为什么教学环境适合\_--depth\_1

假设我们的目标只是：

```text
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

```text
git clone --depth 1 ...
```

通常比：

```text
git clone ...
```

更符合我们的目的。

两者得到的当前源码基本都是完整的：

```text
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

```text
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

### 2.2.3\_但我们还没有指定到底要哪个\_Zephyr\_版本

例如：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone --depth 1 https://github.com/zephyrproject-rtos/zephyr.git
```

虽然减少了历史，但是它仍然会按照远程仓库默认分支进行克隆。

教学环境通常不应该这样。

因为：

```text
今天下载
```

和：

```text
半年后下载
```

得到的源码可能发生变化。

教学文档最重要的一件事情就是：

> 固定版本。

例如：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

### 2.2.4\_branch\_是什么

这里：

```text
--branch v4.4.0
```

表示：

> 我们明确指定要获取哪个分支或者标签。

`--branch` 可以简写为：

```text
-b
```

所以：

```text
git clone --branch v4.4.0 ...
```

和：

```text
git clone -b v4.4.0 ...
```

意思相同。

Git 官方 `clone` 文档也说明，`--branch` 可以让 clone 指向指定 branch，也可以指定 tag。[Git](https://git-scm.com/docs/git-clone.html?utm_source=chatgpt.com)

### 2.2.5\_什么是\_branch

`branch` 就是：

```text
分支
```

可以把软件开发想象成：

```text
                 ┌── 开发功能 A
                 │
主开发线 ─────────┼── 开发功能 B
                 │
                 └── 修复 Bug
```

Git 可以同时维护不同开发线。

例如：

```text
main
release
development
```

都可以是不同 branch。

### 2.2.6\_什么是\_tag

软件发布正式版本时，经常会给某个 commit 打一个固定标记。

例如：

```text
某个 commit
    │
    └── tag: v4.4.0
```

这个 tag 可以理解成：

> 给某个确定版本贴了一个不会随开发继续前进的版本标签。

例如：

```text
v4.3.0
v4.3.1
v4.4.0
```

所以教学环境一般更喜欢：

```text
--branch v4.4.0
```

而不是：

```text
--branch main
```

因为：

```text
main
```

会不断变化。

而：

```text
v4.4.0
```

指向确定版本。

### 2.2.7\_现在把整条命令重新读一遍

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

不要把它当成一串魔法命令。

可以逐项翻译。

```text
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

<a id="section-3-1"></a>

## 2.3\_理解检出与稀疏工作区

从 checkout 的含义开始，区分磁盘上显示哪些文件与网络实际传输了什么。

### 2.3.1\_那么\_sparse-checkout\_又是什么

到这里开始进入另外一个完全不同的问题。

前面的：

```text
--depth 1
```

解决的是：

> 历史太多。

而 `sparse-checkout` 主要解决的是：

> 当前仓库里的目录和文件太多，我只想让其中一部分出现在工作目录中。

这是两个完全不同的维度。

### 2.3.2\_什么叫\_checkout

这是 Git 初学者非常容易困惑的一个单词。

`checkout` 在这里可以简单理解成：

> 把 Git 仓库里的某个版本真正展开成我们可以看到和编辑的文件。

例如 `.git` 中保存 Git 数据：

```text
.git/
```

然后 Git 根据某个版本，将文件展开到：

```text
kernel/
drivers/
arch/
...
```

这些我们能够：

```text
打开
阅读
编辑
编译
```

的文件，组成：

```text
working tree
```

中文通常叫：

> 工作树 / 工作目录。

因此：

```text
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

### 2.3.3\_什么叫\_sparse

`sparse`：

```text
稀疏的
```

因此：

```text
sparse-checkout
```

可以理解成：

> 不把仓库里的所有目录都展开到工作目录，只展开我指定的一部分。

例如一个仓库有：

```text
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

```text
arch/
drivers/
kernel/
```

使用 sparse-checkout 后，工作目录可以只显示：

```text
project/
├── arch/
├── drivers/
└── kernel/
```

Git 官方文档把 sparse-checkout 描述为：让工作树只包含用户关注的一部分文件；在 cone mode 下可以按目录指定范围。[Git](https://git-scm.com/docs/sparse-checkout?utm_source=chatgpt.com)

### 2.3.4\_一个最简单的\_sparse-checkout\_示例

这里先不用 Zephyr。

假设有一个仓库：

```text
demo/
├── app/
├── driver/
├── docs/
├── test/
└── tools/
```

我们只想看到：

```text
app/
driver/
```

可以执行：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout init --cone
```

然后：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout set app driver
```

逐条解释。

#### (1)\_git\_sparse-checkout

表示：

> 使用 Git 的 sparse-checkout 功能。

#### (2)\_init

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout init
```

表示：

> 初始化 sparse-checkout 配置。

也就是告诉 Git：

```text
从现在开始，这个仓库不是默认把所有目录都放到工作区。
```

#### (3)\_--cone

```text
--cone
```

表示使用比较适合“按目录选择”的 cone 模式。

例如：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout set app driver
```

这种写法就非常直观：

```text
我要 app/
我要 driver/
```

官方文档也区分了 cone mode 和 non-cone mode；cone mode 主要按目录选择，而 non-cone mode 可以使用更复杂的类似 gitignore 的模式。[Git](https://git-scm.com/docs/sparse-checkout?utm_source=chatgpt.com)

#### (4)\_set

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout set app driver
```

表示：

> 把 sparse-checkout 的目标目录设置为 app 和 driver。

最后工作目录可能主要看到：

```text
app/
driver/
```

### 2.3.5\_这里有一个非常容易产生的误解

很多初学者看到：

```text
工作目录只剩几个目录
```

会认为：

> 那么其他文件一定没有下载。

不一定。

这是学习 Git 下载优化时非常重要的一点。

单独使用：

```text
sparse-checkout
```

主要控制：

> 哪些文件出现在工作树里。

它和：

> 网络到底下载了多少 Git 对象

不是完全同一个问题。

因此：

```text
sparse-checkout
```

不能简单等价为：

```text
只从服务器下载这些目录。
```

这两个概念一定要分清。

### 2.3.6\_用一张图理解三种东西

目前我们已经碰到了三个概念：

```text
branch
depth
sparse-checkout
```

它们分别控制完全不同的事情。

```text
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

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

表达的是：

```text
版本：
v4.4.0

历史：
只要很浅的一层

当前源码：
完整
```

而 sparse-checkout 又是在另外一个维度控制：

```text
工作区需要展开哪些目录。
```

<a id="section-3-2"></a>

## 2.4\_按需取得文件对象

在工作区裁剪之外，继续理解 blob、部分克隆及它们的组合。

### 2.4.1\_如果真的希望减少\_文件内容\_的网络下载呢

Git 还有另外一个概念：

```text
partial clone
```

即：

> 部分克隆。

例如：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --filter=blob:none \
    https://github.com/zephyrproject-rtos/zephyr.git
```

这里出现：

```text
--filter=blob:none
```

### 2.4.2\_什么是\_blob

Git 内部会把不同数据保存成不同类型的对象。

对于初学者目前只需要知道：

```text
blob
```

基本可以理解为：

> 文件内容对象。

比如：

```text
main.c
driver.c
README.md
```

它们的文件内容最终会以 Git 对象形式进行管理。

### 2.4.3\_filter=blob:none\_是什么意思

```text
--filter=blob:none
```

大致可以理解为：

> 初始克隆时不要把所有历史文件内容全部下载下来，需要的时候再获取。

Git 官方文档明确说明：

```text
--filter=blob:none
```

会过滤 blob，文件内容在需要时再由 Git 获取。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

于是：

```text
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

```text
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

### 2.4.4\_sparse-checkout\_和\_partial\_clone\_可以组合

例如：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
git clone \
    --filter=blob:none \
    --sparse \
    https://example.com/project.git
```

Git 官方 `clone` 本身就提供：

```text
--sparse
```

以及：

```text
--filter=<filter-spec>
```

两个独立选项。[Git](https://git-scm.com/docs/git-clone?utm_source=chatgpt.com)

可以粗略理解：

```text
--filter
    ↓
控制服务器初始给我多少 Git 对象

--sparse
    ↓
控制工作目录先展开多少文件
```

两者解决的问题不同。

<a id="section-4-1"></a>

## 2.5\_选择适合实验的下载策略

回到 Zephyr 和 HC32 的依赖特点，比较源码、历史、仓库数量与工具链四层优化。

### 2.5.1\_为什么我们暂时不推荐对\_Zephyr\_主仓库做\_sparse-checkout

现在读者终于有足够背景理解这句话了。

原因不是：

> sparse-checkout 不好。

而是：

> Zephyr 本身不是一个几个目录互不相关的简单工程。

Zephyr 构建涉及大量跨目录依赖。

例如：

```text
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

```text
我的这个板子编译到底会访问哪些目录？
```

如果一开始就写：

```bash
# 当前位置：待检查的 Zephyr 源码根目录；终端：UCRT64 Bash。
git sparse-checkout set \
    kernel \
    drivers \
    arch/arm
```

看起来很精简。

但是可能很快发现：

```text
还需要 cmake/
```

补上以后：

```text
又需要 scripts/
```

之后：

```text
还需要 dts/
```

然后：

```text
还需要 include/
soc/
boards/
lib/
subsys/
```

最后可能变成：

```text
我们为了节省一点目录，
却花了大量时间维护“到底缺哪个目录”。
```

对于教学环境，这不是很好的收益交换。

### 2.5.2\_所以我们真正推荐什么

对于 **Zephyr 主仓库**，推荐：

```text
git clone \
    --branch <固定版本> \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

原则是：

```text
源码目录：
完整保留

Git 历史：
大幅减少
```

即：

```text
              普通 clone       推荐方案

当前源代码        完整             完整

Git 历史          很多             很少

构建兼容性         高               高

初学难度           低               低
```

而不是首先：

```text
砍 kernel
砍 drivers
砍 subsys
砍 scripts
砍 cmake
```

### 2.5.3\_真正应该大规模裁剪的是\_仓库数量

这里开始进入 Zephyr 与普通单仓库项目最大的区别。

Zephyr 开发环境并不只有：

```text
zephyr.git
```

还可能存在很多独立 Git 仓库：

```text
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

```text
少下载一个 Zephyr 源码目录
```

和：

```text
整个 hal_nxp 仓库都不下载
```

完全不是一个量级的优化思路。

我们的策略因此应该是：

```text
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

### 2.5.4\_用\_HC32F4A0\_举例

例如我们的目标芯片是：

```text
HC32F4A0PITB
```

CPU：

```text
ARM Cortex-M4F
```

我们首先推导：

```text
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

```text
STM32 HAL
NXP HAL
Nordic HAL
ESP32 HAL
Renesas HAL
```

所以真正应该优化的是：

```text
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

```text
只要：

Zephyr
+
CMSIS
+
HC32 支持代码
+
ARM Toolchain
```

### 2.5.5\_因此最终的下载优化可以分成四层

以后整篇教程都可以沿着这个模型往下讲。

```text
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

```text
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

### 2.5.6\_给完全没有\_Git\_基础读者的一张总结表

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

```text
--depth
```

和：

```text
sparse-checkout
```

并不是同一个东西。

更不是：

```bash
# 当前位置：~/zephyr-download-lab；终端：UCRT64 Bash。
west manifest
```

。

它们分别处在三层：

```text
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

[参考资料目录](README.md) · [上一篇](P001_如何下载zephyr.md) · [下一篇](P003_国内如何更快下载zephyr.md)
