---
id: learning.zephyr-docs.basic_samples.page-64
title: Sysbuild多板目标问候示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sysbuild/hello_world/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sysbuild_hello_world"></a>

# 第64章\_Sysbuild多板目标问候示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sysbuild/hello_world/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 64.1 概述（Overview）

本示例演示如何使用[系统构建（Sysbuild，System build）](../sysbuild/P001_系统构建.md#sysbuild)，为两个开发板目标（Board target）构建Hello World应用。例如，在多核片上系统（SoC）中，每个处理器核都作为一个开发板目标暴露出来，此示例可用于检查这种场景；它也适用于同一开发板包含多个SoC的情况。使用Zephyr Sysbuild时，构建系统根据项目附加配置与构建文件中的选项，加入额外镜像（Image）。

所有镜像使用同一份`main.c`，打印应用所烧录到的开发板目标。

<a id="building-and-running"></a>

## 64.2 构建与运行（Building and Running）

本示例必须使用`--sysbuild`选项，通过Sysbuild构建。使用`SB_CONFIG_REMOTE_BOARD`指定远端开发板目标。不同平台可能还需要其他设置，例如启动远端处理器核所需的配置。

> 注意：建议通过`-T`选项使用[samples/sysbuild/hello_world/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sysbuild/hello_world/tests.yaml)中的示例配置，以便自动应用远端开发板、配置片段（Snippet）等附加设置。

下面以[nRF54H20 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf54h20dk/doc/index.html#nrf54h20dk)为例，面向应用核（Application core）与无线电核（Radio core）构建并烧录：

```sh
west build -b nrf54h20dk/nrf54h20/cpuapp --sysbuild samples/sysbuild/hello_world -- -DSB_CONFIG_REMOTE_BOARD='"nrf54h20dk/nrf54h20/cpurad"'
west flash
```

也可以使用[samples/sysbuild/hello_world/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sysbuild/hello_world/tests.yaml)中的配置达到相同目的：

```sh
west build -b nrf54h20dk/nrf54h20/cpuapp -T sample.sysbuild.hello_world.nrf54h20dk_cpuapp_cpurad samples/sysbuild/hello_world
west flash
```

将示例烧录到开发板后，应在每个目标所配置的Zephyr控制台看到Hello World消息。以上例为例，应用核输出：

```text
*** Booting Zephyr OS build v3.6.0-274-g466084bd8c5d ***
Hello world from nrf54h20dk/nrf54h20/cpuapp
```

无线电核输出：

```text
*** Booting Zephyr OS build v3.6.0-274-g466084bd8c5d ***
Hello world from nrf54h20dk/nrf54h20/cpurad
```

> 译注——多镜像与启动条件：当前`sysbuild.cmake`通过`ExternalZephyrProject_Add`建立远端镜像，远端CMake文件引用同一份`src/main.c`，并设置构建及烧录依赖。当前`tests.yaml`在上述`-T`场景中配置`SB_CONFIG_REMOTE_NRF54H20_CPURAD_CORE=y`及`hello_world_CONFIG_SOC_NRF54H20_CPURAD_ENABLE=y`，并通过公共设置启用Sysbuild。直接指定远端名称与采用完整测试场景不应被视为在所有版本中都具有相同的启动配置；使用时以目标版本文件为准。这里的版本号与串口日志来自官方示例，未在本次翻译中实际烧录验证。


> 译注——实现依据：[samples/sysbuild/hello_world/sysbuild.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/sysbuild.cmake)、[samples/sysbuild/hello_world/Kconfig.sysbuild](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/Kconfig.sysbuild)、[samples/sysbuild/hello_world/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/tests.yaml)、[samples/sysbuild/hello_world/remote/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/remote/CMakeLists.txt)、[samples/sysbuild/hello_world/pytest/test_both_uart.py](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/pytest/test_both_uart.py)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/sysbuild/hello_world/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/hello_world/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sysbuild/hello_world/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sysbuild/hello_world/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P063_Sysbuild示例目录.md) · [返回大纲](大纲.md) · [下一章](P065_Sysbuild与MCUboot示例.md)
