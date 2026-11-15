---
id: learning.zephyr-docs.intercore_reference.ipcguide-95
title: IPC服务ICMsg示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/icmsg/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipc-icmsg"></a>

# 第95章\_IPC服务ICMsg示例

原文：[IPC service: icmsg backend](https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/icmsg/README.html)。读取日期：2026-10-13，`latest`。

本应用演示在Zephyr中使用处理器间通信（Inter-Processor Communication，IPC）服务与核间消息（Inter Core Messaging，ICMsg）后端，从构建与代码两个方面展示集成方式。后端说明见[ICMsg消息后端](P093_ICMsg消息后端.md)。

## 95.1\_构建应用

在Zephyr仓库根目录，为`nrf5340dk/nrf5340/cpuapp`通过系统构建（Sysbuild）构建并调试：

```sh
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/subsys/ipc/ipc_service/icmsg
west debug
```

## 95.2\_运行与原始输出

用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，采用速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。日志中的OS为操作系统（Operating System），HOST为主机端（Host），REMOTE为远端（Remote）；INST为实例（Instance），ENDP为端点（Endpoint）。原版本号、时间与计数按原样保留。

复位开发板后，对应串口分别显示主机端和远端输出。主机端日志展示发送1000毫秒、等待500毫秒让网络核心完成发送、停止网络核心、重置IPC服务并重新运行网络核心的过程：

```text
*** Booting Zephyr OS build zephyr-v3.2.0-323-g468d4ae383c1  ***
[00:00:00.415,985] <inf> host: IPC-service HOST demo started
[00:00:00.417,816] <inf> host: Ep bounded
[00:00:00.417,877] <inf> host: Perform sends for 1000 [ms]
[00:00:01.417,114] <inf> host: Sent 488385 [Bytes] over 1000 [ms]
[00:00:01.417,175] <inf> host: Wait 500ms. Let net core finish its sends
[00:00:01.917,266] <inf> host: Stop network core
[00:00:01.917,297] <inf> host: Reset IPC service
[00:00:01.917,327] <inf> host: Run network core
[00:00:01.924,865] <inf> host: Ep bounded
[00:00:01.924,896] <inf> host: Perform sends for 1000 [ms]
[00:00:02.924,194] <inf> host: Sent 489340 [Bytes] over 1000 [ms]
[00:00:02.924,224] <inf> host: IPC-service HOST demo ended
```

远端原输出如下，其中RTC表示实时时钟（Real-time Clock），同步时间戳提示和重启日志保持原样：

```text
*** Booting Zephyr OS build zephyr-v3.2.0-323-g468d4ae383c1  ***
[00:00:00.006,256] <inf> remote: IPC-service REMOTE demo started
[00:00:00.006,378] <inf> remote: Ep bounded
[00:00:00.006,439] <inf> remote: Perform sends for 1000 [ms]
[00:00:00.833,160] <inf> sync_rtc: Updated timestamp to synchronized RTC by 1)
[00:00:01.417,572] <inf> remote: Sent 235527 [Bytes] over 1000 [ms]
[00:00:01.417,602] <inf> remote: IPC-service REMOTE demo ended
*** Booting Zephyr OS build zephyr-v3.2.0-323-g468d4ae383c1  ***
[00:00:00.006,256] <inf> remote: IPC-service REMOTE demo started
[00:00:00.006,347] <inf> remote: Ep bounded
[00:00:00.006,378] <inf> remote: Perform sends for 1000 [ms]
[00:00:01.006,164] <inf> remote: Sent 236797 [Bytes] over 1000 [ms]
[00:00:01.006,195] <inf> remote: IPC-service REMOTE demo ended
```

这些发送字节数为原示例输出，不能当作本次测得的吞吐性能。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/ipc_service/icmsg)。

另见[IPC接口](P181_IPC接口总览.md)。

---

[上一章：ICBMsg块消息后端](P094_ICBMsg块消息后端.md) · [下一章：IPC服务多端点示例](P096_IPC服务多端点示例.md) · [返回大纲](大纲.md)
