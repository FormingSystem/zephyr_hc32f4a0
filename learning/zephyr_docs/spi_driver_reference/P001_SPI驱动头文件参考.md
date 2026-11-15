---
id: learning.zephyr-docs.spi-driver-reference.page-1
title: SPI驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2spi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_SPI驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2spi_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SPI驱动主头文件参考与源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

SPI（串行外设接口，Serial Peripheral Interface）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/spi/spi.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/stats/stats.h>
#include <zephyr/syscalls/spi.h>
```

查看此文件的源码。

SPI（串行外设接口，Serial Peripheral Interface）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_spi_5Fcs_5Fcontrol"></a>

```c
struct spi_cs_control
```

相关声明：[spi_cs_control](../hardware/P319_SPI片选控制结构.md)。

SPI片选（Chip Select，CS）控制结构。

<a id="r_spi_5Fconfig"></a>

```c
struct spi_config
```

相关声明：[spi_config](../hardware/P320_SPI控制器配置结构.md)。

SPI控制器（Controller）配置结构。

<a id="r_spi_5Fdt_5Fspec"></a>

```c
struct spi_dt_spec
```

相关声明：[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)。

完整的SPI设备树（Devicetree，DT）信息。

<a id="r_spi_5Fbuf"></a>

```c
struct spi_buf
```

相关声明：[spi_buf](../hardware/P322_SPI缓冲区结构.md)。

SPI缓冲区（Buffer）结构。

<a id="r_spi_5Fbuf_5Fset"></a>

```c
struct spi_buf_set
```

相关声明：[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

SPI分散／聚集（Scatter-Gather）缓冲区数组结构。

<a id="r_spi_5Fdriver_5Fapi"></a>

```c
struct spi_driver_api
```

相关声明：[spi_driver_api](../hardware/P325_SPI驱动函数表.md)。

驱动操作（Driver Operations）：SPI驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gaf7d4888063e5b739f2a3bee295962bfe"></a>

```c
#define SPI_CONFIG_DT(node_id, operation_)
```

相关声明：[SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)。

从设备树生成spi_config的结构初始化器（Structure Initializer）。

<a id="r_ga67837cbae6f29c5f8ad9a05dbc9b05f8"></a>

```c
#define SPI_CONFIG_DT_INST(inst, operation_)
```

相关声明：[SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)。

从设备树实例生成spi_config的结构初始化器。

<a id="r_ga43857c934651c4bfb3823a5080a4a294"></a>

```c
#define SPI_DT_SPEC_GET(node_id, operation_)
```

相关声明：[SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)。

从设备树生成spi_dt_spec的结构初始化器。

<a id="r_gac9537325ca3188121d0f8c382c798ca1"></a>

```c
#define SPI_DT_SPEC_INST_GET(inst, operation_)
```

相关声明：[SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)。

从设备树实例生成spi_dt_spec的结构初始化器。

<a id="r_ga1dbef324b98a8921507de0da1c4e4fa6"></a>

```c
#define SPI_SDO_OVERRUN_UNKNOWN 0x100
```

相关声明：[SPI_SDO_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga1dbef324b98a8921507de0da1c4e4fa6)。

不会与任何有效的溢出填充值（Overrun Character）比较相等的值。

<a id="r_ga15b5fa509a3b7dc87bfd451af5a11917"></a>

```c
#define SPI_MOSI_OVERRUN_UNKNOWN SPI_SDO_OVERRUN_UNKNOWN __DEPRECATED_MACRO
```

相关声明：[SPI_MOSI_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga15b5fa509a3b7dc87bfd451af5a11917)、[SPI_SDO_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga1dbef324b98a8921507de0da1c4e4fa6)。

不会与任何有效的溢出填充值（Overrun Character）比较相等的值。

<a id="r_gaf66331d56f20e0c37f2a3cff998c6bce"></a>

```c
#define SPI_SDO_OVERRUN_DT(node_id)
```

相关声明：[SPI_SDO_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaf66331d56f20e0c37f2a3cff998c6bce)。

所有TX字节均已发送、RX仍继续时，在SDO上发送的值。

<a id="r_gaa9621b033dfaf128602b1432927a67fe"></a>

```c
#define SPI_MOSI_OVERRUN_DT(node_id)
```

相关声明：[SPI_MOSI_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaa9621b033dfaf128602b1432927a67fe)。

所有TX字节均已发送、RX仍继续时，在SDO上发送的值。

<a id="r_ga0e05910cd0be7211389514b7b4edc0cc"></a>

```c
#define SPI_SDO_OVERRUN_DT_INST(inst)
```

相关声明：[SPI_SDO_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga0e05910cd0be7211389514b7b4edc0cc)。

所有TX字节均已发送、RX仍继续时，在SDO上发送的值。

<a id="r_ga24c7416a98421e353a8892151f34122c"></a>

```c
#define SPI_MOSI_OVERRUN_DT_INST(inst)
```

相关声明：[SPI_MOSI_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga24c7416a98421e353a8892151f34122c)。

所有TX字节均已发送、RX仍继续时，在SDO上发送的值。

<a id="r_ga83fa04d1e9f281cd566ee32cf807325e"></a>

```c
#define SPI_STATS_RX_BYTES_INC(dev_)
```

相关声明：[SPI_STATS_RX_BYTES_INC](../hardware/P318_SPI公共接口.md#ga83fa04d1e9f281cd566ee32cf807325e)。

<a id="r_gadd3b82af2396b91930ece09fa79fc4e2"></a>

```c
#define SPI_STATS_TX_BYTES_INC(dev_)
```

相关声明：[SPI_STATS_TX_BYTES_INC](../hardware/P318_SPI公共接口.md#gadd3b82af2396b91930ece09fa79fc4e2)。

<a id="r_ga6f69e68a79afbbe016aecc515f14de3a"></a>

```c
#define SPI_STATS_TRANSFER_ERROR_INC(dev_)
```

相关声明：[SPI_STATS_TRANSFER_ERROR_INC](../hardware/P318_SPI公共接口.md#ga6f69e68a79afbbe016aecc515f14de3a)。

<a id="r_gad7d1058f600d6aef4fc4e2bdff5d55f3"></a>

```c
#define spi_transceive_stats(dev, error, tx_bufs, rx_bufs)
```

相关声明：[spi_transceive_stats](../hardware/P318_SPI公共接口.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)。

<a id="r_ga27af5f053c5fd4e9eef0900406fbf854"></a>

```c
#define SPI_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, ...)
```

相关声明：[SPI_DEVICE_DT_DEFINE](../hardware/P318_SPI公共接口.md#ga27af5f053c5fd4e9eef0900406fbf854)。

类似DEVICE_DT_DEINIT_DEFINE()，但不提供反初始化（Deinitialization）函数。

<a id="r_ga50cbb6845d230033f192f1e716fd9f2b"></a>

```c
#define SPI_DEVICE_DT_INST_DEINIT_DEFINE(inst, ...)
```

相关声明：[SPI_DEVICE_DT_INST_DEINIT_DEFINE](../hardware/P318_SPI公共接口.md#ga50cbb6845d230033f192f1e716fd9f2b)。

类似SPI_DEVICE_DT_DEINIT_DEFINE()，但使用与DT_DRV_COMPAT匹配的设备树实例，而非节点标识符。

<a id="r_ga84811e0fdd574477c8569d559f773dae"></a>

```c
#define SPI_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[SPI_DEVICE_DT_INST_DEFINE](../hardware/P318_SPI公共接口.md#ga84811e0fdd574477c8569d559f773dae)。

类似SPI_DEVICE_DT_DEFINE()，但使用与DT_DRV_COMPAT匹配的设备树实例，而非节点标识符。

<a id="define-members-0"></a>

### SPI工作模式（Operational Mode）

<a id="r_gace0f0d954c2bd7d603c4003289c11102"></a>

```c
#define SPI_OP_MODE_CONTROLLER 0U
```

相关声明：[SPI_OP_MODE_CONTROLLER](../hardware/P318_SPI公共接口.md#gace0f0d954c2bd7d603c4003289c11102)。

控制器模式（Controller Mode）。

<a id="r_gaa1f42ffeac36380f4d1d8f84bda2990b"></a>

```c
#define SPI_OP_MODE_PERIPHERAL BIT(0)
```

相关声明：[SPI_OP_MODE_PERIPHERAL](../hardware/P318_SPI公共接口.md#gaa1f42ffeac36380f4d1d8f84bda2990b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

外设模式（Peripheral Mode）。

<a id="r_ga5b9d40fa0f455b1e63f8040b3316b0da"></a>

```c
#define SPI_OP_MODE_MASTER SPI_OP_MODE_CONTROLLER __DEPRECATED_MACRO
```

相关声明：[SPI_OP_MODE_MASTER](../hardware/P318_SPI公共接口.md#ga5b9d40fa0f455b1e63f8040b3316b0da)、[SPI_OP_MODE_CONTROLLER](../hardware/P318_SPI公共接口.md#gace0f0d954c2bd7d603c4003289c11102)。

控制器模式（Controller Mode）。

<a id="r_ga1c3310d3711cb99cdb78fa9d1c970779"></a>

```c
#define SPI_OP_MODE_SLAVE SPI_OP_MODE_PERIPHERAL __DEPRECATED_MACRO
```

相关声明：[SPI_OP_MODE_SLAVE](../hardware/P318_SPI公共接口.md#ga1c3310d3711cb99cdb78fa9d1c970779)、[SPI_OP_MODE_PERIPHERAL](../hardware/P318_SPI公共接口.md#gaa1f42ffeac36380f4d1d8f84bda2990b)。

外设模式（Peripheral Mode）。

<a id="r_ga6dd4395e027407a7b3b92cff2abcc8b3"></a>

```c
#define SPI_OP_MODE_GET(_operation_)
```

相关声明：[SPI_OP_MODE_GET](../hardware/P318_SPI公共接口.md#ga6dd4395e027407a7b3b92cff2abcc8b3)。

从spi_operation_t取得SPI工作模式的位掩码（Bitmask）。

<a id="define-members-1"></a>

### SPI时钟模式（Clock Modes）

<a id="r_ga5a2be1003873beaa0ade10e7218d67d5"></a>

```c
#define SPI_MODE_CPOL BIT(1)
```

相关声明：[SPI_MODE_CPOL](../hardware/P318_SPI公共接口.md#ga5a2be1003873beaa0ade10e7218d67d5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟极性（Clock Polarity）：时钟空闲状态。

<a id="r_ga35e98b37e3ec4889a90100abe884590f"></a>

```c
#define SPI_MODE_CPHA BIT(2)
```

相关声明：[SPI_MODE_CPHA](../hardware/P318_SPI公共接口.md#ga35e98b37e3ec4889a90100abe884590f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟相位（Clock Phase）：时钟的数据采样边沿。

<a id="r_ga8619b297de563eca6852af34c79daa62"></a>

```c
#define SPI_MODE_LOOP BIT(3)
```

相关声明：[SPI_MODE_LOOP](../hardware/P318_SPI公共接口.md#ga8619b297de563eca6852af34c79daa62)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

控制器环回模式（Controller Loopback Mode）。

<a id="r_gaa3582b96ff42dba0b0ad815c727d5e42"></a>

```c
#define SPI_MODE_GET(_mode_)
```

相关声明：[SPI_MODE_GET](../hardware/P318_SPI公共接口.md#gaa3582b96ff42dba0b0ad815c727d5e42)。

从spi_operation_t取得SPI时钟极性和相位模式的位掩码。

<a id="define-members-2"></a>

### SPI数据字配置（Data Word Configurations）

SPI数据字（Data Word）是移入／移出控制器硬件先进先出队列（First In, First Out，FIFO）的值，也是SPI总线通信的原子单位。

在此API中，数据字也称为数据帧（Data Frame）。一次传输由任意数量的数据字组成。以下选项指定本次操作所用SPI数据字的配置。

<a id="r_ga7761f42c6241cf396fc02d0de8617e46"></a>

```c
#define SPI_TRANSFER_MSB (0U)
```

相关声明：[SPI_TRANSFER_MSB](../hardware/P318_SPI公共接口.md#ga7761f42c6241cf396fc02d0de8617e46)。

数据字以最高有效位优先（Most Significant Bit First，MSB First）传输，用于spi_operation_t。

<a id="r_ga93504a76a265bedbe781c107beebc9dc"></a>

```c
#define SPI_TRANSFER_LSB BIT(4)
```

相关声明：[SPI_TRANSFER_LSB](../hardware/P318_SPI公共接口.md#ga93504a76a265bedbe781c107beebc9dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

数据字以最低有效位优先（Least Significant Bit First，LSB First）传输，用于spi_operation_t。

<a id="r_gacd7edd9ce02bd8351f8eebe5b5c07c7a"></a>

```c
#define SPI_WORD_SIZE_GET(operation)
```

相关声明：[SPI_WORD_SIZE_GET](../hardware/P318_SPI公共接口.md#gacd7edd9ce02bd8351f8eebe5b5c07c7a)。

从spi_operation_t取得SPI数据字长度，单位为位（bit）。

<a id="r_gac1115bf80134efd38d88161e3f5e3e1a"></a>

```c
#define SPI_WORD_SET(word_size)
```

相关声明：[SPI_WORD_SET](../hardware/P318_SPI公共接口.md#gac1115bf80134efd38d88161e3f5e3e1a)。

取得用于在spi_operation_t中设置数据字长度的位掩码。

<a id="define-members-3"></a>

### SPI传输控制标志（Transfer Control Flags）

<a id="r_gae917312adef283b4bf67cdb53566e4bb"></a>

```c
#define SPI_HOLD_ON_CS BIT(12)
```

相关声明：[SPI_HOLD_ON_CS](../hardware/P318_SPI公共接口.md#gae917312adef283b4bf67cdb53566e4bb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事务（Transaction）结束后保持片选有效。

<a id="r_gafe8dc164d6fc0a0f93f2ff9d5381af14"></a>

```c
#define SPI_LOCK_ON BIT(13)
```

相关声明：[SPI_LOCK_ON](../hardware/P318_SPI公共接口.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

保留对SPI设备的所有权（Ownership）。

<a id="r_ga44076fa14703997f7e3aefb2bfccd801"></a>

```c
#define SPI_CS_ACTIVE_HIGH BIT(14)
```

相关声明：[SPI_CS_ACTIVE_HIGH](../hardware/P318_SPI公共接口.md#ga44076fa14703997f7e3aefb2bfccd801)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

片选有效状态（Active State）的配置。

<a id="define-members-4"></a>

### SPI串行数据输入线（Serial Data Input，SDI）

某些控制器支持以双线、四线或八线SDI连接外设。

默认采用单线，这是大多数场景下的配置。未启用CONFIG_SPI_EXTENDED_MODES时，仅支持单线。

<a id="r_ga7a183f157e8cb8b437857a0babbd923b"></a>

```c
#define SPI_LINES_SINGLE (0U << 16)
```

相关声明：[SPI_LINES_SINGLE](../hardware/P318_SPI公共接口.md#ga7a183f157e8cb8b437857a0babbd923b)。

单线（Single Line）。

<a id="r_ga120ab60329d664d5d6e828f90251a98a"></a>

```c
#define SPI_LINES_DUAL (1U << 16)
```

相关声明：[SPI_LINES_DUAL](../hardware/P318_SPI公共接口.md#ga120ab60329d664d5d6e828f90251a98a)。

双线（Dual Lines）。

<a id="r_ga30866b948e995224de854e10a428bda5"></a>

```c
#define SPI_LINES_QUAD (2U << 16)
```

相关声明：[SPI_LINES_QUAD](../hardware/P318_SPI公共接口.md#ga30866b948e995224de854e10a428bda5)。

四线（Quad Lines）。

<a id="r_ga512d76085e600886654b8541aab31cf7"></a>

```c
#define SPI_LINES_OCTAL (3U << 16)
```

相关声明：[SPI_LINES_OCTAL](../hardware/P318_SPI公共接口.md#ga512d76085e600886654b8541aab31cf7)。

八线（Octal Lines）。

<a id="r_gadc79f986c4b30fe5b263841cd8bb5676"></a>

```c
#define SPI_LINES_MASK (0x3U << 16)
```

相关声明：[SPI_LINES_MASK](../hardware/P318_SPI公共接口.md#gadc79f986c4b30fe5b263841cd8bb5676)。

spi_operation_t中SDI线数的掩码。

<a id="define-members-5"></a>

### SPI GPIO片选控制（Chip Select Control）

<a id="r_ga48aa19f45413d56b03596d10b72c732e"></a>

```c
#define SPI_CS_GPIOS_DT_SPEC_GET(spi_dev)
```

相关声明：[SPI_CS_GPIOS_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga48aa19f45413d56b03596d10b72c732e)。

取得描述SPI设备片选引脚的struct gpio_dt_spec。

<a id="r_ga88fefbfadb8184806123e1f935a4ff7c"></a>

```c
#define SPI_CS_GPIOS_DT_SPEC_INST_GET(inst)
```

相关声明：[SPI_CS_GPIOS_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#ga88fefbfadb8184806123e1f935a4ff7c)。

取得描述SPI设备片选引脚的struct gpio_dt_spec。

<a id="r_ga81308d27cd78e65f0a3ddaa918f2a74a"></a>

```c
#define SPI_CS_CONTROL_INIT(node_id)
```

相关声明：[SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)。

根据设备树节点标识符初始化spi_cs_control，并取得指向它的指针。

<a id="r_ga92195f45dac561b19204f6be21f62b55"></a>

```c
#define SPI_CS_CONTROL_INIT_INST(inst)
```

相关声明：[SPI_CS_CONTROL_INIT_INST](../hardware/P318_SPI公共接口.md#ga92195f45dac561b19204f6be21f62b55)。

从设备树节点取得指向spi_cs_control的指针。

<a id="define-members-6"></a>

### SPI设备树设备宏（Devicetree Device Macros）

<a id="r_gaf98b0cb38cb316b9fe05146bba34126d"></a>

```c
#define SPI_DEVICE_DT_DEINIT_DEFINE(node_id, init_fn, deinit_fn, pm, data, config, level, prio, api, ...)
```

相关声明：[SPI_DEVICE_DT_DEINIT_DEFINE](../hardware/P318_SPI公共接口.md#gaf98b0cb38cb316b9fe05146bba34126d)。

类似DEVICE_DT_DEINIT_DEFINE()，并加入SPI专用处理。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga398a8ae1c4799e77fb6c067b6d47294a"></a>

```c
typedef uint16_t spi_operation_t
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spi_operation_t](../hardware/P318_SPI公共接口.md#ga398a8ae1c4799e77fb6c067b6d47294a)。

保存SPI操作标志的抽象类型（Opaque Type）。

<a id="r_ga3fc669f866b03cfdad98754de69cda13"></a>

```c
typedef int(* spi_api_io) (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_api_io](../hardware/P324_SPI驱动后端接口.md#ga3fc669f866b03cfdad98754de69cda13)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

I/O回调API（Callback API）。

<a id="r_ga1db2a410f482d0f26c49f96352aa606d"></a>

```c
typedef void(* spi_callback_t) (const struct device *dev, int result, void *data)
```

相关声明：[spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)、[device](../device_reference/P002_设备对象结构.md)。

用于异步传输请求（Asynchronous Transfer Requests）的SPI回调。

<a id="r_ga03be7f33032ac479153616bbe26848e7"></a>

```c
typedef int(* spi_api_io_async) (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, spi_callback_t cb, void *userdata)
```

相关声明：[spi_api_io_async](../hardware/P324_SPI驱动后端接口.md#ga03be7f33032ac479153616bbe26848e7)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)。

异步I/O回调API。

<a id="r_gae274c0d704e8fd8993631fc1b91bfcb1"></a>

```c
typedef void(* spi_api_iodev_submit) (const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[spi_api_iodev_submit](../hardware/P324_SPI驱动后端接口.md#gae274c0d704e8fd8993631fc1b91bfcb1)、[device](../device_reference/P002_设备对象结构.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通过实时I/O（Real-Time I/O，RTIO）向SPI设备提交工作的回调API。

<a id="r_gac651ff7cd3dde7abe2525e20ef2e9e7d"></a>

```c
typedef int(* spi_api_release) (const struct device *dev, const struct spi_config *config)
```

相关声明：[spi_api_release](../hardware/P324_SPI驱动后端接口.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)。

用于解锁SPI设备的回调API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gae1156a4ee1b5909c321811045566d888"></a>

```c
static bool spi_cs_is_gpio (const struct spi_config *config)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[spi_cs_is_gpio](../hardware/P318_SPI公共接口.md#gae1156a4ee1b5909c321811045566d888)、[spi_config](../hardware/P320_SPI控制器配置结构.md)。

检查SPI片选是否通过通用输入／输出（General-Purpose Input/Output，GPIO）控制。

<a id="r_gaa13f0da1f28cffa0da4677987db0c9c5"></a>

```c
static bool spi_cs_is_gpio_dt (const struct spi_dt_spec *spec)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[spi_cs_is_gpio_dt](../hardware/P318_SPI公共接口.md#gaa13f0da1f28cffa0da4677987db0c9c5)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)。

检查spi_dt_spec中的SPI片选是否通过GPIO控制。

<a id="r_ga37b4e5079ed18b70b0c5a260f4c36403"></a>

```c
static bool spi_is_ready_dt (const struct spi_dt_spec *spec)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[spi_is_ready_dt](../hardware/P318_SPI公共接口.md#ga37b4e5079ed18b70b0c5a260f4c36403)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)。

验证SPI总线以及已定义的片选GPIO是否就绪（Ready）。

<a id="r_ga0c4f4f0a93bb83a4f58d551a7491164e"></a>

```c
int spi_release (const struct device *dev, const struct spi_config *config)
```

相关声明：[spi_release](../hardware/P318_SPI公共接口.md#ga0c4f4f0a93bb83a4f58d551a7491164e)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)。

释放当前配置所锁定的SPI设备和／或片选。

<a id="r_ga829b59767c51b20b546eee8a9cc84b69"></a>

```c
static int spi_release_dt (const struct spi_dt_spec *spec)
```

相关声明：[spi_release_dt](../hardware/P318_SPI公共接口.md#ga829b59767c51b20b546eee8a9cc84b69)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)。

释放spi_dt_spec指定的SPI设备。

<a id="func-members-0"></a>

### SPI同步传输函数（Synchronous Transfer Functions）

这些函数会等待传输完成后才返回。

<a id="r_gad51054c1ba259db5a64619788506a6f5"></a>

```c
int spi_transceive (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_transceive](../hardware/P318_SPI公共接口.md#gad51054c1ba259db5a64619788506a6f5)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

通过SPI驱动读／写指定数量的数据。

<a id="r_ga52c017066736414b31ff709ddc67c4ff"></a>

```c
static int spi_transceive_dt (const struct spi_dt_spec *spec, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_transceive_dt](../hardware/P318_SPI公共接口.md#ga52c017066736414b31ff709ddc67c4ff)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

在spi_dt_spec指定的SPI总线上读／写数据。

<a id="r_ga41f771785a4fa9ca0954125d1e97959e"></a>

```c
static int spi_read (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_read](../hardware/P318_SPI公共接口.md#ga41f771785a4fa9ca0954125d1e97959e)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

通过SPI驱动读取指定数量的数据。

<a id="r_ga7a1d7ebd37d2861b169c265cb90015bf"></a>

```c
static int spi_read_dt (const struct spi_dt_spec *spec, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_read_dt](../hardware/P318_SPI公共接口.md#ga7a1d7ebd37d2861b169c265cb90015bf)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

从spi_dt_spec指定的SPI总线读取数据。

<a id="r_ga7e7c4460670ec1c0433ba19accd97796"></a>

```c
static int spi_write (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs)
```

相关声明：[spi_write](../hardware/P318_SPI公共接口.md#ga7e7c4460670ec1c0433ba19accd97796)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

通过SPI驱动写入指定数量的数据。

<a id="r_ga292d6d1fe82f3f1ce0d9a2aa5437201b"></a>

```c
static int spi_write_dt (const struct spi_dt_spec *spec, const struct spi_buf_set *tx_bufs)
```

相关声明：[spi_write_dt](../hardware/P318_SPI公共接口.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)、[spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

向spi_dt_spec指定的SPI总线写入数据。

<a id="func-members-1"></a>

### SPI异步传输函数（Asynchronous Transfer Functions）

使用此API时，传输函数会在传输启动后返回，并通过回调（Callback）或信号（Signal）通知完成。

注意（Note）：总线已经忙碌时，异步API调用仍然可能阻塞。函数会一直阻塞到总线可用，能够启动所请求的传输为止。

<a id="r_ga6114e63ca23b82f9be0ac70e372b878b"></a>

```c
static int spi_transceive_cb (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, spi_callback_t callback, void *userdata)
```

相关声明：[spi_transceive_cb](../hardware/P318_SPI公共接口.md#ga6114e63ca23b82f9be0ac70e372b878b)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)。

通过SPI驱动异步读／写指定数量的数据。

<a id="r_ga41b8a541257c0d45575fdc4593417edc"></a>

```c
static int spi_transceive_signal (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs, struct k_poll_signal *sig)
```

相关声明：[spi_transceive_signal](../hardware/P318_SPI公共接口.md#ga41b8a541257c0d45575fdc4593417edc)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过SPI驱动读／写指定数量的数据。

<a id="r_ga9a1ceadb217368232af5b688c12169c5"></a>

```c
static int spi_read_signal (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *rx_bufs, struct k_poll_signal *sig)
```

相关声明：[spi_read_signal](../hardware/P318_SPI公共接口.md#ga9a1ceadb217368232af5b688c12169c5)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过SPI驱动读取指定数量的数据。

<a id="r_gadcb19d43461ef88e31f6b382cc87fd0b"></a>

```c
static int spi_write_signal (const struct device *dev, const struct spi_config *config, const struct spi_buf_set *tx_bufs, struct k_poll_signal *sig)
```

相关声明：[spi_write_signal](../hardware/P318_SPI公共接口.md#gadcb19d43461ef88e31f6b382cc87fd0b)、[device](../device_reference/P002_设备对象结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)。

通过SPI驱动写入指定数量的数据。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.5\_SPI实时I/O API（RTIO API）

这些函数通过基于RTIO的API使用SPI驱动类别。

<a id="r_ga1eec8a77be8a512e8b0fa74d270877e5"></a>

```c
#define SPI_DT_IODEV_DEFINE(name, node_id, operation_)
```

相关声明：[SPI_DT_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga1eec8a77be8a512e8b0fa74d270877e5)。

为总线上给定的设备树节点定义I/O设备（iodev）。

<a id="r_ga4e5633f6e8da22f4c00a723a669b2d9a"></a>

```c
#define SPI_DT_INST_IODEV_DEFINE(name, inst, operation_)
```

相关声明：[SPI_DT_INST_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga4e5633f6e8da22f4c00a723a669b2d9a)。

为总线上的设备树实例定义I/O设备（iodev）。

<a id="r_ga8b23855bdc7dab7d02b8f7daa7db651b"></a>

```c
static void spi_iodev_submit (struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[spi_iodev_submit](../hardware/P318_SPI公共接口.md#ga8b23855bdc7dab7d02b8f7daa7db651b)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

向SPI设备提交请求。

<a id="r_gafea78af1fe1fa49fdc5459ab3a2d5f73"></a>

```c
static bool spi_is_ready_iodev (const struct rtio_iodev *spi_iodev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[spi_is_ready_iodev](../hardware/P318_SPI公共接口.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

验证SPI总线以及已定义的片选GPIO是否就绪（Ready）。

## 1.6\_源码定位与版本边界

相对源码定位：[SPI驱动主头文件](../../../include/zephyr/drivers/spi.h)、[SPI绑定常量](../../../include/zephyr/dt-bindings/spi/spi.h)、[SPI设备树辅助宏](../../../include/zephyr/devicetree/spi.h)、[RTIO实现](../../../drivers/spi/spi_rtio.c)、[配置选项](../../../drivers/spi/Kconfig)、[控制器绑定](../../../dts/bindings/spi/spi-controller.yaml)和[设备绑定](../../../dts/bindings/spi/spi-device.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：操作位与类型：SPI_OP_MODE_CONTROLLER为0，PERIPHERAL占位0；旧MASTER／SLAVE名称为弃用别名（Deprecated Alias）。SPI_MODE_MASK为0xE，实际同时包含CPOL、CPHA和LOOP，不能只按摘要措辞理解为极性与相位。SPI_WORD_SIZE_GET取出位5至10的6位字段，SPI_WORD_SET仅左移，不做取值范围检查。多线选择位于位16至17，spi_operation_t在CONFIG_SPI_EXTENDED_MODES启用时为uint32_t，否则为uint16_t；类型和标志存在不表示具体驱动具备相应硬件能力。

> 译注——源码核对：片选初始化形式：原文将SPI_CS_CONTROL_INIT及其实例版描述为“取得指针”，但本次读取的实现展开为花括号结构初始化器（Structure Initializer），并非指针表达式；spi_config.cs也按值保存结构。cs_is_gpio区分GPIO与原生片选（Native Chip Select）的联合体分支。GPIO分支把setup与hold纳秒延时的较大值向上取整转换为微秒delay，原生分支分别保留setup_ns与hold_ns，不能混用字段或单位。

> 译注——源码核对：字间延时：word_delay非零时直接返回其纳秒数；为零且frequency非零时，以整数除法计算1秒纳秒数除以频率，先将整个周期限制到UINT16_MAX，再除以2。因此结果是经上述限幅与截断后的半周期，最大32767纳秒；frequency为零则返回0。原注释写作“频率的一半（half of the frequency）”，代码与绑定定义对应的是周期的一半（Half Period），这里保留原注释并明确单位差异。

> 译注——源码核对：设备树配置与就绪：SPI_CONFIG_DT把调用方operation_与duplex、frame-format、极性、相位、位序、保持片选及片选高有效属性按位或（Bitwise OR）合并；值为0的参数不能清除其他来源已置位的选项。spi_is_ready_dt只检查总线设备以及确实采用GPIO片选时的GPIO端口是否就绪，并不向外设发送探测事务。SPI_SDO_OVERRUN_UNKNOWN为0x100，是无法与有效8位填充值相等的哨兵值（Sentinel）。

> 译注——源码核对：同步、异步与对象生存期：spi_read／spi_write通过spi_transceive分别传入空TX／RX集合；设备树包装传递同一配置的地址。异步函数启动传输后通过回调或信号报告完成，但总线忙时启动调用本身仍可能阻塞。配置、缓冲区描述符、数据及用户上下文应保持有效至相关操作完成，不能把提交返回当作完成。当前回调和信号包装直接调用transceive_async，不检查空函数指针；信号参数为NULL时不提供完成通知。配置选项SPI_ASYNC依赖多线程并选择POLL，网页中的__DOXYGEN__分支不意味着固件已启用这些能力。

> 译注——源码核对：片选保持与总线锁：SPI_HOLD_ON_CS请求在支持且可行时保持片选，SPI_LOCK_ON保留软件所有权，二者不是同一个状态。锁的身份使用传入的spi_config指针，继续事务或调用spi_release时要使用相同配置对象，不能仅复制相同字段后换一个地址。原始主头文件建议通过RTIO提交路径串联异步事务，避免从可能位于中断服务程序（Interrupt Service Routine，ISR）上下文的完成回调重新进入transceive。

> 译注——源码核对：RTIO提交边界：当前spi_iodev_submit直接调用设备API中的iodev_submit，不在此包装中检查NULL或自动选择回退（Fallback）。官方spi_rtio.c另有默认提交函数，将工作交给RTIO工作队列并转换为同步spi_transceive_dt调用；实际采用哪个入口取决于驱动函数表。默认处理支持RX、TX、TINY_TX与TXRX，事务中的提交数量超过CONFIG_SPI_RTIO_FALLBACK_MSGS时报告-ENOMEM，工作请求分配失败也报告-ENOMEM。不能把存在默认实现等同于任意驱动自动支持RTIO。

> 译注——源码核对：统计范围：当前spi_transceive_stats在error非零时增加错误计数，并在每个非空TX／RX集合的count非零时只取第一个缓冲区的len，没有遍历数组求和；无论成功与否都会执行这些长度计数。因此它既不是完整分散／聚集请求的字节总量，也不是实际成功传输字节数。回调和信号包装没有经过这一同步统计调用；具体驱动若有额外统计需另行核对。

> 译注——源码核对：版本边界：本批核对主头文件、SPI绑定常量、设备树SPI宏、RTIO实现、Kconfig与两个公共绑定，共七份官方源码并记录摘要。源码页非注释代码与读取的官方主头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、连接总线、收发数据或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.7\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/dt-bindings/spi/spi.h](../dt_bus_binding_reference/P004_SPI绑定常量头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html)
- [查看此文件的源码](P002_SPI驱动头文件源码.md)
- [spi_cs_control](../hardware/P319_SPI片选控制结构.md)
- [spi_config](../hardware/P320_SPI控制器配置结构.md)
- [spi_dt_spec](../hardware/P321_SPI设备树描述结构.md)
- [spi_buf](../hardware/P322_SPI缓冲区结构.md)
- [spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)
- [spi_driver_api](../hardware/P325_SPI驱动函数表.md)
- [SPI_CONFIG_DT](../hardware/P318_SPI公共接口.md#gaf7d4888063e5b739f2a3bee295962bfe)
- [SPI_CONFIG_DT_INST](../hardware/P318_SPI公共接口.md#ga67837cbae6f29c5f8ad9a05dbc9b05f8)
- [SPI_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga43857c934651c4bfb3823a5080a4a294)
- [SPI_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#gac9537325ca3188121d0f8c382c798ca1)
- [SPI_SDO_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga1dbef324b98a8921507de0da1c4e4fa6)
- [SPI_MOSI_OVERRUN_UNKNOWN](../hardware/P318_SPI公共接口.md#ga15b5fa509a3b7dc87bfd451af5a11917)
- [SPI_SDO_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaf66331d56f20e0c37f2a3cff998c6bce)
- [SPI_MOSI_OVERRUN_DT](../hardware/P318_SPI公共接口.md#gaa9621b033dfaf128602b1432927a67fe)
- [SPI_SDO_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga0e05910cd0be7211389514b7b4edc0cc)
- [SPI_MOSI_OVERRUN_DT_INST](../hardware/P318_SPI公共接口.md#ga24c7416a98421e353a8892151f34122c)
- [SPI_STATS_RX_BYTES_INC](../hardware/P318_SPI公共接口.md#ga83fa04d1e9f281cd566ee32cf807325e)
- [SPI_STATS_TX_BYTES_INC](../hardware/P318_SPI公共接口.md#gadd3b82af2396b91930ece09fa79fc4e2)
- [SPI_STATS_TRANSFER_ERROR_INC](../hardware/P318_SPI公共接口.md#ga6f69e68a79afbbe016aecc515f14de3a)
- [spi_transceive_stats](../hardware/P318_SPI公共接口.md#gad7d1058f600d6aef4fc4e2bdff5d55f3)
- [SPI_DEVICE_DT_DEFINE](../hardware/P318_SPI公共接口.md#ga27af5f053c5fd4e9eef0900406fbf854)
- [DEVICE_DT_DEINIT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gaa53f7267950569df898b0e5362e6f583)
- [SPI_DEVICE_DT_INST_DEINIT_DEFINE](../hardware/P318_SPI公共接口.md#ga50cbb6845d230033f192f1e716fd9f2b)
- [SPI_DEVICE_DT_DEINIT_DEFINE()](../hardware/P318_SPI公共接口.md#gaf98b0cb38cb316b9fe05146bba34126d)
- [SPI_DEVICE_DT_INST_DEFINE](../hardware/P318_SPI公共接口.md#ga84811e0fdd574477c8569d559f773dae)
- [SPI_OP_MODE_CONTROLLER](../hardware/P318_SPI公共接口.md#gace0f0d954c2bd7d603c4003289c11102)
- [SPI_OP_MODE_PERIPHERAL](../hardware/P318_SPI公共接口.md#gaa1f42ffeac36380f4d1d8f84bda2990b)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SPI_OP_MODE_MASTER](../hardware/P318_SPI公共接口.md#ga5b9d40fa0f455b1e63f8040b3316b0da)
- [SPI_OP_MODE_SLAVE](../hardware/P318_SPI公共接口.md#ga1c3310d3711cb99cdb78fa9d1c970779)
- [SPI_OP_MODE_GET](../hardware/P318_SPI公共接口.md#ga6dd4395e027407a7b3b92cff2abcc8b3)
- [spi_operation_t](../hardware/P318_SPI公共接口.md#ga398a8ae1c4799e77fb6c067b6d47294a)
- [SPI_MODE_CPOL](../hardware/P318_SPI公共接口.md#ga5a2be1003873beaa0ade10e7218d67d5)
- [SPI_MODE_CPHA](../hardware/P318_SPI公共接口.md#ga35e98b37e3ec4889a90100abe884590f)
- [SPI_MODE_LOOP](../hardware/P318_SPI公共接口.md#ga8619b297de563eca6852af34c79daa62)
- [SPI_MODE_GET](../hardware/P318_SPI公共接口.md#gaa3582b96ff42dba0b0ad815c727d5e42)
- [SPI_TRANSFER_MSB](../hardware/P318_SPI公共接口.md#ga7761f42c6241cf396fc02d0de8617e46)
- [SPI_TRANSFER_LSB](../hardware/P318_SPI公共接口.md#ga93504a76a265bedbe781c107beebc9dc)
- [SPI_WORD_SIZE_GET](../hardware/P318_SPI公共接口.md#gacd7edd9ce02bd8351f8eebe5b5c07c7a)
- [SPI_WORD_SET](../hardware/P318_SPI公共接口.md#gac1115bf80134efd38d88161e3f5e3e1a)
- [SPI_HOLD_ON_CS](../hardware/P318_SPI公共接口.md#gae917312adef283b4bf67cdb53566e4bb)
- [SPI_LOCK_ON](../hardware/P318_SPI公共接口.md#gafe8dc164d6fc0a0f93f2ff9d5381af14)
- [SPI_CS_ACTIVE_HIGH](../hardware/P318_SPI公共接口.md#ga44076fa14703997f7e3aefb2bfccd801)
- [CONFIG_SPI_EXTENDED_MODES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_EXTENDED_MODES)
- [SPI_LINES_SINGLE](../hardware/P318_SPI公共接口.md#ga7a183f157e8cb8b437857a0babbd923b)
- [SPI_LINES_DUAL](../hardware/P318_SPI公共接口.md#ga120ab60329d664d5d6e828f90251a98a)
- [SPI_LINES_QUAD](../hardware/P318_SPI公共接口.md#ga30866b948e995224de854e10a428bda5)
- [SPI_LINES_OCTAL](../hardware/P318_SPI公共接口.md#ga512d76085e600886654b8541aab31cf7)
- [SPI_LINES_MASK](../hardware/P318_SPI公共接口.md#gadc79f986c4b30fe5b263841cd8bb5676)
- [SPI_CS_GPIOS_DT_SPEC_GET](../hardware/P318_SPI公共接口.md#ga48aa19f45413d56b03596d10b72c732e)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [SPI_CS_GPIOS_DT_SPEC_INST_GET](../hardware/P318_SPI公共接口.md#ga88fefbfadb8184806123e1f935a4ff7c)
- [SPI_CS_CONTROL_INIT](../hardware/P318_SPI公共接口.md#ga81308d27cd78e65f0a3ddaa918f2a74a)
- [SPI_CS_CONTROL_INIT_INST](../hardware/P318_SPI公共接口.md#ga92195f45dac561b19204f6be21f62b55)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [spi_api_io](../hardware/P324_SPI驱动后端接口.md#ga3fc669f866b03cfdad98754de69cda13)
- [device](../device_reference/P002_设备对象结构.md)
- [spi_callback_t](../hardware/P324_SPI驱动后端接口.md#ga1db2a410f482d0f26c49f96352aa606d)
- [spi_api_io_async](../hardware/P324_SPI驱动后端接口.md#ga03be7f33032ac479153616bbe26848e7)
- [spi_api_iodev_submit](../hardware/P324_SPI驱动后端接口.md#gae274c0d704e8fd8993631fc1b91bfcb1)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [spi_api_release](../hardware/P324_SPI驱动后端接口.md#gac651ff7cd3dde7abe2525e20ef2e9e7d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [spi_cs_is_gpio](../hardware/P318_SPI公共接口.md#gae1156a4ee1b5909c321811045566d888)
- [spi_cs_is_gpio_dt](../hardware/P318_SPI公共接口.md#gaa13f0da1f28cffa0da4677987db0c9c5)
- [spi_is_ready_dt](../hardware/P318_SPI公共接口.md#ga37b4e5079ed18b70b0c5a260f4c36403)
- [spi_release](../hardware/P318_SPI公共接口.md#ga0c4f4f0a93bb83a4f58d551a7491164e)
- [spi_release_dt](../hardware/P318_SPI公共接口.md#ga829b59767c51b20b546eee8a9cc84b69)
- [spi_transceive](../hardware/P318_SPI公共接口.md#gad51054c1ba259db5a64619788506a6f5)
- [spi_transceive_dt](../hardware/P318_SPI公共接口.md#ga52c017066736414b31ff709ddc67c4ff)
- [spi_read](../hardware/P318_SPI公共接口.md#ga41f771785a4fa9ca0954125d1e97959e)
- [spi_read_dt](../hardware/P318_SPI公共接口.md#ga7a1d7ebd37d2861b169c265cb90015bf)
- [spi_write](../hardware/P318_SPI公共接口.md#ga7e7c4460670ec1c0433ba19accd97796)
- [spi_write_dt](../hardware/P318_SPI公共接口.md#ga292d6d1fe82f3f1ce0d9a2aa5437201b)
- [spi_transceive_cb](../hardware/P318_SPI公共接口.md#ga6114e63ca23b82f9be0ac70e372b878b)
- [spi_transceive_signal](../hardware/P318_SPI公共接口.md#ga41b8a541257c0d45575fdc4593417edc)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [spi_read_signal](../hardware/P318_SPI公共接口.md#ga9a1ceadb217368232af5b688c12169c5)
- [spi_write_signal](../hardware/P318_SPI公共接口.md#gadcb19d43461ef88e31f6b382cc87fd0b)
- [SPI_DT_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga1eec8a77be8a512e8b0fa74d270877e5)
- [SPI_DT_INST_IODEV_DEFINE](../hardware/P318_SPI公共接口.md#ga4e5633f6e8da22f4c00a723a669b2d9a)
- [spi_iodev_submit](../hardware/P318_SPI公共接口.md#ga8b23855bdc7dab7d02b8f7daa7db651b)
- [spi_is_ready_iodev](../hardware/P318_SPI公共接口.md#gafea78af1fe1fa49fdc5459ab3a2d5f73)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_SPI驱动头文件源码.md)
