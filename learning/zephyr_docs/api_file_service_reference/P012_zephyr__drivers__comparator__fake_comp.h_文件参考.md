---
id: learning.zephyr-docs.api-file-service-reference.page-12
title: zephyr__drivers__comparator__fake_comp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_comparator\_\_fake\_comp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟比较器（Fake Comparator）驱动的API函数。

<a id="details"></a>

```c
#include <zephyr/drivers/comparator.h>
#include <zephyr/fff.h>
```

查看此文件的源码。

模拟比较器（Fake Comparator）驱动的API函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.1\_函数（Functions）

<a id="r_ga013745edeee1a931088f6f9e336e92a6"></a>

```c
int comp_fake_comp_get_output (const struct device *)
```

相关声明：[comp_fake_comp_get_output](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga013745edeee1a931088f6f9e336e92a6)、[device](../device_reference/P002_设备对象结构.md)。

`comparator_driver_api::get_output` 驱动操作的伪实现（Fake Implementation）。

<a id="r_ga59ca6b865fe755dfdfc632ede9710f2e"></a>

```c
int comp_fake_comp_set_trigger (const struct device *, enum comparator_trigger)
```

相关声明：[comp_fake_comp_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga59ca6b865fe755dfdfc632ede9710f2e)、[device](../device_reference/P002_设备对象结构.md)、[comparator_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#gab02743771baf02ee0105aa1303931674)。

`comparator_driver_api::set_trigger` 驱动操作的伪实现（Fake Implementation）。

<a id="r_ga0e6a3ea88289165a28f9b3abd051f281"></a>

```c
int comp_fake_comp_set_trigger_callback (const struct device *, comparator_callback_t, void *)
```

相关声明：[comp_fake_comp_set_trigger_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga0e6a3ea88289165a28f9b3abd051f281)、[device](../device_reference/P002_设备对象结构.md)、[comparator_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#ga409308b8ba2efdca4a6ec4bdc4d3bc31)。

`comparator_driver_api::set_trigger_callback` 驱动操作的伪实现（Fake Implementation）。

<a id="r_ga3cdbc9e3140c8e3b92fa328bd0917787"></a>

```c
int comp_fake_comp_trigger_is_pending (const struct device *)
```

相关声明：[comp_fake_comp_trigger_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga3cdbc9e3140c8e3b92fa328bd0917787)、[device](../device_reference/P002_设备对象结构.md)。

`comparator_driver_api::trigger_is_pending` 驱动操作的伪实现（Fake Implementation）。


## 12.2\_原页交叉引用（Cross References）

- [zephyr/drivers/comparator.h](../analog_reference/P002_比较器公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P254_fake_comp.h_源码浏览.md)
- [comp_fake_comp_get_output](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga013745edeee1a931088f6f9e336e92a6)
- [device](../device_reference/P002_设备对象结构.md)
- [comparator_driver_api::get_output](https://docs.zephyrproject.org/latest/doxygen/html/structcomparator__driver__api.html#ae77115fe6af249dd44672cfd75c22ccd)
- [comp_fake_comp_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga59ca6b865fe755dfdfc632ede9710f2e)
- [comparator_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#gab02743771baf02ee0105aa1303931674)
- [comparator_driver_api::set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/structcomparator__driver__api.html#ab97de2135a45220ec48ac3cfc5681e59)
- [comp_fake_comp_set_trigger_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga0e6a3ea88289165a28f9b3abd051f281)
- [comparator_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#ga409308b8ba2efdca4a6ec4bdc4d3bc31)
- [comparator_driver_api::set_trigger_callback](https://docs.zephyrproject.org/latest/doxygen/html/structcomparator__driver__api.html#a497475c2d68b9f56cad3f7132b50ebb8)
- [comp_fake_comp_trigger_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga3cdbc9e3140c8e3b92fa328bd0917787)
- [comparator_driver_api::trigger_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/structcomparator__driver__api.html#a6a2361913f1891cfe9f82688eb48f504)

<a id="header-details"></a>

---

[上一章](P011_zephyr__net__ethernet_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__authentication__fido2__fido2_attestation.h_文件参考.md)
