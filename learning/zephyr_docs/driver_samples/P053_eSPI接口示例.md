---
id: learning.zephyr-docs.driver_samples.page-53
title: eSPI接口示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/espi/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="espi"></a>

# 第53章\_eSPI接口示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/espi/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 53.1\_概览（Overview）

本例演示[增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）API](../hardware/P071_增强型SPI总线.md#espi-api)的使用。在一个包含虚拟线数据包（Virtual Wire Packet）交换的简单eSPI握手（Handshake）流程中，展示如何配置和选择控制器能力。

标准平台信号以虚拟线数据包的形式在总线上传输。示例注册回调（Callback），在控制台报告主要eSPI事件，以及接收到虚拟线的事件。

<a id="building-and-running"></a>

## 53.2\_构建与运行（Building and Running）

示例可以在支持eSPI的开发板上构建并运行。应配置最小eSPI握手所需的全部引脚，并正确设置测试执行机制（Harness）和测试夹具（Fixture）。将eSPI设备连接到测试板后，原文要求在板卡映射文件（Map File）中添加以下夹具设置，以便Twister正确执行本例：

```yaml
- fixture: espi_device_connect
```

> 译注——夹具字段：原片段按原样保留。当前[tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/espi/tests.yaml)在harness_config中使用单数fixture声明espi_device_connect，而[硬件映射模式](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/scripts/schemas/twister/hwmap-schema.yaml)在每个板条目中要求复数fixtures字符串列表。编辑当前格式的板卡硬件映射时，应在目标条目内使用下面的字段，保留该条目的其他设备信息；它不是一个完整映射文件：

```yaml
fixtures:
  - espi_device_connect
```

> 译注——两端角色与运行条件：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/espi/src/main.c)从espi0设备树节点取得设备，配置本地目标端（Target）通道，并与eSPI控制器／主机（Controller／Host）握手。需要匹配的对端、平台信号和通道支持；不能把普通SPI接线直接当作eSPI握手环境。原页没有给出通用构建命令，本批没有运行Twister或硬件握手。

<a id="sample-output"></a>

### 53.2.1\_示例输出（Sample output）

```text
Hello eSPI test <BOARD USED>
eSPI target configured successfully!
eSPI test - callbacks initialization... complete
eSPI test - callbacks registration... complete

eSPI BUS reset 1

eSPI test - Handshake with eSPI controller (host)...
VW channel event 1
OOB channel event 1

1st phase completed
SLP signal changed 1
SLP signal changed 1
SLP signal changed 1

2nd phase completed
PLT_RST changed 1

3rd phase completed

request_temp
OOB transaction completed rcvd: 11 bytes
request_temp
OOB transaction completed rcvd: 5 bytes
eSPI sample completed err: 0
```

**注意：**上面显示的值可能随实际执行的子测试（Subtest）而不同。

> 译注——日志字段：VW表示虚拟线（Virtual Wire）通道，OOB表示带外（Out-of-Band）通道；SLP是睡眠相关信号，PLT_RST表示平台复位信号。日志展示握手阶段及温度请求事务，末尾err: 0属于官方示例输出，不是本仓库实测结果。原页将最后的注意事项显示为未正确渲染的note::文本，这里保留其含义并排为明确的注意段。

<a id="see-also"></a>

## 53.3\_相关接口（See also）

[eSPI接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html)、[SPI接口参考](../hardware/P318_SPI公共接口.md)。


对应官方文档源码：[samples/drivers/espi/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/espi/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/espi/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/espi/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P052_Bouffalolab_GPIO_FIFO串口示例.md) · [返回大纲](大纲.md) · [下一章](P054_nRF内部存储示例.md)
