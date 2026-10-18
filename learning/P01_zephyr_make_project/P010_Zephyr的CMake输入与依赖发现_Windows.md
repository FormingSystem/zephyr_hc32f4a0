---
id: learning.zephyr.chapter-010
title: Zephyr的CMake输入与依赖发现
kind: engineering
status: maintained
slides: slides/P010_Zephyr的CMake输入与依赖发现_Windows.pptx
domains: [zephyr, cmake, tools]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 第10章\_Zephyr的CMake输入与依赖发现

前置：P007 的目标模型与 P008 的应用构建。现在从一个具体疑问继续：应用 CMakeLists 只写了 `src/main.c`，为什么编译清单还出现 `soc/arm/mps2/soc.c`、`uart_cmsdk_apb.c`，却没有华大 DDL？本章沿“文件怎样被选中”逐步读源码，最后回到生成结果核对。

SDK、CMSIS 和 HC32 DDL 下载分别回到 P003、P004、P006；缓存与排错继续 P011。这里先分开三件事：文件在磁盘上、模块入口被发现、源码被本次配置选入。一个项目完成了前一件事，不表示后两件已经发生。

配套 [PPT](slides/P010_Zephyr的CMake输入与依赖发现_Windows.pptx) 与正文同序。源码依据为 `25c8f4a23988dd3b2cfb463613622738298c2d6c`；网页 latest 用于阅读，固定提交用于核对。Windows 命令默认 UCRT64，实验根为 `/g/zephyr_practice/zephyr-main`。

**官方译文对照：** [配置文件发现](../zephyr_docs/cmake_reference/P004_configuration_files.md)、[CMake 扩展接口](../zephyr_docs/cmake_reference/P008_extensions.md)、[模块与外部项目](../zephyr_docs/modules/P001_模块与外部项目.md)及 [Zephyr SDK](../zephyr_docs/toolchains/P002_ZephyrSDK.md)。接口规则与当前固定源码相互核对；模块已发现、功能已启用和源文件已编译分别判断。

**复制命令：** [本章完整操作单元](commands/P010_Windows/README.md)。按正文选择分支，不把整个目录的命令依次执行。

**视频与复习对照：** 页码按当前正式 PPT；以阶段名称和正文链接定位，操作前提、完整命令、输出判断与恢复以 Markdown 为准。

| PPT 页面 | 阶段 | 完整正文 | 正文进一步展开 |
| --- | --- | --- | --- |
| 2—5 | 先分清调用者、输入与结果 | [10.1.1](#section-10-1-1) | 回顾 P008 的职责思维导图和初始化流程 |
| 6—7、9—11 | 应用、板、功能和硬件输入 | [10.1.2](#section-10-1-2) | 源码包、BOARD、Kconfig、Devicetree 的读取者 |
| 8 | 一个 BOARD 值怎样选到 soc.c | 10.1.3 | board.yml 登记 mps2/an386；Kconfig.mps2 按 BOARD_MPS2_AN386 选择 SOC_AN386；SoC Kconfig 继续选择 MPS2 系列、ARM 和 Cortex-M4 能力。 |
| 12—17 | SDK 和工具链类型 | [10.2](#section-10-2) | 默认发现、按需覆盖与 CPU/FPU 参数来源 |
| 18—23 | 外部模块怎样被发现 | [10.3.1](#section-10-3-1) | 候选列表、元数据、外部接入脚本与派生变量 |
| 24、26 | 源码进入目标 | [10.3.4](#section-10-3-4) | 库、功能选择与头文件使用范围 |
| 25 | 怎样查出硬件支持在内置驱动还是厂商库 | 10.3.4 | 先分开硬件支持职责与包名：MPS2 有 Keil BSP；本次复位/NVIC、SysTick、GPIO/pinctrl 与 UART 来自 Zephyr，通用 Core 接口来自 CMSIS_6。 |

<a id="section-10-1"></a>

## 10.1\_输入接口怎样把应用、板和配置交给构建系统

<a id="section-10-1-1"></a>

### 10.1.1\_先区分命令、输入和结果

先拿 P008 的结果问三个问题：`main.c` 是谁加进来的？`mps2/soc.c` 是谁选择的？CMSIS_6 的头文件目录是谁加到编译命令的？下面每个接口都对应其中一步：应用的 `target_sources` 加入应用代码，`BOARD` 经硬件与配置模型选择平台代码，模块发现和模块 CMake 加入外部材料。

所谓接口，是调用者与读取者之间的约定：传什么、在哪里传、何时读取、产生什么结果。Zephyr 的 CMake 接口不只有变量，也包括包入口、函数、目标、属性以及模块元数据。先识别名字属于输入还是生成结果，才能知道该修改哪一个文件。

| 看到的写法 | 属于谁 | 在这里的用途 |
| --- | --- | --- |
| `find_package`、`target_sources`、`add_subdirectory` | CMake 原生命令 | 查包、修改目标、执行子目录构建脚本 |
| `zephyr_library()`、`zephyr_library_sources_ifdef()` | Zephyr 在 extensions.cmake 定义的宏/函数 | 按 Zephyr 的库约定创建目标并按配置加入源码 |
| `BOARD`、`CONF_FILE`、`EXTRA_ZEPHYR_MODULES` | Zephyr 构建脚本接受的输入 | 选硬件、选配置片段、追加模块 |
| `Zephyr_DIR` | CMake 的 `<Package>_DIR` 约定 | 定位名为 Zephyr 的包配置目录 |
| `CONFIG_GPIO` | Kconfig 配置结果 | 供 CMake 和 C 代码决定是否启用相应功能 |
| `ZEPHYR_HAL_XHSC_MODULE_DIR` | Zephyr 模块发现产生的结果 | 让后续 CMake 脚本引用已识别模块根 |

`-D名字=值` 是 CMake 的传入语法；它本身不会赋予某个名字功能。如果 Zephyr 没有读取 `MY_HAL_PATH`，单独添加这个自造变量不会接入 HAL。同样，结果变量通常不该由使用者提前伪造。依据：[CMake 原生命令索引](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html)（原件 `CMake 原生命令手册`）；[扩展函数参考页](https://docs.zephyrproject.org/latest/build/cmake-ref/module/extensions.html)（原件 `doc/build/cmake-ref/module/extensions.rst`，第 1 行附近）；[派生模块目录变量创建处](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/zephyr_module.cmake#L141)（原件 `cmake/modules/zephyr_module.cmake`，第 141 行附近）。

<a id="section-10-1-2"></a>

### 10.1.2\_源码包位置和应用位置是不同输入

应用是 `-S` 所指向的目录；Zephyr 源码根含 `boards`、`cmake`、`kernel` 等目录；SDK 则是另外安装的工具包。三者必须分清。

`ZEPHYR_BASE` 表示 Zephyr 源码根，例如本系列的 `G:/zephyr_practice/zephyr-main`。`Zephyr_DIR` 表示包含 `ZephyrConfig.cmake` 的包目录，在该源码中为 `share/zephyr-package/cmake`。应用可以根据包搜索规则找到 Zephyr；`west zephyr-export` 可把源码包加入当前用户的 CMake 包记录。显式指定入口适合同时存在多份源码、需要固定本次选择的情形。

因此并不是每个工程都必须同时设置两项。若两项同时提供，必须指向同一份源码，防止“找到了 A 的包，却要求它使用 B 的源码”。P012 为明确区分本机源码副本给出具体选择；这不会选择 SDK。依据：[Zephyr 包发现说明](https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html)（原件 `doc/build/zephyr_cmake_package.rst`，第 3 行附近）；[包入口 include_boilerplate](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/share/zephyr-package/cmake/ZephyrConfig.cmake#L28)（原件 `share/zephyr-package/cmake/ZephyrConfig.cmake`，第 28 行附近）。

<a id="section-10-1-3"></a>

### 10.1.3\_BOARD 怎样落实到硬件

`BOARD=mps2/an386` 表示选择官方 MPS2 的 AN386 目标，值是板目标标识，不是路径。`boards.cmake` 等脚本解析板名和限定项，硬件模型再把它联系到 SoC、CPU 与架构。板的设备树及默认配置参与后续计算；应用不应自己把板名翻译为一串 GCC 参数。

这一步可以在本机逐文件走完，不需要从板名猜 CPU。以下路径均相对 `G:/zephyr_practice/zephyr-main`：

| 从哪里开始读 | 看到的选择 | 下一步结果 |
| --- | --- | --- |
| `boards/arm/mps2/board.yml` | `name: mps2`，SoC 列表含 `an386` | 板目标 `mps2/an386` 可被识别 |
| `boards/arm/mps2/Kconfig.mps2:8` | `BOARD_MPS2_AN386` 时 `select SOC_AN386` | 选中对应 SoC |
| `soc/arm/mps2/Kconfig.soc:23` | AN386 归属 `SOC_SERIES_MPS2` | 系列和家族进入配置 |
| `soc/arm/mps2/Kconfig:23` | `SOC_AN386` 选择 `CPU_CORTEX_M4` 等能力 | 使用 Cortex-M4 架构支持 |
| `soc/arm/CMakeLists.txt:4` | 按 `CONFIG_SOC_SERIES` 加载子目录 | 进入 `soc/arm/mps2` |
| `soc/arm/mps2/CMakeLists.txt:3` | `zephyr_sources(soc.c)` | 这份平台实现进入构建 |

这解释了为什么“应用没有写 `soc.c`”仍会编译它：应用加载 Zephyr 的构建规则后，规则读取 `BOARD` 所引出的配置并加入源码。应在构建目录的 `zephyr/.config` 中同时查到 `CONFIG_SOC="an386"` 和 `CONFIG_CPU_CORTEX_M4=y`，再在编译清单查到 `soc/arm/mps2/soc.c`。[板级选择源码](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/boards/arm/mps2/Kconfig.mps2#L8)、[SoC 选入源码](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/soc/arm/mps2/CMakeLists.txt#L3)。

官方板位于默认源码搜索范围内，通常不需要 `BOARD_ROOT`。当 P012 创建树外练习板时，`BOARD_ROOT` 才用于增加搜索根；它应指向**下面包含 boards 目录的上层目录**，而不是 `board.yml` 文件。模块的 `build.settings.board_root` 也能提供搜索根，这是前面先发现模块再找板的原因。

`SOC_ROOT`、`DTS_ROOT` 分别扩展 SoC 和设备树相关文件的查找范围，各有目录约定。新增驱动、板、SoC 是不同工作，不能只增加 BOARD_ROOT 就声称芯片已完成支持。依据：[BOARD 变量参考](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/BOARD.html)（原件 `doc/build/cmake-ref/variable/BOARD.rst`，第 4 行附近）；[BOARD_ROOT 变量参考](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/BOARD_ROOT.html)（原件 `doc/build/cmake-ref/variable/BOARD_ROOT.rst`，第 4 行附近）；[板选择的说明与实现](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/boards.cmake#L6)（原件 `cmake/modules/boards.cmake`，第 6 行附近）；[外部项目模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)（原件 `doc/develop/modules.rst`，第 3 行附近）。

<a id="section-10-1-4"></a>

### 10.1.4\_CONF_FILE 选文件，Kconfig 决定有效值

应用通常用原有 `prj.conf` 提出功能配置请求，例如某功能的 `CONFIG_...=y`。`CONF_FILE` 用于选择应用配置片段，`EXTRA_CONF_FILE` 用于在基础配置之外追加片段。它们的值是文件路径或文件列表；文件名本身不是功能开关。

`configuration_files.cmake` 在未显式指定 CONF_FILE 时按规则查找默认应用和硬件相关片段；接着 `kconfig.cmake` 调用 Python 的 Kconfig 处理脚本，结合配置定义与依赖关系产生 `zephyr/.config`，并生成供 C 编译使用的 `zephyr/include/generated/zephyr/autoconf.h`。CMake 也读取计算后的配置来决定加入哪些源码。

例如请求打开某驱动但它依赖的总线没有启用，Kconfig 会处理约束并给出诊断。读者应查最终 `.config` 与配置日志，不能只凭 prj.conf 里写了 y 就认为驱动必然编译。源码中的 `Kconfig` 是配置项定义，应用 `prj.conf` 是请求，构建目录 `.config` 是计算结果；三种文件来源与作用不同。依据：[CONF_FILE 变量参考](https://docs.zephyrproject.org/latest/build/cmake-ref/variable/CONF_FILE.html)（原件 `doc/build/cmake-ref/variable/CONF_FILE.rst`，第 4 行附近）；[配置片段的选取](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/configuration_files.cmake#L43)（原件 `cmake/modules/configuration_files.cmake`，第 43 行附近）；[Kconfig 脚本调用处](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/kconfig.cmake#L473)（原件 `cmake/modules/kconfig.cmake`，第 473 行附近）。

把这条规则落到当前控制台：`mps2_an386_defconfig` 默认请求 `SERIAL`、`CONSOLE` 和 `UART_CONSOLE`；`drivers/serial/Kconfig.cmsdk_apb` 定义的 `UART_CMSDK_APB` 又依赖设备树给出的 `DT_HAS_ARM_CMSDK_UART_ENABLED`，条件满足时默认开启。最终 `.config` 的 `CONFIG_UART_CMSDK_APB=y`，才是下一步 CMake 选入驱动文件时读取的值。不是在应用里随便写一个同名变量就能跳过这些依赖。[UART 配置定义](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/drivers/serial/Kconfig.cmsdk_apb#L6)。

<a id="section-10-1-5"></a>

### 10.1.5\_设备树输入怎样成为编译信息

板的 `.dts` 和 SoC 的 `.dtsi` 描述硬件。应用的 overlay 可以覆盖相应节点属性。`DTC_OVERLAY_FILE` 指定应用 overlay 列表；`EXTRA_DTC_OVERLAY_FILE` 追加在基础 overlay 后处理的文件。不显式指定时有默认文件查找规则，不能把“追加”和“完全换掉选择”当成同一种动作。

`dts.cmake` 先用预处理器处理包含关系与宏，再调用 Zephyr 的 Python 工具解析设备树和 bindings。输出的 `zephyr/zephyr.dts` 用于查看最终硬件描述；`zephyr/include/generated/zephyr/devicetree_generated.h` 提供编译所需宏。C 源码通常通过 `zephyr/devicetree.h` 使用这些信息。

启用外设一般还涉及 Kconfig 选择驱动，所以“设备树节点 okay”与“驱动功能启用”需要分别成立。这正是 Zephyr 没有把所有配置都混进一个 CMake 变量的原因：硬件数据、功能依赖和目标构建关系由各自工具处理，再共同进入固件。依据：[设备树配置入口](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/dts.cmake#L9)（原件 `cmake/modules/dts.cmake`，第 9 行附近）；[构建阶段说明](https://docs.zephyrproject.org/latest/build/cmake/index.html#build-and-configuration-phases)（原件 `doc/build/cmake/index.rst`，第 52 行附近）。

现在接上 UART 的硬件一端：`mps2_an386.dts` 包含 `mps2_base.dtsi`；后者的 `chosen` 把 `zephyr,console` 指向 `uart0`，而 `uart0` 的 `compatible` 是 `arm,cmsdk-uart`。最终设备树保留硬件地址等信息，驱动里的 `DT_DRV_COMPAT arm_cmsdk_uart` 与它对应。仅在磁盘里找到一个名称相似的驱动不足以证明匹配，要核对这条 compatible 链。

```mermaid
flowchart LR
    A["DTS：uart0 / arm,cmsdk-uart"] --> B["Kconfig：UART_CMSDK_APB=y"]
    B --> C["serial/CMakeLists：条件加入 uart_cmsdk_apb.c"]
    A --> D["生成硬件宏：寄存器地址等"]
    C --> E["编译并链接驱动"]
    D --> E
```

从完整硬件支持看，UART 只是其中一项。复位/向量/C 运行环境由 Cortex-M 的 `reset.S`、`vector_table.S`、`prep_c.c` 实现；`irq_manage.c` 通过 CMSIS NVIC 接口管理中断；`cortex_m_systick.c` 提供系统时钟；DTS 与共用链接脚本决定内存布局；GPIO/pinctrl 各有内置驱动。它们都有可追的 CMake 选择规则，本次编译并不是绕过硬件抽象直接执行应用。

MPS2 另外也有 [Arm Keil 独立 BSP Pack](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil/boards/)。这说明“厂商提供包”与“当前 Zephyr 构建采用哪些实现”是两件事；本例使用 Zephyr 架构/SoC/驱动与外部 CMSIS，没有直接把那个 Pack 加入构建。P008 的职责对照表列出完整来源，这里继续用一条 UART 路径展示查证方法。

该驱动第 27 行起定义 CMSDK UART 寄存器结构，第 113 行直接写波特率寄存器；实例的寄存器基址由第 515 行 `DT_INST_REG_ADDR(n)` 取得。**MPS2 的这项硬件支持已由 Zephyr 内置驱动实现**，没有要求另下载一个 MPS2 HAL/DDL。其他芯片驱动可以采用另一种实现：调用厂商 HAL 函数；那时再根据它的 include、调用和模块 CMake 查外部厂商库，不能由“同为 Arm”推断。依据：[板级 UART 节点](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/boards/arm/mps2/mps2_base.dtsi#L116)、[CMSDK UART 驱动](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/drivers/serial/uart_cmsdk_apb.c#L104)。

<a id="toolchain-contract"></a>


<a id="section-10-2"></a>

## 10.2\_工具链扩展怎样连接编译器与目标芯片

<a id="section-10-2-1"></a>

### 10.2.1\_先区分两个 CMake 包

`find_package(Zephyr)` 找的是**源码构建规则**；这些规则需要工具时，通过 `FindHostTools.cmake` 请求 `find_package(Zephyr-sdk ...)`。后者才寻找 **SDK 工具包**。两个包各有入口，也各有当前用户的包记录。

SDK 安装根的 `cmake/Zephyr-sdkConfig.cmake` 说明 SDK 在哪里，并在没有其他选择时提供默认工具链类型。Windows 的 `setup.cmd /c` 把 SDK 包位置写入当前用户的 CMake 包注册表，供之后不同工程的包搜索使用；它不把 SDK 复制到应用中，也不改应用 CMakeLists。该记录跨终端保留，Python venv 的启停不会删除它。

没有显式选择其他工具链，且有效包记录可访问时，普通主线让 Zephyr 查找兼容 SDK 即可。**不要求再重复填写默认类型 `zephyr` 和 SDK 根。** 如果已有环境或缓存设置，默认分支可能被覆盖，11.1 再解释怎样定位。依据：[SDK 输入与默认查找分支](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/FindZephyr-sdk.cmake#L44)（原件 `cmake/modules/FindZephyr-sdk.cmake`，第 44 行附近）；[SDK 文档](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)（原件 `doc/develop/toolchains/zephyr_sdk.rst`，第 3 行附近）；[SDK 1.0.1 的默认类型实现（安装包内）](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)（原件 `cmake/Zephyr-sdkConfig.cmake`，第 15 行附近）。

<a id="section-10-2-2"></a>

### 10.2.2\_为什么有工具链类型，而不只填 gcc.exe

编译器可执行文件只是工具链的一部分。构建还需要预处理方式、汇编器、链接器、目标库、参数检测、链接脚本处理以及二进制工具。Zephyr 用一个类型名选择一组知道这些规则的 CMake 脚本。

`ZEPHYR_TOOLCHAIN_VARIANT` 就是该类型输入。`zephyr` 路线使用 SDK 的接入规则；`cross-compile` 路线接受独立 GNU 工具的共同前缀。其他类型须遵循各自文档，不能只替换名字继续套用 SDK 参数。

`FindHostTools.cmake` 加载 `cmake/toolchain/<类型>/generic.cmake`，先准备通用处理所需工具，例如设备树预处理器。`FindTargetTools.cmake` 再加载 `target.cmake`，建立目标编译、链接和库相关设置。目标 CPU 配置并不会由“工具链名字包含 arm”完整推出。

```mermaid
flowchart LR
    A["选择工具链类型"] --> B["generic.cmake：通用工具"]
    B --> C["处理硬件与功能配置"]
    C --> D["target.cmake：目标工具与库"]
    D --> E["目标参数与编译任务"]
```

注意 HostTools 中的 generic 不是要求先用 Windows 的本机 GCC 编一份固件。此阶段需要的是运行在主机上的工具及通用能力，可以使用交叉编译器做预处理。依据：[树外工具链设计说明](https://docs.zephyrproject.org/latest/develop/toolchains/custom_cmake.html)（原件 `doc/develop/toolchains/custom_cmake.rst`，第 3 行附近）；[SDK 请求与通用工具规则](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/FindHostTools.cmake#L51)（原件 `cmake/modules/FindHostTools.cmake`，第 51 行附近）；[目标工具链规则](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/FindTargetTools.cmake#L30)（原件 `cmake/modules/FindTargetTools.cmake`，第 30 行附近）。

<a id="section-10-2-3"></a>

### 10.2.3\_BOARD 与 SDK 怎样共同决定 ARM 编译

以 Cortex-M 目标为例，板与 SoC 的配置确定 ARM 架构和具体 CPU/FPU 需求。SDK 1.0.1 的 GNU `target.cmake` 把 ARM 32 位架构映射到 `arm-zephyr-eabi`，据 SDK 根拼出 `gnu/arm-zephyr-eabi/bin/arm-zephyr-eabi-` 前缀；Zephyr 的 `cmake/compiler/gcc/target_arm.cmake` 再根据配置确定 `-mcpu`、指令集和适用的浮点选项。

所以同一 ARM 工具链可以服务多个 Cortex-M 芯片。给 HC32F4A0 增加板与 SoC 支持时，主要补硬件和驱动适配；不能因为换了厂商就凭空新增 `hc32` 工具链类型。反过来，选择 arm 工具链也不会替读者创建 HC32 的寄存器描述、启动、时钟和驱动。

这条链中，BOARD 是读者输入；ARCH 与 CPU/FPU 配置是硬件选择产生的信息；编译器完整路径和参数是工具规则的结果。P012 最后通过 `compile_commands.json` 核对它们，而不是只看终端的 `gcc --version`。依据：[SDK 1.0.1 的 ARM 映射（安装包内）](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v1.0.1)（原件 `cmake/zephyr/gnu/target.cmake`，第 5 行附近）；[ARM CPU 参数实现](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/compiler/gcc/target_arm.cmake#L5)（原件 `cmake/compiler/gcc/target_arm.cmake`，第 5 行附近）。

<a id="section-10-2-4"></a>

### 10.2.4\_完整 SDK、Minimal 与独立工具链共用哪些接口

完整 GNU SDK 带 SDK 的 CMake 接入层和多个目标工具链；Minimal SDK 仍带 SDK 接入层，但需要另装目标组件。Minimal 补齐 ARM 组件后，两者都作为 SDK 被发现，**工程接口没有另起一套 Minimal 体系**。

`G:/zephyr_practice/arm-zephyr-eabi` 是本机独立 ARM 工具组件目录。单组件可以只有 bin、库和目标头文件，没有 SDK 的包配置。选择直接使用它时，走 Zephyr 源码已提供的 `cross-compile` 接口，给 `CROSS_COMPILE` 提供共同前缀；不是在该目录手建一个 SDK CMake 包。

| 场景 | 读者需要表达什么 | 为什么 |
| --- | --- | --- |
| 已注册的完整 SDK 或补齐后的 Minimal | 默认可省略类型与 SDK 根 | 包发现给出工具位置及默认规则 |
| 多套 SDK 中选择一套 | 在新的构建目录中给 `ZEPHYR_SDK_INSTALL_DIR` 指定目标 SDK 根 | 核对实际 `Zephyr-sdk_DIR` 和编译器，避免旧包缓存继续生效 |
| 独立 GNU 工具组件 | `cross-compile` 配合 `CROSS_COMPILE` | 告诉已有 GNU 规则如何定位程序 |
| 维护尚无接入规则的新工具链 | 自定义类型与 `TOOLCHAIN_ROOT`，并实现所需规则 | 这是扩展构建系统，不是普通 SDK 安装 |

`CROSS_COMPILE` 的值由程序目录加共同文件名前缀组成，包含末尾横线，例如 `G:/zephyr_practice/arm-zephyr-eabi/bin/arm-zephyr-eabi-`。它不是仅到 bin 的目录，也不是 gcc.exe 的完整文件名。目标库还须匹配，必要时根据该路线文档设置 `SYSROOT_DIR`；程序可运行并不等于目标库齐全。具体包准备见 P003，完整构建见 P012。依据：[独立 GNU 接入说明](https://docs.zephyrproject.org/latest/develop/toolchains/other_x_compilers.html)（原件 `doc/develop/toolchains/other_x_compilers.rst`，第 3 行附近）；[树外工具链设计说明](https://docs.zephyrproject.org/latest/develop/toolchains/custom_cmake.html)（原件 `doc/develop/toolchains/custom_cmake.rst`，第 3 行附近）；[SDK 文档](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)（原件 `doc/develop/toolchains/zephyr_sdk.rst`，第 3 行附近）。

[官方 SDK 译文](../zephyr_docs/toolchains/P002_ZephyrSDK.md)还允许 `ZEPHYR_SDK_INSTALL_DIR` 指向包含多套 SDK 的父目录，由包发现选择兼容版本。因此该输入是 SDK 搜索位置，不能仅凭写了它就认定只会选中某个版本。希望固定一套时，使用新构建目录并指向该套 SDK 的根，随后核对配置日志、`Zephyr-sdk_DIR` 和编译器路径；它不会清除已有包缓存。

`TOOLCHAIN_ROOT` 指 Zephyr 工具链接入规则所在根，默认使用 Zephyr 源码；它不等于 SDK 安装根。树外规则按官方约定提供 `cmake/toolchain/<类型>/generic.cmake` 和 `target.cmake`，并满足其依赖的 compiler/linker/bintools 规则。SDK 工具、树外规则与源码模块三类目录不能互换。

<a id="module-contract"></a>


<a id="section-10-3"></a>

## 10.3\_外部源码模块怎样进入 CMake 构建模型

<a id="section-10-3-1"></a>

### 10.3.1\_下载完成之后，还缺一个接入动作

west 清单告诉 west 去哪里、按哪个修订取得项目。下载到磁盘只完成了“文件存在”。CMake 还需要知道候选项目有哪些、哪些具有 Zephyr 接口，以及每个项目的 CMake/Kconfig 入口在哪里。这才是模块发现阶段的工作。

默认情况下，`zephyr_module.cmake` 调用 `scripts/zephyr_module.py`，由脚本通过 west API 得到工作区候选项目。脚本识别项目的 `zephyr/module.yml`，或兼容的约定入口；不是递归扫描整块磁盘。目录不在候选列表里，单凭其内部有 module.yml，不会使它自动参与当前工程。

怎样判断“该去哪里取包”？先从目标对应的 SoC/驱动确认确实引用了外部材料，再在活动工作区执行 `west list` 查项目名称、路径和修订；清单列出的项目才有现成 `west update <项目名>` 入口。若上游清单没有该项目，须阅读该外部库自己的接入说明，选择追加本地模块或维护自己的 manifest。`west list` 列出的是当前清单项目，不是 Zephyr 支持的全部板清单，也不会按 BOARD 自动求出全部必需库。

本例中，`west.yml` 的 `cmsis_6` 项目提供外部 CMSIS Core；`boards/arm/mps2`、`soc/arm/mps2`、`drivers/serial/uart_cmsdk_apb.c` 已在 Zephyr 主仓库里，不对应三个必须另外下载的 west 项目。将它们一起叫“包”会掩盖各自位置：查板看硬件目录，查可下载项目看 manifest，查实际使用看配置和编译规则。

已在官方清单中的 CMSIS 先按 P004 交给 west 下载。清单之外的新增 HAL，可通过 `EXTRA_ZEPHYR_MODULES` 给**这次 CMake 配置**追加模块根。该变量接受以分号分隔的路径列表，指模块根，不是 module.yml 文件。`ZEPHYR_MODULES` 则可以显式取代默认基础候选列表，容易漏掉 CMSIS 等原依赖；单加一个 HAL 时通常使用追加接口。同名模块同时来自 west 和追加列表时，追加列表中的模块优先；这里的“追加”并不意味着两个同名实现一起编译，见[官方模块译文的构建接入说明](../zephyr_docs/modules/P001_模块与外部项目.md)。依据：[外部项目模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)（原件 `doc/develop/modules.rst`，第 3 行附近）；[模块输入与发现脚本调用](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/zephyr_module.cmake#L34)（原件 `cmake/modules/zephyr_module.cmake`，第 34 行附近）；[候选项目解析实现](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/scripts/zephyr_module.py#L627)（原件 `scripts/zephyr_module.py`，第 627 行附近）。

<a id="section-10-3-2"></a>

### 10.3.2\_用已下载的 CMSIS 看真实的两端

本系列 west 下载的 `../modules/hal/cmsis_6/zephyr/module.yml` 是**官方外部下载文件**，当前内容如下，仅供阅读：

```yaml
# 只读：工作区 modules/hal/cmsis_6/zephyr/module.yml。
name: cmsis_6
build:
  cmake-ext: true
  kconfig-ext: true
```

名字说明该模块以 `cmsis_6` 被识别；`cmake-ext` 和 `kconfig-ext` 表示接入文件放在模块外部。对于本源码，接入脚本位于**官方原有** `zephyr-main/modules/cmsis_6/CMakeLists.txt` 和同目录 Kconfig。CMSIS 的头文件留在工作区下载目录，接入代码留在 Zephyr 源码里，两边由规则关联起来。这种布局让上游库文件和 Zephyr 的构建适配可以分别维护。

`modules/modules.cmake` 为这些外置接入目录设置相应 CMake/Kconfig 位置。模块发现记录和后续调用最终把 CMSIS 库根交给接入脚本；其中按 `CONFIG_CPU_CORTEX_M` 条件加入 `${ZEPHYR_CURRENT_MODULE_DIR}/CMSIS/Core/Include`。因此没有必要把下载的 CMSIS 整包复制进应用，或把两处同名 modules 目录混为一谈。当前 `soc/arm/mps2/soc.h:10` 先包含 Zephyr 适配头，`modules/cmsis_6/cmsis_core_m_defaults.h:132` 的 Cortex-M4 分支再包含外部 `core_cm4.h`；这条头文件链解释了 CMSIS_6 为什么仍是本目标的外部依赖。

另外一种模块会在 module.yml 写 `build.cmake: zephyr` 和 `build.kconfig: zephyr/Kconfig`，含义是入口位于模块自身；这些路径相对模块根。P006 已用厂商 HAL 讲完整目录，不能把一个项目的内部布局猜成所有模块的固定布局。依据：[外部项目模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)（原件 `doc/develop/modules.rst`，第 3 行附近）；[外置模块接入文件选择](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/modules/modules.cmake#L5)（原件 `modules/modules.cmake`，第 5 行附近）；[CMSIS 头文件接入实现](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/modules/cmsis_6/CMakeLists.txt#L4)（原件 `modules/cmsis_6/CMakeLists.txt`，第 4 行附近）。

<a id="section-10-3-3"></a>

### 10.3.3\_派生变量究竟是谁建立的

```mermaid
flowchart TD
    A["CMake：west 候选与显式追加路径"] --> B["zephyr_module.py：读取模块元数据"]
    B --> C["生成 zephyr_modules.txt 与 Kconfig 接入记录"]
    C --> D["zephyr_module.cmake：设置模块目录变量"]
    D --> E["根 CMakeLists：add_subdirectory 加载入口"]
    E --> F["模块脚本：加入头文件、源码和库"]
```

`zephyr_modules.txt` 是**工具生成文件**，位于所选构建目录。它不是读者必须提前创建的清单，也不是 west.yml。`zephyr_module.cmake` 读取其中名字、模块根和 CMake 入口，把模块名转为大写、将非字母数字字符替换为下划线后设置变量；例如模块名 `hal_xhsc` 对应 `ZEPHYR_HAL_XHSC_MODULE_DIR`。

接着 Zephyr 根 CMakeLists 遍历已识别模块，设置本轮 `ZEPHYR_CURRENT_MODULE_DIR` 等上下文，对提供非空 CMake 入口的模块，再调用 `add_subdirectory` 执行入口；只有 Kconfig 或其他元数据的模块不一定有可执行的 CMake 入口。只有走过候选识别、元数据解析和记录读取，才有这个派生变量。**预先手填同名 MODULE_DIR 不会代替模块注册与入口执行。**

再换成时序图看“谁先调用谁”。图中的 Zephyr CMake 和模块入口实际都由同一个 CMake 进程执行，分列只是区分脚本的职责；Python 发现脚本由 CMake 启动。

```mermaid
sequenceDiagram
    participant A as 应用配置调用者
    participant C as Zephyr CMake 脚本
    participant P as Python 模块发现脚本
    participant M as 模块 CMake 入口
    A->>C: 发起配置，提供追加模块根
    C->>P: 传入候选列表与追加路径
    Note over P: 读取 module.yml 并写出模块记录
    P-->>C: 完成识别，返回状态
    C->>C: 读取记录并设置模块目录变量
    C->>M: add_subdirectory 加载接入入口
    M->>C: 添加库、源码与头文件目录
```

发现成功也不保证模块里所有源文件都编译。模块 CMake 还会受 CONFIG 条件限制；芯片、板和驱动是否已经适配是更后面的事实。P006 解释并验证模块发现，P012 展开目标板的实际构建。依据：[模块输入与发现脚本调用](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/zephyr_module.cmake#L34)（原件 `cmake/modules/zephyr_module.cmake`，第 34 行附近）；[派生模块目录变量创建处](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/zephyr_module.cmake#L141)（原件 `cmake/modules/zephyr_module.cmake`，第 141 行附近）；[外部模块 CMake 入口加载处](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/CMakeLists.txt#L778)（原件 `CMakeLists.txt`，第 778 行附近）。

<a id="section-10-3-4"></a>

### 10.3.4\_进入模块后，CMake 函数怎样组织源码

应用使用 `target_sources(app PRIVATE ...)`，是因为 app 已由 Zephyr 建好。独立子系统或驱动常用 `zephyr_library()` 创建属于自己目录的库，再用 `zephyr_library_sources()` 加入实现。它们由 `extensions.cmake` 定义，底层仍调用 CMake 的库与目标接口，并把库纳入 Zephyr 的全局构建关系。

`zephyr_library_sources_ifdef(CONFIG_某功能 文件.c)` 先检查功能条件，再给当前库加源码。这里的条件来自前面 Kconfig 的结果；名字不是预处理器的 `#ifdef` 指令，而是一个 Zephyr CMake 函数的参数。

当前 `drivers/serial/CMakeLists.txt:36` 原文就是 `zephyr_library_sources_ifdef(CONFIG_UART_CMSDK_APB uart_cmsdk_apb.c)`。前面经过 BOARD、DTS 和 Kconfig 得到的值，在这一行终于变成一个具体 `.c` 文件的加入动作。这才补齐了最初的问题：应用显式加入 `main.c`，SoC 规则加入 `soc.c`，驱动规则按条件加入 UART 实现；它们不需要全部写进应用 CMakeLists。

头文件目录也有范围。`target_include_directories(app PRIVATE ...)` 只修改 app；`zephyr_library_include_directories(...)` 作用于当前 Zephyr 库；`zephyr_include_directories(...)` 则作用于 Zephyr 的公共接口目标，使参加构建的相应目标继承。应按真正需要的可见范围选择，不能为解决一个库的 include 问题把所有路径无条件变成公共输入。

因此“外部模块接入接口”和“模块内部构建接口”是连续的两层：前者使入口被执行，后者使源码真正进入目标。把一个路径传给 CMake，只完成前者所需的信息，并不会自动扫描所有 `.c` 文件。依据：[Zephyr 库创建接口](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/extensions.cmake#L682)（原件 `cmake/modules/extensions.cmake`，第 682 行附近）；[Zephyr 库源码接口](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/extensions.cmake#L769)（原件 `cmake/modules/extensions.cmake`，第 769 行附近）；[按配置加入源码](https://github.com/zephyrproject-rtos/zephyr/blob/25c8f4a23988dd3b2cfb463613622738298c2d6c/cmake/modules/extensions.cmake#L2831)（原件 `cmake/modules/extensions.cmake`，第 2831 行附近）；[扩展函数参考页](https://docs.zephyrproject.org/latest/build/cmake-ref/module/extensions.html)（原件 `doc/build/cmake-ref/module/extensions.rst`，第 1 行附近）。

### 10.3.5\_把选择过程和生成结果一一对上

先确保 P008 的 `cmake-demo` 已配置成功且启用了 `CMAKE_EXPORT_COMPILE_COMMANDS`，再执行下面的只读块。它读取同一个构建目录，避免把另一次 IDE 构建、另一个板或以前留下的缓存混进证据。

```bash
# Windows UCRT64；P008 的 cmake-demo 已配置成功；只读生成结果。
cd /g/zephyr_practice/zephyr-main
source .venv/Scripts/activate
python - <<'PY'
from pathlib import Path
import json
build = Path('build/learning-tools/p003/cmake-demo')
required = ['CMakeCache.txt', 'zephyr/.config', 'zephyr_modules.txt', 'compile_commands.json']
missing = [name for name in required if not (build / name).is_file()]
if missing:
    raise SystemExit('先完成 P008 配置，或核对构建目录：' + ', '.join(missing))
print('BUILD:', build.resolve())
for line in (build / 'CMakeCache.txt').read_text(encoding='utf-8').splitlines():
    if line.startswith(('BOARD:', 'BOARD_DIR:', 'CMAKE_C_COMPILER:', 'ZEPHYR_SDK_INSTALL_DIR:', 'Zephyr-sdk_DIR:')):
        print(line)
for line in (build / 'zephyr/.config').read_text(encoding='utf-8').splitlines():
    if line.startswith(('CONFIG_BOARD=', 'CONFIG_BOARD_TARGET=', 'CONFIG_SOC=',
                        'CONFIG_CPU_CORTEX_M4=', 'CONFIG_UART_CMSDK_APB=',
                        'CONFIG_HAS_CMSIS_CORE=', 'CONFIG_ZEPHYR_CMSIS_6_MODULE=')):
        print(line)
print('MODULE RECORDS:\n' + (build / 'zephyr_modules.txt').read_text(encoding='utf-8'))
rows = json.loads((build / 'compile_commands.json').read_text(encoding='utf-8'))
wanted = [
    'samples/hello_world/src/main.c', 'soc/arm/mps2/soc.c',
    'arch/arm/core/cortex_m/reset.S', 'arch/arm/core/cortex_m/thread.c',
    'drivers/console/uart_console.c', 'drivers/serial/uart_cmsdk_apb.c',
    'drivers/timer/cortex_m_systick.c', 'kernel/init.c',
]
for suffix in wanted:
    matches = [r for r in rows if r['file'].replace('\\', '/').endswith('/' + suffix)]
    print('SELECTED' if matches else 'NOT SELECTED', suffix)
main = next((r for r in rows if r['file'].replace('\\', '/').endswith('/hello_world/src/main.c')), None)
if main:
    print('MAIN COMPILE:', main.get('command', main.get('arguments')))
print('HC32/DDL translation units:', [r['file'] for r in rows
      if any(word in r['file'].lower() for word in ('hal_xhsc', 'hc32_ddl'))])
PY
```

应先看到 `mps2/an386`、AN386/Cortex-M4 与 CMSDK UART 配置，再看到所列应用、SoC、架构、控制台、驱动和内核文件被选中。`MAIN COMPILE` 中的 `-mcpu=cortex-m4` 来自目标能力，编译器路径来自工具链选择，CMSIS include 来自外部模块接入，三者不是同一个配置项。

此处 `SELECTED` 证明配置生成了相应编译任务；它不证明任务已经执行成功。实际编译是否成功仍看 P008 的 build 返回值和产物。头文件一般不作为独立翻译单元出现，应从编译命令的 include 路径和源码 include 链核验。`MODULE RECORDS` 列出候选接入记录，也不能据此宣称每个模块的实现都被编译。

若 `.config` 中没有预期符号，回查板、DTS 与 Kconfig；配置符号正确但缺相应 `.c`，回查 CMake 选入条件；`.c` 已加入但 include 缺失，回查模块根和头文件接口。这样每次只返回有证据缺失的一层，不反复下载所有包。[完整反查块](commands/P010_Windows/trace-selected-sources.txt)。

<a id="input-lifetime"></a>



上一篇：[P009](P009_west零基础与Zephyr构建_Windows.md)；下一篇：[P011](P011_CMake缓存与构建排错_Windows.md)。
