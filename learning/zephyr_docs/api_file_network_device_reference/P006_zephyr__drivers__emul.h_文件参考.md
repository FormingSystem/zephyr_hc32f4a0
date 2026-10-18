---
id: learning.zephyr-docs.api-file-network-device-reference.page-6
title: zephyr__drivers__emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备仿真框架（Device Emulation Framework）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/espi_emul.h>
#include <zephyr/drivers/i2c_emul.h>
#include <zephyr/drivers/spi_emul.h>
#include <zephyr/drivers/mspi_emul.h>
#include <zephyr/drivers/uart_emul.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

设备仿真框架（Device Emulation Framework）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_emul_5Flink_5Ffor_5Fbus"></a>

```c
struct emul_link_for_bus
```

相关声明：[emul_link_for_bus](../hardware/P478_总线仿真器链接结构.md)。

唯一标识待仿真设备的结构。

<a id="r_emul_5Flist_5Ffor_5Fbus"></a>

```c
struct emul_list_for_bus
```

相关声明：[emul_list_for_bus](../hardware/P479_总线仿真器列表结构.md)。

连接到总线的仿真器（Emulator）列表。

<a id="r_no_5Fbus_5Femul"></a>

```c
struct no_bus_emul
```

相关声明：[no_bus_emul](../hardware/P480_无总线仿真器桩结构.md)。

仿真器未实际置于总线时使用的仿真器API占位实现（Emulator API Stub）。

<a id="r_emul"></a>

```c
struct emul
```

相关声明：[emul](../hardware/P477_仿真器实例结构.md)。

仿真器实例（Emulator Instance），表示通过仿真总线交互的目标仿真设备或外设。

<a id="r_emul_3A_3Abus"></a>

```c
union emul::bus
```

相关声明：[emul::bus](../hardware/P485_仿真器总线联合体.md)。

指向仿真总线节点（Emulated Bus Node）的指针。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gac1638c8cad48dab50f9ebc83592236db"></a>

```c
#define EMUL_DT_NAME_GET(node_id)
```

相关声明：[EMUL_DT_NAME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gac1638c8cad48dab50f9ebc83592236db)。

使用设备树节点标识符（Devicetree Node Identifier）作为唯一名称。

<a id="r_gad6292e3cd7f17a3600be396777f304c8"></a>

```c
#define EMUL_DT_DEFINE(node_id, init_fn, data_ptr, cfg_ptr, bus_api, _backend_api)
```

相关声明：[EMUL_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8)。

定义新的仿真器（Emulator）。

<a id="r_gafe7f4912bcffed1366ce07d024a4f977"></a>

```c
#define EMUL_DT_INST_DEFINE(inst, ...)
```

相关声明：[EMUL_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gafe7f4912bcffed1366ce07d024a4f977)。

类似 `EMUL_DT_DEFINE()`，但使用兼容标识为 `DT_DRV_COMPAT` 的实例，代替节点标识符（Node Identifier）。

<a id="r_ga300d997df388118ae380e79b972f85cf"></a>

```c
#define EMUL_DT_GET(node_id)
```

相关声明：[EMUL_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga300d997df388118ae380e79b972f85cf)。

根据设备树节点标识符（Devicetree Node Identifier）获取 `const struct emul*`。

<a id="r_gab37b4f8b4c434ca38f523eb6391d4e3b"></a>

```c
#define EMUL_DT_GET_OR_NULL(node_id)
```

相关声明：[EMUL_DT_GET_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gab37b4f8b4c434ca38f523eb6391d4e3b)。

获取仿真器可选引用（Optional Reference）的辅助宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_gaa6129de6e0edef345242559a3dac3a50"></a>

```c
typedef int(* emul_init_t) (const struct emul *emul, const struct device *parent)
```

相关声明：[emul_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaa6129de6e0edef345242559a3dac3a50)、[emul](../hardware/P477_仿真器实例结构.md)、[emul](../hardware/P477_仿真器实例结构.md)、[device](../device_reference/P002_设备对象结构.md)。

仿真器初始化（Emulator Initialisation）的标准回调，提供初始化记录，以及调用仿真器函数的设备。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga39b7a9438507b0be95038fe9464762aa"></a>

```c
enum emul_bus_type { EMUL_BUS_TYPE_I2C , EMUL_BUS_TYPE_ESPI , EMUL_BUS_TYPE_SPI , EMUL_BUS_TYPE_MSPI , EMUL_BUS_TYPE_UART , EMUL_BUS_TYPE_NONE }
```

相关声明：[emul_bus_type](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga39b7a9438507b0be95038fe9464762aa)、[EMUL_BUS_TYPE_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)、[EMUL_BUS_TYPE_ESPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)、[EMUL_BUS_TYPE_SPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)、[EMUL_BUS_TYPE_MSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46)、[EMUL_BUS_TYPE_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6)、[EMUL_BUS_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)。

支持的总线类型（Bus Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gad587b2852a182e1a7fdcb3b056d898f1"></a>

```c
int emul_init_for_bus (const struct device *dev)
```

相关声明：[emul_init_for_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad587b2852a182e1a7fdcb3b056d898f1)、[device](../device_reference/P002_设备对象结构.md)。

设置仿真器列表（Emulator List）。

<a id="r_gaad94c1e07998417cb9aa06d03be3b280"></a>

```c
const struct emul * emul_get_binding (const char *name)
```

相关声明：[emul](../hardware/P477_仿真器实例结构.md)、[emul_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaad94c1e07998417cb9aa06d03be3b280)。

按名称取得仿真器的 `emul` 结构体。


## 6.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/drivers/espi_emul.h](../api_source_configuration_reference/P026_espi_emul.h_源码浏览.md)
- [zephyr/drivers/i2c_emul.h](../api_source_reference/P328_i2c_emul.h_源码浏览.md)
- [zephyr/drivers/spi_emul.h](../api_source_reference/P808_spi_emul.h_源码浏览.md)
- [zephyr/drivers/mspi_emul.h](../api_source_reference/P567_mspi_emul.h_源码浏览.md)
- [zephyr/drivers/uart_emul.h](../api_source_reference/P880_uart_emul.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [emul_link_for_bus](../hardware/P478_总线仿真器链接结构.md)
- [emul_list_for_bus](../hardware/P479_总线仿真器列表结构.md)
- [no_bus_emul](../hardware/P480_无总线仿真器桩结构.md)
- [emul](../hardware/P477_仿真器实例结构.md)
- [emul::bus](../hardware/P485_仿真器总线联合体.md)
- [EMUL_DT_NAME_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gac1638c8cad48dab50f9ebc83592236db)
- [EMUL_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad6292e3cd7f17a3600be396777f304c8)
- [EMUL_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gafe7f4912bcffed1366ce07d024a4f977)
- [EMUL_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga300d997df388118ae380e79b972f85cf)
- [EMUL_DT_GET_OR_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gab37b4f8b4c434ca38f523eb6391d4e3b)
- [emul_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaa6129de6e0edef345242559a3dac3a50)
- [device](../device_reference/P002_设备对象结构.md)
- [emul_bus_type](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#ga39b7a9438507b0be95038fe9464762aa)
- [EMUL_BUS_TYPE_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f)
- [EMUL_BUS_TYPE_ESPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1)
- [EMUL_BUS_TYPE_SPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a)
- [EMUL_BUS_TYPE_MSPI](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46)
- [EMUL_BUS_TYPE_UART](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6)
- [EMUL_BUS_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)
- [emul_init_for_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gad587b2852a182e1a7fdcb3b056d898f1)
- [emul_get_binding](https://docs.zephyrproject.org/latest/doxygen/html/group__io__emulators.html#gaad94c1e07998417cb9aa06d03be3b280)

<a id="header-details"></a>

---

[上一章](P005_zephyr__console__console.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__firmware__scmi__reset.h_文件参考.md)
