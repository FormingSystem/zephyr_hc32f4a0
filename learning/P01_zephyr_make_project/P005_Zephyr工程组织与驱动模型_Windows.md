---
id: zephyr-p006-project-organization-components
title: Zephyr 工程组织与驱动模型
kind: engineering
status: evolving
slides: slides/P005_Zephyr工程组织与驱动模型_Windows.pptx
domains: [zephyr, application, modules, build]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第5章\_Zephyr工程组织与驱动模型

前面已经取得 Zephyr、SDK 和 CMSIS。现在先不下载更多厂商包，而是用官方 `hello_world + mps2/an386` 看清一套工程：

1. 应用、板、SoC、架构和驱动分别在哪里；
2. 同一份外设驱动怎样取得本板配置；
3. Kconfig、板默认配置和 CMake 怎样决定编译什么。

本章按 **硬件身份 → 目录与复用范围 → 选择应用和板 → DTS/Kconfig/defconfig → CMake 与生成宏 → 设备实例和 API 调用** 展开。构建侧回答“哪些代码进入固件”，设备模型回答“调用进入哪个设备实例”；两者不能互相代替。

前提是 P002 的工具与 `.venv`、P003 的 SDK、P004 的 CMSIS 下载已完成。普通操作使用 UCRT64，从 `/g/zephyr_practice/zephyr-main` 执行。这里复用官方支持，先建立可反查的基线；下一章再为 HC32 选择和引入独立 DDL。

配套 [PPT](slides/P005_Zephyr工程组织与驱动模型_Windows.pptx)；返回 [环境与依赖导航](环境与依赖导航.md)。

**复制命令：** 本章完整操作统一放在 [P005 命令索引](commands/P005_Windows/README.md)。按正文前提选择分支，不批量执行全部文件。实验生成目录中的 `p003`、`p006` 保留原有标识，不因教材重排搬动。

<a id="architecture-soc-board"></a>

<a id="section-5-1"></a>

## 5.1\_先认识 MPS2、AN386 和 Cortex-M4F

<a id="section-5-1-1"></a>

### 5.1.1\_物理板、FPGA 系统和 CPU 不是同一个名字

MPS2 是 Arm 的 Cortex-M 原型开发平台。它使用 FPGA 装载不同的处理器系统设计，板上的连接器、存储器和调试接口承载这些系统。不能把 MPS2 当成一颗固定型号、内部外设永远不变的 MCU。

AN386 是 Arm 应用说明对应的一套 **Cortex-M4 系统设计/FPGA 映像**；Zephyr 用 `an386` 标识这个目标。它配置 Cortex-M4F：M4 是处理器内核，F 表示具有浮点能力；当前 Zephyr 配置选择 Cortex-M4、FPU 与 MPU。更精确地说，Cortex-M4 实现 Armv7E-M，属于 Armv7-M 架构家族的增强分支；不能把处理器名与指令集架构名当成同一层。当前外部 CMSIS_6 原件 `CMSIS/Documentation/Doxygen/Core/src/ref_cm4_simd.txt` 也将 Cortex-M4/M7 对应到 Armv7E-M。相邻 AN385 是 Cortex-M3 目标，不能因为同用 MPS2 板名就混用 CPU 或内存/外设假设。

`mps2/an386` 因而同时表达“使用 MPS2 这块平台的板支持”和“使用 AN386 这套系统目标”。本章面对的是这个具体组合，不是在介绍所有 MPS2 映像，也不把 QEMU 运行当作物理板全部功能已经验证。

| 认识层次 | MPS2 对照 | HC32 主线中的对应项 |
| --- | --- | --- |
| 架构/CPU | Arm Cortex-M4F；Zephyr 使用 Cortex-M 架构实现 | HC32F4A0 也使用 Cortex-M4，需配芯片实际能力 |
| 系统/SoC | FPGA 中的 AN386 系统目标 | 华大 HC32F4A0PITB 微控制器 |
| 板 | MPS2 平台及其板资源连接 | UYUP-RPI-A-2.5 板及实际晶振、引脚、连接 |
| 完整 BOARD | `mps2/an386` | 适配定义完成后的 `uyup_rpi_a/hc32f4a0pitb` |
| 应用 | 独立的 `samples/hello_world` | 同一 hello_world 或独立业务应用 |

两者可以共享 Cortex-M 架构的一部分代码，但 UART 寄存器、时钟树、引脚与板资源不同，所以不能从“同为 M4”推出“无需移植即可换板”。

<a id="section-5-1-2"></a>

### 5.1.2\_为什么先用这个目标建立对照

当前 Zephyr 已有 MPS2/AN386 的板、SoC、DTS 和外设驱动接入。我们可以固定这些已存在的支持，先检查应用选择、CMSIS 与 SDK，在后续 P006 再只增加一个普通组件，避免同时面对新板移植与新组件两类变量。

当前源码的板列表可列出 `an386`，本系列已用这套目标完成构建并用 SDK 自带 QEMU 观察输出。物理板烧录与其他外设验证仍有各自前提，不包含在本章实验中。

平台依据：[Arm MPS2/MPS2+ TRM](https://documentation-service.arm.com/static/5fd9f120d68fe412ba040ffd) 的 1.2 节说明 FPGA 原型开发板；[QEMU MPS2 系统说明](https://www.qemu.org/docs/master/system/arm/mps2.html) 明确区分板与 FPGA 映像，并对应 AN386/Cortex-M4。Zephyr 接入核对入口：[Zephyr MPS2 板文档](https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html)，本地 `boards/arm/mps2/doc/mps2_armv7m.rst`、`board.yml`、`soc/arm/mps2/Kconfig`。正文后面会说明其中硬件支持怎样工作，不要求读者自行从这些文件推导结论。

<a id="component-concepts"></a>

<a id="section-5-2"></a>

## 5.2\_模块、CMSIS、HAL 与 SDK 各解决什么问题

<a id="section-5-2-1"></a>

### 5.2.1\_先分清接口源码、硬件实现与编译工具

**CMSIS（Common Microcontroller Software Interface Standard）** 是 Arm 维护的微控制器标准软件接口体系，包含接口规范、公共 API、软件组件与相关工具。当前 AN386 构建使用的是 **CMSIS_6 中 CMSIS-Core 的内核头**，例如 Cortex-M4 的寄存器定义与 NVIC 操作接口；不是要求把这个大包的每一项能力都编译进来，也不是一个能替所有厂商实现 UART 的通用 HAL。NVIC 是 Cortex-M 的嵌套向量中断控制器；CMSIS-Core 把它的寄存器与操作组织成统一接口，让上层不必为每个厂商重复定义同一套内核访问方式。[Arm CMSIS 介绍](https://arm-software.github.io/CMSIS_6/latest/General/index.html)、[CMSIS-Core 概览](https://arm-software.github.io/CMSIS_6/latest/Core/index.html)可核对这两个层次。

HAL（Hardware Abstraction Layer，硬件抽象层）表示一类职责：把具体寄存器操作包装成调用接口。部分厂商把自己的底层设备驱动库命名为 DDL（Device Driver Library，设备驱动库）。Zephyr 驱动可以调用这种厂商库，也可以在树内直接访问寄存器；一个受支持目标未必依赖名字为 `hal_厂商` 的独立仓库。MPS2 的完整实现来源会在 5.3 展开，HC32 的外部 DDL 路线则在 P006 对照。

Zephyr SDK 是电脑上运行的编译工具包。它为所选架构提供编译器、链接器和相关库；它不等于 CMSIS，也不提供某块板的接线描述。安装 SDK、取得源码模块、拥有板/SoC 接入是三个需要分别成立的条件。

<a id="section-5-2-2"></a>

### 5.2.2\_module 是源码包接入 Zephyr 的契约

一个外部源码目录要被 Zephyr 当作模块，需具备可识别的入口，例如 `zephyr/module.yml`。声明给出模块名及 CMake/Kconfig 位置；构建先拿到模块根，再按入口读取这些规则。**磁盘上有一个目录，不等于它已经进入当前构建。**

CMSIS_6、hal_xhsc 和P006 将自写的 app_greeting 都可以通过模块机制接入，但它们贡献不同内容：CMSIS-Core 提供内核头，hal_xhsc 提供华大设备/外设源码，普通组件提供业务函数。模块是组织与接入方式，不能单凭“它是模块”判断它适用哪颗芯片。

west 管理多仓库的获取和版本。清单中的项目可能是模块，也可能是其他工具或资源；模块记录出现一个包，也不代表该包的每个源文件都被选入。真正选择还要结合 BOARD、Kconfig、设备树与 CMake。

<a id="section-5-2-3"></a>

### 5.2.3\_先分清复用范围，再看代码放在哪里

如果把 `drivers/` 中的文件全部叫“通用驱动”，就解释不了为什么里面有寄存器位定义；如果又把寄存器代码全部叫“MPS2 私有 HAL”，就解释不了同一份文件为什么能被另一块板复用。这里至少有四种不同的复用范围。

| 层次 | 本章实际对象 | 什么可以共享，什么随硬件改变 |
| --- | --- | --- |
| Zephyr 标准设备接口 | `include/zephyr/drivers/uart.h` 与 `uart_driver_api` | 上层统一请求发送、接收；不规定每种 UART 的寄存器布局 |
| 外设 IP 的具体驱动 | `drivers/serial/uart_cmsdk_apb.c` | 针对 CMSDK APB UART 这一种硬件接口；采用相同 IP 的系统可以复用其寄存器操作 |
| SoC 与设备实例配置 | `soc/arm/mps2`、SoC/板 DTS 中的地址、中断、时钟 | 描述这套系统有哪些硬件、外设实例接在哪里，以及 SoC 特定的初始化 |
| 板级连接与应用选择 | `boards/arm/mps2`、`chosen`、应用配置/overlay | 描述板上接线和本应用选择哪个设备，例如 console 使用 uart0 |

这里的 IP 指一种可复用的硬件设计。`uart_cmsdk_apb.c` 中的 `cmsdk_apb` 已经标明了硬件类型；它不是不区分硬件的万能 UART，也不必因为被 MPS2 使用就改名成 `uart_mps2.c`。如果两颗 SoC 集成同一种 UART，只是地址和中断号不同，共享 IP 驱动、分别提供设备配置，比复制两份收发算法更容易维护。反过来，HC32 的 USART 寄存器接口不同，不能只换地址就使用 CMSDK 驱动。

**代码放在主仓还是外部仓库，是另外一个维度。** 主仓可以收录某种 IP 的专用驱动；外部模块也可以提供多块板共享的代码。`module.yml` 解决源码怎样进入构建，不会把芯片专用接口自动变成通用接口。独立 HAL/DDL 则是另一个可选择的分层：把具体寄存器操作提取到厂商库，由 Zephyr 驱动适配调用它。

用目录看这个责任划分时，当前官方原有文件应这样对应：

```text
zephyr-main/
├── include/zephyr/drivers/uart.h     标准 UART API 与操作表约定
├── drivers/serial/uart_cmsdk_apb.c   CMSDK UART 实现与设备实例生成
├── dts/bindings/serial/              设备树属性的规则，不是驱动函数
├── soc/arm/mps2/                    MPS2 系列的 SoC 身份和接入
├── boards/arm/mps2/                 板目标、DTS 与默认配置
└── arch/arm/                        ARM 架构的启动、中断、调度等支持
```

因此，一个目录里维护很多具体硬件驱动，并不表示它们都进入每次固件；下面会逐步跟踪哪些规则选择一个源文件、哪些宏生成一个设备实例，以及这份实例如何调用它自己的操作函数。这个组织方式允许树内驱动直接访问寄存器，也允许本教程将 HC32 适配与华大 DDL 分开维护。

以上设备接口与实例分工依据 [Zephyr 设备驱动模型](https://docs.zephyrproject.org/latest/kernel/drivers/index.html)，当前仓库说明在 `doc/kernel/drivers/index.rst`，实际接口在 `include/zephyr/device.h` 和 `include/zephyr/drivers/uart.h`。模块与源码管理边界依据 [Zephyr 模块](https://docs.zephyrproject.org/latest/develop/modules.html)及 `doc/develop/modules.rst`；这些入口供复核，下面正文会把连接过程展开。

<a id="application-and-board"></a>

<a id="section-5-3"></a>

## 5.3\_在一块板上选定一个应用，并找到硬件支持

<a id="section-5-3-1"></a>

### 5.3.1\_hello\_world 说明做什么，BOARD 说明在哪里运行

先在 VS Code 打开官方原有 `G:/zephyr_practice/zephyr-main/samples/hello_world`，只读看 `CMakeLists.txt`、`prj.conf` 和 `src/main.c`。应用提供业务逻辑，以及它希望启用的 Zephyr 功能；它不因为目录里有 `main.c` 就自动知道目标芯片的启动方式、内存地址和串口寄存器。

`BOARD=mps2/an386` 是另一项输入。`mps2` 是板名，`an386` 是该板的目标限定。它选择已有板/SoC 支持，进而决定 CPU 架构、硬件描述和相关驱动。**应用目录不是板目录；hello_world 也不是 mps2 的别名。** 同一应用可以面向多个受支持的板构建，每种组合应有自己的构建目录。

```mermaid
flowchart LR
    A["应用：hello_world\n业务代码与功能配置"] --> B["一次具体构建"]
    T["BOARD：mps2/an386\n板、SoC、架构和硬件描述"] --> B
    M["所需源码模块\n本例包含 CMSIS_6"] --> B
    S["SDK\n提供目标编译器和库"] --> B
    B --> O["独立构建目录\n配置记录、编译命令、ELF"]
```

图中四项输入解决不同问题。更换应用会改变业务源文件，更换 BOARD 会改变硬件相关选择，更换组件会改变可用代码与配置，更换 SDK 则改变构建使用的工具。不要用其中一项替代另一项。

<a id="section-5-3-2"></a>

### 5.3.2\_如何把应用选为编译主线

Zephyr 源码根包含很多应用，编译时并不会把整个 `samples` 都加入。命令中的应用路径决定 CMake 从哪一个 `CMakeLists.txt` 进入；这个文件再用 `target_sources(app ...)` 指定本应用的源文件。官方 hello_world 的入口完整功能内容是：

```cmake
# 官方已有 samples/hello_world/CMakeLists.txt，只读理解。
cmake_minimum_required(VERSION 3.28.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(hello_world)
target_sources(app PRIVATE src/main.c)
```

因此 `src/main.c` 是此应用的业务起点；`prj.conf` 给应用功能赋值，当前 hello_world 的该文件只有注释，说明它接受板和系统的默认配置。应用还可以有 overlay 修改本应用使用的设备树设置；这是可选项，hello_world 并不要求为打印一行字额外创建 overlay。板默认 DTS 和应用 overlay 不能混为一个文件。

| 要选择什么 | west 写法 | 原生 CMake 写法 | 输入交给谁 |
| --- | --- | --- | --- |
| 应用根 | `west build ... samples/hello_world` | `cmake -S samples/hello_world` | CMake 读取此目录的应用入口 |
| 目标板 | `-b mps2/an386` | `-DBOARD=mps2/an386` | Zephyr 板/硬件模型读取并带出 SoC/架构 |
| 生成目录 | `-d build/learning-tools/p006/hello_world` | `-B build/learning-tools/p006/hello_world-cmake` | CMake/Ninja 保存此次配置与产物 |
| 应用功能 | 默认应用 `prj.conf`，或 `--` 后的相关 CMake 变量 | `CONF_FILE` / `EXTRA_CONF_FILE` 等 | Kconfig 合并配置；不是在终端直接编译某个 CONFIG |
| 应用硬件调整 | 默认应用 overlay 或 `-- -DDTC_OVERLAY_FILE=...` | `-DDTC_OVERLAY_FILE=...` | DTS 合并流程；只在应用确有需求时指定 |

认识上从架构到应用逐层展开，操作上通常先选 BOARD 和应用。不要同时随意给 Cortex-M3 架构、AN386 系统和另一块板拼接参数；BOARD 支持文件应提供内部一致的硬件组合。

同板换应用，例如本章后面从 `samples/hello_world` 换成 `G:/zephyr_practice/applications/component_hello`，输出改为 `build/learning-tools/p006/component_hello`；同应用换板，例如从 AN386 改为同样受支持的 AN385，输出应另设 `build/learning-tools/p006/hello_world-an385`。三次都是独立组合，不复用同一个缓存目录。此处只解释组合，后面的实验会实际执行前两项。

<a id="section-5-3-3"></a>

### 5.3.3\_沿用官方应用，明确本教程选择 AN386

官方 MPS2 Armv7-M 板文档的 hello_world 示例使用 **`mps2/an385`**。同一文档把 AN385、AN386 和 AN500 都列为受支持目标。本教程保留官方 `samples/hello_world` 应用，另外选择 AN386 来和 Cortex-M4 的 HC32 主线作对照；下面这条 AN386 命令是本教程组合，不冒充官网原样命令。

先运行 [check-baseline-inputs.txt](commands/P005_Windows/check-baseline-inputs.txt)，确认 west 根是 `G:/zephyr_practice`，清单仓库是 `zephyr-main`，CMSIS_6 关键文件存在，板列表包含 mps2 的 an386 目标。若缺少输入，先回到对应环境章节；这时创建应用组件不能修好 SDK 或缺失的 CMSIS。

以下命令使用官方应用，保留 west 默认模块发现，并生成可反查的编译数据库。SDK 已可自动发现时不必再传安装路径。完整命令见 [build-baseline-west.txt](commands/P005_Windows/build-baseline-west.txt)。

完整操作：[打开 TXT](commands/P005_Windows/build-baseline-west.txt)。

```bash
# P005 5.3.3：用 west 构建官方 hello_world 与 MPS2/AN386
# 按正文前提选择本操作，不批量执行整个目录。
# Windows UCRT64；官方hello_world + mps2/an386，先建立可解释的基线。
# 前提：check-baseline-inputs.txt 核对通过，SDK已可自动发现。仅构建，不烧录。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
export ZEPHYR_BASE='G:/zephyr_practice/zephyr-main'
west build -b mps2/an386 samples/hello_world \
  -d build/learning-tools/p006/hello_world \
  -- -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
# SDK查找失败时，按P003补发现或在--后增加具体SDK根参数；不继续创建组件掩盖错误。
```

`-b` 选择板目标，后面的目录选择应用，`-d` 指定生成文件保存位置。`--` 前是 west 参数；后面的 `-D` 交给 CMake，要求它记录每个源文件的编译命令。更细的 CMake/目标模型在 P007、Zephyr 应用构建在 P008、west 操作在 P009 展开，本章先把同一完整命令连接到产物。

成功后应有 `build/learning-tools/p006/hello_world/zephyr/zephyr.elf`、`compile_commands.json` 和 `zephyr_modules.txt`。如果 SDK 查找失败，返回 P003 检查默认发现，或在 `--` 后追加 `-DZEPHYR_SDK_INSTALL_DIR=G:/zephyr_practice/zephyr-sdk-1.0.1` 固定具体 SDK 根。不要改成某个编译器的 bin 目录，也不要为修 SDK 去替换模块清单。

若要看与 west 对应的原生入口，在同一已激活环境、同一 Zephyr 源码根执行下列可选命令。它仍保留当前工作区的模块发现；直接调用 CMake 不等于禁止使用现有 west 信息。完全手管模块列表的例子在 6.7.11。

完整操作：[打开 TXT](commands/P005_Windows/build-baseline-cmake.txt)。

```bash
# P005 5.3.3：官方 MPS2 baseline 的直接 CMake 分支
# 按正文前提选择本操作，不批量执行整个目录。
# 可选；Windows UCRT64；SDK/CMSIS/venv已准备，使用当前west默认模块发现。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
export ZEPHYR_BASE='G:/zephyr_practice/zephyr-main'
cmake -S samples/hello_world \
  -B build/learning-tools/p006/hello_world-cmake -G Ninja \
  -DBOARD=mps2/an386 -DCMAKE_EXPORT_COMPILE_COMMANDS=ON && \
cmake --build build/learning-tools/p006/hello_world-cmake
```

这里 `-S` 选应用，不选 SDK 或模块目录；`-B` 选生成目录。`ZEPHYR_BASE`/`find_package(Zephyr)` 才负责找到 Zephyr 源码。含终端激活与目录步骤的完整附件为 [build-baseline-cmake.txt](commands/P005_Windows/build-baseline-cmake.txt)。把下载仓库根、应用根、模块根和构建目录分清以后，“在这块板上编译哪个应用”就有唯一且可检查的入口。


<a id="section-5-3-4"></a>

### 5.3.4\_先跟着名字找到硬件身份

`mps2/an386` 先在 `boards/arm/mps2/board.yml` 中找到板与 SoC 组合。`Kconfig.mps2` 为这个目标选择 `SOC_AN386`；`soc/arm/mps2/Kconfig.soc` 把它放入 MPS2 系列，`soc/arm/mps2/Kconfig` 再选 ARM 架构、Cortex-M4 及相关 CPU 能力。后续规则据此选择架构实现和编译器目标参数。

这不是让读者按图新建同名文件。下面所有路径都是当前 Zephyr **官方原有文件，只读查看**。真正新增硬件文件的流程在 P012。

```mermaid
flowchart TD
    B["BOARD=mps2/an386"] --> Y["board.yml：板与SoC身份"]
    Y --> K["Kconfig.mps2：SOC_AN386"]
    K --> S["soc/arm/mps2：ARM / Cortex-M4"]
    S --> A["arch/arm：启动、中断、线程切换"]
    B --> D["mps2_an386.dts + mps2_base.dtsi"]
    D --> H["内存、外设、console指向uart0"]
    H --> R["Kconfig + CMake选择CMSDK串口驱动"]
    A --> C["编译命令与目标文件"]
    R --> C
    U["应用 main.c 与 prj.conf"] --> C
```

图表示选择关系，不表示每个文件是独立进程。实际 CMake 中 `zephyr_default.cmake` 按顺序加载模块、板、硬件模型、DTS、Kconfig、架构和 SoC 规则；DTS 和 Kconfig 也相互提供配置依据，不能把它们理解成各自孤立的一遍文件扫描。

<a id="section-5-3-5"></a>

### 5.3.5\_从 console 的硬件描述，一直追到驱动调用

<a id="section-5-3-5-1"></a>

#### 5.3.5.1\_相同外设实现，怎样使用不同系统的配置

`mps2_an386.dts` 包含 `mps2_base.dtsi`。后者已经说明 console 使用 uart0、UART 寄存器在 `0x40004000`，当前波特率为 115200。下面是官方原有文件的相关摘录，只读理解，不新建或替换：

```devicetree
/* 只读：boards/arm/mps2/mps2_base.dtsi，省去无关节点。 */
chosen {
    zephyr,console = &uart0;
};
uart0: uart@40004000 {
    compatible = "arm,cmsdk-uart";
    reg = <0x40004000 0x1000>;
    interrupts = <1 3 0 3>;
    interrupt-names = "tx", "rx";
    clocks = <&sysclk>;
    current-speed = <115200>;
};
```

`compatible` 描述要匹配的硬件接口，`reg` 提供寄存器地址与范围；不是给驱动源文件随意起一个名字。当前绑定为 `dts/bindings/serial/arm,cmsdk-uart.yaml`，串口驱动声明 `DT_DRV_COMPAT arm_cmsdk_uart`，二者对应同一种硬件。

把它与当前官方原有 `boards/arm/mps3/mps3_common_soc_peripheral.dtsi` 对照，可以看到另一套系统也使用相同的 compatible。这里只读比较，不切换本章构建目标：

| UART0 所属平台描述 | compatible | 基地址 | TX / RX 中断号 |
| --- | --- | --- | --- |
| MPS2 的 `mps2_base.dtsi` | `arm,cmsdk-uart` | `0x40004000` | 1 / 0 |
| MPS3 的 `mps3_common_soc_peripheral.dtsi` | `arm,cmsdk-uart` | `0x09303000` | 34 / 33 |

两个节点提供不同的地址和 IRQ，驱动复用 CMSDK UART 的寄存器布局与收发算法。所谓“为当前板服务”，发生在 **配置不同设备实例** 这一步，不是把共享驱动文件重新复制成一份板专属源码。设备树中的 `interrupts = <1 3 0 3>` 按中断控制器的 cells 定义分别表达中断号和优先级；不能把四个数字全当成四条中断。

设备树由此减少板级地址、中断、时钟和连接关系在 C 文件中的硬编码。它不能生成“哪个状态位表示发送可用”“如何清除中断”“何时写哪个寄存器”等硬件算法；这些仍要由具体 IP 驱动或独立 HAL/DDL 提供。如果新硬件的寄存器语义不同，必须提供对应实现，不能靠改 `compatible` 的文字冒充兼容。

<a id="section-5-3-5-2"></a>

#### 5.3.5.2\_Kconfig 文件怎样进入配置体系

知道磁盘上有一个 `Kconfig.cmsdk_apb` 还不够：Kconfig 不会因为它位于 `drivers/serial/` 就自动读取所有文件。本例由明确的包含关系接入。下面是当前官方原文件中的相关语句，只读对照；注释标明每一句所在文件：

```kconfig
# Zephyr 根 Kconfig
source "Kconfig.zephyr"
# Kconfig.zephyr
source "drivers/Kconfig"
# drivers/Kconfig
source "drivers/serial/Kconfig"
# drivers/serial/Kconfig
rsource "Kconfig.cmsdk_apb"
```

`source` 的相对路径按这套配置的源根解析，`rsource` 则相对当前 Kconfig 文件的位置解析，所以最后一句指向 `drivers/serial/Kconfig.cmsdk_apb`。Zephyr 的 Kconfig 扩展允许包含路径写 glob，但**此处 serial 文件逐项使用 rsource，并不是 `Kconfig.*` 自动扫描**。如果自己新增一个配置文件，必须把它接入父文件或模块入口；文件名看起来像 Kconfig 不会使它自动生效。`drivers/serial/Kconfig` 又把具体驱动定义放在 `if SERIAL` 范围中，意味着整体串口支持也是它们的前提。

随后读取 CMSDK 驱动的完整配置项：

```kconfig
# 只读：drivers/serial/Kconfig.cmsdk_apb
config UART_CMSDK_APB
    bool "ARM CMSDK APB UART driver"
    default y
    depends on DT_HAS_ARM_CMSDK_UART_ENABLED
    select SERIAL_HAS_DRIVER
    select SERIAL_SUPPORT_INTERRUPT
    select PINCTRL
    help
      This option enables the UART driver for ARM CMSDK APB UART.
```

`config UART_CMSDK_APB` **定义**一个名为 `UART_CMSDK_APB` 的符号，此处没有 `CONFIG_` 前缀。`bool` 表示取 y/n；`default y` 表示条件满足且没有其他有效选择时默认开启，不等于无条件编译。`depends on` 要求最终设备树中存在启用的 CMSDK UART；父级 `if SERIAL` 同样构成依赖。`select` 则声明此驱动需要的串口能力和 PINCTRL。这里选择“支持中断的能力”与是否启用完整 `UART_INTERRUPT_DRIVEN` 功能仍是两个符号，不能混成同一开关。

那么 `DT_HAS_ARM_CMSDK_UART_ENABLED` 是谁定义的？DTS 配置阶段调用 `scripts/dts/gen_driver_kconfig_dts.py`，根据已发现的 bindings 生成本次构建的 `Kconfig/Kconfig.dts`。其中为这个 compatible 写出：

```kconfig
# 只读：构建目录 Kconfig/Kconfig.dts 中的生成片段，不手工创建。
DT_COMPAT_ARM_CMSDK_UART := arm,cmsdk-uart

config DT_HAS_ARM_CMSDK_UART_ENABLED
    def_bool $(dt_compat_enabled,$(DT_COMPAT_ARM_CMSDK_UART))
```

`Kconfig.zephyr` 先包含 `dts/Kconfig`，后者再包含这份生成文件；`dt_compat_enabled` 查询本次解析后的设备树是否有启用的匹配节点。因此这个符号来自 **binding 生成的定义 + 当前 DTS 的实际状态**，不是要求读者在 `prj.conf` 中凭空手写的芯片开关。

接下来要区分几类经常被都叫作“配置”的文件。名字中都有 config，不表示它们由同一规则读取：

| 实际文件 | 内容属于什么 | 当前 AN386 例子 |
| --- | --- | --- |
| `drivers/serial/Kconfig.cmsdk_apb` 等 Kconfig 文件 | 符号定义、类型、提示、默认值、依赖 | 定义 `UART_CMSDK_APB`，要求启用的 CMSDK UART 节点 |
| `boards/arm/mps2/Kconfig.defconfig` | 给已有符号增加带条件的默认值，仍是 Kconfig 定义语法 | MPS2/AN386 且 SERIAL 生效时，为 `UART_INTERRUPT_DRIVEN` 提供 `default y` |
| `boards/arm/mps2/mps2_an386_defconfig` | 这块板目标的初始赋值片段，使用 `CONFIG_名字=值` | 写出 `CONFIG_SERIAL=y`、`CONFIG_CONSOLE=y`、`CONFIG_UART_CONSOLE=y` |
| `samples/hello_world/prj.conf` | 这个应用的需求赋值片段，同样使用 `CONFIG_名字=值` | 当前文件只有注释，使用板与系统已有选择；其他应用可以提出不同需求 |

`Kconfig.defconfig` 与 `xxx_defconfig` 不是两种拼写风格。前者通过 Kconfig 的 source 链加载。例如板的文件实际写的是 `config UART_INTERRUPT_DRIVEN` 下的 `default y`；它不是给应用写一条强制赋值。`Kconfig.zephyr` 先包含 shield、板、SoC 等默认规则，再包含一般定义；同一个符号合并了多处定义后，按顺序选择第一个条件满足的默认值。因此讨论 **默认规则** 时，不能套用简单的“最后一行覆盖前面”。

后者是 **赋值输入**：板目标识别以后，`cmake/modules/kconfig.cmake` 用 `zephyr_file(... DEFCONFIG BOARD_DEFCONFIG)` 找到所选板目标的 `_defconfig` 文件，再组织传给配置脚本的片段。对本章没有 shield、额外配置或命令行 Kconfig 赋值的 baseline，顺序就是：

```text
Kconfig 定义与默认规则已经可用
        ↓ 读取赋值片段
mps2_an386_defconfig → hello_world/prj.conf
        ↓ 结合依赖等规则求最终值
zephyr/.config + zephyr/include/generated/zephyr/autoconf.h
```

若像本章组件关闭实验那样提供 `EXTRA_CONF_FILE=off.conf`，附加片段在应用配置之后读取；对允许用户赋值的同一符号，后面的赋值可以覆盖前面片段的请求。当前 `merge_config_files` 的完整顺序还包含板修订/扩展、shield、额外命令行选项和构建目录附加片段，不能把上面的最小例子说成所有工程只有两个文件。默认 `prj.conf` 可由 `CONF_FILE` 换成其他应用片段，所以它也不是任何工程都无法改变的固定文件名。

配置脚本是 `scripts/kconfig/kconfig.py`：它先加载第一个赋值文件，再对后续文件调用 `load_config(..., replace=False)` 合并，最后结合符号的类型、可见性和依赖计算结果。文件被读入不保证每个请求都能成立。**赋值文件不是符号定义文件**；依赖不满足时，强写 `CONFIG_UART_CMSDK_APB=y` 也不能把不存在的硬件和驱动能力变出来，应检查告警及最终 `.config`。

当前 baseline 的 `build_info.yml` 中可看到 `mps2_an386_defconfig`、`hello_world/prj.conf` 的实际输入顺序；`zephyr/kconfig/sources.txt` 则记录加载过哪些 Kconfig 定义文件。结果 `.config` 中有 `CONFIG_UART_CMSDK_APB=y`，生成头中有 `#define CONFIG_UART_CMSDK_APB 1`；`UART_INTERRUPT_DRIVEN` 也为开启，能追溯到板的条件默认规则。已有构建目录可能复用上次 `.config`，因此换板或应用时本章一直要求独立输出；不要手改生成头，把结果文件冒充长期配置入口。

这条配置包含与赋值规则依据 [Kconfig 扩展](https://docs.zephyrproject.org/latest/build/kconfig/extensions.html)和 [设置 Kconfig 值](https://docs.zephyrproject.org/latest/build/kconfig/setting.html)；本地对应 `doc/build/kconfig/extensions.rst`、`setting.rst`，上述包含文件、生成脚本和 `scripts/kconfig/kconfigfunctions.py` 中 `dt_compat_enabled` 是当前实现。

<a id="section-5-3-5-3"></a>

#### 5.3.5.3\_CMake 选源文件，预处理器再选择文件内部功能

Kconfig 的结果供两个使用方读取。第一条是 **CMake 选源**：`cmake/modules/kconfig.cmake` 通过 `import_kconfig(... ${DOTCONFIG})` 把最终 `.config` 导入为 `CONFIG_*` CMake 变量。Zephyr 主 CMake 进入 `drivers`；父目录再按 `CONFIG_SERIAL` 进入 `serial`，由该目录建立库并选择文件：

```cmake
# 只读：以下语句分属三个官方原文件，不写入应用。
# Zephyr 主 CMakeLists.txt
add_subdirectory(drivers)
# drivers/CMakeLists.txt
add_subdirectory_ifdef(CONFIG_SERIAL serial)
# drivers/serial/CMakeLists.txt
zephyr_library()
zephyr_library_sources_ifdef(CONFIG_UART_CMSDK_APB uart_cmsdk_apb.c)
```

`zephyr_library_sources_ifdef` 是 `cmake/modules/extensions.cmake` 提供的 CMake 函数：条件为真才把 `.c` 加入当前库。它不是 C 语言的 `#ifdef`，也不是扫描所有 C 文件后再指望链接器删掉不需要的驱动。因此仓库可以维护多个 UART IP 驱动，本次固件只编译满足构建规则的那些文件。

第二条是 **C 预处理**：当前 GCC 路线的编译命令包含 `-imacros .../zephyr/autoconf.h`。这个参数由 Zephyr 主 `CMakeLists.txt` 的 `zephyr_compile_options` 加入，GCC 的 imacros 属性定义在 `cmake/compiler/gcc/compiler_flags.cmake`。它先让生成头中的宏参与预处理，所以驱动即使没有手写 `#include <...autoconf.h>`，也能使用 `CONFIG_*`。

例如 `uart_cmsdk_apb.c` 内部有：

```c
/* 只读源码片段：文件已经被 CMake 选入，才会走到这些条件。 */
#ifdef CONFIG_UART_INTERRUPT_DRIVEN
    /* 中断相关数据、函数、操作表成员按各自所在位置保留。 */
#endif
```

开启时生成头定义此宏，相应代码参加编译；关闭时这些条件块被排除，轮询收发实现仍可以保留。**CMake 是否加入整个文件，与 C 预处理是否保留文件内的一部分，是两道不同的选择。** 修改驱动内的宏不能补救源文件根本没进入 CMake 的问题；只把 `.c` 编进去也不保证全部 API 都被启用。

<a id="section-5-3-5-4"></a>

#### 5.3.5.4\_设备树宏怎样生成当前 UART 的设备实例

驱动开头在相关头文件之前声明：

```c
/* 只读：uart_cmsdk_apb.c 中的本地硬件身份。 */
#define DT_DRV_COMPAT arm_cmsdk_uart
```

这里 `arm,cmsdk-uart` 转换成可用的 C 标识符 `arm_cmsdk_uart`，逗号、连字符改成下划线。`DT_DRV_COMPAT` 是当前源文件的宏，告诉后面的 `DT_INST_*` 要处理哪种 compatible 的实例；它不是 Kconfig 配置项，也不需要读者在终端写 `-DDT_DRV_COMPAT=...`。

DTS 构建生成 `zephyr/include/generated/zephyr/devicetree_generated.h`；`include/zephyr/devicetree.h` 包含它，并提供 `DT_DRV_INST`、`DT_INST_REG_ADDR` 等访问宏。于是源码中的宏最终能展开成当前板的常量和节点标识，而不是运行时再去打开 `.dts` 文件。

当前驱动末尾定义 `CMSDK_UART_INIT(n)`，再执行 `DT_INST_FOREACH_STATUS_OKAY(CMSDK_UART_INIT)`。后者为本种 compatible 下每个启用的节点展开一次；`n` 是这种驱动的实例索引，不能把它固定理解成板标签 `uart0` 的数字 0。每次展开主要生成如下对象：

| 生成对象 | 源码中的名字或字段 | 从哪里取值、用来做什么 |
| --- | --- | --- |
| 只读硬件配置 | `uart_cmsdk_apb_dev_cfg_##n` | `.uart = DT_INST_REG_ADDR(n)` 取得寄存器基地址；时钟来自 phandle，pinctrl 引用对应引脚配置 |
| 运行数据 | `uart_cmsdk_apb_dev_data_##n` | 初始波特率由 `DT_INST_PROP(n, current_speed)` 给出，保存回调等可变状态 |
| 中断接入函数 | `uart_cmsdk_apb_irq_config_func_##n` | 开启中断功能时，用 `DT_INST_IRQ_BY_NAME` 取得 tx/rx IRQ，交给 `IRQ_CONNECT` 和 `irq_enable` |
| 标准操作表 | 共享的 `uart_cmsdk_apb_driver_api` | 同种 IP 的实例共享收发函数，函数通过传入的 `dev` 区分当前实例 |
| 设备对象与初始化记录 | `DEVICE_DT_INST_DEFINE(...)` | 将本实例的 config、data、初始化函数与操作表关联，并指定初始化等级/优先级 |

下面两段是驱动原有片段的只读摘录，不是让读者粘贴创建另一个驱动；`##n` 的写法来自原来的宏定义：

```c
/* 只读：操作表中的两个成员；其他已支持成员省略。 */
static DEVICE_API(uart, uart_cmsdk_apb_driver_api) = {
    .poll_in = uart_cmsdk_apb_poll_in,
    .poll_out = uart_cmsdk_apb_poll_out,
};

/* 只读：CMSDK_UART_INIT(n) 宏内的设备定义调用，重排换行。 */
DEVICE_DT_INST_DEFINE(n, uart_cmsdk_apb_init, NULL,
                     &uart_cmsdk_apb_dev_data_##n,
                     &uart_cmsdk_apb_dev_cfg_##n,
                     PRE_KERNEL_1, CONFIG_SERIAL_INIT_PRIORITY,
                     &uart_cmsdk_apb_driver_api);
```

这就是“共享代码怎样配上当前板的硬件配置”的关键连接。`struct device` 保存 `config`、`data`、`api` 等指针；这里 config 指向某一个实际 UART 的地址与时钟，api 指向共享的 CMSDK 操作表。固件启动时按初始化记录调用 `uart_cmsdk_apb_init(dev)`，它通过这个 `dev` 取回本实例配置，而不是在函数里猜当前是哪块板。

这些定义会随驱动一起编译、链接进入固件。`DEVICE_API(uart, ...)` 不只给一个结构体取名，还把操作表放入 UART 对应的链接区域；设备定义保存对该表和配置对象的引用，初始化记录也由链接规则组织。表中的函数指针已经引用实际实现，不能因为业务 `main()` 没有直接写出函数名，就断言这些函数会自动被链接器删除。按功能关闭不需要的 API，仍要使用上节解释的配置和条件编译机制。

**生成设备实例与选择源文件仍不是一回事。** CMake 先决定是否编译这份驱动，`DT_INST_FOREACH_STATUS_OKAY` 再决定这份驱动针对当前硬件生成哪些实例。驱动没有选择、节点未启用或依赖不满足时，仅有 `DEVICE_DT_GET` 的上层引用不能替它创建实例。

<a id="section-5-3-5-5"></a>

#### 5.3.5.5\_标准 API 怎样进入本实例的寄存器实现

现在回到 hello_world 的输出。`drivers/console/uart_console.c` 使用 `DEVICE_DT_GET(DT_CHOSEN(zephyr_console))` 取得 chosen 节点对应的设备指针；该指针关联前面生成的 UART 实例。控制台再调用标准接口 `uart_poll_out(dev, c)`。当前 `include/zephyr/drivers/uart/uart_internal.h` 中，实际分派只有一个关键动作：

```c
/* 只读：标准 UART 接口内部的分派，不含任何具体 UART 寄存器地址。 */
static inline void z_impl_uart_poll_out(const struct device *dev, unsigned char out_char)
{
    DEVICE_API_GET(uart, dev)->poll_out(dev, out_char);
}
```

操作表的 `.poll_out` 在上节已指向 `uart_cmsdk_apb_poll_out`。该函数用 `dev->config` 取得当前实例的基地址，然后等待发送状态位、写数据寄存器：

```c
/* 只读：uart_cmsdk_apb_poll_out 中的实际硬件访问。 */
const struct uart_cmsdk_apb_config *dev_cfg = dev->config;
while (dev_cfg->uart->state & UART_TX_BF) {
    ; /* 等待发送缓冲区可用。 */
}
dev_cfg->uart->data = (uint32_t)c;
```

`uart_cmsdk_apb` 寄存器结构也定义在这个驱动文件中：`data` 位于偏移 `0x000`，`state` 位于 `0x004`，`ctrl` 位于 `0x008`。MPS2 实例配置中的基地址为 `0x40004000`，所以写 `data` 就是写该地址；换成前面的 MPS3 实例，相同函数使用另一份 config 中的基地址。变化的是实例数据，IP 的寄存器偏移和访问算法保持不变。

```mermaid
flowchart TD
    T["板/SoC DTS：compatible、reg、IRQ、clock"] --> G["构建时生成设备树宏"]
    G --> D["设备实例：config / data / init / api"]
    C["chosen：本应用 console 使用哪个节点"] --> P["console 取得对应设备指针"]
    P --> U["标准 uart_poll_out(dev, c)"]
    D --> U
    U --> A["通过 dev 的操作表调用 poll_out"]
    A --> F["CMSDK 函数读取 dev.config"]
    F --> R["基地址 + IP 寄存器偏移：访问硬件"]
```

这条链已经具备设备树描述、标准驱动接口和具体设备实例；它没有再向下调用独立厂商 HAL。此处是静态构建出的实例，不能套用 Linux 在运行时解析 DTB、匹配后调用 `probe()` 的完整过程。设备模型负责统一接入；是否额外拆出裸机库，是另一个设计选择。

同时，共享 IP 驱动不意味着实现完全没有 SoC 特例。当前文件的初始化函数确有 `CONFIG_SOC_SERIES_BEETLE` 条件下的时钟处理，外围时钟与 pinctrl 仍需平台接入。判断是否应继续拆分，要看这些差异能否用已有子系统接口和实例配置表达，以及硬件行为是否相同；不能仅凭文件放在 `drivers/serial` 就断言完全通用，也不能因为有直接寄存器访问就断言没有设备模型。

上述实例和分派机制的文档入口为 [设备驱动模型](https://docs.zephyrproject.org/latest/kernel/drivers/index.html)与 [设备树 API 的 Linux 对照](https://docs.zephyrproject.org/latest/build/dts/api-usage.html)。当前实现分别在 `doc/kernel/drivers/index.rst`、`doc/build/dts/api-usage.rst`、`include/zephyr/device.h`、`include/zephyr/devicetree.h` 和前面逐项解释的 UART 文件中。

<a id="section-5-3-6"></a>

### 5.3.6\_MPS2 的硬件支持已经在哪里实现

MPS2 有自己的硬件支持体系。按前面的分层，**本例的 CMSDK UART 寄存器定义与底层操作没有再剥离成一套独立的厂商 HAL/DDL 库，它们与 Zephyr 接口适配一起位于 `drivers/serial/uart_cmsdk_apb.c`。** 独立厂商库没有加入此依赖链，不表示设备树和标准设备模型缺失；上一节已逐步说明它们怎样接到真实寄存器。

因此本例应登记为“外设底层实现：Zephyr 树内 IP 驱动；独立 MPS2 HAL/DDL 包：本次构建未使用”。不要把整个 `boards + soc + arch + drivers` 笼统改称一个厂商 HAL 包，它们承担的是不同层的硬件支持。启动、中断和线程上下文还有 Zephyr 架构代码参与，不能只看有没有 `hal_mps2` 目录就判断支持是否存在。

Arm Keil 也确实提供独立的 **V2M-MPS2_CMx_BSP**。官方 Pack 页面在本次核对时列出 `Keil::V2M-MPS2_CMx_BSP@1.8.2`，包含板支持与设备支持；官方板页面还列出 USART 驱动和示例。所以本章的结论不是“Arm 没有给 MPS2 提供库”，而是：**当前 Zephyr 的 `mps2/an386` 接入采用了下面这套实现，本次依赖链未直接使用该 BSP Pack。** 其他 IDE、裸机示例或 CMSIS 工程可能选择它，不能把它们的依赖直接套到本次 Zephyr 构建。[Arm Keil Pack](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil/boards/)、[Arm V2M-MPS2 板与示例](https://www.keil.com/boards2/arm/v2m_mps2/)是查找入口，不是本章新增下载步骤。

上一节 UART 的例子说明了一项外设怎样连接。下面把范围扩展到整个板目标，避免只看到串口就以为启动、时钟、GPIO 或中断支持尚未提供。

| 硬件支持职责 | 已有位置与作用 | 选择依据与本次使用范围 |
| --- | --- | --- |
| 板资源、内存与时钟描述 | `boards/arm/mps2/mps2_base.dtsi`：Flash、SRAM、25 MHz fixed-clock、外设与 console | BOARD 加载 DTS；内存描述供链接布局使用，时钟节点提供外设时钟频率 |
| SoC 身份和共用接入 | `soc/arm/mps2`：SoC/CPU选择、`soc.h`、`soc_registers.h`、共用 `soc.c` | 系列 CMake 进入 mps2；AN386 选 Cortex-M4。共用文件包含其他变体辅助函数，不能推断每个函数都运行 |
| 复位、向量和线程上下文 | `arch/arm/core/cortex_m`：`reset.S`、`vector_table.S`、`thread.c` 等 | Cortex-M 架构条件选入；这些是系统启动与调度所需支持 |
| NVIC 中断接口 | `arch/arm/core/cortex_m/irq_manage.c` 配合外部 CMSIS 内核头 | Zephyr 中断函数调用 `NVIC_EnableIRQ()`、`NVIC_SetPriority()` 等接口访问内核中断控制器 |
| CMSIS 内核寄存器与接口定义 | 外部 `modules/hal/cmsis_6/CMSIS/Core/Include` | Cortex-M 模块接入添加头目录，MPS2 `soc.h` 经兼容头最终包含 `core_cm4.h` |
| 系统节拍 | `drivers/timer/cortex_m_systick.c` | `CONFIG_CORTEX_M_SYSTICK=y` 使驱动 CMake 选入，用于内核计时 |
| console 和 UART | `drivers/console/uart_console.c`、`drivers/serial/uart_cmsdk_apb.c` | 默认配置与 DTS 选中驱动，hello_world 通过 console 输出问候 |
| CMSDK GPIO 与板载 MMIO GPIO | `drivers/gpio/gpio_cmsdk_ahb.c`、`gpio_mmio32.c` | 板默认开启 GPIO，对应 DTS 节点及 Kconfig 选入；文件被编译不代表 hello_world 业务调用了 GPIO |
| 引脚复用 | `drivers/pinctrl/pinctrl_arm_mps2.c` 与 `drivers/pinctrl/common.c` | UART 驱动选择 PINCTRL，匹配 MPS2 pinctrl 节点后选入 |
| 其他板描述中的外设 | `drivers/counter/` 中 CMSDK timer、`drivers/watchdog/wdt_cmsdk_apb.c`，以及相应 I²C/以太网驱动 | 是否进入某次固件还要看功能配置、节点状态与实际编译；本章不把板支持范围当成全部已启用或运行验证 |

例如内核希望开启一个外部中断时，先经过 Zephyr 的架构中断管理代码，再调用 CMSIS 的 NVIC 接口，最终写 Cortex-M 的中断控制寄存器。系统节拍则由 Zephyr 的 Cortex-M SysTick 驱动管理。这里 CMSIS 提供内核接口，Zephyr 提供系统如何使用这些接口的策略；不需要重复引入另一套启动与中断管理代码来替换它们。

内存和时钟也不是空白：当前板描述给出 `0x00000000` 起始的 4 MiB Flash 区和 `0x20000000` 起始的 4 MiB SRAM 区，并给 UART 等外设引用的 `sysclk` 声明 25 MHz 固定频率。这些是当前 AN386 板目标的输入，不能改写成所有 MPS2 FPGA 配置或所有实际晶振都相同。此处也没有证据表明 `soc.c` 承担 AN386 的 PLL 配置，不能照搬其他 MCU 的“先跑厂商 SystemInit 配时钟”叙述。

GPIO 不是遗漏的一份 DDL：`gpio_cmsdk_ahb.c` 也从设备树取得寄存器地址，在自己的接口实现里读写端口寄存器；`gpio_mmio32.c` 处理对应的通用 MMIO GPIO。当前 hello_world 的默认板配置已打开 GPIO，因此两份 GPIO 源文件可出现在编译数据库中，但应用 `main()` 没有因此自动开始闪灯或读取按键。

这形成三层不同的判断：**板支持了什么、本次配置编译了什么、应用实际使用并验证了什么。** 官方板文档可用来确认支持范围；`.config`、最终 DTS 和编译数据库说明本次选择；运行观察才能说明行为。模块记录同样不能证明每个模块都提供了运行时代码。下面继续用本次构建记录确认，而不是要求读者凭目录名猜测。

这里的 **CMSDK** 是板上相应 Arm 外设接口的名称，**CMSIS** 是本例使用的 Arm 内核接口源码，**Zephyr SDK** 是电脑上的编译工具包，三者不能因拼写相近混为一个下载对象。

依据路径为 `boards/arm/mps2/mps2_base.dtsi`、`drivers/serial/Kconfig.cmsdk_apb`、`drivers/serial/CMakeLists.txt`。设备树解释见 [官方 Devicetree](https://docs.zephyrproject.org/latest/build/dts/index.html)，构建阶段说明见 [CMake build system](https://docs.zephyrproject.org/latest/build/cmake/index.html)。

<a id="section-5-3-7"></a>

### 5.3.7\_反查同一次构建的记录

现在运行 [trace-baseline-build.txt](commands/P005_Windows/trace-baseline-build.txt)，它只读取 5.3.3 产生的 baseline。先看 `.config` 中的板、SoC、CPU 与串口符号，再看最终 `zephyr.dts` 中的 console 和 UART，最后在 `compile_commands.json` 找到真正的驱动源码。

应能看到 `samples/hello_world/src/main.c`、MPS2 的 `soc.c`、Cortex-M 架构源文件、`uart_console.c`、`uart_cmsdk_apb.c` 等编译记录。CMSIS_6 通过编译参数中的 `CMSIS/Core/Include` 被使用：MPS2 的 `soc.h` 引入 `cmsis_core_m_defaults.h`，Cortex-M4 条件再引入 `core_cm4.h`。并非每个依赖都必须表现为独立 `.c` 文件。

同一个源码根可以产生多个构建目录，所以一定读本次 `build/learning-tools/p006/hello_world`。以前另一个目标的 `.config` 不能证明这一次选中了相同驱动。

<a id="section-5-4"></a>

## 5.4\_从已有构建确认主仓与 CMSIS 的边界

<a id="section-5-4-1"></a>

### 5.4.1\_清单管理源码，构建记录证明使用

在 VS Code 只读打开官方原有的 `zephyr-main/west.yml`。`projects` 中每项的 `name` 是 west 使用的项目名，`revision` 固定需要的版本，`path` 是相对 west 工作区根的落盘位置。清单还可能导入其他文件，所以最终集合用解析清单的 west 命令确认：

完整操作：[打开 TXT](commands/P005_Windows/inspect-manifest-selection.txt)。

```bash
# P005 5.4.1：只读对照完整清单与 CMSIS 的实际项目身份
# Windows UCRT64；P004 工作区与 CMSIS 已就绪；不下载、不改清单。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
west list -f '{name}: {path} @ {revision}'
west list cmsis_6 -f '{name} {revision} {path} {url}'
```

本次源码 `25c8f4a23988dd3b2cfb463613622738298c2d6c` 的 `cmsis_6` 项指向 `modules/hal/cmsis_6`，修订为 `1c1840af7a7e757d6e2fec3ddb0e5ce0dfcc93c8`。目录相对 `G:/zephyr_practice`，因此源码在 `G:/zephyr_practice/modules/hal/cmsis_6`，不在 `zephyr-main/modules/hal/cmsis_6`。**west list 不是“输入 BOARD 就算出全部依赖”的包依赖求解器**，它显示当前清单管理范围；具体构建选择仍由板、配置和接入代码共同决定。

`west update cmsis_6` 能按这条清单取得所选修订；具体下载与 Git 排错回到 P004。清单也列有其他 CMSIS 项，不能只按名字相似任意替换。当前 Cortex-M 规则使用 CMSIS_6 的接入代码和头文件，是选择此项目的源码依据。

**west 管理项目不等于全部项目都编进当前固件。** 模块发现记录说明某目录可被构建系统使用；Kconfig、设备树和 CMake 还会进一步决定具体代码。CMSIS 在本例主要贡献头文件，所以编译数据库没有 CMSIS 的 `.c` 条目，也不能据此认为它未使用。

<a id="section-5-4-2"></a>

### 5.4.2\_两个 modules 目录怎样配合

`G:/zephyr_practice/zephyr-main/modules/cmsis_6` 是 **主仓里的 Zephyr 接入规则**，不是完整 Arm CMSIS 源码；真正包在工作区根的 `G:/zephyr_practice/modules/hal/cmsis_6`。前者告诉 Zephyr 如何使用包，后者提供接口头等内容。只下载主仓并看到前者目录，不能认为 CMSIS 已经取得。

外部 CMSIS 包的 `zephyr/module.yml` 声明 `name: cmsis_6`，并设置 `cmake-ext: true`、`kconfig-ext: true`。这表示使用 Zephyr 一侧提供的接入规则。主仓 `modules/cmsis_6/CMakeLists.txt` 在 Cortex-M 条件下加入 `${ZEPHYR_CURRENT_MODULE_DIR}/CMSIS/Core/Include`，因此实际头文件从外部包读取。

<a id="section-5-4-3"></a>

### 5.4.3\_换硬件时怎样判断要不要另找底层库

第一步看该板官方文档的功能与限制，确定当前想使用哪个外设；再从板 DTS 中找到对应节点的 compatible。本章查到的是 `arm,cmsdk-uart`，不是先猜一个 `hal_mps2` 仓库名。

第二步找到匹配的驱动及其 Kconfig/CMake。确认它是直接访问寄存器，还是调用厂商接口、引用 `${ZEPHYR_某模块_MODULE_DIR}` 下的源码或头文件。本章 UART 是树内直接实现；当前 Cortex-M 接入又确实引用了树外 CMSIS_6。这两种情况可以在同一次构建中并存。

第三步按发现的外部引用核对当前 `west list` 和模块声明。项目在清单中就按固定 revision 获取；不在清单中则先查来源、兼容性和 Zephyr 接口，再决定外部模块追加或维护自有清单。清单没有一个猜测出来的名称，不足以证明板缺支持；必须先确认驱动是否已经内置。

第四步配置实际应用，检查模块记录、最终 Kconfig/DTS 与编译数据库。由此得到三类结论：**树内已实现的支持直接使用；清单管理的外部依赖按清单获取；清单外需求有依据地集成。** 这比“每块芯片都先找一份 HAL/DDL”更符合实际 Zephyr 工程。

<a id="section-5-5"></a>

## 5.5\_把配置来源、选源与设备调用放回同一条链

到这里有三件事不能互相替代。源码包管理决定磁盘上有什么、从哪个版本取得；构建选择决定哪些 `.c` 和头文件参加当前固件；设备模型决定运行时一个 API 调用进入哪份设备配置和操作函数。即使驱动来自外部模块，后两件事仍然需要完成，不会因为“已经是一个独立库”就自动接上设备树。

```mermaid
flowchart TD
    M["源码位置：主仓 / west 项目 / 额外模块"] --> E["CMake、Kconfig 与硬件描述入口可用"]
    E --> K["板与应用配置 + DTS<br/>得到最终 CONFIG 值"]
    K --> C["CMake 选择驱动与必要底层库源文件"]
    K --> H["autoconf.h：C 文件内部功能裁剪"]
    E --> T["DTS 生成宏：地址、IRQ、启用实例"]
    C --> O["编译、链接为固件"]
    H --> O
    T --> D["驱动宏定义设备对象与初始化记录"]
    D --> O
    O --> I["启动：初始化选中的设备实例"]
    I --> R["调用：标准 API → 实例操作表 → 具体硬件实现"]
```

箭头上半部分在电脑构建时发生，下半部分在固件启动和运行时发生。下载 HAL 并不会执行芯片初始化；Kconfig 文件中有驱动名字并不表示它被编译；编译成功也不表示本应用实际调用过全部设备。对 MPS2，具体 UART 实现已经位于主仓；对 HC32，下一章会同时引入树外适配和所需 DDL 源码，之后仍进入相同的实例/操作表链。

下面是完整只读检查块，在 **5.3.3 baseline 已成功** 后执行。它使用本章已有的构建目录，不重新编译，也不生成新工程：

完整操作：[打开 TXT](commands/P005_Windows/check-driver-model-evidence.txt)。

```bash
# P005 5.5：只读核对 Kconfig 来源、生成宏与编译命令
# 按正文前提选择本操作，不批量执行整个目录。
# Windows UCRT64；前提：5.3.3 baseline 已产生配置与编译数据库。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
python - <<'PY'
import json
from pathlib import Path

build = Path('build/learning-tools/p006/hello_world')
for rel in ('zephyr/.config', 'zephyr/include/generated/zephyr/autoconf.h'):
    print('\n' + rel)
    for line in (build / rel).read_text(encoding='utf-8').splitlines():
        if 'CONFIG_UART_CMSDK_APB' in line or 'CONFIG_UART_INTERRUPT_DRIVEN' in line:
            print(line)
sources = (build / 'zephyr/kconfig/sources.txt').read_text(encoding='utf-8')
print('\nKconfig.cmsdk_apb 已被读取:', 'Kconfig.cmsdk_apb' in sources)
entries = json.loads((build / 'compile_commands.json').read_text(encoding='utf-8'))
for entry in entries:
    if Path(entry['file']).name == 'uart_cmsdk_apb.c':
        print('已选驱动:', entry['file'])
        print('编译命令含 -imacros:', '-imacros' in entry['command'])
        print('编译命令含 autoconf.h:', 'autoconf.h' in entry['command'])
print('设备树生成头存在:',
      (build / 'zephyr/include/generated/zephyr/devicetree_generated.h').is_file())
PY
```

本章已有 baseline 的两个 UART 符号均为开启；配置文件显示 y，生成头显示 1；配置来源记录包含 `Kconfig.cmsdk_apb`，编译数据库有该驱动且命令读取 autoconf.h，设备树生成头存在。如果第一个文件就缺失，先确认 baseline 是否成功和输出目录是否一致；如果配置为 n，不应把它当成编译器漏文件，而应回到 5.3.5.2 检查最终配置依据。该检查证明构建输入和生成记录，模拟运行结果在 P006 6.7.12 的独立记录中说明。

<a id="section-5-6"></a>

## 5.6\_带着已有模型进入 HC32 适配

在需要对照原文件时，可使用 [硬件来源只读查询](commands/P005_Windows/trace-mps2-source.txt) 和 [CMSIS 接入原文件查询](commands/P005_Windows/read-cmsis-adapter.txt)。前者对应本章 UART 硬件链，后者只读取 board/SoC/CMSIS 接入规则；它们不是下载或新增适配步骤。关键解释已经在正文展开，不需要先自行搜索才能理解。

本章选的是官方已支持目标，尚不创建 HC32 适配，也不下载华大 DDL。下一章才将相同接口换成 HC32 外设，决定厂商底层源码、Zephyr 适配和板配置各由谁维护，再把这些源码通过模块机制接入。

上一篇：[P004 CMSIS 选择与下载](P004_CMSIS选择与下载_Windows.md)；下一篇：[P006 HC32 与外部源码模块接入](P006_HC32与外部源码模块接入_Windows.md)。
