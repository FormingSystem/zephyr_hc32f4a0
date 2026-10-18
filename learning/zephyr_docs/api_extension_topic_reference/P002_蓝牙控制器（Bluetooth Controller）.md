---
id: learning.zephyr-docs.api-extension-topic-reference.page-2
title: 蓝牙控制器（Bluetooth Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙控制器（Bluetooth Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙控制器（Bluetooth Controller）

<a id="details"></a>

蓝牙控制器（Bluetooth Controller）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.1\_函数（Functions）

<a id="r_ga541cabe76fd3cb019aae2fe01d45cbfc"></a>

```c
void bt_ctlr_set_public_addr (const uint8_t *addr)
```

相关声明：[bt_ctlr_set_public_addr](#ga541cabe76fd3cb019aae2fe01d45cbfc)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置控制器的公共地址（Public Address）。

## 2.2\_详细说明（Detailed Documentation）

<a id="ga541cabe76fd3cb019aae2fe01d45cbfc"></a>

### `bt_ctlr_set_public_addr()`

```c
void bt_ctlr_set_public_addr ( const uint8_t * addr)
```

```c
#include <zephyr/bluetooth/controller.h>
```

设置控制器的公共地址（Public Address）。

应在 `bt_enable()` 之前调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 公共地址（Public Address）。 |


## 2.3\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/controller.h](../api_file_supplement_reference/P010_zephyr__bluetooth__controller.h_文件参考.md)
- [bt_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_BlueNRG HCI 驱动扩展 API.md) · [返回大纲](大纲.md) · [下一章](P003_桥接配置公共头文件（Bridge Configuration common header）.md)
