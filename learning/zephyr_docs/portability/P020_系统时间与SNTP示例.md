---
id: learning.zephyr-docs.portability.page-20
title: 系统时间与SNTP示例
kind: reference
status: maintained
domains: [zephyr, portability, posix]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/gettimeofday/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_系统时间与SNTP示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/portability/posix/gettimeofday/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 20.1\_概述

本示例调用 POSIX [`gettimeofday()`](https://pubs.opengroup.org/onlinepubs/009604599/functions/gettimeofday.html) 函数，每秒显示绝对墙上时钟时间（Wall Clock Time）和本地时间（Local Time）。系统启动时通过简单网络时间协议（Simple Network Time Protocol，SNTP）查询当前时间；设置 [`CONFIG_NET_CONFIG_CLOCK_SNTP_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_CLOCK_SNTP_INIT) 和 [`CONFIG_NET_CONFIG_SNTP_INIT_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_SNTP_INIT_SERVER) 选项即可启用这一初始化过程。

> 译注：这里的墙上时钟用于表示日期和时刻，与从启动开始累计的运行时间不同。当前源码每轮调用 [`gettimeofday()`](https://pubs.opengroup.org/onlinepubs/009604599/functions/gettimeofday.html)，再通过 `time()`、`localtime_r()` 和 `asctime()` 形成可读时间；`tv_sec` 分为高、低部分输出，`tv_usec` 表示微秒。本地时间的具体时区取决于所用运行环境，不能仅凭函数名认定已配置为读者所在地时区。

## 20.2\_要求

- 按[与宿主系统联网](../networking/P007_与主机系统联网.md#networking-with-host)建立连接，或者使用具有硬件网络接口的开发板。
- 配置网络地址转换（Network Address Translation，NAT）／路由，使系统能够访问互联网。
- 宿主上应提供用于解析域名的域名系统（Domain Name System，DNS）服务器。

> 译注：当前 `prj.conf` 使用 `time.nist.gov`，并启用 `CONFIG_NET_CONFIG_SNTP_INIT_RESYNC`；网络地址与 DNS 配置采用官方网络实验布局。实际运行前应按上面的联网文档配置自己的网络，不能只完成编译就认为时间同步已经成功。该配置和程序属于官方示例，不依赖本仓库作者的网络或磁盘目录。

## 20.3\_构建与运行

本项目向控制台输出信息，可按下列方式在 QEMU 上构建和运行。

> 译注：在所使用的 Zephyr 源码根目录执行，先准备目标工具链、QEMU 和上一节的网络条件。若构建成功但时间不正确，应返回联网与 DNS／SNTP 配置环节核对。

```bash
west build -b qemu_x86 samples/subsys/portability/posix/gettimeofday
west build -t run
```

作为对照，如果宿主操作系统（Host OS）符合 POSIX，例如 Linux，也可以直接为宿主构建：

```bash
cd samples/subsys/portability/posix/gettimeofday
make -f Makefile.host
```

`make` 的输出文件位于 `samples/subsys/portability/posix/gettimeofday/build`。

> 译注：宿主路线需要 C 编译器与 `make`，上述 `cd` 从源码根目录出发。当前 `Makefile.host` 将可执行程序放在样例目录下的 `build/gettimeofday`。这条路线直接编译 `src/main.c`，读取宿主已有系统时钟，不应用 Zephyr 的 `prj.conf`，因此不会由这份配置替宿主执行 SNTP 初始化。官方页面没有给出具体输出日志，本译文也不补造实测结果。


译注核对来源：[samples/subsys/portability/posix/gettimeofday/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/gettimeofday/src/main.c)、[samples/subsys/portability/posix/gettimeofday/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/gettimeofday/prj.conf)、[samples/subsys/portability/posix/gettimeofday/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/gettimeofday/tests.yaml)、[samples/subsys/portability/posix/gettimeofday/Makefile.host](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/portability/posix/gettimeofday/Makefile.host)。

本仓库的[对应源码](../../../samples/subsys/portability/posix/gettimeofday/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-gettimeofday"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>

[上一章](P019_eventfd事件通知示例.md) · [返回大纲](大纲.md) · [下一章](P021_POSIX哲学家就餐示例.md)
