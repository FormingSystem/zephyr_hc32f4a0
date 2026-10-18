---
id: learning.zephyr-docs.intercore_reference.openampsample-90
title: RPMsg服务示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/rpmsg_service/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="rpmsg-service"></a>

# 第90章\_RPMsg服务示例

原文：[RPMsg service](https://docs.zephyrproject.org/latest/samples/subsys/ipc/rpmsg_service/README.html)。读取日期：2026-10-13，`latest`。

RPMsg服务（RPMsg Service）是在OpenAMP之上建立的抽象层，用于简化初始化与端点（Endpoint）创建。RPMsg指远程处理器消息（Remote Processor Messaging），OpenAMP保留原框架名称。本应用从构建和代码两个方面展示如何在Zephyr中集成该服务。

主核心（Primary Core）与远端核心（Remote Core）的镜像可以分别烧录；若要一次性烧录两个镜像，原文要求使用系统构建（Sysbuild）。下列原命令块没有`--sysbuild`参数，分别按原样保留，不把它们改写为一步烧录命令。

各命令均从Zephyr仓库根目录执行。日志中的OS为操作系统（Operating System），Master为主端，Remote为远端。

## 90.1\_构建nrf5340dk

目标为`nrf5340dk/nrf5340/cpuapp`。

```sh
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/ipc/rpmsg_service
west debug
```

## 90.2\_构建mps2

目标为`mps2/an521/cpu0`。

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0 samples/subsys/ipc/rpmsg_service
west debug
```

## 90.3\_构建v2m_musca_b1

目标为`v2m_musca_b1/musca_b1`。

```sh
# From the root of the zephyr repository
west build -b v2m_musca_b1/musca_b1 samples/subsys/ipc/rpmsg_service
west debug
```

## 90.4\_通用运行与输出

使用minicom、PuTTY等串口终端（Serial Terminal），配置速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。复位开发板后，对应串口分别出现主端和远端输出。主端收到奇数1至99，远端收到偶数0至98，随后演示结束：

```text
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

```text
**** Booting Zephyr OS build zephyr-v1.14.0-2064-g888fc98fddaa ****
Starting application thread!

RPMsg Service [remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
RPMsg Service demo ended.
```

## 90.5\_构建与运行BL5340开发套件

分别为应用核心（Application Core）和网络核心（Network Core）构建、调试：

```sh
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpuapp samples/subsys/ipc/rpmsg_service
west debug
```

```sh
# From the root of the zephyr repository
west build -b bl5340_dvk/nrf5340/cpunet samples/subsys/ipc/rpmsg_service
west debug
```

使用minicom、PuTTY等串口终端（Serial Terminal），配置速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。两个串口均使用这些设置。烧录应用核心与网络核心的镜像后复位开发套件，对应串口分别输出：

```text
*** Booting Zephyr OS build v2.7.0-rc1-103-ge19875c88916  ***
Starting application thread!

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

```text
*** Booting Zephyr OS build v2.7.0-rc1-103-ge19875c88916  ***
Starting application thread!

RPMsg Service [remote] demo started
Remote core received a message: 0
Remote core received a message: 2
Remote core received a message: 4
...
Remote core received a message: 98
RPMsg Service demo ended.
```

## 90.6\_构建STM32H747I-DISCO应用

原页标题使用`stm32h747i_disco/stm32h7xx`，命令目标为`stm32h747i_disco/stm32h7xx/m7`：

```sh
# From the root of the zephyr repository
west build -b stm32h747i_disco/stm32h7xx/m7 samples/subsys/ipc/rpmsg_service
west debug
```

原串口输出：

```text
*** Booting Zephyr OS build 15736b7415be ***
Starting application thread!

RPMsg Service [master] demo started
Master core received a message: 1
Master core received a message: 3
Master core received a message: 5
...
Master core received a message: 99
RPMsg Service demo ended.
```

**译注：**此处目标拼写与[H7硬件信号量示例](P087_STM32H7双核信号量示例.md)的`stm32h747xx`不同，按各自原页保留；上述版本号与计数均为历史示例输出，并非本次构建或硬件测试结果。

另见[RPMsg服务应用程序编程接口（Application Programming Interface，API）](P121_RPMsg服务公共接口.md)。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/rpmsg_service)。

---

[上一章：OpenAMP资源表示例](P089_OpenAMP资源表示例.md) · [下一章：RenesasLinux与Zephyr通信示例](P091_RenesasLinux与Zephyr通信示例.md) · [返回大纲](大纲.md)
