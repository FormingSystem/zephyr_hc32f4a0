---
id: learning.zephyr-docs.api-file-signal-device-reference.page-6
title: zephyr__drivers__i3c__devicetree.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_i3c\_\_devicetree.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga917b45ec38e08d0c464cebe3372b682e"></a>

```c
#define I3C_DEVICE_ID_DT(node_id)
```

相关声明：[I3C_DEVICE_ID_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga917b45ec38e08d0c464cebe3372b682e)。

根据设备树（Devicetree）构造 `i3c_device_id` 的结构体初始化器（Initializer）。

<a id="r_gadc45c0fdd41c081a0c3767159aae0c57"></a>

```c
#define I3C_DEVICE_ID_DT_INST(inst)
```

相关声明：[I3C_DEVICE_ID_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gadc45c0fdd41c081a0c3767159aae0c57)。

根据设备树实例（Devicetree Instance）构造 `i3c_device_id` 的结构体初始化器（Initializer）。

<a id="r_ga1e695c97b85614a2b03090a591751618"></a>

```c
#define I3C_CONTROLLER_CONFIG_FLAGS_DT_INST(inst)
```

相关声明：[I3C_CONTROLLER_CONFIG_FLAGS_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga1e695c97b85614a2b03090a591751618)。

从设备树实例（Devicetree Instance）获取 I3C 驱动配置标志（Config Flags）。

<a id="r_ga07eca721a06080900d976474138346fc"></a>

```c
#define I3C_DEVICE_DESC_DT(node_id)
```

相关声明：[I3C_DEVICE_DESC_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga07eca721a06080900d976474138346fc)。

根据设备树（Devicetree）构造 `i3c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_gafb9b50f7d6e288d1722db5b4176742e9"></a>

```c
#define I3C_DEVICE_DESC_DT_INST(inst)
```

相关声明：[I3C_DEVICE_DESC_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gafb9b50f7d6e288d1722db5b4176742e9)。

根据设备树实例（Devicetree Instance）构造 `i3c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_gae5c3df5af3fe52476a506c4eff34ca1e"></a>

```c
#define I3C_DEVICE_DESC_DT_FILTERED(node_id)
```

相关声明：[I3C_DEVICE_DESC_DT_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gae5c3df5af3fe52476a506c4eff34ca1e)。

根据设备树（Devicetree）构造 `i3c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_ga88aac6c42bbcd2f3276b6686c6786363"></a>

```c
#define I3C_DEVICE_ARRAY_DT(node_id)
```

相关声明：[I3C_DEVICE_ARRAY_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga88aac6c42bbcd2f3276b6686c6786363)。

根据设备树（Devicetree）构造 `i3c_device_desc` 列表的数组初始化器（Array Initializer）。

<a id="r_ga3153fd2d2b68eb760730827f6d6986c5"></a>

```c
#define I3C_DEVICE_ARRAY_DT_INST(inst)
```

相关声明：[I3C_DEVICE_ARRAY_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga3153fd2d2b68eb760730827f6d6986c5)。

根据设备树实例（Devicetree Instance）构造 `i3c_device_desc` 列表的数组初始化器（Array Initializer）。

<a id="r_gaab3219d45b125dd12d583bfd1823a61c"></a>

```c
#define I3C_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, ...)
```

相关声明：[I3C_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gaab3219d45b125dd12d583bfd1823a61c)。

类似 `DEVICE_DT_DEFINE()`，但包含 I3C 目标设备（Target Device）专用处理。

<a id="r_ga77a471977d2c6edc530d3ce0febb8dbe"></a>

```c
#define I3C_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[I3C_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga77a471977d2c6edc530d3ce0febb8dbe)。

类似 `I3C_TARGET_DT_DEFINE()`，用于与 `DT_DRV_COMPAT` 兼容的实例（Instance）。

<a id="r_gaf317b1bcec787d594d3952dda2b9dc51"></a>

```c
#define I3C_I2C_DEVICE_DESC_DT(node_id)
```

相关声明：[I3C_I2C_DEVICE_DESC_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gaf317b1bcec787d594d3952dda2b9dc51)。

根据设备树（Devicetree）构造 `i3c_i2c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_ga4c004a38164a56a1d1d027f2d29974e4"></a>

```c
#define I3C_I2C_DEVICE_DESC_DT_INST(inst)
```

相关声明：[I3C_I2C_DEVICE_DESC_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga4c004a38164a56a1d1d027f2d29974e4)。

根据设备树实例（Devicetree Instance）构造 `i3c_i2c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_ga703052c71216a4f152028540592ad581"></a>

```c
#define I3C_I2C_DEVICE_DESC_DT_FILTERED(node_id)
```

相关声明：[I3C_I2C_DEVICE_DESC_DT_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga703052c71216a4f152028540592ad581)。

根据设备树（Devicetree）构造 `i3c_i2c_device_desc` 的结构体初始化器（Initializer）。

<a id="r_ga78f4d3fa3977989a731e33089d535701"></a>

```c
#define I3C_I2C_DEVICE_ARRAY_DT(node_id)
```

相关声明：[I3C_I2C_DEVICE_ARRAY_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga78f4d3fa3977989a731e33089d535701)。

根据设备树（Devicetree）构造 `i3c_i2c_device_desc` 列表的数组初始化器（Array Initializer）。

<a id="r_gab441564c36a5d7e0856bba5eed51906f"></a>

```c
#define I3C_I2C_DEVICE_ARRAY_DT_INST(inst)
```

相关声明：[I3C_I2C_DEVICE_ARRAY_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gab441564c36a5d7e0856bba5eed51906f)。

根据设备树实例（Devicetree Instance）构造 `i3c_i2c_device_desc` 列表的数组初始化器（Array Initializer）。

<a id="define-members-0"></a>

### I3C 设备标志（Device Flags）



<a id="r_ga24fbe85a8cb5ffc049288b1b82e1c15b"></a>

```c
#define I3C_SUPPORTS_SETAASA BIT(0)
```

相关声明：[I3C_SUPPORTS_SETAASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga24fbe85a8cb5ffc049288b1b82e1c15b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设备支持 `SETAASA` 公共命令代码（CCC）。

<a id="r_ga91bb0d3b4b86524d5f7a6a0429a123da"></a>

```c
#define I3C_V1P0_SUPPORT BIT(1)
```

相关声明：[I3C_V1P0_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga91bb0d3b4b86524d5f7a6a0429a123da)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设备支持 I3C v1.0。

<a id="define-members-1"></a>

### I3C 驱动配置标志（Driver Config Flags）



<a id="r_gad2ae95d27ea32b70e3d36a7b6d74e468"></a>

```c
#define I3C_CONTROLLER_FLAG_DISABLE_BUS_INIT BIT(0)
```

相关声明：[I3C_CONTROLLER_FLAG_DISABLE_BUS_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gad2ae95d27ea32b70e3d36a7b6d74e468)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在驱动初始化期间禁用 `i3c_bus_init`。

<a id="r_ga7f9635ee0f0b43869478477668259432"></a>

```c
#define I3C_CONTROLLER_FLAG_DISABLE_HJ_AT_INIT BIT(1)
```

相关声明：[I3C_CONTROLLER_FLAG_DISABLE_HJ_AT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga7f9635ee0f0b43869478477668259432)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在驱动初始化期间禁用热加入确认（Hot-Join ACK）。


## 6.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P157_devicetree.h_源码浏览.md)
- [I3C_DEVICE_ID_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga917b45ec38e08d0c464cebe3372b682e)
- [i3c_device_id](../hardware/P400_I3C设备匹配标识.md)
- [I3C_DEVICE_ID_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gadc45c0fdd41c081a0c3767159aae0c57)
- [I3C_CONTROLLER_CONFIG_FLAGS_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga1e695c97b85614a2b03090a591751618)
- [I3C_DEVICE_DESC_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga07eca721a06080900d976474138346fc)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [I3C_DEVICE_DESC_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gafb9b50f7d6e288d1722db5b4176742e9)
- [I3C_DEVICE_DESC_DT_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gae5c3df5af3fe52476a506c4eff34ca1e)
- [I3C_DEVICE_ARRAY_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga88aac6c42bbcd2f3276b6686c6786363)
- [I3C_DEVICE_ARRAY_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga3153fd2d2b68eb760730827f6d6986c5)
- [I3C_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gaab3219d45b125dd12d583bfd1823a61c)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [I3C_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga77a471977d2c6edc530d3ce0febb8dbe)
- [I3C_I2C_DEVICE_DESC_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gaf317b1bcec787d594d3952dda2b9dc51)
- [i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)
- [I3C_I2C_DEVICE_DESC_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga4c004a38164a56a1d1d027f2d29974e4)
- [I3C_I2C_DEVICE_DESC_DT_FILTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga703052c71216a4f152028540592ad581)
- [I3C_I2C_DEVICE_ARRAY_DT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga78f4d3fa3977989a731e33089d535701)
- [I3C_I2C_DEVICE_ARRAY_DT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gab441564c36a5d7e0856bba5eed51906f)
- [I3C_SUPPORTS_SETAASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga24fbe85a8cb5ffc049288b1b82e1c15b)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [I3C_V1P0_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga91bb0d3b4b86524d5f7a6a0429a123da)
- [I3C_CONTROLLER_FLAG_DISABLE_BUS_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#gad2ae95d27ea32b70e3d36a7b6d74e468)
- [I3C_CONTROLLER_FLAG_DISABLE_HJ_AT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__devicetree.html#ga7f9635ee0f0b43869478477668259432)

<a id="I3C_DEVICE_FLAGS"></a>
<a id="I3C_CONTROLLER_CONFIG_FLAGS"></a>

---

[上一章](P005_zephyr__display__cfb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__sensor__mcp9600.h_文件参考.md)
