---
id: learning-cmake-2
title: 接入 Zephyr 模块
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2. 接入 Zephyr 模块

上一章把一个普通 C 库链接到主机程序。现在想让同一组功能在 Zephyr 应用中可选择地启用：开启时编译库，关闭时应用仍能构建。仅把目录复制进仓库，还缺“从哪里读规则”和“是否启用”两件事。

这就是本章要建立的最小模块。我们只做模块发现、配置与编译；运行测试留到 Twister/QEMU 章节。不要为了看懂怎样接入一个目录，先背另一套测试工具的选项。

## 2.1 三个叫“模块”的东西，先按职责区分

普通 CMake 库是一个构建目标。**Zephyr module** 是带元数据的源码目录，用元数据告诉 Zephyr 到哪里读 CMake、Kconfig 等入口。west project 则是由清单管理的 Git 仓库。一份仓库可以提供一个模块，但下载成功并不会自动让代码参与编译。

本章用仓库自带原件，不添加网络依赖。需要已安装 SDK 和项目 Python 环境；在仓库根目录打开 UCRT64 Bash，执行：

```bash
source .venv/Scripts/activate
python scripts/project_env.py doctor
mkdir build/learning-tools/module-textbook
cp -R learning/cmake/labs/zephyr_app build/learning-tools/module-textbook/zephyr_app
cp -R learning/cmake/labs/zephyr_module build/learning-tools/module-textbook/zephyr_module
```

若尚无 .venv，先按准备章的工程工具准备建立它；doctor 检查工具而不替你创建模块。module-textbook 必须是新目录。以下始终从仓库根目录执行，只编辑这份复制品。

## 2.2 先让一个目录被发现

zephyr_module 的内容很小：

```text
zephyr_module/
  zephyr/module.yml
  CMakeLists.txt
  Kconfig
  include/scale.h
  src/scale.c
```

zephyr/module.yml 的完整内容是：

```yaml
name: learning_scale
build:
  cmake: .
  kconfig: Kconfig
```

name 是模块名；cmake 指模块根目录下的 CMake 入口所在目录，点表示根目录本身；kconfig 指选项定义文件。路径相对模块根，不相对 shell 当前目录。元数据说明“如何接入”，还没有决定开关是否打开。

应用 zephyr_app/CMakeLists.txt 完整如下：

```cmake
cmake_minimum_required(VERSION 3.28.0)
get_filename_component(lesson_root "${CMAKE_CURRENT_LIST_DIR}/../../../.." ABSOLUTE)
set(ZEPHYR_BASE "${lesson_root}")
set(Zephyr_DIR "${lesson_root}/share/zephyr-package/cmake")
set(ZEPHYR_MODULES
  "${lesson_root}/modules/hal/cmsis_6"
  "${lesson_root}/modules/hal/xhsc"
)
list(APPEND EXTRA_ZEPHYR_MODULES "${CMAKE_CURRENT_LIST_DIR}/../zephyr_module")
find_package(Zephyr REQUIRED)
project(learning_module)
target_sources(app PRIVATE src/main.c)
```

CMAKE_CURRENT_LIST_DIR 是当前 CMake 文件所在目录，与终端位置无关。向上四层取得本仓库根：原件与本章复制品都保持这个深度，所以相对位置仍成立。这里明确选择本仓库 Zephyr 和已纳管的 CMSIS/HAL，不会回退到电脑旁边另一份源码。

EXTRA_ZEPHYR_MODULES 追加我们的目录，find_package(Zephyr REQUIRED) 才开始 Zephyr 的配置过程，并要求找不到时停止。追加必须发生在 find_package 之前，因为模块发现就在这个过程中完成。应用最终仍通过 target_sources 给 app 目标增加自己的 main.c。

## 2.3 再决定是否编译它

Kconfig 是 Zephyr 定义软件选项的机制。本章只用一个布尔选项；复杂依赖留到板级配置章节。模块 Kconfig 内容为：

```kconfig
config LEARNING_SCALE
    bool "Enable the learning scale module"
    default y
    help
      Compile the small demonstration module and expose its header.
```

它定义名字与类型，默认启用。应用的 prj.conf 请求 `CONFIG_LEARNING_SCALE=y`，no_module.conf 请求 `CONFIG_LEARNING_SCALE=n`。定义时名字不带 CONFIG_，应用配置和生成结果带这个前缀。

模块 CMakeLists.txt 把开关接到构建：

```cmake
if(CONFIG_LEARNING_SCALE)
  zephyr_library()
  zephyr_library_sources(src/scale.c)
  zephyr_include_directories(include)
endif()
```

只有开启时才建库、加入源文件并提供头文件目录。zephyr_library 系列函数由 Zephyr 提供，参与它的构建组织，不是 CMake 自带同名命令。

src/scale.c 的有效代码如下：

```c
#include "scale.h"

int scale_sample(int value)
{
    return value * 2;
}
```

include/scale.h 的完整有效内容为：

```c
#ifndef LEARNING_SCALE_H
#define LEARNING_SCALE_H
int scale_sample(int value);
#endif
```

应用的完整 main.c 为：

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>
#ifdef CONFIG_LEARNING_SCALE
#include "scale.h"
#endif

int main(void)
{
#ifdef CONFIG_LEARNING_SCALE
    printk("module result=%d\n", scale_sample(21));
#else
    printk("module disabled\n");
#endif
    return 0;
}
```

printk 是 Zephyr 的输出函数。应用与模块使用同一开关，所以关闭时既不编译库，也不留下对 scale_sample 的调用。这一点比“开时能编译”多了一个要求：可选模块关闭时也应完整成立。

## 2.4 分别配置开启与关闭的构建

这里选择已支持的模拟目标 mps2/an386，仅作可移植软件构建，不代表 HC32 板。先构建默认开启状态：

```bash
python scripts/project_env.py exec cmake -S build/learning-tools/module-textbook/zephyr_app -B build/learning-tools/module-textbook/enabled -G Ninja -DBOARD=mps2/an386
python scripts/project_env.py exec cmake --build build/learning-tools/module-textbook/enabled
rg -n "CONFIG_LEARNING_SCALE" build/learning-tools/module-textbook/enabled/zephyr/.config
rg -n "zephyr_module.*scale.c" build/learning-tools/module-textbook/enabled/compile_commands.json
```

project_env.py 用项目记录的工具环境运行后面的命令。预期 .config 为 y，编译数据库含模块 scale.c，构建生成 ELF。它证明选项开启且源码编入，没有证明程序已经在模拟器运行。

再使用独立目录关闭：

```bash
python scripts/project_env.py exec cmake -S build/learning-tools/module-textbook/zephyr_app -B build/learning-tools/module-textbook/disabled -G Ninja -DBOARD=mps2/an386 -DEXTRA_CONF_FILE=no_module.conf
python scripts/project_env.py exec cmake --build build/learning-tools/module-textbook/disabled
rg -n "CONFIG_LEARNING_SCALE" build/learning-tools/module-textbook/disabled/zephyr/.config
rg -n "zephyr_module.*scale.c" build/learning-tools/module-textbook/disabled/compile_commands.json
echo $?
```

EXTRA_CONF_FILE 相对应用源码目录解析，所以找到复制品中的 no_module.conf。最终配置应显示未设置该选项；第二个 rg 应无匹配并返回 1，这是本次所需观察：关闭后那个源文件没有参与编译。不要把“找到模块目录”和“编译了模块源码”合成同一个结论。

## 2.5 改一个条件，看看调用端会怎样

先做一个可恢复的错误。备份复制品的 main.c，再将它临时改为不加条件的调用：

```bash
cp build/learning-tools/module-textbook/zephyr_app/src/main.c build/learning-tools/module-textbook/main-before.c
```

新的完整 main.c：

```c
#include <zephyr/sys/printk.h>

int scale_sample(int value);

int main(void)
{
    printk("module result=%d\n", scale_sample(21));
    return 0;
}
```

此处直接给出函数声明，故意排除头文件找不到的干扰，让我们观察链接阶段。构建关闭状态：

```bash
python scripts/project_env.py exec cmake --build build/learning-tools/module-textbook/disabled
echo $?
```

应报告 scale_sample 未定义：应用仍调用，模块却没有提供实现。恢复备份，再重建两种状态：

```bash
cp build/learning-tools/module-textbook/main-before.c build/learning-tools/module-textbook/zephyr_app/src/main.c
python scripts/project_env.py exec cmake --build build/learning-tools/module-textbook/disabled
python scripts/project_env.py exec cmake --build build/learning-tools/module-textbook/enabled
```

都应通过。找不到选项定义时查模块发现与 Kconfig 入口；找不到头文件查模块开关与 include；链接缺实现查源文件是否编入及调用条件。每种错误都有一个可以检查的连接点。

## 2.6 将这个模式用于项目

新增普通业务文件时继续放进 app；需要多个应用复用并带独立开关时，再考虑模块。接入外部模块还要管理版本、许可证与来源。对于本仓库的长期基础依赖，需同步受控源码、dependencies.lock.json 及模块选择规则，不能把本机邻居目录偷偷当成构建输入。

练习把复制品 scale.c 的倍数改成 3，再构建 enabled。编译数据库仍包含同一文件，构建日志应重新编译它；disabled 不受这个实现的业务变化影响。按源码推算，开启后的输出会是 63，但本章尚未运行它，不把推算写成实测。练习后恢复倍数 2，给后面运行测试留下统一起点。

[Zephyr 模块元数据说明](https://docs.zephyrproject.org/latest/develop/modules.html)用于核对入口关系。[上一章](P01_把源文件和库加入构建.md) · [大纲](大纲.md)
