---
id: zephyr-download-notes-01
title: Zephyr 指定芯片的最小化下载方案
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 1. Zephyr 指定芯片的最小化下载方案

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。当前 HC32 工程请按[项目安装流程](../../project-docs/environment.md)操作；已整理的入门主线见[工程准备大纲](../P01_zephyr_make_project/大纲.md)。

### 1. 我们真正想解决的问题

标准 Zephyr 环境通常这样初始化：

```
west init zephyrproject
cd zephyrproject
west update
```

问题在于：

```
west update
```

会根据 Zephyr 自己的 `west.yml` 下载大量外部仓库，例如：

```
hal_stm32
hal_nxp
hal_nordic
hal_espressif
mbedtls
mcuboot
lvgl
littlefs
openthread
open-amp
trusted-firmware-m
...
```

对于一个明确的 MCU 项目，例如：

```
MCU：HC32F4A0PITB
CPU：ARM Cortex-M4F
架构：ARMv7-M
开发板：UYUP-RPI-A
```

显然没有必要把 NXP、Nordic、Espressif 等所有厂商 HAL 全部下载下来。

我们希望最终得到这样的“小环境”：

```
zephyr-workspace/
│
├── .west/
│
├── manifest/
│   └── west.yml
│
├── zephyr/
│   ├── arch/
│   ├── kernel/
│   ├── drivers/
│   ├── dts/
│   ├── boards/
│   ├── subsys/
│   ├── include/
│   └── ...
│
├── modules/
│   └── hal/
│       ├── cmsis/
│       └── hc32/
│
└── toolchain/
    └── ARM Cortex-M toolchain
```

核心原则是：

> **Zephyr 主仓库保留，外部模块按目标芯片裁剪，SDK 按 CPU 架构裁剪。**

这才是比较适合公司内部环境、教学环境和固定 MCU 开发环境的方案。

------

## 1.1 首先理解 Zephyr 到底由哪些东西组成

Zephyr 并不是一个 Git 仓库就包含所有内容。

可以把它分为三层：

```
                Zephyr 开发环境
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
 Zephyr 主仓库      外部 Modules      Toolchain
        │              │               │
 kernel             CMSIS            GCC
 arch               Vendor HAL       binutils
 drivers            mbedTLS          GDB
 dts                littlefs         host tools
 boards             LVGL             ...
 subsys             MCUboot
 cmake              ...
 scripts
```

其中真正值得裁剪的是：

```
外部 Modules
Toolchain
Git 历史
```

而不是首先去裁 Zephyr 主仓库。

Zephyr 主仓库本身包含 kernel、通用驱动框架、DTS、Kconfig、CMake、架构代码等，是整个构建系统的核心。官方仓库本身就是 Zephyr 的主要源码仓库。[GitHub](https://github.com/zephyrproject-rtos/zephyr?utm_source=chatgpt.com)

------

## 1.2 第一层裁剪：Zephyr 主仓库不要下载全部 Git 历史

首先不要这样：

```
git clone https://github.com/zephyrproject-rtos/zephyr.git
```

因为这会把完整 Git 历史都拉下来。

教学环境和固定版本开发环境应该指定版本，并使用浅克隆。

例如：

```
git clone \
    --branch v4.4.0 \
    --depth 1 \
    https://github.com/zephyrproject-rtos/zephyr.git
```

Windows PowerShell：

```
git clone `
    --branch v4.4.0 `
    --depth 1 `
    https://github.com/zephyrproject-rtos/zephyr.git
```

这样得到：

```
zephyr/
├── arch/
├── boards/
├── cmake/
├── drivers/
├── dts/
├── include/
├── kernel/
├── lib/
├── modules/
├── samples/
├── scripts/
├── soc/
├── subsys/
└── ...
```

但是 Git 历史只保留当前需要的浅层历史。

这一步非常重要。

### 不推荐一开始就 sparse-checkout

理论上 Git 可以这样：

```
git sparse-checkout
```

只下载：

```
arch/arm
drivers/
kernel/
soc/
boards/
...
```

但我不建议把这种方式作为教学环境的默认方案。

因为 Zephyr 的构建系统会横跨：

```
cmake/
scripts/
dts/
include/
modules/
soc/
boards/
arch/
subsys/
lib/
```

不同 Kconfig 选项还可能引入其它路径。

因此更稳定的策略是：

```
Zephyr 主仓库：

保留完整源码目录
+
减少 Git 历史
```

也就是：

```
--depth 1
```

而不是裁源码目录。

------

## 1.3 第二层裁剪：外部 Modules 才是重点

真正造成：

```
west update
```

下载大量仓库的，是 Zephyr 的 manifest。

也就是：

```
zephyr/west.yml
```

west workspace 中，manifest 决定哪些 Git project 属于这个工作区，而 `west update` 根据 manifest 更新这些项目。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/basics.html?utm_source=chatgpt.com)

例如 Zephyr 会定义类似：

```
projects:

  - name: cmsis
    path: modules/hal/cmsis

  - name: hal_stm32
    path: modules/hal/stm32

  - name: hal_nxp
    path: modules/hal/nxp

  - name: hal_nordic
    path: modules/hal/nordic

  - name: mbedtls
    path: modules/crypto/mbedtls

  - name: mcuboot
    path: bootloader/mcuboot

  - name: littlefs
    path: modules/fs/littlefs
```

如果直接：

```
west update
```

那么这些 active projects 都可能被下载。

官方 west 支持只更新指定项目：

```
west update PROJECT
```

也支持通过 manifest project groups 控制 active projects。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/built-in.html?utm_source=chatgpt.com)

但是对于我们的目标，我更推荐：

> **自己建立一个最小 manifest。**

------

## 1.4 推荐方案：自己维护一个 Mini Manifest

这是我认为最适合教学文档和项目工程化的方案。

不要让：

```
zephyr/west.yml
```

直接成为你的顶层 manifest。

而是建立自己的：

```
manifest/
└── west.yml
```

例如整个目录设计：

```
zephyr_hc32_workspace/
│
├── .west/
│
├── manifest/
│   └── west.yml
│
├── zephyr/
│
└── modules/
```

关系变成：

```
我们自己的 manifest
        │
        ├── Zephyr
        │
        ├── CMSIS
        │
        └── HC32 HAL / DDL
```

而不是：

```
Zephyr west.yml
        │
        ├── STM32
        ├── NXP
        ├── Nordic
        ├── Espressif
        ├── Infineon
        ├── Renesas
        ├── ...
        └── 几十个模块
```

------

## 1.5 第一种 Mini Manifest 写法：明确列出我们需要的模块

这是最容易理解的方案。

例如：

```
manifest:

  remotes:
    - name: zephyrproject
      url-base: https://github.com/zephyrproject-rtos

    - name: company
      url-base: https://git.example.com/embedded

  projects:

    - name: zephyr
      remote: zephyrproject
      revision: v4.4.0
      path: zephyr
      clone-depth: 1
      west-commands: scripts/west-commands.yml

    - name: cmsis
      remote: zephyrproject
      revision: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
      path: modules/hal/cmsis
      clone-depth: 1

    - name: hal_hc32
      remote: company
      revision: v1.0.0
      path: modules/hal/hc32
      clone-depth: 1

  self:
    path: manifest
```

这个环境里最终只有：

```
zephyr/
modules/hal/cmsis/
modules/hal/hc32/
```

不会出现：

```
hal_stm32
hal_nxp
hal_nordic
hal_espressif
lvgl
openthread
mbedtls
...
```

west manifest 本身原生支持 `clone-depth`，可以限制 project 的 Git 历史深度。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/manifest.html?utm_source=chatgpt.com)

这就是我们所谓的：

> **按芯片建立 Zephyr 小环境。**

------

## 1.6 为什么 HC32F4A0 至少需要 CMSIS

HC32F4A0 是：

```
ARM Cortex-M4F
```

所以整个软件栈可以粗略分成：

```
Application
    │
Zephyr API
    │
Zephyr Driver
    │
HC32 SoC / Board Support
    │
HC32 DDL
    │
CMSIS
    │
ARM Cortex-M4F
```

这里：

```
CMSIS
```

负责 ARM Cortex-M 体系结构相关的标准定义。

例如：

```
NVIC
SCB
SysTick
Core registers
Cortex-M intrinsic
```

Zephyr 的 ARM Cortex-M 支持会使用 CMSIS。

因此对于 HC32：

```
cmsis
```

通常属于基础模块。

------

## 1.7 HC32 自己的代码放在哪里

对于 HC32F4A0，我们现在有两种可能。

### 情况 A：HC32 DDL 直接放在 Zephyr fork 中

比如：

```
zephyr/
├── soc/
│   └── hdsc/
│       └── hc32f4a0/
│
├── boards/
│   └── uyup/
│       └── uyup_rpi_a/
│
└── drivers/
```

DDL 可能直接存在：

```
soc/hdsc/hc32f4a0/
```

或者某个 vendor 目录。

那么 mini workspace 可能只需要：

```
zephyr
cmsis
```

甚至：

```
workspace/
├── zephyr/
└── modules/
    └── hal/
        └── cmsis/
```

------

### 情况 B：把 HC32 DDL 单独做成 Module

长期来看我更推荐这种。

例如：

```
hal_hc32/
├── CMakeLists.txt
├── Kconfig
├── zephyr/
│   └── module.yml
└── hc32f4a0/
    ├── driver/
    ├── cmsis/
    └── ddl/
```

然后：

```
zephyr/
modules/
└── hal/
    ├── cmsis/
    └── hc32/
```

Zephyr Module 和 west project 是两个概念：

```
west project
    =
Git 仓库管理概念

Zephyr Module
    =
Zephyr 构建系统模块概念
```

west 可以把 repository 下载下来，然后 Zephyr 构建系统通过 module metadata 使用它。官方文档也特别区分了 project 和 module。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/basics.html?utm_source=chatgpt.com)

这种方式更适合以后：

```
HC32F4A0
HC32F460
HC32F448
...
```

共用同一套 HAL。

------

## 1.8 更漂亮的方案：Import Zephyr manifest，但只允许特定模块

如果不希望自己维护所有外部模块的 commit hash，还有另一种方法。

这也是我更推荐最终教学文档介绍的方法。

可以：

```
- name: zephyr
  ...
  import:
```

让自己的 manifest 导入：

```
zephyr/west.yml
```

但是增加：

```
name-allowlist:
```

只允许我们需要的项目。

west 官方明确支持这种 manifest import allowlist。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/manifest.html?utm_source=chatgpt.com)

例如：

```
manifest:

  remotes:
    - name: zephyrproject
      url-base: https://github.com/zephyrproject-rtos

  projects:

    - name: zephyr
      remote: zephyrproject
      revision: v4.4.0
      path: zephyr
      clone-depth: 1

      import:
        name-allowlist:
          - cmsis

  self:
    path: manifest
```

它表达的意思是：

```
下载 Zephyr

读取：
zephyr/west.yml

但是只从里面导入：

cmsis
```

其它：

```
hal_nxp
hal_stm32
hal_nordic
mbedtls
lvgl
mcuboot
...
```

全部忽略。

这种方式有一个很大的好处。

我们不用自己写：

```
cmsis:
    revision: 123456789abcdef
```

因为 CMSIS 对应的 revision 直接由：

```
Zephyr v4.4.0
```

自己的：

```
west.yml
```

决定。

也就是说：

```
Zephyr v4.4.0
        │
        └── 它自己指定兼容的 CMSIS commit
```

这样版本对应关系不会被我们破坏。

这实际上就是 west manifest imports 设计的重要使用场景：下游工程可以引用一个 Zephyr release，再选择性导入它的 projects。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/workspaces.html?utm_source=chatgpt.com)

------

## 1.9 对我们这个项目，我推荐这种结构

最终可以这样设计：

```
zephyr_hc32f4a0/
│
├── manifest/
│   └── west.yml
│
├── zephyr/
│
├── modules/
│   └── hal/
│       ├── cmsis/
│       └── hc32/
│
├── app/
│
└── build/
```

manifest：

```
manifest:

  remotes:

    - name: zephyrproject
      url-base: https://github.com/zephyrproject-rtos

    - name: hc32
      url-base: https://github.com/your-company

  projects:

    # Zephyr 主源码
    - name: zephyr
      remote: zephyrproject
      revision: v4.4.0
      path: zephyr
      clone-depth: 1

      import:
        name-allowlist:
          - cmsis

    # HC32 DDL/HAL
    - name: hal_hc32
      remote: hc32
      revision: main
      path: modules/hal/hc32
      clone-depth: 1

  self:
    path: manifest
```

最终下载链：

```
west
 │
 │ 读取
 ▼
manifest/west.yml
 │
 ├───────────────► zephyr
 │
 │                  │
 │                  │ import west.yml
 │                  ▼
 │                cmsis
 │
 └───────────────► hal_hc32
```

最终不会下载：

```
STM32 HAL
NXP HAL
Nordic HAL
ESP HAL
Renesas HAL
TI HAL
Bluetooth 模拟环境
TensorFlow Lite
OpenThread
LVGL
MCUboot
Trusted Firmware
...
```

------

## 1.10 Workspace 初始化

建立：

```
mkdir zephyr_hc32f4a0
cd zephyr_hc32f4a0
```

准备：

```
manifest/west.yml
```

然后：

```
west init -l manifest
```

这里：

```
-l
```

表示：

```
local manifest
```

也就是说：

> 不让 `west init` 去 GitHub 克隆一个 manifest repository，而直接使用当前本地 manifest。

之后：

```
west update
```

west 就只会按照我们的 manifest 下载项目。

最终：

```
zephyr_hc32f4a0/
│
├── .west/
│
├── manifest/
│
├── zephyr/
│
└── modules/
    └── hal/
        ├── cmsis/
        └── hc32/
```

------

## 1.11 甚至可以让 `west update` 只下载单个模块

west 不是一定要：

```
west update
```

全部更新。

它支持：

```
west update PROJECT
```

例如：

```
west update zephyr
```

或者：

```
west update cmsis
```

甚至：

```
west update zephyr cmsis
```

官方 `west update` 文档明确支持在命令行指定 project；如果指定了项目，就只更新这些项目。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/built-in.html?utm_source=chatgpt.com)

所以教学时可以解释为：

```
west update

= 更新 manifest 中所有 active projects
```

而：

```
west update zephyr cmsis
```

等于：

```
只更新 zephyr 和 cmsis
```

------

## 1.12 不过“只执行 west update zephyr”不能替代 Mini Manifest

这一点要特别说明。

假设官方 manifest 有：

```
100 个 project
```

你运行：

```
west update zephyr cmsis
```

确实只下载两个。

但是 workspace 的逻辑定义里：

```
那 100 个项目依然存在
```

以后别人执行：

```
west update
```

还是会全部拉下来。

因此：

```
west update zephyr cmsis
```

更适合：

```
临时实验
```

而：

```
自定义 west.yml
```

更适合：

```
教学
公司开发环境
CI
量产工程
固定 SDK
```

------

## 1.13 第三层裁剪：工具链也不要全部下载

Zephyr SDK 支持很多架构。

完整 SDK 可能包含：

```
ARM
ARM64
RISC-V
x86
Xtensa
ARC
MIPS
SPARC
...
```

HC32F4A0：

```
Cortex-M4F
     ↓
ARM
```

所以实际上只需要：

```
arm-zephyr-eabi
```

当前 Zephyr 的 SDK 工具支持：

```
west sdk install --toolchains ...
```

官方示例就是：

```
west sdk install --toolchains arm-zephyr-eabi riscv64-zephyr-elf
```

并明确说明，只选择需要的 toolchain 可以减少数 GB 下载和磁盘占用。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html?utm_source=chatgpt.com)

HC32 就可以：

```
west sdk install --toolchains arm-zephyr-eabi
```

这样：

```
不会安装：

riscv64-zephyr-elf
x86_64-zephyr-elf
xtensa-*
arc-zephyr-elf
...
```

只安装 ARM 工具链。

------

## 1.14 SDK 还可以进一步理解为两部分

Zephyr SDK 实际可以理解成：

```
Zephyr SDK
│
├── Host Tools
│
└── Target Toolchains
```

例如：

```
Host Tools
├── OpenOCD
├── QEMU
├── CMake integration
└── 其它辅助工具

Target Toolchain
└── arm-zephyr-eabi
    ├── gcc
    ├── g++
    ├── as
    ├── ld
    ├── objcopy
    ├── objdump
    └── gdb
```

Zephyr SDK 当前也提供：

```
gnu
llvm
minimal
```

等 bundle 类型，其中 `minimal` 包含 host tools 但不预装目标工具链，可以在 setup 时再按需要下载。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html?utm_source=chatgpt.com)

对于我们：

```
Host Tools
+
arm-zephyr-eabi
```

就够了。

------

## 1.15 HC32F4A0 最小环境到底应该下载什么

如果我们暂时只做：

```
UART
GPIO
SPI
I2C
Timer
RTC
Shell
FreeRTOS 类基础 RTOS 功能
Zephyr Kernel
```

没有：

```
Bluetooth
Wi-Fi
TLS
GUI
MCUboot
File system
OpenThread
TF-M
```

那么最小环境可以非常简单：

| 组件              | 是否需要   |
| ----------------- | ---------- |
| Zephyr 主源码     | 必须       |
| CMSIS             | 必须       |
| HC32 DDL/HAL      | 必须       |
| ARM GCC Toolchain | 必须       |
| Zephyr Host Tools | 建议       |
| STM32 HAL         | 不需要     |
| NXP HAL           | 不需要     |
| Nordic HAL        | 不需要     |
| ESP HAL           | 不需要     |
| mbedTLS           | 不需要     |
| LVGL              | 不需要     |
| OpenThread        | 不需要     |
| MCUboot           | 暂时不需要 |
| littlefs          | 暂时不需要 |
| FatFS             | 暂时不需要 |
| TF-M              | 不需要     |

于是整个环境就可以压缩到：

```
Zephyr
+
CMSIS
+
HC32 DDL
+
ARM Toolchain
```

------

## 1.16 以后需要什么，再把什么加入 manifest

比如以后需要：

```
LittleFS
```

修改：

```
import:
  name-allowlist:
    - cmsis
    - littlefs
```

然后：

```
west update
```

就会多出来：

```
modules/fs/littlefs/
```

如果需要：

```
mbedTLS
```

增加：

```
- mbedtls
```

需要：

```
MCUboot
```

增加：

```
- mcuboot
```

所以可以把环境理解成：

```
              HC32 Base
                  │
       ┌──────────┴──────────┐
       │                     │
     Zephyr                 CMSIS
       │
     HC32 HAL
       │
       ├──── + littlefs
       │
       ├──── + mbedtls
       │
       ├──── + mcuboot
       │
       └──── + lvgl
```

不是：

> 第一天就把 Zephyr 所有东西全下载下来。

------

## 1.17 我建议我们的教学文档把“环境下载”设计成三种级别

这个地方非常适合教学。

```
Level 1
官方完整环境

west init
west update
```

用途：

```
Zephyr 学习
研究所有平台
官方开发
```

↓

```
Level 2
指定 Project 更新

west update zephyr cmsis
```

用途：

```
快速实验
临时环境
```

↓

```
Level 3
自定义 Mini Manifest

HC32F4A0
+
Cortex-M4F
+
CMSIS
+
HC32 HAL
+
ARM Toolchain
```

用途：

```
正式项目
公司 SDK
教学环境
CI
固定产品平台
```

我们的教程最终应该主要教：

> **Level 3。**

因为这个方案才能真正解释：

```
我用什么 MCU
      ↓
我需要什么架构
      ↓
需要什么 HAL
      ↓
需要什么 Zephyr Module
      ↓
需要什么 Toolchain
      ↓
生成什么 manifest
      ↓
west 下载什么
```

而不是把：

```
west update
```

当作一个黑盒。

------

## 1.18 对 HC32F4A0，我们最终可以把下载规则写成一张图

```
目标芯片
HC32F4A0PITB
      │
      ▼
CPU Architecture
ARM Cortex-M4F
      │
      ├────────────────────────┐
      │                        │
      ▼                        ▼
CMSIS                    ARM Toolchain
      │                  arm-zephyr-eabi
      │
      ▼
HC32 SoC Support
      │
      ▼
HC32 DDL / HAL
      │
      ▼
Zephyr
      │
      ├── Kernel
      ├── ARM Arch
      ├── Driver Framework
      ├── DeviceTree
      ├── Kconfig
      ├── CMake
      └── Subsystems
```

所以下载集合：

```
Download Set
│
├── zephyr
├── cmsis
├── hal_hc32
└── arm-zephyr-eabi
```

**这就是我们后面这份教学文档应该围绕的核心思想。**

我建议下一节就接着写：

```
《如何根据一款 MCU 判断到底需要下载哪些 Zephyr 仓库》
```

重点把 **MCU → CPU 架构 → SoC → Vendor HAL → Zephyr Module → Toolchain → west.yml** 这条依赖链完整讲明白。这样学生以后换成 STM32、NXP、Nordic，也能自己判断该下载哪些仓库，而不是死记 HC32 的命令。

[参考资料目录](README.md) · [下一篇](P02_零基础获得zephyr.md)
