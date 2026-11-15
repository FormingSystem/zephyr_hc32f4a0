---
id: learning.zephyr-docs.api-file-supplement-reference.page-41
title: zephyr__drivers__bluetooth__h4.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/h4_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_drivers\_\_bluetooth\_\_h4.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/h4_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

查看此文件的源码。

蓝牙H:4 UART驱动的厂商扩展接口（Vendor Extension Interface）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 41.1\_函数（Functions）

<a id="r_ga4ac11c5a18b0891a04bb791e2f7c15bd"></a>

```c
int bt_h4_vnd_open (const struct device *dev, const struct device *uart, struct bt_hci_lockstep *ls)
```

相关声明：[bt_h4_vnd_open](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html#ga4ac11c5a18b0891a04bb791e2f7c15bd)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

在 H:4 传输通道（H:4 Transport）打开期间配置控制器（Controller）。


## 41.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/bluetooth/hci_lockstep.h](../api_source_reference/P309_hci_lockstep.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P305_h4.h_源码浏览.md)
- [bt_h4_vnd_open](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html#ga4ac11c5a18b0891a04bb791e2f7c15bd)
- [device](../device_reference/P002_设备对象结构.md)
- [bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)

<a id="header-details"></a>

---

[上一章](P040_zephyr__drivers__gpio__gpio_pcal64xxa.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__drivers__bluetooth__hci_driver_bluenrg.h_文件参考.md)
