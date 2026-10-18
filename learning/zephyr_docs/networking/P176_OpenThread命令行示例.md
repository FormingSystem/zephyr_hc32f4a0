---
id: learning.zephyr-docs.networking.page-176
title: OpenThread命令行示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/openthread/shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_OpenThread命令行示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/openthread/shell/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例通过 OpenThread 命令行（Shell），在不同开发板上测试 Thread 协议和底层 IEEE 802.15.4 驱动。官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/openthread/shell)提供配置与入口。

## 2. 构建与运行

首先确认目标开发板和芯片提供 IEEE 802.15.4 支持。原文在 `shell` 示例目录中列出以下配置：

| 文件 | 原文用途 |
| --- | --- |
| `prj.conf` | 通用配置。 |
| `overlay-ot-rcp-host-nxp.conf` | 启用 NXP 芯片上通过 IMU 接口运行的 OpenThread 无线电协处理器主机（Radio Co-Processor Host，RCP Host）支持。 |

> 源码差异：当前[示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/openthread/shell)包含 `prj-ot-host.conf` 和 `prj-ot-host-no-l2-nxp-mcxw.conf`，不再列出上述旧名称 `overlay-ot-rcp-host-nxp.conf`。下文官方构建示例也已使用这些现有文件，因此以对应命令和实际版本的目录为准，不手工创建一个仅同名的空覆盖文件。

在具备目标板依赖的 Zephyr 环境中，从读者自己的 Zephyr 源码根目录构建：

```sh
west build -b <board to use> samples/net/openthread/shell -- -DCONF_FILE=<config file to use>
```

Nordic nRF52840 DK 示例：

```sh
west build -b nrf52840dk/nrf52840 samples/net/openthread/shell -- -DCONF_FILE="prj.conf"
```

NXP RW612 FRDM 的 RCP Host 示例：

```sh
west build -b frdm_rw612 samples/net/openthread/shell -- -DEXTRA_CONF_FILE="prj-ot-host.conf"
```

NXP MCXW72 FRDM 的主机侧示例：

```sh
west build -b frdm_mcxw72/mcxw727c samples/net/openthread/shell -- -DEXTRA_CONF_FILE="prj-ot-host.conf"
```

同一 MCXW72 FRDM 使用厂商专用无线电实现的示例：

```sh
west build -b frdm_mcxw72/mcxw727c samples/net/openthread/shell -- -DEXTRA_CONF_FILE="prj-ot-host.conf;prj-ot-host-no-l2-nxp-mcxw.conf"
```

Silicon Labs EFR32MG24 4187c 无线电板示例：

```sh
west build -b xg24_rb4187c samples/net/openthread/shell -- -DCONF_FILE="prj.conf"
```

> 译注：`CONF_FILE` 指定应用配置集合，`EXTRA_CONF_FILE` 则追加配置；多文件示例中的分号和引号应保留。这里不同命令对应不同平台和无线电架构，并非依次执行的步骤。

> 源码对照：当前[无 L2 的 MCXW 配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/shell/prj-ot-host-no-l2-nxp-mcxw.conf)关闭 Zephyr [`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING) 与 [`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)，启用独立 OpenThread 模块及系统初始化，并用相对文件名 `nxp_mcxw_radio.c` 选择厂商无线电实现。因此，该示例不能被解释为所有 OpenThread 应用都必须启用 Zephyr L2；不同接入方式见[Thread 协议指南](P171_Thread协议.md)。

## 3. 控制台交互示例

在设备控制台运行原文命令：

```console
uart:~$ ot scan
| PAN  | MAC Address      | Ch | dBm | LQI |
+------+------------------+----+-----+-----+
| fe09 | abcdef1234567890 | 15 | -78 |  60 |
Done
```

结果各列为个域网标识（Personal Area Network，PAN）、MAC 地址、信道（Channel，Ch）、以 dBm 表示的接收功率，以及链路质量指示（Link Quality Indicator，LQI）。此处 `fe09`、地址、信道 `15` 和信号值属于官方示例。扫描到网络不等于已经加入网络；`Done` 也只表示该命令完成。本次未执行扫描或实板组网。

## 4. 另见（See Also）

[网络统计库（Network Statistics Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html)。


<a id="openthread-shell"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-console-interaction"></a>
<a id="see-also"></a>

[上一章](P175_OpenThread协处理器.md) · [返回大纲](大纲.md) · [下一章](P177_IEEE802154串口无线电.md)
