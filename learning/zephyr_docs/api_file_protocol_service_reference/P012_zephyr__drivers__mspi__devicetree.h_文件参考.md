---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-12
title: zephyr__drivers__mspi__devicetree.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_mspi\_\_devicetree.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI设备树辅助宏（Devicetree Helper Macros）。

<a id="details"></a>

```c
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

MSPI设备树辅助宏（Devicetree Helper Macros）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_gaa8e730d85dede3d1e5dc9f69f30098b2"></a>

```c
#define MSPI_DEVICE_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_DEVICE_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaa8e730d85dede3d1e5dc9f69f30098b2)。

根据设备树（Devicetree）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga52ebf325f9a1eb7d9fda6736ac8188f1"></a>

```c
#define MSPI_DEVICE_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_DEVICE_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga52ebf325f9a1eb7d9fda6736ac8188f1)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga10adb4485f539b81e6cbafe49623a7d6"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT_NO_CHECK(mspi_dev)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT_NO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga10adb4485f539b81e6cbafe49623a7d6)。

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga8dded3aee3ae6098e2fe0416333bdc72"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga8dded3aee3ae6098e2fe0416333bdc72)。

根据设备树（Devicetree）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_gaaf82576a11df72c2e10ea27944211413"></a>

```c
#define MSPI_MEMMAP_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_MEMMAP_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaaf82576a11df72c2e10ea27944211413)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_memmap_cfg` 的结构体初始化器（Initializer）。

<a id="r_gad1f36df770167384cc4e3f2c9be07d34"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK(mspi_dev)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gad1f36df770167384cc4e3f2c9be07d34)。

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_ga10ee161794b5c7986a4411b8fc90ea7d"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT(mspi_dev)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga10ee161794b5c7986a4411b8fc90ea7d)。

根据设备树（Devicetree）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_gaa9b32a8f6984468b5198524bea42ed8c"></a>

```c
#define MSPI_SCRAMBLE_CONFIG_DT_INST(inst)
```

相关声明：[MSPI_SCRAMBLE_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaa9b32a8f6984468b5198524bea42ed8c)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_scramble_cfg` 的结构体初始化器（Initializer）。

<a id="r_gafa7c0d76c85a31004d72392016da1246"></a>

```c
#define MSPI_DEVICE_ID_DT(mspi_dev)
```

相关声明：[MSPI_DEVICE_ID_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gafa7c0d76c85a31004d72392016da1246)。

根据设备树（Devicetree）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

<a id="r_gabfd0d3beb91762e939636c87a91a6673"></a>

```c
#define MSPI_DEVICE_ID_DT_INST(inst)
```

相关声明：[MSPI_DEVICE_ID_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gabfd0d3beb91762e939636c87a91a6673)。

根据设备树实例（Devicetree Instance）构造 `struct mspi_dev_id` 的结构体初始化器（Initializer）。

<a id="r_ga0a91ef9392be4493ede6cea607ee8728"></a>

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_GET(mspi_dev)
```

相关声明：[MSPI_DEV_CE_GPIOS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga0a91ef9392be4493ede6cea607ee8728)。

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

<a id="r_ga0b98f7a625324abce90933cb2395fb17"></a>

```c
#define MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET(inst)
```

相关声明：[MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga0b98f7a625324abce90933cb2395fb17)。

获取 MSPI 设备片选使能引脚（Chip Enable Pin）的 `struct gpio_dt_spec`。

<a id="r_ga1ca28d7ead69cd3a5e26198bc6815b54"></a>

```c
#define MSPI_CE_GPIOS_DT_SPEC_GET(node_id)
```

相关声明：[MSPI_CE_GPIOS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga1ca28d7ead69cd3a5e26198bc6815b54)。

根据设备树（Devicetree）获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

<a id="r_ga5ae4bd8071da4babd0bdf9767e9542e4"></a>

```c
#define MSPI_CE_GPIOS_DT_SPEC_INST_GET(inst)
```

相关声明：[MSPI_CE_GPIOS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga5ae4bd8071da4babd0bdf9767e9542e4)。

获取 MSPI 控制器的 `struct gpio_dt_spec` 数组。

<a id="r_ga501b2e19e358083f2b47838cde58a676"></a>

```c
#define MSPI_CE_CONTROL_INIT(node_id, delay_)
```

相关声明：[MSPI_CE_CONTROL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga501b2e19e358083f2b47838cde58a676)。

根据设备树节点标识符（Devicetree Node Identifier）初始化 `mspi_ce_control`，并获取其指针。

<a id="r_gacec91c9080052adf96aa5d36c6301d8c"></a>

```c
#define MSPI_CE_CONTROL_INIT_INST(inst, delay_)
```

相关声明：[MSPI_CE_CONTROL_INIT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gacec91c9080052adf96aa5d36c6301d8c)。

根据设备树节点（Devicetree Node）获取 `mspi_ce_control` 指针。


## 12.2\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P166_devicetree.h_源码浏览.md)
- [MSPI_DEVICE_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaa8e730d85dede3d1e5dc9f69f30098b2)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [MSPI_DEVICE_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga52ebf325f9a1eb7d9fda6736ac8188f1)
- [MSPI_MEMMAP_CONFIG_DT_NO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga10adb4485f539b81e6cbafe49623a7d6)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [MSPI_MEMMAP_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga8dded3aee3ae6098e2fe0416333bdc72)
- [MSPI_MEMMAP_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaaf82576a11df72c2e10ea27944211413)
- [MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gad1f36df770167384cc4e3f2c9be07d34)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [MSPI_SCRAMBLE_CONFIG_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga10ee161794b5c7986a4411b8fc90ea7d)
- [MSPI_SCRAMBLE_CONFIG_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gaa9b32a8f6984468b5198524bea42ed8c)
- [MSPI_DEVICE_ID_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gafa7c0d76c85a31004d72392016da1246)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [MSPI_DEVICE_ID_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gabfd0d3beb91762e939636c87a91a6673)
- [MSPI_DEV_CE_GPIOS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga0a91ef9392be4493ede6cea607ee8728)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga0b98f7a625324abce90933cb2395fb17)
- [MSPI_CE_GPIOS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga1ca28d7ead69cd3a5e26198bc6815b54)
- [MSPI_CE_GPIOS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga5ae4bd8071da4babd0bdf9767e9542e4)
- [MSPI_CE_CONTROL_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#ga501b2e19e358083f2b47838cde58a676)
- [mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)
- [MSPI_CE_CONTROL_INIT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html#gacec91c9080052adf96aa5d36c6301d8c)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__crc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__pcie__controller.h_文件参考.md)
