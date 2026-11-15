---
id: learning.zephyr-docs.api-file-service-reference.page-21
title: zephyr__drivers__mfd__mfd_maxq10xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_mfd\_\_mfd\_maxq10xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.1\_函数（Functions）

<a id="r_afab2fb34feb7d84e42caea6021dd1ed9"></a>

```c
struct k_sem * mfd_maxq10xx_get_lock (const struct device *dev)
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[mfd_maxq10xx_get_lock](#afab2fb34feb7d84e42caea6021dd1ed9)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAXQ1xx 实例（Instance）的信号量引用（Semaphore Reference）。

## 21.2\_详细说明（Detailed Documentation）

<a id="afab2fb34feb7d84e42caea6021dd1ed9"></a>

### `mfd_maxq10xx_get_lock()`

```c
struct k_sem * mfd_maxq10xx_get_lock ( const struct device * dev)
```

获取 MAXQ1xx 实例（Instance）的信号量引用（Semaphore Reference）。

调用者应将返回值传递给 `k_sem_take`／`k_sem_give`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例设备结构体（Device Struct of the Driver Instance）的指针（Pointer）。 |

返回（Returns）：信号量地址（Semaphore Address）。


## 21.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P519_mfd_maxq10xx.h_源码浏览.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_zephyr__drivers__clock_control__mchp_sam_pmc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__mgmt__mcumgr__mgmt__mgmt_defines.h_文件参考.md)
