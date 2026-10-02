---
id: zephyr-download-notes-05
title: Zephyr SDK 与 ARM 交叉编译工具链：HC32F4A0 到底需要下载什么
kind: reference
status: draft
domains: [zephyr, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 5. Zephyr SDK 与 ARM 交叉编译工具链：HC32F4A0 到底需要下载什么

> 本篇为下载方案的参考草稿，保留原有讨论与示例，尚未完成逐项版本核验和完整安装实测。当前 HC32 工程请按[项目安装流程](../../project-docs/environment.md)操作；已整理的入门主线见[工程准备大纲](../P01_zephyr_make_project/大纲.md)。

前面我们已经把“源码下载”拆开了：

```
Zephyr 主源码 ZIP
        +
目标芯片需要的 Module ZIP
        +
目标架构工具链
```

现在进入第三部分：

```
目标架构工具链
```

这一部分非常容易出现一个误区：

> “Zephyr SDK 是 Zephyr 开发必须下载的一大包东西。”

其实不是。

Zephyr SDK 本身已经支持按架构拆分。对于 HC32F4A0 这种 Cortex-M4F 芯片，我们没有必要把 RISC-V、Xtensa、x86、ARC 等工具链一起下载。

我们真正要解决的是：

```
我的电脑是什么架构？
        ↓
我的目标 MCU 是什么架构？
        ↓
需要哪一个交叉编译器？
        ↓
Zephyr SDK 又提供了哪些公共 Host Tools？
        ↓
怎样只下载最少的一套？
```

------

## 5.1 首先区分两台“计算机”

做嵌入式开发时，实际上同时存在两个运行环境：

```
开发电脑
Host
Windows 11 / x86-64
        │
        │ 编译
        ▼
目标板
Target
HC32F4A0 / ARM Cortex-M4F
```

这两个一定不能混淆。

例如你的开发电脑可能是：

```
Windows 11
Intel/AMD x86-64
```

但你最终生成的程序不是运行在 Windows PC 上。

而是运行在：

```
HC32F4A0
ARM Cortex-M4F
```

所以：

```
编译器自己运行在哪里？
```

答案是：

```
Windows x86-64
```

但：

```
编译器生成谁能执行的机器码？
```

答案是：

```
ARM Cortex-M4F
```

这就是：

> **交叉编译。**

------

## 5.2 什么叫交叉编译

普通 PC 程序可能是：

```
x86-64 PC
   │
   │ gcc
   ▼
x86-64 程序
   │
   ▼
还是运行在 x86-64 PC
```

编译环境和目标环境相同。

这种情况不需要特别强调“交叉”。

而 MCU 开发则是：

```
Windows x86-64 PC
        │
        │ ARM GCC
        ▼
ARM Cortex-M4F Machine Code
        │
        ▼
HC32F4A0
```

也就是说：

```
Host Architecture != Target Architecture
```

因此叫：

```
Cross Compilation
交叉编译
```

------

## 5.3 所以我们实际上需要两类工具

整个 Zephyr 构建环境可以先划分为：

```
                 Zephyr 开发工具
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
         Host Tools          Target Toolchain
             │                   │
         在 PC 上工作         给 MCU 编译程序
             │                   │
        CMake 等工具         GCC
        OpenOCD              Assembler
        QEMU                 Linker
        ...                  objcopy
                             GDB
```

官方 Zephyr SDK 也正是这样组织的：SDK 包含针对不同目标架构的 GNU/LLVM 工具链，同时提供 OpenOCD、QEMU 等 Host Tools。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.4 什么是 Toolchain

`Toolchain` 中文通常叫：

```
工具链
```

为什么不是一个“compiler”就结束了？

因为从：

```
main.c
```

最终变成：

```
zephyr.bin
```

并不是只经过一个程序。

大概经历：

```
main.c
   │
   │ Compiler
   ▼
main.o
   │
   │
driver.c
   │
   │ Compiler
   ▼
driver.o
   │
   ├───────────┐
   │           │
   ▼           ▼
各种 .o      静态库 .a
   │           │
   └─────┬─────┘
         │
         │ Linker
         ▼
     zephyr.elf
         │
         ├── objcopy
         │      ↓
         │  zephyr.bin
         │
         └── objcopy
                ↓
            zephyr.hex
```

所以真正需要的是一组工具。

------

## 5.5 GCC 只是其中一个

例如 ARM Zephyr GNU Toolchain 中会存在类似：

```
arm-zephyr-eabi-gcc
arm-zephyr-eabi-g++
arm-zephyr-eabi-as
arm-zephyr-eabi-ld
arm-zephyr-eabi-ar
arm-zephyr-eabi-objcopy
arm-zephyr-eabi-objdump
arm-zephyr-eabi-readelf
arm-zephyr-eabi-size
arm-zephyr-eabi-gdb
```

这些名字先不要怕。

把后半部分拆出来就非常容易理解。

| 程序      | 作用                    |
| --------- | ----------------------- |
| `gcc`     | C 编译器                |
| `g++`     | C++ 编译器              |
| `as`      | 汇编器                  |
| `ld`      | 链接器                  |
| `ar`      | 创建静态库              |
| `objcopy` | 转换 ELF/BIN/HEX 等格式 |
| `objdump` | 反汇编、查看目标文件    |
| `readelf` | 查看 ELF 信息           |
| `size`    | 查看代码和数据大小      |
| `gdb`     | 调试器                  |

所以：

```
Toolchain
```

就是把这些相关工具组织在一起。

------

## 5.6 为什么每个程序前面都有 `arm-zephyr-eabi-`

例如：

```
arm-zephyr-eabi-gcc
```

可以拆成：

```
arm
-
zephyr
-
eabi
-
gcc
```

这里最重要的是第一部分：

```
arm
```

说明：

> 这是为 ARM 目标生成代码的工具链。

最后：

```
gcc
```

说明：

> 这是其中的 C 编译器。

而：

```
eabi
```

可以理解成：

```
Embedded Application Binary Interface
```

也就是嵌入式目标使用的一套 ABI 约定。

对于初学阶段，不需要深入 ABI 的每一个细节，只需要知道：

```
arm-zephyr-eabi-gcc
```

不是：

```
给 Windows PC 编译程序的 gcc
```

而是：

> **在 Host 电脑上运行，为 ARM Zephyr 目标生成程序的 GCC。**

------

## 5.7 为什么不是 `aarch64-zephyr-elf`

Zephyr SDK Release 页面还会看到：

```
aarch64-zephyr-elf
```

这很容易让初学者认为：

> ARM 芯片是不是应该选这个？

不是。

HC32F4A0：

```
ARM Cortex-M4F
```

属于：

```
32-bit ARM
```

因此应该选择：

```
arm-zephyr-eabi
```

而：

```
aarch64-zephyr-elf
```

是：

```
64-bit ARM
```

目标使用的。

例如 Cortex-A 系列的一些 64 位处理器。

所以：

```
HC32F4A0
    ↓
Cortex-M4F
    ↓
32-bit ARM
    ↓
arm-zephyr-eabi
```

不是：

```
aarch64-zephyr-elf
```

。

Zephyr SDK 官方支持 ARM A/R/M Profiles，同时把具体 GNU 工具链拆分为 `arm-zephyr-eabi` 和 `aarch64-zephyr-elf` 等不同 target。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.8 一个特别容易混淆的文件名

假设我们在 Windows 11 PC 上开发 HC32F4A0。

Release 页面会看到类似：

```
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

这个文件名第一次看非常长。

其实可以分成：

```
toolchain_gnu
│
└── GNU 工具链


windows
│
└── 工具链本身运行在 Windows


x86_64
│
└── 工具链这个程序运行在 x86-64 PC


arm-zephyr-eabi
│
└── 最终生成 ARM 目标代码
```

所以：

```
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

翻译成一句话就是：

> **运行在 Windows x86-64 PC 上、给 ARM Zephyr 目标生成程序的 GNU 工具链。**

这里同时出现：

```
x86_64
```

和：

```
arm
```

一点都不冲突。

它们分别描述：

```
x86_64
   ↓
编译器在哪里运行


arm
   ↓
编译出来的程序在哪里运行
```

------

## 5.9 如果是在 Linux PC 呢

假如 Host 是：

```
Ubuntu 22.04
x86-64
```

HC32 还是：

```
ARM Cortex-M4F
```

那么文件名变成类似：

```
toolchain_gnu_linux-x86_64_arm-zephyr-eabi.tar.xz
```

变化的是：

```
Windows
   ↓
Linux
```

目标仍然是：

```
arm-zephyr-eabi
```

因此：

```
Host OS
+
Host CPU
+
Target Architecture
```

共同决定应该下载哪个工具链包。

------

## 5.10 所以选择工具链的判断方法非常简单

对于任何板子，都可以按照：

```
我的开发电脑
        ↓
Host OS
        ↓
Windows / Linux / macOS

        +

我的开发电脑 CPU
        ↓
x86-64 / AArch64

        +

我的目标 CPU
        ↓
ARM / RISC-V / Xtensa / x86 ...
```

组合选择。

对于我们的环境：

```
Host OS:
Windows 11

Host CPU:
x86-64

Target MCU:
HC32F4A0

Target CPU:
ARM Cortex-M4F
```

所以：

```
toolchain
    =
GNU
+
Windows
+
x86_64
+
arm-zephyr-eabi
```

最终就是：

```
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

当前 Zephyr SDK Release 确实提供这种按目标架构拆开的工具链压缩包。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/releases?utm_source=chatgpt.com)

------

## 5.11 那 Zephyr SDK 又是什么

现在可以把：

```
Zephyr SDK
```

重新理解一下。

它不是单纯一个 GCC。

而是一套 Zephyr 官方整理好的：

```
Zephyr SDK
│
├── Host Tools
│
├── GNU Toolchains
│
├── LLVM Toolchain
│
├── CMake Integration
│
└── SDK Metadata
```

传统方式会直接下载一个很大的：

```
GNU SDK Bundle
```

里面把很多目标架构一起打包：

```
ARM
AArch64
RISC-V
x86
Xtensa
ARC
...
```

对于我们只开发：

```
HC32F4A0
```

明显没有必要。

------

## 5.12 Zephyr SDK 现在提供三种 Bundle

当前官方 SDK 文档把 bundle 分成：

| Bundle    | Host Tools | Target Toolchains   |
| --------- | ---------- | ------------------- |
| `gnu`     | 有         | 所有 GNU Toolchains |
| `llvm`    | 有         | LLVM/Clang          |
| `minimal` | 有         | 没有                |

也就是说：

```
minimal
```

这个名字非常重要。

它不是：

```
什么都没有的 SDK
```

而是：

> **保留 SDK 基础设施和 Host Tools，但不预装具体目标架构 Toolchain。**

这是官方现在专门提供的一种发行形式。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.13 这正好符合我们的“小环境”思想

传统：

```
Zephyr GNU SDK
│
├── Host Tools
├── ARM
├── AArch64
├── RISC-V
├── Xtensa
├── x86
├── ARC
└── ...
```

我们的方案：

```
Zephyr Minimal SDK
│
├── Host Tools
└── SDK Integration

        +

arm-zephyr-eabi
│
└── HC32F4A0 真正需要的 Toolchain
```

这样就实现：

```
需要 ARM
    ↓
只下载 ARM
```

而不是：

```
需要 ARM
    ↓
把 Zephyr 支持的所有 CPU 工具链一起下载
```

------

## 5.14 HC32F4A0 推荐下载的两个压缩包

以当前 Zephyr SDK 1.0.1 和 Windows x86-64 为例，可以在 SDK Release 页面中找到：

```
zephyr-sdk-1.0.1_windows-x86_64_minimal.7z
```

以及：

```
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

第一个：

```
minimal SDK
```

负责：

```
SDK 基础目录
Host Tools
CMake SDK integration
SDK metadata
```

第二个：

```
arm-zephyr-eabi
```

负责：

```
ARM GCC
ARM G++
assembler
linker
binutils
GDB
target libraries
```

当前 1.0.1 Release 同时提供 Minimal Bundle 和独立 `arm-zephyr-eabi` Windows 工具链包。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/releases?utm_source=chatgpt.com)

------

## 5.15 为什么我们不直接执行 `west sdk install`

官方 Getting Started 会告诉用户：

```
west sdk install
```

它确实非常方便。

west 会帮你：

```
确定 SDK
        ↓
下载
        ↓
安装
```

还可以指定：

```
west sdk install --toolchains arm-zephyr-eabi
```

官方也推荐使用 `--toolchains` 来避免下载不需要的架构，从而节省大量磁盘和下载流量。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html?utm_source=chatgpt.com)

但我们的教学环境有一个特殊目标：

> **避免让 GitHub 网络稳定性成为环境搭建的阻塞条件。**

所以我们暂时不选择：

```
命令运行过程中在线下载
```

而选择：

```
浏览器 / 下载工具
        ↓
把压缩包一次性拿下来
        ↓
离线解压和安装
```

这和前面：

```
Zephyr ZIP
CMSIS ZIP
HC32 HAL ZIP
```

采用的是完全相同的思想。

------

## 5.16 我们的下载目录现在可以设计成这样

例如：

```
downloads/
│
├── source/
│   ├── zephyr-vX.Y.Z.zip
│   ├── CMSIS_6-xxxxxxxx.zip
│   └── hal_hc32-xxxxxxxx.zip
│
└── sdk/
    ├── zephyr-sdk-1.0.1_windows-x86_64_minimal.7z
    └── toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

到这里：

```
源码
+
编译器
```

已经全部在本地。

以后即使：

```
GitHub 暂时打不开
```

也不影响重新搭环境。

------

## 5.17 下载完先不要急着安装

建议首先检查：

```
文件是否完整。
```

比如 Windows PowerShell：

```
Get-FileHash `
    .\zephyr-sdk-1.0.1_windows-x86_64_minimal.7z `
    -Algorithm SHA256
```

逐项解释。

------

### `Get-FileHash`

这是 PowerShell 用来：

```
计算文件摘要
```

的命令。

这里用于判断：

> 下载的压缩包是否完整。

------

### `-Algorithm SHA256`

表示：

```
使用 SHA-256 算法
```

最后会输出类似：

```
Algorithm Hash                                     Path
--------- ----                                     ----
SHA256    ABCDEF123456...                          ...
```

然后和 Zephyr SDK Release 提供的：

```
sha256.sum
```

进行比较。

官方安装文档也要求下载 SDK 后进行 SHA256 验证。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.18 为什么需要检查 SHA256

因为下载大文件时可能发生：

```
网络中断
代理问题
缓存异常
文件截断
下载工具异常
```

有时候压缩包甚至：

```
可以解压
```

但里面某部分数据已经损坏。

SHA256 相当于给文件算一个：

```
数字指纹
```

如果官方：

```
SHA256 = ABCD...
```

本地：

```
SHA256 = ABCD...
```

说明拿到的文件内容一致。

如果不同：

```
不要继续安装。
```

------

## 5.19 解压 Minimal SDK

例如我们准备：

```
D:\zephyr_env\
```

使用 7-Zip 解压：

```
zephyr-sdk-1.0.1_windows-x86_64_minimal.7z
```

最终得到类似：

```
D:\zephyr_env\
└── zephyr-sdk-1.0.1\
    ├── cmake\
    ├── hosttools\
    ├── sdk_version
    ├── sdk_gnu_toolchains
    ├── setup.cmd
    └── ...
```

这时候注意：

```
arm-zephyr-eabi
```

还没有安装。

因为我们下载的是：

```
minimal
```

。

官方定义中 Minimal Bundle 本身不携带任何 target toolchain。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.20 如果这时候直接运行 `setup.cmd` 会发生什么

例如：

```
cd D:\zephyr_env\zephyr-sdk-1.0.1

.\setup.cmd
```

脚本会询问类似：

```
Install GNU toolchain?
```

如果发现某些 GNU toolchain 不存在，还会继续询问：

```
是否安装某个 target toolchain
```

这里需要特别注意。

如果你回答：

```
Yes
```

但对应 Toolchain 尚未存在于 SDK 目录中，`setup.cmd` 会尝试从 Zephyr SDK GitHub Release 在线下载它。

从当前 Windows `setup.cmd` 的实现可以看到，它会构造：

```
https://github.com/zephyrproject-rtos/sdk-ng/releases/...
```

然后使用 SDK 自带的 `wget` 获取缺失的 toolchain。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/blob/main/scripts/template_setup_win)

这正是我们想避免的：

```
安装进行到一半
        ↓
突然依赖 GitHub 网络
        ↓
下载失败
        ↓
环境搭建中断
```

------

## 5.21 所以我们的方案是：工具链也提前下载

提前从 Release 页面下载：

```
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

然后将它安装到 Minimal SDK 的：

```
gnu/
```

目录中。

最终目标应该类似：

```
zephyr-sdk-1.0.1/
│
├── hosttools/
│
├── cmake/
│
├── gnu/
│   └── arm-zephyr-eabi/
│       ├── bin/
│       ├── include/
│       ├── lib/
│       └── ...
│
├── setup.cmd
├── sdk_version
└── ...
```

Zephyr SDK 的 Windows 安装脚本本身就是通过检查：

```
gnu\<toolchain-name>\
```

是否存在来判断工具链是否已经装好；缺失时才进行下载和解压。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/blob/main/scripts/template_setup_win)

所以对于我们的离线环境：

```
先把 ARM 工具链准备好
        ↓
再执行 SDK 注册配置
```

更加稳定。

------

## 5.22 为什么目录叫 `gnu/arm-zephyr-eabi`

这是非常值得理解的一层。

最终：

```
zephyr-sdk-1.0.1/
│
└── gnu/
    └── arm-zephyr-eabi/
```

其中：

```
gnu
```

表示：

```
工具链家族
```

：

```
arm-zephyr-eabi
```

表示：

```
目标平台
```

以后如果还有 RISC-V：

```
gnu/
├── arm-zephyr-eabi/
└── riscv64-zephyr-elf/
```

如果还有 AArch64：

```
gnu/
├── arm-zephyr-eabi/
├── riscv64-zephyr-elf/
└── aarch64-zephyr-elf/
```

所以 Zephyr SDK 不是一个“不可拆的大编译器”。

而更像：

```
SDK 框架
    +
若干可以插入的 Toolchain
```

。

------

## 5.23 安装完成以后怎么确认 ARM GCC 真正存在

假设 SDK 在：

```
D:\zephyr_env\zephyr-sdk-1.0.1
```

工具链可能位于：

```
D:\zephyr_env\
└── zephyr-sdk-1.0.1\
    └── gnu\
        └── arm-zephyr-eabi\
            └── bin\
```

进入：

```
cd D:\zephyr_env\zephyr-sdk-1.0.1\gnu\arm-zephyr-eabi\bin
```

查看：

```
Get-ChildItem
```

应该能够看到：

```
arm-zephyr-eabi-gcc.exe
arm-zephyr-eabi-g++.exe
arm-zephyr-eabi-ld.exe
arm-zephyr-eabi-objcopy.exe
arm-zephyr-eabi-objdump.exe
arm-zephyr-eabi-gdb.exe
...
```

------

## 5.24 验证 GCC

可以直接：

```
.\arm-zephyr-eabi-gcc.exe --version
```

其中：

```
.\
```

表示：

> 从当前目录运行这个程序。

：

```
arm-zephyr-eabi-gcc.exe
```

是：

> ARM Zephyr C 编译器。

：

```
--version
```

表示：

> 打印版本信息，而不是开始编译。

只要正常输出 GCC 版本：

```
arm-zephyr-eabi-gcc ...
Copyright ...
```

至少说明：

```
工具链文件存在
+
Windows 可以启动这个程序
```

。

------

## 5.25 还可以验证 `objcopy`

执行：

```
.\arm-zephyr-eabi-objcopy.exe --version
```

这一步验证：

```
GNU binutils
```

也安装完整。

因为最终 Zephyr 经常需要把：

```
zephyr.elf
```

转换成：

```
zephyr.bin
zephyr.hex
```

这就是：

```
objcopy
```

负责的工作之一。

------

## 5.26 Zephyr 最终编译为什么首先产生 ELF

初学者经常只关心：

```
.bin
```

但编译系统真正核心的最终产物通常是：

```
zephyr.elf
```

ELF 中不仅有：

```
机器码
```

还可以保存：

```
符号表
段信息
调试信息
函数名
变量信息
地址
```

因此：

```
编译
   ↓
zephyr.elf
```

之后才能进一步：

```
zephyr.elf
    │
    ├── objcopy
    │      ↓
    │  zephyr.bin
    │
    ├── objcopy
    │      ↓
    │  zephyr.hex
    │
    ├── size
    │      ↓
    │  RAM / Flash 信息
    │
    └── gdb
           ↓
       调试
```

所以工具链远远不只是一个 GCC。

------

## 5.27 `GDB` 为什么也属于 Target Toolchain

例如：

```
arm-zephyr-eabi-gdb
```

GDB 本身在 Windows PC 上运行。

但是它理解：

```
ARM 寄存器
ARM 指令
ARM ELF
ARM 调试信息
```

然后通过：

```
GDB
  │
  ▼
GDB Server
  │
  ▼
SWD/JTAG
  │
  ▼
HC32F4A0
```

完成调试。

例如 GDB Server 可以由：

```
OpenOCD
pyOCD
J-Link GDB Server
```

提供。

这也是为什么：

```
GDB
```

和：

```
OpenOCD
```

不是同一个东西。

------

## 5.28 GDB 和 OpenOCD 的关系

可以理解成：

```
VS Code
    │
    ▼
arm-zephyr-eabi-gdb
    │
    │ GDB protocol
    ▼
OpenOCD / pyOCD
    │
    │ SWD
    ▼
DAP / Debug Probe
    │
    ▼
HC32F4A0
```

GDB 负责：

```
断点
单步
变量
寄存器
调用栈
符号
```

OpenOCD / pyOCD 负责：

```
连接实际 Debug Probe
控制 SWD/JTAG
读写目标内存
控制 CPU
烧写 Flash
```

因此 Zephyr SDK 里提供 Host Tools 也是有意义的。

------

## 5.29 那么 Host Tools 为什么不跟 ARM Toolchain 放在一起

因为：

```
arm-zephyr-eabi
```

是与：

```
Target Architecture
```

绑定的。

但很多工具与目标架构没有这种一一关系。

例如：

```
OpenOCD
QEMU
wget
SDK CMake scripts
```

更接近：

```
Host Environment
```

。

因此 SDK 结构上把它们分开：

```
Host Tools
        +
Target Toolchain
```

是更加合理的。

------

## 5.30 什么是 Sysroot

这里顺便解释另一个常见术语：

```
sysroot
```

在交叉编译环境里，可以暂时理解成：

> **给目标平台准备的一套“根目录视角”。**

例如一个 Linux 交叉工具链可能存在：

```
sysroot/
├── usr/
│   ├── include/
│   └── lib/
└── lib/
```

里面放：

```
目标平台头文件
目标平台 C 库
目标平台链接库
```

而不是直接使用 Windows：

```
C:\Program Files\...
```

里面的东西。

否则就会出现荒唐情况：

```
Windows PC 的库
    ↓
拿去链接 ARM MCU 程序
```

这是不可能的。

------

## 5.31 MCU Toolchain 和 Linux Sysroot 又有区别

对于嵌入式 Linux：

```
Target
=
Linux
```

通常会有比较完整的：

```
sysroot
```

例如：

```
glibc
/usr/include
/usr/lib
动态链接器
```

。

但 HC32F4A0：

```
Target
=
Bare-metal MCU + Zephyr RTOS
```

它没有：

```
Linux /usr
Linux glibc
Linux dynamic linker
```

。

所以这里不能照搬嵌入式 Linux 的 sysroot 概念。

Zephyr 自己负责：

```
Kernel
Scheduler
Driver
IPC
Device Model
System API
```

Toolchain 则提供：

```
Compiler
Binutils
目标架构运行库
C/C++ 基础支持
```

二者最终组合形成 MCU 固件。

------

## 5.32 Zephyr SDK 1.0.x 的 C 库

当前 Zephyr SDK 1.0.x 的 GNU Toolchain 已经以 GCC 14.3 / Binutils 2.43 为基础，并由 SDK 提供 Picolibc；1.0.0 起 SDK 不再提供 Newlib/Newlib-nano。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/blob/main/release-notes.md?utm_source=chatgpt.com)

不过这里教学时不要误解：

```
SDK 中存在 C library
```

不意味着：

```
所有 Zephyr 工程永远强制使用同一个 libc 配置。
```

最终启用哪种 libc 仍然与：

```
Zephyr configuration
Kconfig
SDK version
```

有关。

这一章只需要知道：

> Toolchain 不仅仅是 `gcc.exe`，它还带着目标架构相关的运行时和库支持。

------

## 5.33 `setup.cmd` 到底做什么

现在终于可以理解：

```
setup.cmd
```

不是：

```
安装一个 Windows 软件
```

这种传统意义上的 Installer。

Zephyr SDK 本身主要就是：

```
解压后的目录
```

。

官方甚至明确说明，要卸载 SDK，删除安装目录即可。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

`setup.cmd` 主要完成：

```
检查依赖
        ↓
选择/安装 Toolchain
        ↓
准备 Host Tools
        ↓
向 CMake 注册 Zephyr SDK
```

当前 Windows setup 脚本还提供：

```
/t <toolchain>
/h
/c
```

等选项，其中 `/c` 用于注册 SDK 的 CMake package。[GitHub](https://github.com/zephyrproject-rtos/sdk-ng/blob/main/scripts/template_setup_win)

------

## 5.34 什么叫“向 CMake 注册 SDK”

Zephyr 构建最终需要回答：

```
Zephyr SDK 在哪里？
```

假设：

```
D:\zephyr_env\zephyr-sdk-1.0.1
```

如果 CMake 已经登记了这个 SDK：

```
Zephyr Build
      │
      ▼
CMake
      │
      ▼
CMake Package Registry
      │
      ▼
zephyr-sdk-1.0.1
```

它可以自动找到。

如果没有注册，也可以显式告诉它：

```
ZEPHYR_SDK_INSTALL_DIR
```

官方文档明确支持这种方式。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.35 `ZEPHYR_SDK_INSTALL_DIR` 是什么

例如 PowerShell：

```
$env:ZEPHYR_SDK_INSTALL_DIR =
    "D:\zephyr_env\zephyr-sdk-1.0.1"
```

拆开解释。

```
$env:
```

表示：

```
PowerShell 环境变量
```

：

```
ZEPHYR_SDK_INSTALL_DIR
```

表示：

```
Zephyr SDK 安装目录
```

：

```
"D:\zephyr_env\zephyr-sdk-1.0.1"
```

就是实际路径。

整句话相当于告诉 Zephyr：

> 不要猜 SDK 在哪里，我明确告诉你 SDK 在这个目录。

------

## 5.36 `ZEPHYR_TOOLCHAIN_VARIANT` 又是什么

另外还会看到：

```
$env:ZEPHYR_TOOLCHAIN_VARIANT = "zephyr"
```

意思是：

> 使用 Zephyr SDK 提供的 Toolchain。

因为 Zephyr 不只支持：

```
Zephyr SDK
```

也可以使用：

```
GNU Arm Embedded
LLVM
IAR
Host GCC
其它受支持 Toolchain
```

所以这个变量实际上是在告诉构建系统：

```
到底选择哪一类 Toolchain。
```

官方文档也说明，可以设置：

```
ZEPHYR_TOOLCHAIN_VARIANT=zephyr
```

明确使用 Zephyr SDK。[Zephyr Project Documentation](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)

------

## 5.37 我们最终推荐的 HC32F4A0 工具链环境

因此第一版教学环境可以收敛成：

```
D:\zephyr_env\
│
├── zephyr\
│
├── modules\
│   └── hal\
│       ├── cmsis_6\
│       └── hc32\
│
└── zephyr-sdk-1.0.1\
    │
    ├── hosttools\
    │
    ├── cmake\
    │
    └── gnu\
        └── arm-zephyr-eabi\
```

重点是：

```
没有：

gnu/riscv64-zephyr-elf
gnu/aarch64-zephyr-elf
gnu/x86_64-zephyr-elf
gnu/xtensa-...
gnu/arc-...
```

因为：

```
当前开发对象只有 HC32F4A0。
```

------

## 5.38 到这里我们的“小环境”已经非常清晰

下载集合现在变成：

```
HC32F4A0 Zephyr Mini Environment

Source
│
├── Zephyr 固定版本 ZIP
├── CMSIS_6 固定 revision ZIP
└── HC32 HAL 固定 revision ZIP
        │
        ▼
Tool
│
├── Zephyr SDK Minimal
└── GNU arm-zephyr-eabi Toolchain
```

整个决策过程是：

```
选择 MCU
   ↓
HC32F4A0
   ↓
确认 CPU
   ↓
Cortex-M4F
   ↓
确认架构
   ↓
32-bit ARM
   ↓
选择 Toolchain
   ↓
arm-zephyr-eabi
   ↓
确认 Host
   ↓
Windows x86-64
   ↓
选择下载包
   ↓
toolchain_gnu_windows-x86_64_arm-zephyr-eabi.7z
```

这个逻辑比：

```
去 Zephyr 网站
↓
把 SDK 全下载下来
```

更值得教给初学者。

因为以后目标换成：

```
RISC-V
```

他自己就知道：

```
Target Architecture 变了
        ↓
Toolchain 也应该变
```

而不是重新找一份教程照抄命令。

------

## 5.39 这一阶段我们仍然不需要 Git

注意现在整个环境：

```
Zephyr ZIP
CMSIS ZIP
HC32 ZIP
Minimal SDK 7z
ARM Toolchain 7z
```

全部都可以通过浏览器或者稳定的下载工具一次性获取。

所以：

```
GitHub 的 git clone 链路
```

完全没有成为第一阶段环境搭建的前置条件。

我们的思想始终没有变化：

```
第一目标：
先获得可以工作的源码和工具链

第二目标：
让工程可以配置和编译

第三目标：
有需要以后再给源码补 Git 能力
```

而不是：

```
第一步：
先把 Git 世界搭完整

然后才允许编译。
```

------

## 5.40 现在只剩下一个非常关键的问题

到目前为止我们已经拥有：

```
源码
Modules
ARM Toolchain
SDK Host Tools
```

但是电脑上还有：

```
Python
CMake
Ninja
west
Devicetree Compiler
```

这些东西。

它们和：

```
Zephyr SDK
```

又是什么关系？

哪些属于：

```
必须安装
```

？

哪些其实：

```
SDK 已经带了
```

？

哪些属于：

```
Python package
```

？

哪些只有：

```
Linux 需要
```

？

最容易犯的错误就是把：

```
Zephyr SDK
```

误认为：

> “下载了以后 Zephyr 所有构建依赖就齐了。”

实际上并不是。

所以**下一节应该继续写《Host 端到底需要安装哪些工具：Python、CMake、Ninja、west、DTC 和 Zephyr SDK 分别负责什么》**。

那一节之后，我们就可以真正开始把这些 ZIP/7z 拼成一个**完全不依赖 `git clone`、不用 `west update`、下载后即可配置编译的 HC32F4A0 Zephyr 小环境**。

[参考资料目录](README.md) · [上一篇](P04_如何从west.yml获得需要下载的包.md) · [下一篇](P06_环境依赖需要安装的工具.md)
