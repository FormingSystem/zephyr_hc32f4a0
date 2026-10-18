---
id: learning.zephyr-docs.intercore_reference.ipmsample-81
title: NXPiMX处理器间邮箱示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_imx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipm-imx"></a>

# 第81章\_NXPiMX处理器间邮箱示例

原文：[IPM on NXP i.MX](https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_imx/README.html)。读取日期：2026-10-13，`latest`。

本简单示例适用于带消息单元（Messaging Unit，MU）外设的多核i.MX片上系统（System on Chip，SoC）。示例通过处理器间邮箱（Inter-Processor Mailbox，IPM）读取MU收到的数据，原样回传，并在控制台打印接收信息。回传时会阻塞，直到远端读取数据。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 81.1\_寄存器与通道配置

i.MX消息单元提供四个32位发送寄存器和四个32位接收寄存器。以下配置选项决定这些寄存器如何形成IPM通道：

| 配置选项 | 形成的通道 |
| --- | --- |
| [`CONFIG_IPM_IMX_MAX_DATA_SIZE_4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM_IMX_MAX_DATA_SIZE_4) | 本示例使用；四个32位通道 |
| [`CONFIG_IPM_IMX_MAX_DATA_SIZE_8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM_IMX_MAX_DATA_SIZE_8) | 两个64位通道 |
| [`CONFIG_IPM_IMX_MAX_DATA_SIZE_16`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPM_IMX_MAX_DATA_SIZE_16) | 一个128位通道 |

原文强调：这只是展示i.MX IPM功能的简单演示，**阻塞回传发生在中断处理程序（Interrupt Handler）中，不适合真实应用**。

## 81.2\_构建与运行Zephyr端

示例需要远端核心发送数据，才能将其回显（Echo）。i.MX多核处理器上的另一个核心通常运行Linux，而不是Zephyr。

项目把数据输出到控制台，可按原命令构建和烧录：

```sh
west build -b udoo_neo_full/mcimx6x/m4 samples/drivers/ipm/ipm_imx
west flash
```

如何把Zephyr二进制文件加载到目标核心并执行，参见[Neo Full开发板文档](https://docs.zephyrproject.org/latest/boards/udoo/udoo_neo_full/doc/index.html#udoo_neo_full)。

## 81.3\_构建与运行Linux端

远端代码是可加载Linux内核模块（Loadable Kernel Module），创建`/dev/mu0`至`/dev/mu3`四个字符设备（Character Device），用于从消息单元读数据、向消息单元写数据。

原文给出的远端代码及构建运行说明入口为[CodeAurora的imx-mu项目](https://source.codeaurora.org/external/imxsupport/imx-mu/)。**访问译注（2026-10-13）：**本次检查该历史地址时发生传输层安全协议（Transport Layer Security，TLS）连接提前结束错误，未能验证其当前内容。保留原来源，不据此声称远端代码仍可下载或已构建。

## 81.4\_输入与原始输出

在Linux控制台输入：

```sh
# cat > /dev/mu0
abcdefgh
^D
```

其中`^D`表示按Ctrl+D结束输入。原文给出的Zephyr端输出如下：

```text
***** Booting Zephyr OS v1.12.0-291-g8cc508b *****
IPM initialized, data size = 4
ipm_callback: id = 0, data = 0x03323130
ipm_callback: id = 0, data = 0x03353433
ipm_callback: id = 0, data = 0x03383736
ipm_callback: id = 0, data = 0x02000a39
```

**译注：**输入例为`abcdefgh`，输出示例中的十六进制数据并非与该文本逐字节对应；两个代码块均按原文保留，不能据此推出字符到寄存器的编码规则。日志版本`v1.12.0-291-g8cc508b`也是原文历史输出。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/ipm/ipm_imx)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：ESP32双核IPM示例](P080_ESP32双核IPM示例.md) · [下一章：IVSHMEM处理器间邮箱示例](P082_IVSHMEM处理器间邮箱示例.md) · [返回大纲](大纲.md)
