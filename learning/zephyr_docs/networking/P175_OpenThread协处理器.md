---
id: learning.zephyr-docs.networking.page-175
title: OpenThread协处理器
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/openthread/coprocessor/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第175章\_OpenThread协处理器

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/openthread/coprocessor/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

OpenThread 协处理器（Co-Processor）可用于构建 Thread 边界路由器（Thread Border Router）。本示例代码仅包含完整边界路由器的 MCU 目标端部分。

协处理器有两种形式：网络协处理器（Network Co-Processor，NCP）和无线电协处理器（Radio Co-Processor，RCP），详见官方[协处理器架构说明](https://openthread.io/platforms/co-processor)。搭建完整边界路由器还需要主机端工具，例如 `otbr-agent`，可按照[边界路由器主机构建指南](https://openthread.io/guides/border-router/build-docker)获取并配置。

> 链接译注：原文的 `guides/border-router/build#set-up-the-border-router` 当前重定向至 Docker 构建指南，旧章节锚点已不存在；上面的入口已指向实际落地页面。部署方式以该页面当前要求为准，不把旧锚点当作仍可定位的步骤。

原文指出，OpenThread 目前优先采用 RCP 配置。

源码位于官方[samples/net/openthread/coprocessor](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/openthread/coprocessor)。

## 2. 构建与运行

在具备相应目标板依赖的 Zephyr 环境中，从读者自己的 Zephyr 源码根目录构建 NCP 示例：

```sh
west build -b <board to use> samples/net/openthread/coprocessor -- -DCONF_FILE=<config file to use>
```

`<board to use>` 和 `<config file to use>` 是需要替换的占位符。

使用 USB 通信设备类抽象控制模型（Communications Device Class Abstract Control Model，CDC ACM）UART 设备的 NCP 示例：

```sh
west build -b nrf52840dk/nrf52840 samples/net/openthread/coprocessor -- -DDTC_OVERLAY_FILE=usb.overlay -DEXTRA_CONF_FILE=overlay-usb-nrf-br.conf
west flash
```

在 `nrf52840dk/nrf52840` 上构建 RCP 的示例：

```sh
west build -b nrf52840dk/nrf52840 samples/net/openthread/coprocessor -- -DEXTRA_CONF_FILE=overlay-rcp.conf
west flash
```

> 译注：`DTC_OVERLAY_FILE` 选择设备树覆盖文件，`EXTRA_CONF_FILE` 在基础配置上追加 Kconfig 配置，它们修改的对象不同。上述命令仍需与实际连接开发板对应，`west flash` 会写入设备。USB 传输配置与 NCP／RCP 角色也不是同一个选择维度；只加入 USB 覆盖配置不会自动把 NCP 改成 RCP。

## 3. 配置文件

`coprocessor` 示例目录为不同开发板及组合提供以下文件：

| 文件 | 说明 |
| --- | --- |
| `prj.conf` | 通用 NCP 配置，需要 NCP 时使用。 |
| `overlay-rcp.conf` | RCP 覆盖配置；需要 RCP 时与 `prj.conf` 组合。 |
| `overlay-tri-n4m-br.conf` | 专用 Thread 边界路由器硬件的覆盖配置。产品资料见原文[Tridonic net4more Borderrouter PoE-Thread 数据表](https://www.tridonic.com/com/en/download/data_sheets/net4more_Borderrouter_PoE-Thread_en.pdf)。该板的支持不在 Zephyr 仓库中，产品基于 NXP K64 和 AT86RF233；可将此文件作为由开发板组成实验系统的配置示例。 |

> 源码对照：当前[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coprocessor/prj.conf)启用 [`CONFIG_OPENTHREAD_COPROCESSOR_NCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_COPROCESSOR_NCP)；[overlay-rcp.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/coprocessor/overlay-rcp.conf)显式关闭 NCP 并打开 RCP，因此原文所说的“组合”是必要的基础配置关系。通用命令使用 `CONF_FILE` 选择整组文件，不能仅指定一份 RCP 增量文件就假定默认基础配置仍会自动加入。

## 4. 另见（See Also）

[OpenThread 协议栈 API](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html)。

> 验证边界：本页完成官方示例翻译与配置核对；没有构建、烧写、连接协处理器或部署主机侧 `otbr-agent`。仅 MCU 示例构建成功也不等于完整边界路由器工作正常。


<a id="openthread-coprocessor"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P174_OpenThread的CoAP示例.md) · [返回大纲](大纲.md) · [下一章](P176_OpenThread命令行示例.md)
