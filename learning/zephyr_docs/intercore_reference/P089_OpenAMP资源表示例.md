---
id: learning.zephyr-docs.intercore_reference.openampsample-89
title: OpenAMP资源表示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp_rsc_table/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="openamp-rsc-table"></a>

# 第89章\_OpenAMP资源表示例

原文：[OpenAMP using resource table](https://docs.zephyrproject.org/latest/samples/subsys/ipc/openamp_rsc_table/README.html)。读取日期：2026-10-13，`latest`。

本应用展示使用资源表（Resource Table）在Zephyr中运行OpenAMP。它作为应答端，响应[Linux RPMsg客户端示例](https://elixir.bootlin.com/linux/latest/source/samples/rpmsg/rpmsg_client_sample.c)和[Linux RPMsg终端驱动](https://elixir.bootlin.com/linux/latest/source/drivers/tty/rpmsg_tty.c)。

这种实现适用于主处理器（Main Processor）运行Linux内核操作系统（Operating System，OS）、协处理器（Co-processor）运行Zephyr应用的平台。RPMsg为远程处理器消息（Remote Processor Messaging）；TTY指终端接口（原名Teletype）。OpenAMP保留框架名称。

## 89.1\_构建Zephyr应用

原命令在Zephyr仓库根目录执行：

```sh
# From the root of the zephyr repository
west build -b None samples/subsys/ipc/openamp_rsc_table
west build -t test
```

**译注：**原构建片段的`-b None`没有指定有效开发板，不能直接当作已配置的构建目标。此处保留原命令及`test`目标，实际构建仍需依据所用平台选择对应开发板；原页没有给出具体目标替代值。

## 89.2\_运行Linux客户端示例

Linux端启用配置选项`SAMPLE_RPMSG_CLIENT`，构建内核模块（Kernel Module）`rpmsg_client_sample.ko`。Zephyr端打开minicom、PuTTY等串口终端，使用开发板的默认串口设置连接。

在Linux命令行（Shell）中，可经minicom或安全外壳（Secure Shell，SSH）连接，向内核插入`rpmsg_client_sample`模块。随后会出现通道创建／销毁与传入消息日志：

```text
root@linuxshell: insmod rpmsg_client_sample.ko
[   44.625407] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: new channel: 0x401 -> 0x400!
[   44.631401] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: incoming msg 1 (src: 0x400)
[   44.640614] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: incoming msg 2 (src: 0x400)
...
[   45.152269] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: incoming msg 99 (src: 0x400)
[   45.157678] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: incoming msg 100 (src: 0x400)
[   45.158822] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: goodbye!
[   45.159741] virtio_rpmsg_bus virtio0: destroying channel rpmsg-client-sample addr 0x400
[   45.160856] rpmsg_client_sample virtio0.rpmsg-client-sample.-1.1024: rpmsg sample client driver is removed
```

Zephyr每收到一条消息，就显示其内容并回传给Linux。原Zephyr输出如下：

```text
*** Booting Zephyr OS build zephyr-v#.#.#-####-g########## ***
Starting application threads!

OpenAMP[remote] Linux responder demo started

OpenAMP[remote] Linux sample client responder started

OpenAMP[remote] Linux TTY responder started
[Linux sample client] incoming msg 1: hello world!
[Linux sample client] incoming msg 2: hello world!
...
[Linux sample client] incoming msg 99: hello world!
[Linux sample client] incoming msg 100: hello world!
OpenAMP Linux sample client responder ended
```

输出中展示100条`hello world!`消息及应答演示结束，版本中的`#`是原文占位符。

## 89.3\_运行RPMsg终端演示

Linux内核启用`RPMSG_TTY`配置选项。Zephyr端仍使用默认串口设置连接串口终端。

在Linux命令行打印初始化时建立的`rpmsg-tty`端点（Endpoint）收到的消息，再向Zephyr发送消息。Zephyr回应前缀为`TTY <addr>:`，其中`<addr>`是Zephyr的`rpmsg-tty`端点地址：

```sh
$> cat /dev/ttyRPMSG0 &
$> echo "Hello Zephyr" >/dev/ttyRPMSG0
TTY 0x0401: Hello Zephyr
```

Zephyr控制台显示收到的消息，然后将其发送回Linux：

```text
*** Booting Zephyr OS build zephyr-v#.#.#-####-g########## ***
Starting application threads!

OpenAMP[remote] Linux responder demo started

OpenAMP[remote] Linux sample client responder started

OpenAMP[remote] Linux TTY responder started
[Linux TTY] incoming msg: Hello Zephyr
```

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/ipc/openamp_rsc_table)。

---

[上一章：OpenAMP双核通信示例](P088_OpenAMP双核通信示例.md) · [下一章：RPMsg服务示例](P090_RPMsg服务示例.md) · [返回大纲](大纲.md)
