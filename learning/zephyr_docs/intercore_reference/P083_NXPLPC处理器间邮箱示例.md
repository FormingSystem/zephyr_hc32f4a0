---
id: learning.zephyr-docs.intercore_reference.ipmsample-83
title: NXPLPC处理器间邮箱示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_mcux/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipm-mcux"></a>

# 第83章\_NXPLPC处理器间邮箱示例

原文：[IPM on NXP LPC](https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_mcux/README.html)。读取日期：2026-10-13，`latest`。

NXP LPC系列中的部分微控制器（Microcontroller）具有双核。本示例使用邮箱（Mailbox）把消息从一个处理器核心发送到另一个核心，即处理器间邮箱（Inter-Processor Mailbox，IPM）通信。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 83.1\_适用开发板与要求

| 开发板 | 双核组成 |
| --- | --- |
| [LPCXPRESSO54114](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso54114/doc/index.html#lpcxpresso54114) | Cortex-M4F和Cortex-M0+ |
| [LPCXPRESSO55S69](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#lpcxpresso55s69) | 两个Cortex-M33 |

原“要求”章节同样列出上述两款开发板，选择对应目标进行构建。

## 83.2\_构建LPCXPRESSO54114应用

以下原命令在Zephyr仓库根目录执行，通过系统构建（Sysbuild）构建，随后启动调试：

```sh
# From the root of the zephyr repository
west build -b lpcxpresso54114/lpc54114/m4 --sysbuild samples/drivers/ipm/ipm_mcux
west debug
```

## 83.3\_构建LPCXPRESSO55S69应用

同样在Zephyr仓库根目录执行：

```sh
# From the root of the zephyr repository
west build -b lpcxpresso55s69/lpc55s69/cpu0 --sysbuild samples/drivers/ipm/ipm_mcux
west debug
```

## 83.4\_运行与原始输出

使用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，设置如下：

| 项目 | 值 |
| --- | --- |
| 速率（Speed） | 115200 |
| 数据位（Data Bits） | 8 |
| 校验（Parity） | 无（None） |
| 停止位（Stop Bits） | 1 |

复位开发板后，对应串口出现下列消息，表示主端（Master）输出问候并接收计数值1至99。原历史版本日志保持原样：

```text
***** Booting Zephyr OS v1.11.0-764-g4e3007a *****
Hello World from MASTER! arm
Received: 1
...
Received: 99
```

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/ipm/ipm_mcux)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：IVSHMEM处理器间邮箱示例](P082_IVSHMEM处理器间邮箱示例.md) · [下一章：ArmMHU双核IPM示例](P084_ArmMHU双核IPM示例.md) · [返回大纲](大纲.md)
