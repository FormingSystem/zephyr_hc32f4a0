---
id: learning.zephyr-docs.dt-bus-binding-reference.page-3
title: SPI绑定常量头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2spi_2spi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_SPI绑定常量头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2spi_2spi_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择GPIO、SPI绑定常量或设备树宏工具包装头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### SPI双工模式（Duplex Mode）

某些控制器支持半双工传输（Half-duplex Transfer），采用三线连接。

默认采用全双工（Full Duplex）。

<a id="r_ga5585d5e81dec606b605f31b6745c35d3"></a>

```c
#define SPI_FULL_DUPLEX (0U << 11)
```

相关声明：[SPI_FULL_DUPLEX](../hardware/P318_SPI公共接口.md#ga5585d5e81dec606b605f31b6745c35d3)。

<a id="r_ga602a7804b7434d7ebc1ebe6cb9b47a2f"></a>

```c
#define SPI_HALF_DUPLEX (1U << 11)
```

相关声明：[SPI_HALF_DUPLEX](../hardware/P318_SPI公共接口.md#ga602a7804b7434d7ebc1ebe6cb9b47a2f)。

<a id="define-members-1"></a>

### SPI帧格式（Frame Format）

提供两种帧格式（Frame Format）：Motorola 和 TI。

主要区别在于片选线（Chip Select，CS）的行为。Motorola 格式在整个传输期间保持 CS 有效；TI 格式只在实际传输之前的一个串行时钟周期内使 CS 有效，因此传输期间 CS 为无效状态，传输随时钟结束而结束。默认采用最常用的 Motorola 帧格式。

<a id="r_ga6a1b4ba33900165b6e09706903a6e6ee"></a>

```c
#define SPI_FRAME_FORMAT_MOTOROLA (0U << 15)
```

相关声明：[SPI_FRAME_FORMAT_MOTOROLA](../hardware/P318_SPI公共接口.md#ga6a1b4ba33900165b6e09706903a6e6ee)。

<a id="r_ga22801357a9682371e3d8a10e522de388"></a>

```c
#define SPI_FRAME_FORMAT_TI (1U << 15)
```

相关声明：[SPI_FRAME_FORMAT_TI](../hardware/P318_SPI公共接口.md#ga22801357a9682371e3d8a10e522de388)。

## 3.2\_源码定位与版本边界

相对源码定位：[GPIO绑定常量](../../../include/zephyr/dt-bindings/gpio/gpio.h)、[SPI绑定常量](../../../include/zephyr/dt-bindings/spi/spi.h)、[设备树宏工具包装](../../../include/zephyr/dt-bindings/dt-util.h)、[GPIO驱动接口](../../../include/zephyr/drivers/gpio.h)、[SPI驱动接口](../../../include/zephyr/drivers/spi.h)、[基础宏工具](../../../include/zephyr/sys/util_macro.h)、[GPIO控制器绑定](../../../dts/bindings/gpio/gpio-controller.yaml)和[SPI设备绑定](../../../dts/bindings/spi/spi-device.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：位编码与绑定：全双工值为0、半双工值为1U<<11（2048）；Motorola帧格式为0、TI格式为1U<<15（32768）。官方spi-device公共绑定的duplex和frame-format分别使用这些枚举，默认都是0，建议在DTS中使用宏名表达含义。数值并不代表所有控制器都实现相应模式。

> 译注——源码核对：配置路径：SPI_CONFIG_DT把调用方operation_、duplex、frame-format以及CPOL、CPHA等属性按位或合并到operation。半双工与帧格式是独立字段，CPOL／CPHA控制时钟极性与相位，不能用TI或Motorola格式替代它们。按位或合并也不能清除调用方已经置1的位，因此默认值0不等于强制覆盖其他配置。

> 译注——源码核对：传输时序：本页关于三线与CS行为保留官方概述。TI格式中的CS脉冲描述是帧格式规则，不表示配置任意GPIO片选就可模拟全部TI时序；实际连接方式、控制器能力与驱动支持仍需对应平台资料和运行时结果确认。

> 译注——源码核对：版本边界：本批记录三个绑定头文件、GPIO与SPI驱动公共头文件、宏工具头文件和两个公共绑定，共八份官方源码摘要；三个源码浏览页的非注释内容与读取的原始头文件一致。latest、滚动main与仓库参照版本不自动相同。相对链接用于源码跟踪，本次未生成设备树、构建固件或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P004_SPI绑定常量头文件源码.md)
- [SPI_FULL_DUPLEX](../hardware/P318_SPI公共接口.md#ga5585d5e81dec606b605f31b6745c35d3)
- [SPI_HALF_DUPLEX](../hardware/P318_SPI公共接口.md#ga602a7804b7434d7ebc1ebe6cb9b47a2f)
- [SPI_FRAME_FORMAT_MOTOROLA](../hardware/P318_SPI公共接口.md#ga6a1b4ba33900165b6e09706903a6e6ee)
- [SPI_FRAME_FORMAT_TI](../hardware/P318_SPI公共接口.md#ga22801357a9682371e3d8a10e522de388)

---

[上一章](P002_GPIO绑定常量头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_SPI绑定常量头文件源码.md)
