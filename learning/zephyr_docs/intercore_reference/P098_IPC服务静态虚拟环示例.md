---
id: learning.zephyr-docs.intercore_reference.ipcguide-98
title: IPC服务静态虚拟环示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/static_vrings/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipc-static-vrings"></a>

# 第98章\_IPC服务静态虚拟环示例

原文：[IPC service: static vrings backend](https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/static_vrings/README.html)。读取日期：2026-10-13，`latest`。

本应用演示在Zephyr中使用处理器间通信（Inter-Processor Communication，IPC）服务与静态虚拟环（Static Vrings）后端，从构建与代码两个方面展示集成方式。以下命令都在Zephyr仓库根目录执行，使用系统构建（Sysbuild）和`west debug`。

## 98.1\_构建nrf5340dk

开发板目标为`nrf5340dk/nrf5340/cpuapp`。

```sh
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.2\_构建lpcxpresso55s69

开发板目标为`lpcxpresso55s69/lpc55s69/cpu0`。

```sh
# From the root of the zephyr repository
west build -b lpcxpresso55s69/lpc55s69/cpu0 --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.3\_构建mimxrt1160_evk

开发板目标为`mimxrt1160_evk/mimxrt1166/cm7`。

```sh
# From the root of the zephyr repository
west build -b mimxrt1160_evk/mimxrt1166/cm7 --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.4\_构建mimxrt1170_evk

开发板目标为`mimxrt1170_evk/mimxrt1176/cm7`。

```sh
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.5\_构建frdm_mcxn947

开发板目标为`frdm_mcxn947/mcxn947/cpu0`。

```sh
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.6\_构建ek_ra8p1

开发板目标为`ek_ra8p1/r7ka8p1kflcac/cm85`。

```sh
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 --sysbuild samples/subsys/ipc/ipc_service/static_vrings
west debug
```

## 98.7\_串口运行与原始输出

用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，采用速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。日志中的OS为操作系统（Operating System），HOST为主机端（Host），REMOTE为远端（Remote）；INST为实例（Instance），ENDP为端点（Endpoint）。原版本号、时间与计数按原样保留。

复位后，对应串口分别显示主机端与远端日志，包含实例0的端点A／B和实例1。

```text
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
IPC-service HOST [INST 0 - ENDP A] demo started
IPC-service HOST [INST 0 - ENDP B] demo started
IPC-service HOST [INST 1] demo started
HOST [1]: 1
HOST [1]: 3
HOST [1]: 5
HOST [1]: 7
HOST [1]: 9
...
```

```text
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
IPC-service REMOTE [INST 0 - ENDP A] demo started
IPC-service REMOTE [INST 0 - ENDP B] demo started
IPC-service REMOTE [INST 1] demo started
REMOTE [1]: 0
REMOTE [1]: 2
REMOTE [1]: 4
REMOTE [1]: 6
REMOTE [1]: 8
...
```

原日志中的省略号和`zephyr-v3.1.0-2383-g147aee22f273`版本字符串均保留，不代表本次运行。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/ipc_service/static_vrings)。

另见[IPC接口](P181_IPC接口总览.md)。

---

[上一章：IPC服务RPMSG-Lite示例](P097_IPC服务RPMSG-Lite示例.md) · [下一章：Infineon处理器间通信绑定](P099_Infineon处理器间通信绑定.md) · [返回大纲](大纲.md)
