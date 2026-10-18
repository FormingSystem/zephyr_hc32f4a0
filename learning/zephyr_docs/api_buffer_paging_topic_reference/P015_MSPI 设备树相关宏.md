---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-15
title: MSPI 设备树相关宏
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_MSPI 设备树相关宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI 设备树相关宏

<a id="details"></a>

MSPI 设备树相关宏

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_devicetree_2Eh"></a>

```c
file devicetree.h
```

相关声明：[devicetree.h](../api_file_protocol_service_reference/P012_zephyr__drivers__mspi__devicetree.h_文件参考.md)。

MSPI设备树辅助宏（Devicetree Helper Macros）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_gaa8e730d85dede3d1e5dc9f69f30098b2"></a>

```c
#define MSPI_DEVICE_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_DEVICE_CONFIG_DT](#gaa8e730d85dede3d1e5dc9f69f30098b2)。

根据设备树（Devicetree）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga52ebf325f9a1eb7d9fda6736ac8188f1"></a>

```c
#define MSPI_DEVICE_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_DEVICE_CONFIG_DT_INST](#ga52ebf325f9a1eb7d9fda6736ac8188f1)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga10adb4485f539b81e6cbafe49623a7d6"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT_NO_CHECK(mspi_dev)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT_NO_CHECK](#ga10adb4485f539b81e6cbafe49623a7d6)。

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga8dded3aee3ae6098e2fe0416333bdc72"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT](#ga8dded3aee3ae6098e2fe0416333bdc72)。

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_gaaf82576a11df72c2e10ea27944211413"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT_INST](#gaaf82576a11df72c2e10ea27944211413)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_gad1f36df770167384cc4e3f2c9be07d34"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK(mspi_dev)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK](#gad1f36df770167384cc4e3f2c9be07d34)。

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga10ee161794b5c7986a4411b8fc90ea7d"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT](#ga10ee161794b5c7986a4411b8fc90ea7d)。

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_gaa9b32a8f6984468b5198524bea42ed8c"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT_INST](#gaa9b32a8f6984468b5198524bea42ed8c)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_gafa7c0d76c85a31004d72392016da1246"></a>

```c
#define MSPI_DEVICE_ID_DT(mspi_dev)
```

相关声明：[MSPI_DEVICE_ID_DT](#gafa7c0d76c85a31004d72392016da1246)。

根据设备树（Devicetree）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

<a id="r_gabfd0d3beb91762e939636c87a91a6673"></a>

```c
#define MSPI_DEVICE_ID_DT_INST(inst)
```

相关声明：[MSPI_DEVICE_ID_DT_INST](#gabfd0d3beb91762e939636c87a91a6673)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

<a id="r_ga0a91ef9392be4493ede6cea607ee8728"></a>

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_GET(mspi_dev)
```

相关声明：[MSPI_DEV_CE_GPIOS_DT_SPEC_GET](#ga0a91ef9392be4493ede6cea607ee8728)。

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

<a id="r_ga0b98f7a625324abce90933cb2395fb17"></a>

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET(inst)
```

相关声明：[MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET](#ga0b98f7a625324abce90933cb2395fb17)。

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

<a id="r_ga1ca28d7ead69cd3a5e26198bc6815b54"></a>

```c
#define MSPI_CE_GPIOS_DT_SPEC_GET(node_id)
```

相关声明：[MSPI_CE_GPIOS_DT_SPEC_GET](#ga1ca28d7ead69cd3a5e26198bc6815b54)。

根据设备树（Devicetree）获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

<a id="r_ga5ae4bd8071da4babd0bdf9767e9542e4"></a>

```c
#define MSPI_CE_GPIOS_DT_SPEC_INST_GET(inst)
```

相关声明：[MSPI_CE_GPIOS_DT_SPEC_INST_GET](#ga5ae4bd8071da4babd0bdf9767e9542e4)。

获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

<a id="r_ga501b2e19e358083f2b47838cde58a676"></a>

```c
#define MSPI_CE_CONTROL_INIT(node_id, delay_)
```

相关声明：[MSPI_CE_CONTROL_INIT](#ga501b2e19e358083f2b47838cde58a676)。

根据设备树节点标识符（Devicetree Node Identifier）初始化 `mspi_ce_control`，并获取其指针。

<a id="r_gacec91c9080052adf96aa5d36c6301d8c"></a>

```c
#define MSPI_CE_CONTROL_INIT_INST(inst, delay_)
```

相关声明：[MSPI_CE_CONTROL_INIT_INST](#gacec91c9080052adf96aa5d36c6301d8c)。

根据设备树节点（Devicetree Node）获取 `mspi_ce_control` 指针。

## 15.3\_详细说明（Detailed Documentation）

<a id="ga501b2e19e358083f2b47838cde58a676"></a>

### `MSPI_CE_CONTROL_INIT`

```c
#define MSPI_CE_CONTROL_INIT ( node_id, delay_ )
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                         \
        .gpio = MSPI_DEV_CE_GPIOS_DT_SPEC_GET(node_id), .delay = (delay_),                \
}
```

根据设备树节点标识符（Devicetree Node Identifier）初始化 `mspi_ce_control`，并获取其指针。

此辅助接口用于初始化 MSPI 总线上的设备：初始化一个 struct mspi_ce_control 并返回其指针。这里的 node_id 是 MSPI 设备的节点标识符（Node Identifier），而不是 MSPI 控制器的节点标识符。

设备树片段示例：

原始示例（Example）：

```c
mspi@abcd0001 {
        ce-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>;
        mspidev: mspi-device@0 { ... };
};
```

使用示例：

原始示例（Example）：

```c
struct mspi_ce_control ctrl =
        MSPI_CE_CONTROL_INIT(DT_NODELABEL(mspidev), 2);
```

此示例等价于：

原始示例（Example）：

```c
struct mspi_ce_control ctrl = {
        .gpio = MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_NODELABEL(mspidev)),
        .delay = 2,
};
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | MSPI 总线上设备的设备树节点标识符（Devicetree Node Identifier） |
| `delay_` | 要在 mspi_ce_control 中设置的 delay 字段 |

**返回（Returns）**：返回值（Returns）：指向 mspi_ce_control 结构体的指针。

<a id="gacec91c9080052adf96aa5d36c6301d8c"></a>

### `MSPI_CE_CONTROL_INIT_INST`

```c
#define MSPI_CE_CONTROL_INIT_INST ( inst, delay_ )
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_CE_CONTROL_INIT(DT_DRV_INST(inst), delay_)
```

根据设备树节点（Devicetree Node）获取 `mspi_ce_control` 指针。

等价于 `MSPI_CE_CONTROL_INIT(DT_DRV_INST(inst), delay)`。

因此，使用此宏之前必须已定义 DT_DRV_COMPAT。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树节点实例编号（Devicetree Node Instance Number） |
| `delay_` | 要在 mspi_ce_control 中设置的 delay 字段 |

**返回（Returns）**：返回值（Returns）：指向 mspi_ce_control 结构体的指针。

<a id="ga1ca28d7ead69cd3a5e26198bc6815b54"></a>

### `MSPI_CE_GPIOS_DT_SPEC_GET`

```c
#define MSPI_CE_GPIOS_DT_SPEC_GET ( node_id)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                                 \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, ce_gpios),                                          \
                (DT_FOREACH_PROP_ELEM_SEP(node_id, ce_gpios, GPIO_DT_SPEC_GET_BY_IDX, (,))),      \
                ())                                                                               \
}
```

根据设备树（Devicetree）获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

此辅助宏首先检查 ce_gpios 绑定（Binding）是否存在，然后调用 GPIO_DT_SPEC_GET_BY_IDX，展开为 gpio_dt_spec 数组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | MSPI 控制器的设备树节点标识符（Devicetree Node Identifier） |

**返回（Returns）**：返回值（Returns）：与 mspi_dev 的片选使能（Chip Enables）对应的 gpio_dt_spec 结构体数组。

<a id="ga5ae4bd8071da4babd0bdf9767e9542e4"></a>

### `MSPI_CE_GPIOS_DT_SPEC_INST_GET`

```c
#define MSPI_CE_GPIOS_DT_SPEC_INST_GET ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))
```

获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

等价于 `MSPI_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

**返回（Returns）**：返回值（Returns）：与 mspi_dev 的片选使能（Chip Enables）对应的 gpio_dt_spec 结构体数组。

<a id="ga0a91ef9392be4493ede6cea607ee8728"></a>

### `MSPI_DEV_CE_GPIOS_DT_SPEC_GET`

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_GET ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
GPIO_DT_SPEC_GET_BY_IDX_OR(DT_BUS(mspi_dev), ce_gpios,                            \
                           DT_REG_ADDR_RAW(mspi_dev), {})
```

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

设备树片段示例：

原始示例（Example）：

```c
gpio1: gpio@abcd0001 { ... };

gpio2: gpio@abcd0002 { ... };

mspi@abcd0003 {
        compatible = "ambiq,mspi";
        ce-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: mspi-dev-a@0 {
                reg = <0>;
        };

        b: mspi-dev-b@1 {
                reg = <1>;
        };
};
```

使用示例：

原始示例（Example）：

```c
MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_NODELABEL(a)) \
      // { DEVICE_DT_GET(DT_NODELABEL(gpio1)), 10, GPIO_ACTIVE_LOW }
MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_NODELABEL(b)) \
      // { DEVICE_DT_GET(DT_NODELABEL(gpio2)), 20, GPIO_ACTIVE_LOW }
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备节点标识符（Device Node Identifier） |

**返回（Returns）**：返回值（Returns）：与 mspi_dev 的片选使能（Chip Enable）对应的 gpio_dt_spec 结构体。

<a id="ga0b98f7a625324abce90933cb2395fb17"></a>

### `MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET`

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))
```

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

等价于 `MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

**返回（Returns）**：返回值（Returns）：与 mspi_dev 的片选使能（Chip Enable）对应的 gpio_dt_spec 结构体。

<a id="gaa8e730d85dede3d1e5dc9f69f30098b2"></a>

### `MSPI_DEVICE_CONFIG_DT`

```c
#define MSPI_DEVICE_CONFIG_DT ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                         \
        .ce_num               = DT_PROP_OR(mspi_dev, mspi_hardware_ce_num, 0),            \
        .freq                 = DT_PROP(mspi_dev, mspi_max_frequency),                    \
        .io_mode              = DT_ENUM_IDX_OR(mspi_dev, mspi_io_mode,                    \
                                        MSPI_IO_MODE_SINGLE),                             \
        .data_rate            = DT_ENUM_IDX_OR(mspi_dev, mspi_data_rate,                  \
                                        MSPI_DATA_RATE_SINGLE),                           \
        .cpp                  = DT_ENUM_IDX_OR(mspi_dev, mspi_cpp_mode, MSPI_CPP_MODE_0), \
        .endian               = DT_ENUM_IDX_OR(mspi_dev, mspi_endian,                     \
                                        MSPI_XFER_LITTLE_ENDIAN),                         \
        .ce_polarity          = DT_ENUM_IDX_OR(mspi_dev, mspi_ce_polarity,                \
                                        MSPI_CE_ACTIVE_LOW),                              \
        .dqs_enable           = DT_PROP(mspi_dev, mspi_dqs_enable),                       \
        .rx_dummy             = DT_PROP_OR(mspi_dev, rx_dummy, 0),                        \
        .tx_dummy             = DT_PROP_OR(mspi_dev, tx_dummy, 0),                        \
        .read_cmd             = DT_PROP_OR(mspi_dev, read_command, 0),                    \
        .write_cmd            = DT_PROP_OR(mspi_dev, write_command, 0),                   \
        .cmd_length           = DT_ENUM_IDX_OR(mspi_dev, command_length, 0),              \
        .addr_length          = DT_ENUM_IDX_OR(mspi_dev, address_length, 0),              \
        .mem_boundary         = COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, ce_break_config),  \
                                        (DT_PROP_BY_IDX(mspi_dev, ce_break_config, 0)),   \
                                        (0)),                                             \
        .time_to_break        = COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, ce_break_config),  \
                                        (DT_PROP_BY_IDX(mspi_dev, ce_break_config, 1)),   \
                                        (0)),                                             \
}
```

根据设备树（Devicetree）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

此辅助宏读取设备树（Devicetree）中的相关数据，展开为 struct mspi_dev_cfg 的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_dev_cfg 创建初始化器。 |

<a id="ga52ebf325f9a1eb7d9fda6736ac8188f1"></a>

### `MSPI_DEVICE_CONFIG_DT_INST`

```c
#define MSPI_DEVICE_CONFIG_DT_INST ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_DEVICE_CONFIG_DT(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

等价于 `MSPI_DEVICE_CONFIG_DT(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="gafa7c0d76c85a31004d72392016da1246"></a>

### `MSPI_DEVICE_ID_DT`

```c
#define MSPI_DEVICE_ID_DT ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                         \
        .ce                   = MSPI_DEV_CE_GPIOS_DT_SPEC_GET(mspi_dev),                  \
        .dev_idx              = DT_REG_ADDR(mspi_dev),                                    \
}
```

根据设备树（Devicetree）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

此辅助宏读取设备树（Devicetree）中的相关数据，展开为 struct mspi_dev_id 的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_dev_id 创建初始化器。 |

<a id="gabfd0d3beb91762e939636c87a91a6673"></a>

### `MSPI_DEVICE_ID_DT_INST`

```c
#define MSPI_DEVICE_ID_DT_INST ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_DEVICE_ID_DT(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

等价于 `MSPI_DEVICE_ID_DT(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="ga8dded3aee3ae6098e2fe0416333bdc72"></a>

### `MSPI_MEMMAP_CONFIG_DT`

```c
#define MSPI_MEMMAP_CONFIG_DT ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, memmap_config),                            \
        (MSPI_MEMMAP_CONFIG_DT_NO_CHECK(mspi_dev)),                               \
        ({}))
```

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

此辅助宏首先检查 memmap_config 绑定（Binding）是否存在，然后调用 MSPI_MEMMAP_CONFIG_DT_NO_CHECK。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_memmap_cfg 创建初始化器。 |

<a id="gaaf82576a11df72c2e10ea27944211413"></a>

### `MSPI_MEMMAP_CONFIG_DT_INST`

```c
#define MSPI_MEMMAP_CONFIG_DT_INST ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_MEMMAP_CONFIG_DT(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

等价于 `MSPI_MEMMAP_CONFIG_DT(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="ga10adb4485f539b81e6cbafe49623a7d6"></a>

### `MSPI_MEMMAP_CONFIG_DT_NO_CHECK`

```c
#define MSPI_MEMMAP_CONFIG_DT_NO_CHECK ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                         \
        .enable               = DT_PROP_BY_IDX(mspi_dev, memmap_config, 0),               \
        .address_offset       = DT_PROP_BY_IDX(mspi_dev, memmap_config, 1),               \
        .size                 = DT_PROP_BY_IDX(mspi_dev, memmap_config, 2),               \
        .permission           = DT_PROP_BY_IDX(mspi_dev, memmap_config, 3),               \
}
```

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

此辅助宏读取设备树（Devicetree）中的相关数据，展开为 struct mspi_memmap_cfg 的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_memmap_cfg 创建初始化器。 |

<a id="ga10ee161794b5c7986a4411b8fc90ea7d"></a>

### `MSPI_SCRAMBLE_CONFIG_DT`

```c
#define MSPI_SCRAMBLE_CONFIG_DT ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, scramble_config),                          \
        (MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK(mspi_dev)),                             \
        ({}))
```

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

此辅助宏首先检查 scramble_config 绑定（Binding）是否存在，然后调用 MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_scramble_cfg 创建初始化器。 |

<a id="gaa9b32a8f6984468b5198524bea42ed8c"></a>

### `MSPI_SCRAMBLE_CONFIG_DT_INST`

```c
#define MSPI_SCRAMBLE_CONFIG_DT_INST ( inst)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
MSPI_SCRAMBLE_CONFIG_DT(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

等价于 `MSPI_SCRAMBLE_CONFIG_DT(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="gad1f36df770167384cc4e3f2c9be07d34"></a>

### `MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK`

```c
#define MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK ( mspi_dev)
```

```c
#include <zephyr/drivers/mspi/devicetree.h>
```

展开值（Value）：

```c
{                                                                                         \
        .enable               = DT_PROP_BY_IDX(mspi_dev, scramble_config, 0),             \
        .address_offset       = DT_PROP_BY_IDX(mspi_dev, scramble_config, 1),             \
        .size                 = DT_PROP_BY_IDX(mspi_dev, scramble_config, 2),             \
}
```

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

此辅助宏读取设备树（Devicetree）中的相关数据，展开为 struct mspi_scramble_cfg 的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mspi_dev` | MSPI 设备的设备树节点标识符（Devicetree Node Identifier），用于为其 struct mspi_scramble_cfg 创建初始化器。 |


## 15.4\_原页交叉引用（Cross References）

- [devicetree.h](../api_file_protocol_service_reference/P012_zephyr__drivers__mspi__devicetree.h_文件参考.md)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_FOREACH_PROP_ELEM_SEP](../dt_foreach_reference/P001_设备树遍历宏.md#ga72d0b6859b4fc61cde518aee118d9ed8)
- [GPIO_DT_SPEC_GET_BY_IDX](../hardware/P266_GPIO公共接口.md#gacb1077b77aecf8f1a9c7636ea583c4cf)
- [GPIO_DT_SPEC_GET_BY_IDX_OR](../hardware/P266_GPIO公共接口.md#ga3db4fa464e191016287f4c4d7eb9a983)
- [DT_BUS](../dt_node_reference/P001_设备树总线查询宏.md#ga1082d31ac2dafdf9e085d4c23f2169dc)
- [DT_REG_ADDR_RAW](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga14ebfb75548e45279f3954a75a5f9ac1)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_ENUM_IDX_OR](../dt_property_reference/P001_设备树属性读取宏.md#gac3616e3aa1a025235032786de8d31576)
- [mspi_io_mode](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga904dfc1c800fb9832f7c6200f767f9a5)
- [MSPI_IO_MODE_SINGLE](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)
- [mspi_data_rate](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gaa2131d9846bbfd74488a6ae1c2003e68)
- [MSPI_DATA_RATE_SINGLE](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)
- [mspi_cpp_mode](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga704e4d3759d3261b4468e9d9900e578c)
- [MSPI_CPP_MODE_0](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)
- [mspi_endian](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga3625cde1379e66cb66a8cb3803ab2e44)
- [MSPI_XFER_LITTLE_ENDIAN](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)
- [mspi_ce_polarity](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga283275f86fe186f4b5e30110ae0d506b)
- [MSPI_CE_ACTIVE_LOW](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__mspi__devicetree_html_ga0a91ef9392be4493ede6cea607ee8728"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__mspi__devicetree_html_ga501b2e19e358083f2b47838cde58a676"></a>
<a id="astructmspi__ce__control_html"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-foreach_html_ga72d0b6859b4fc61cde518aee118d9ed8"></a>
<a id="agroup__gpio__interface_html_gacb1077b77aecf8f1a9c7636ea583c4cf"></a>
<a id="agroup__mspi__devicetree_html_ga1ca28d7ead69cd3a5e26198bc6815b54"></a>
<a id="agroup__devicetree-generic-bus_html_ga1082d31ac2dafdf9e085d4c23f2169dc"></a>
<a id="agroup__devicetree-reg-prop_html_ga14ebfb75548e45279f3954a75a5f9ac1"></a>
<a id="agroup__gpio__interface_html_ga3db4fa464e191016287f4c4d7eb9a983"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__devicetree-generic-prop_html_gac3616e3aa1a025235032786de8d31576"></a>
<a id="agroup__mspi__interface_html_ga283275f86fe186f4b5e30110ae0d506b"></a>
<a id="agroup__mspi__interface_html_ga3625cde1379e66cb66a8cb3803ab2e44"></a>
<a id="agroup__mspi__interface_html_ga704e4d3759d3261b4468e9d9900e578c"></a>
<a id="agroup__mspi__interface_html_ga904dfc1c800fb9832f7c6200f767f9a5"></a>
<a id="agroup__mspi__interface_html_gaa2131d9846bbfd74488a6ae1c2003e68"></a>
<a id="agroup__mspi__interface_html_gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae"></a>
<a id="agroup__mspi__interface_html_gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345"></a>
<a id="agroup__mspi__interface_html_gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90"></a>
<a id="agroup__mspi__interface_html_gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd"></a>
<a id="agroup__mspi__interface_html_ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__mspi__devicetree_html_gaa8e730d85dede3d1e5dc9f69f30098b2"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="agroup__mspi__devicetree_html_gafa7c0d76c85a31004d72392016da1246"></a>
<a id="agroup__mspi__devicetree_html_ga10adb4485f539b81e6cbafe49623a7d6"></a>
<a id="agroup__mspi__devicetree_html_ga8dded3aee3ae6098e2fe0416333bdc72"></a>
<a id="agroup__mspi__devicetree_html_gad1f36df770167384cc4e3f2c9be07d34"></a>
<a id="agroup__mspi__devicetree_html_ga10ee161794b5c7986a4411b8fc90ea7d"></a>

---

[上一章](P014_缓冲区（Buffers）.md) · [返回大纲](大纲.md) · [下一章](P016_多路复用器（MUX）.md)
