---
id: learning.zephyr-docs.dt-peripheral-reference.page-3
title: SPI设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2spi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_SPI设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2spi_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择GPIO、SPI、CAN或显示设备树头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

串行外设接口（SPI）设备树宏公共 API 头文件。

查看此文件的源码。

<a id="details"></a>

串行外设接口（SPI）设备树宏公共 API 头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_gae8db0ce095bdd0066a845bc6a9bf329d"></a>

```c
#define DT_SPI_HAS_CS_GPIOS(spi)
```

相关声明：[DT_SPI_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gae8db0ce095bdd0066a845bc6a9bf329d)。

判断 SPI 控制器节点是否配置了片选 GPIO（Chip Select GPIOs）。

<a id="r_gafe2bddd961fe08672e131cfbd73eb466"></a>

```c
#define DT_SPI_NUM_CS_GPIOS(spi)
```

相关声明：[DT_SPI_NUM_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gafe2bddd961fe08672e131cfbd73eb466)。

SPI 控制器的 `cs-gpios` 属性中的片选 GPIO 数量。

<a id="r_gad66b759d6aa4826f2c68a94e8708ad4f"></a>

```c
#define DT_SPI_DEV_HAS_CS_GPIOS(spi_dev)
```

相关声明：[DT_SPI_DEV_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gad66b759d6aa4826f2c68a94e8708ad4f)。

判断 SPI 设备是否配置了片选线（Chip Select Line）。

<a id="r_ga0eaad9de680b5ac7cd8950957560c199"></a>

```c
#define DT_SPI_DEV_CS_GPIOS_CTLR(spi_dev)
```

相关声明：[DT_SPI_DEV_CS_GPIOS_CTLR](../hardware/P329_SPI设备树宏.md#ga0eaad9de680b5ac7cd8950957560c199)。

取得 SPI 设备的片选 GPIO 控制器的节点标识符。

<a id="r_ga8c1dd6a65c6f7fdf67291be1ed47fc9f"></a>

```c
#define DT_SPI_DEV_CS_GPIOS_PIN(spi_dev)
```

相关声明：[DT_SPI_DEV_CS_GPIOS_PIN](../hardware/P329_SPI设备树宏.md#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)。

取得 SPI 设备的片选 GPIO 引脚编号。

<a id="r_ga49fd9c174931b44584a7dbbc18f7c644"></a>

```c
#define DT_SPI_DEV_CS_GPIOS_FLAGS(spi_dev)
```

相关声明：[DT_SPI_DEV_CS_GPIOS_FLAGS](../hardware/P329_SPI设备树宏.md#ga49fd9c174931b44584a7dbbc18f7c644)。

取得 SPI 设备的片选 GPIO 标志（Flags）。

<a id="r_ga830f87f79c297c090a1929a288edc7ba"></a>

```c
#define DT_INST_SPI_DEV_HAS_CS_GPIOS(inst)
```

相关声明：[DT_INST_SPI_DEV_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#ga830f87f79c297c090a1929a288edc7ba)。

等价于 `DT_SPI_DEV_HAS_CS_GPIOS(DT_DRV_INST(inst))`。

<a id="r_ga0ffb7729cd90dc7bf4a1c33ead96a3d8"></a>

```c
#define DT_INST_SPI_DEV_CS_GPIOS_CTLR(inst)
```

相关声明：[DT_INST_SPI_DEV_CS_GPIOS_CTLR](../hardware/P329_SPI设备树宏.md#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)。

取得 SPI 设备实例的 GPIO 控制器节点标识符；等价于 `DT_SPI_DEV_CS_GPIOS_CTLR(DT_DRV_INST(inst))`。

<a id="r_ga1ce1031b612257718fbab08139db44cf"></a>

```c
#define DT_INST_SPI_DEV_CS_GPIOS_PIN(inst)
```

相关声明：[DT_INST_SPI_DEV_CS_GPIOS_PIN](../hardware/P329_SPI设备树宏.md#ga1ce1031b612257718fbab08139db44cf)。

等价于 `DT_SPI_DEV_CS_GPIOS_PIN(DT_DRV_INST(inst))`。

<a id="r_ga6f42b7305ec5373ae14cad220a3196da"></a>

```c
#define DT_INST_SPI_DEV_CS_GPIOS_FLAGS(inst)
```

相关声明：[DT_INST_SPI_DEV_CS_GPIOS_FLAGS](../hardware/P329_SPI设备树宏.md#ga6f42b7305ec5373ae14cad220a3196da)。

`DT_SPI_DEV_CS_GPIOS_FLAGS(DT_DRV_INST(inst))`。

## 3.2\_源码定位与版本边界

相对源码定位：[GPIO宏](../../../include/zephyr/devicetree/gpio.h)、[SPI宏](../../../include/zephyr/devicetree/spi.h)、[CAN宏](../../../include/zephyr/devicetree/can.h)、[显示宏](../../../include/zephyr/devicetree/display.h)、[宏生成器](../../../scripts/dts/gen_defines.py)和[显示列表绑定](../../../dts/bindings/display/zephyr,displays.yaml)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：片选索引来自reg：设备版本先通过DT_BUS(spi_dev)找到SPI总线节点，再以设备第0个reg的原始值DT_REG_ADDR_RAW(spi_dev)作为总线cs-gpios的条目索引。这里的reg是SPI从设备片选编号，不是CPU寄存器基地址，也不是该设备在子节点列表中的顺序。控制器、引脚和flags读取同一条目。

> 译注——源码核对：有GPIO片选与可用SPI不同：DT_SPI_HAS_CS_GPIOS只检查控制器属性存在，NUM版本缺失时为0；DEV_HAS版本检查该设备索引对应的cs-gpios条目。没有GPIO片选不代表控制器不支持硬件片选，也不能据此判断SPI传输是否可用。读取片选宏不拉高或拉低引脚，不执行传输。

> 译注——源码核对：先区分对象：DT_SPI_HAS_CS_GPIOS与NUM接收控制器节点，DT_SPI_DEV_*接收SPI设备节点，DT_INST_SPI_DEV_*再以DT_DRV_COMPAT转换实例。名字相近但对象层次不同，不应把总线控制器作为从设备传给DEV版本。

> 译注——源码核对：版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P004_SPI设备树头文件源码.md)
- [DT_SPI_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gae8db0ce095bdd0066a845bc6a9bf329d)
- [DT_SPI_NUM_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gafe2bddd961fe08672e131cfbd73eb466)
- [DT_SPI_DEV_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#gad66b759d6aa4826f2c68a94e8708ad4f)
- [DT_SPI_DEV_CS_GPIOS_CTLR](../hardware/P329_SPI设备树宏.md#ga0eaad9de680b5ac7cd8950957560c199)
- [DT_SPI_DEV_CS_GPIOS_PIN](../hardware/P329_SPI设备树宏.md#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)
- [DT_SPI_DEV_CS_GPIOS_FLAGS](../hardware/P329_SPI设备树宏.md#ga49fd9c174931b44584a7dbbc18f7c644)
- [DT_INST_SPI_DEV_HAS_CS_GPIOS](../hardware/P329_SPI设备树宏.md#ga830f87f79c297c090a1929a288edc7ba)
- [DT_INST_SPI_DEV_CS_GPIOS_CTLR](../hardware/P329_SPI设备树宏.md#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)
- [DT_INST_SPI_DEV_CS_GPIOS_PIN](../hardware/P329_SPI设备树宏.md#ga1ce1031b612257718fbab08139db44cf)
- [DT_INST_SPI_DEV_CS_GPIOS_FLAGS](../hardware/P329_SPI设备树宏.md#ga6f42b7305ec5373ae14cad220a3196da)

<a id="header-details"></a>

---

[上一章](P002_GPIO设备树头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_SPI设备树头文件源码.md)
