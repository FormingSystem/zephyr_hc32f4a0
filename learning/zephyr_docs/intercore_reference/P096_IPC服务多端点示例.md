---
id: learning.zephyr-docs.intercore_reference.ipcguide-96
title: IPC服务多端点示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/multi_endpoint/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipc_multi_endpoint"></a>

# 第96章\_IPC服务多端点示例

原文：[IPC service: Multi-endpoint](https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/multi_endpoint/README.html)。读取日期：2026-10-13，`latest`。

本应用演示具有多个端点（Endpoint）的处理器间通信（Inter-Processor Communication，IPC）服务。默认后端为`icmsg_me`，也可配置成[ICBMsg](P094_ICBMsg块消息后端.md)；后端名称按原文保留。

## 96.1\_构建应用

在Zephyr仓库根目录，为`nrf5340dk/nrf5340/cpuapp`构建：

```sh
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/ipc/ipc_service/multi_endpoint
west debug
```

## 96.2\_串口运行与原始输出

用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，采用速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。日志中的OS为操作系统（Operating System），HOST为主机端（Host），REMOTE为远端（Remote）；INST为实例（Instance），ENDP为端点（Endpoint）。原版本号、时间与计数按原样保留。

复位后可看到实例0的端点A／B以及实例1的通信。主机端原输出：

```text
*** Booting Zephyr OS build v3.4.0-rc1-108-gccfbac8b0721 ***
IPC-service HOST [INST 0 - ENDP A] demo started
IPC-service HOST [INST 0 - ENDP B] demo started
IPC-service HOST [INST 1] demo started
HOST [0A]: 1
HOST [0A]: 3
HOST [0B]: 1
HOST [1]: 1
...
HOST [0A]: 99
IPC-service HOST [INST 0 - ENDP A] demo ended.
HOST [0B]: 99
IPC-service HOST [INST 0 - ENDP B] demo ended.
HOST [1]: 99
IPC-service HOST [INST 1] demo ended.
```

远端原输出：

```text
*** Booting Zephyr OS build v3.4.0-rc1-108-gccfbac8b0721 ***
IPC-service REMOTE [INST 0 - ENDP A] demo started
IPC-service REMOTE [INST 0 - ENDP B] demo started
IPC-service REMOTE [INST 1] demo started
REMOTE [0A]: 0
REMOTE [0A]: 2
...
REMOTE [0A]: 98
IPC-service REMOTE [INST 0 - ENDP A] demo ended.
REMOTE [0B]: 98
IPC-service REMOTE [INST 0 - ENDP B] demo ended.
REMOTE [1]: 98
IPC-service REMOTE [INST 1] demo ended.
```

## 96.3\_切换到ICBMsg后端

要改用ICBMsg，切换设备树覆盖文件（Devicetree Overlay）：

```sh
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild -- \
-DDTC_OVERLAY_FILE=boards/nrf5340dk_nrf5340_cpuapp_icbmsg.overlay \
-Dremote_DTC_OVERLAY_FILE=boards/nrf5340dk_nrf5340_cpunet_icbmsg.overlay
```

原命令通过`DTC_OVERLAY_FILE`指定本地覆盖文件，通过`remote_DTC_OVERLAY_FILE`指定远端覆盖文件，并使用`--sysbuild`。**译注：**该代码块未列出示例源码目录；应在已明确该应用来源的构建上下文中使用，不能把它理解为在任意无关目录都能自动找到示例。原参数与路径未修改。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/ipc_service/multi_endpoint)。

另见[IPC接口](P181_IPC接口总览.md)。

---

[上一章：IPC服务ICMsg示例](P095_IPC服务ICMsg示例.md) · [下一章：IPC服务RPMSG-Lite示例](P097_IPC服务RPMSG-Lite示例.md) · [返回大纲](大纲.md)
