---
id: learning.zephyr-docs.shield-samples.page-7
title: Renesas电容触摸扩展板
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/rtk0eg0019b01002bj/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="rtk0eg0019b01002bj"></a>

# 第7章\_RTK0EG0019B01002BJ 电容触摸应用扩展板（Capacitive Touch Application Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/rtk0eg0019b01002bj/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/rtk0eg0019b01002bj/README.rst/..)

<a id="overview"></a>

## 7.1 概述（Overview）

本示例通过 RTK0EG0019B01002BJ 电容触摸应用扩展板和 [Renesas 电容触摸传感器解决方案（Renesas Capacitive Touch Sensor Solutions）](https://www.renesas.com/en/key-technologies/hmi/capacitive-touch-sensor-solutions)，演示电容触摸传感器的用法。 相关链接：[RTK0EG0019B01002BJ 电容触摸应用扩展板（Capacitive Touch Application Shield）](https://docs.zephyrproject.org/latest/boards/shields/rtk0eg0019b01002bj/doc/index.html#rtk0eg0019b01002bj)。

<a id="requirements"></a>

## 7.2 硬件与配置要求（Requirements）

运行需要一套 Renesas 电容触摸评估套件，包含：

- 支持电容触摸检测单元（Capacitive Touch Sensing Unit，CTSU）驱动的 MCU 板，例如 RSSK-RA2L1。

- RTK0EG0019B01002BJ 触摸应用板。

<a id="building-and-running"></a>

## 7.3 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，使用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块和工具链，再核对本页指定主开发板、扩展板、接线与配置。设备 Shell 命令在目标板串口执行。遇到构建或设备就绪错误，先回查所选 board／shield 与接线；下方日志是官方预期示例。本次仅核对文档与源码，未构建、烧录、擦写存储或进行实板测量。

<a id="build-and-flash-with-default-settings-for-shield"></a>

### 7.3.1 使用扩展板默认设置构建与烧录

RTK0EG0019B01002BJ 电容触摸应用扩展板自带经过预先调校的默认 DTS 配置，可直接用于开发。 相关链接：[RTK0EG0019B01002BJ 电容触摸应用扩展板（Capacitive Touch Application Shield）](https://docs.zephyrproject.org/latest/boards/shields/rtk0eg0019b01002bj/doc/index.html#rtk0eg0019b01002bj)。

按以下方式构建和烧录，将 `rssk_ra2l1` 替换为所用开发板：

```text
west build -b rssk_ra2l1 --shield rtk0eg0019b01002bj samples/shields/rtk0eg0019b01002bj
west flash
```

启动后，扩展板上的所有 LED 闪烁 5 次，表示应用已启动。

> 译注——启动与事件：main.c 的五次闪烁各含 200 ms 亮和 200 ms 灭。输入回调先关闭全部 LED，再根据按钮、滑条（Slider）或转轮（Wheel）的事件选择一个 LED；该显示不是保持所有同时触摸位置的完整状态。

可通过控制台输出监视输入事件；触摸某个传感器时，相应 LED 也会点亮。

```text
*** Booting Zephyr OS build v4.1.0-6697-gdc27367ff627 ***
rtk0eg0019b01002bj sample started
I: input event: dev=button1              type= 1 code= 11 value=0
I: input event: dev=wheel                type= 3 code=  8 value=61
I: input event: dev=wheel                type= 3 code=  8 value=67
I: input event: dev=wheel                type= 3 code=  8 value=82
I: input event: dev=wheel                type= 3 code=  8 value=111
I: input event: dev=wheel                type= 3 code=  8 value=124
I: input event: dev=wheel                type= 3 code=  8 value=134
I: input event: dev=slider               type= 3 code=  6 value=0
I: input event: dev=slider               type= 3 code=  6 value=2
I: input event: dev=slider               type= 3 code=  6 value=4
I: input event: dev=slider               type= 3 code=  6 value=6
I: input event: dev=slider               type= 3 code=  6 value=10
I: input event: dev=slider               type= 3 code=  6 value=23
I: input event: dev=slider               type= 3 code=  6 value=26
I: input event: dev=slider               type= 3 code=  6 value=27
I: input event: dev=slider               type= 3 code=  6 value=28
```

<a id="advanced-using-configuration-output-generated-by-renesas-qe-capacitive-touch-workflow"></a>

### 7.3.2 进阶：使用 Renesas QE 电容触摸工作流程生成的配置

本节面向不使用电容触摸扩展板默认配置，而希望通过 Renesas 电容触摸传感器开发辅助工具自行调校参数的进阶读者。 相关链接：[Renesas 电容触摸传感器开发辅助工具（Renesas Development Assistance Tool for Capacitive Touch Sensors）](https://www.renesas.com/en/software-tool/qe-capacitive-touch-development-assistance-tool-capacitive-touch-sensors)。

> 译注——配置来源：当前示例 src 目录已随附 qe_touch_config.c、qe_touch_config.h 和 qe_touch_define.h。CMake 仅在 CONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG 启用时编译该 .c 并加入包含目录。自行调校后的文件属于工具生成结果，应确认输出目录和构建路径对应；默认 DTS 配置与生成参数是两条不同配置路线。

<a id="id1"></a>

#### 7.3.2.1 硬件与配置要求（Requirements）

- 安装 Renesas QE 电容触摸插件的 [e² studio](https://www.renesas.com/en/software-tool/e-studio)，推荐版本为 2025-04.1。

- [RA 灵活软件包（Flexible Software Package，FSP）](https://www.renesas.com/en/software-tool/flexible-software-package)，推荐 v5.8.0 或更高版本。

> 译注——参考链接：本次检查时，上述原文 FSP 链接返回访问限制；可另查已确认可访问的官方 [RA FSP 页面](https://www.renesas.com/en/software-tool/ra-flexible-software-package-fsp)。本节版本要求仍按 Zephyr 原文保留，不把产品网页的最新版自动当成本示例已验证版本。

<a id="building-and-flashing-with-generated-tuning-code"></a>

#### 7.3.2.2 使用生成的调校代码构建与烧录

> 1. 按[《使用 QE 和 FSP 开发电容触摸应用》（Using QE and FSP to Develop Capacitive Touch Applications）](https://www.renesas.com/en/document/apn/using-qe-and-fsp-develop-capacitive-touch-applications?r=1170071)的 6.1～6.5 节操作。
>
> 2. 在 6.5 节“使用 QE for Capacitive Touch 插件调校电容触摸接口”的步骤 8 中，选择 Specify an output folder，指定本应用的子目录作为输出文件夹。
>
> 3. 在应用 CMake 中更新 qe_touch_config.h 与 qe_touch_define.h 的包含路径，并将 qe_touch_config.c 加入构建源文件。
>
> 4. 使用以下命令构建并烧录应用：

```text
west build -b rssk_ra2l1 --shield rtk0eg0019b01002bj samples/shields/rtk0eg0019b01002bj -- -DCONFIG_INPUT_RENESAS_RA_QE_TOUCH_CFG=y
west flash
```

<a id="references"></a>

## 7.4 参考资料（References）

- [Renesas 电容触摸传感器解决方案（Renesas Capacitive Touch Sensor Solutions）](https://www.renesas.com/en/key-technologies/hmi/capacitive-touch-sensor-solutions)

- [Renesas 电容触摸传感器开发辅助工具（Renesas Development Assistance Tool for Capacitive Touch Sensors）](https://www.renesas.com/en/software-tool/qe-capacitive-touch-development-assistance-tool-capacitive-touch-sensors)

<a id="see-also"></a>

## 7.5 另请参阅（See also）

[输入（Input）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)

[Renesas RA 电容触摸检测单元（Renesas RA CTSU）](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__ra__ctsu__interface.html)

> 译注——源码入口：[src/main.c](../../../samples/shields/rtk0eg0019b01002bj/src/main.c)；[CMakeLists.txt](../../../samples/shields/rtk0eg0019b01002bj/CMakeLists.txt)；[prj.conf](../../../samples/shields/rtk0eg0019b01002bj/prj.conf)；[src/qe_touch_config.c](../../../samples/shields/rtk0eg0019b01002bj/src/qe_touch_config.c)；[src/qe_touch_config.h](../../../samples/shields/rtk0eg0019b01002bj/src/qe_touch_config.h)；[src/qe_touch_define.h](../../../samples/shields/rtk0eg0019b01002bj/src/qe_touch_define.h)。本地源码使用相对链接；上游快照摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/shields/rtk0eg0019b01002bj/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/rtk0eg0019b01002bj/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/shields/rtk0eg0019b01002bj/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、擦写存储或连接设备。

[上一章](P006_nPM6001电源评估套件示例.md) · [返回大纲](大纲.md) · [下一章](P008_X_NUCLEO_53L0A1测距扩展板.md)
