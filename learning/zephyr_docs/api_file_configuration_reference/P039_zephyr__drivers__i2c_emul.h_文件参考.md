---
id: learning.zephyr-docs.api-file-configuration-reference.page-39
title: zephyr__drivers__i2c_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_drivers\_\_i2c\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

I2C仿真驱动（Emulation Drivers）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

I2C仿真驱动（Emulation Drivers）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 39.1\_数据结构（Data Structures）

<a id="r_i2c_5Femul"></a>

```c
struct i2c_emul
```

相关声明：[i2c_emul](../hardware/P316_I2C模拟设备节点.md)。

I2C设备仿真器链表（Linked List）中的节点。

<a id="r_i2c_5Femul_5Fapi"></a>

```c
struct i2c_emul_api
```

相关声明：[i2c_emul_api](../hardware/P317_I2C模拟函数表.md)。

仿真器（Emulator）API的定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 39.2\_类型定义（Typedefs）

<a id="r_ga1b27ff11534eeac47cf50ffb2a1c7cca"></a>

```c
typedef int(* i2c_emul_transfer_t) (const struct emul *target, struct i2c_msg *msgs, int num_msgs, int addr)
```

相关声明：[i2c_emul_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga1b27ff11534eeac47cf50ffb2a1c7cca)、[emul](../hardware/P477_仿真器实例结构.md)、[i2c_msg](../hardware/P307_I2C消息结构.md)。

将 I2C 消息（Messages）传递给仿真器（Emulator）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.3\_函数（Functions）

<a id="r_ga92851f09c23531bbaea25301dc2607ce"></a>

```c
int i2c_emul_register (const struct device *dev, struct i2c_emul *emul)
```

相关声明：[i2c_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga92851f09c23531bbaea25301dc2607ce)、[device](../device_reference/P002_设备对象结构.md)、[i2c_emul](../hardware/P316_I2C模拟设备节点.md)、[emul](../hardware/P477_仿真器实例结构.md)。

在控制器（Controller）上注册仿真设备（Emulated Device）。


## 39.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P328_i2c_emul.h_源码浏览.md)
- [i2c_emul](../hardware/P316_I2C模拟设备节点.md)
- [i2c_emul_api](../hardware/P317_I2C模拟函数表.md)
- [i2c_emul_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga1b27ff11534eeac47cf50ffb2a1c7cca)
- [emul](../hardware/P477_仿真器实例结构.md)
- [i2c_msg](../hardware/P307_I2C消息结构.md)
- [i2c_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga92851f09c23531bbaea25301dc2607ce)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P038_zephyr__xen__hvm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__net__igmp.h_文件参考.md)
