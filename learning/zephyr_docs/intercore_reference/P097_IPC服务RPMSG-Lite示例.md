---
id: learning.zephyr-docs.intercore_reference.ipcguide-97
title: IPC服务RPMSG-Lite示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/rpmsg_lite/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="rpmsg-lite"></a>

# 第97章\_IPC服务RPMSG-Lite示例

原文：[IPC service: RPMSG-Lite backend](https://docs.zephyrproject.org/latest/samples/subsys/ipc/ipc_service/rpmsg_lite/README.html)。读取日期：2026-10-13，`latest`。

本应用展示如何在Zephyr中使用处理器间通信（Inter-Processor Communication，IPC）服务的RPMSG-Lite后端，并涵盖构建与代码集成。RPMSG-Lite保留原传输库名称。它在功能上等同于[OpenAMP静态虚拟环示例](P098_IPC服务静态虚拟环示例.md)，但底层传输使用RPMSG-Lite。

## 97.1\_三个顺序执行的实例

实例（Instance）按顺序运行：实例N必须等实例N−1完成交换后才开始。

| 实例 | 演示内容 |
| --- | --- |
| 0 | 主机与远端通过一个具名端点（Named Endpoint）进行普通拷贝收发 |
| 1 | 零拷贝（Zero-copy）接口：`ipc_service_get_tx_buffer``ipc_service_send_nocopy``ipc_service_release_rx_buffer` |
| 2 | 第二个普通拷贝实例；验证多个非所有者实例共用一条物理邮箱通道时，`platform_notify()`的所有者查找（Owner Search）仍能把通知路由到匹配的链接标识`link-id` |

RPMSG-Lite要求邮箱（Mailbox，MBOX）驱动支持**数据传输模式（Data-transfer Mode）**。全部IPC实例通过设备树属性`notification-parent`共用一对发送（Transmit，TX）与接收（Receive，RX）通道；属性`link-id`选择该实例所属的RPMSG-Lite链接。**链接标识必须从0开始连续编号**。

## 97.2\_构建与运行

支持的开发板列于原示例`tests.yaml`中。使用系统构建（Sysbuild）一次编译主机与远端镜像（Image），在Zephyr仓库根目录执行：

```sh
# From the root of the zephyr repository
west build -b mimxrt1170_evk@B/mimxrt1176/cm7 --sysbuild samples/subsys/ipc/ipc_service/rpmsg_lite
west flash
```

用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，采用速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。日志中的OS为操作系统（Operating System），HOST为主机端（Host），REMOTE为远端（Remote）；INST为实例（Instance），ENDP为端点（Endpoint）。原版本号、时间与计数按原样保留。

复位开发板后，两个串口分别显示主机与远端消息。

## 97.3\_原始输出

主机端：

```text
*** Booting Zephyr OS build v4.x.x ***
IPC-service HOST [INST 0] demo started
HOST [0]: 1
HOST [0]: 3
HOST [0]: 5
HOST [0]: 7
HOST [0]: 9
HOST [0]: 11
HOST [0]: 13
HOST [0]: 15
HOST [0]: 17
HOST [0]: 19
IPC-service HOST [INST 0] demo ended.
IPC-service HOST [INST 1] demo started
HOST [1]: 1
HOST [1]: 3
HOST [1]: 5
...
HOST [1]: 37
HOST [1]: 39
IPC-service HOST [INST 1] demo ended.
IPC-service HOST [INST 2] demo started
HOST [2]: 1
HOST [2]: 3
HOST [2]: 5
HOST [2]: 7
HOST [2]: 9
HOST [2]: 11
HOST [2]: 13
HOST [2]: 15
HOST [2]: 17
HOST [2]: 19
IPC-service HOST [INST 2] demo ended.
```

远端：

```text
*** Booting Zephyr OS build v4.x.x ***
IPC-service REMOTE [INST 0] demo started
REMOTE [0]: 0
REMOTE [0]: 2
REMOTE [0]: 4
REMOTE [0]: 6
REMOTE [0]: 8
REMOTE [0]: 10
REMOTE [0]: 12
REMOTE [0]: 14
REMOTE [0]: 16
REMOTE [0]: 18
IPC-service REMOTE [INST 0] demo ended.
IPC-service REMOTE [INST 1] demo started
REMOTE [1]: 0
REMOTE [1]: 2
REMOTE [1]: 4
...
REMOTE [1]: 36
REMOTE [1]: 38
IPC-service REMOTE [INST 1] demo ended.
IPC-service REMOTE [INST 2] demo started
REMOTE [2]: 0
REMOTE [2]: 2
REMOTE [2]: 4
REMOTE [2]: 6
REMOTE [2]: 8
REMOTE [2]: 10
REMOTE [2]: 12
REMOTE [2]: 14
REMOTE [2]: 16
REMOTE [2]: 18
IPC-service REMOTE [INST 2] demo ended.
```

原例实例0与2分别显示主机奇数1至19、远端偶数0至18；实例1显示主机至39、远端至38。版本`v4.x.x`是原日志占位表示。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/ipc_service/rpmsg_lite)。

另见[IPC接口](P181_IPC接口总览.md)。

---

[上一章：IPC服务多端点示例](P096_IPC服务多端点示例.md) · [下一章：IPC服务静态虚拟环示例](P098_IPC服务静态虚拟环示例.md) · [返回大纲](大纲.md)
