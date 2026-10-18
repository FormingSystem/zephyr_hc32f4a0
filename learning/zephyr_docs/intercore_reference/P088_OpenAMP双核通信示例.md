---
id: learning.zephyr-docs.intercore_reference.openampsample-88
title: OpenAMP双核通信示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="openamp"></a>

# 第88章\_OpenAMP双核通信示例

原文：[OpenAMP](https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp/README.html)。读取日期：2026-10-13，`latest`。

本应用演示在Zephyr中使用OpenAMP，并从构建与代码两个方面展示其集成方式。OpenAMP为原框架名称，示例在主核心（Primary Core）与远端核心（Remote Core）之间发送消息。

两个核心的镜像（Image）可以分别烧录，但**必须使用系统构建（Sysbuild）生成镜像**。在任意一个核心上使用`west debug`前，必须先烧录两个核心；原文建议按以下命令使用`west flash`完成烧录。

以下构建命令均从Zephyr仓库根目录执行。日志中的OS表示操作系统（Operating System），版本字符串保留原样。

## 88.1\_构建lpcxpresso54114

目标为`lpcxpresso54114/lpc54114/m4`。

```sh
# From the root of the zephyr repository
west build -b lpcxpresso54114/lpc54114/m4 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.2\_构建lpcxpresso55s69

目标为`lpcxpresso55s69/lpc55s69/cpu0`。

```sh
# From the root of the zephyr repository
west build -b lpcxpresso55s69/lpc55s69/cpu0 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.3\_构建mps2

目标为`mps2/an521/cpu0`。

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.4\_构建v2m_musca_b1

目标为`v2m_musca_b1/musca_b1`。

```sh
# From the root of the zephyr repository
west build -b v2m_musca_b1/musca_b1 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.5\_构建mimxrt1170_evk_cm7

目标为`mimxrt1170_evk_cm7`。

```sh
# From the root of the zephyr repository
west build -b mimxrt1170_evk_cm7 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.6\_构建frdm_mcxn947

目标为`frdm_mcxn947/mcxn947/cpu0`。

```sh
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --sysbuild samples/subsys/ipc/openamp
west flash
```

## 88.7\_构建ek_ra8p1

目标为`ek_ra8p1/r7ka8p1kflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 --sysbuild samples/subsys/ipc/openamp
west debug
```

## 88.8\_构建ek_ra8d2

目标为`ek_ra8d2/r7ka8d2kflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b ek_ra8d2/r7ka8d2kflcac/cm85 --sysbuild samples/subsys/ipc/openamp
west debug
```

## 88.9\_构建ek_ra8m2

目标为`ek_ra8m2/r7ka8m2jflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b ek_ra8m2/r7ka8m2jflcac/cm85 --sysbuild samples/subsys/ipc/openamp
west debug
```

## 88.10\_构建ek_ra8t2

目标为`ek_ra8t2/r7ka8t2lflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b ek_ra8t2/r7ka8t2lflcac/cm85 --sysbuild samples/subsys/ipc/openamp
west debug
```

## 88.11\_构建mck_ra8t2

目标为`mck_ra8t2/r7ka8t2lflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b mck_ra8t2/r7ka8t2lflcac/cm85 --sysbuild samples/subsys/ipc/openamp
west debug
```

## 88.12\_串口运行与原始输出

使用minicom、PuTTY等串口终端（Serial Terminal），配置速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。复位开发板后，两个对应串口分别输出主端（Master）和远端（Remote）的消息。

主端收到1、3、5直至99，随后演示结束：

```text
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

OpenAMP[master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
OpenAMP demo ended.
```

远端收到0、2、4直至98，随后演示结束：

```text
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

OpenAMP[remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
OpenAMP demo ended.
```

**译注：**前六组原命令使用`west flash`，后五组瑞萨目标命令使用`west debug`。后者仍须遵守原概述“调试前两个核心均已烧录”的条件，不能因为命令块省略烧录步骤而忽略此前提。原目标`mimxrt1170_evk_cm7`和历史日志`zephyr-v1.14.0-2064-g888fc98fddaa`按原样保留。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/openamp)。

---

[上一章：STM32H7双核信号量示例](P087_STM32H7双核信号量示例.md) · [下一章：OpenAMP资源表示例](P089_OpenAMP资源表示例.md) · [返回大纲](大纲.md)
