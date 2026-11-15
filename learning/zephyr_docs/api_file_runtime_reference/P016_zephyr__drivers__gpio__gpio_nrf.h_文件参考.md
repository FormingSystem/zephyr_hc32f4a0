---
id: learning.zephyr-docs.api-file-runtime-reference.page-16
title: zephyr__drivers__gpio__gpio_nrf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__nrf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_nrf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__nrf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.1\_函数（Functions）

<a id="r_a7828ba431fda134181dd5366b2f9a292"></a>

```c
void * gpio_nrf_gpiote_by_port_get (const struct device *port)
```

相关声明：[gpio_nrf_gpiote_by_port_get](#a7828ba431fda134181dd5366b2f9a292)、[device](../device_reference/P002_设备对象结构.md)。

获取与指定端口设备节点（Port Device Node）关联的 GPIO 任务和事件驱动实例（GPIOTE Driver Instance）的指针（Pointer）。

## 16.2\_详细说明（Detailed Documentation）

<a id="a7828ba431fda134181dd5366b2f9a292"></a>

### `gpio_nrf_gpiote_by_port_get()`

```c
void * gpio_nrf_gpiote_by_port_get ( const struct device * port)
```

获取与指定端口设备节点（Port Device Node）关联的 GPIO 任务和事件驱动实例（GPIOTE Driver Instance）的指针（Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 指向端口设备节点（Port Device Node）的指针（Pointer）。 |

返回（Returns）：指向 GPIOTE 驱动实例（Driver Instance）的指针；若未找到则返回 `NULL`。


## 16.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P300_gpio_nrf.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_zephyr__authentication__fido2__fido2_up.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__bluetooth__hci_vs.h_文件参考.md)
