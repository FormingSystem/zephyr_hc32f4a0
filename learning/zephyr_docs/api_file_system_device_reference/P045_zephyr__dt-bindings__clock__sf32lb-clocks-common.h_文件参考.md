---
id: learning.zephyr-docs.api-file-system-device-reference.page-45
title: zephyr__dt-bindings__clock__sf32lb-clocks-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_dt-bindings\_\_clock\_\_sf32lb-clocks-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 45.1\_宏定义（Macros）

<a id="r_ac43af3a4a22fac987df9725e4844a4b3"></a>

```c
#define SF32LB_CLOCK_CONFIG(offset, bit)
```

相关声明：[SF32LB_CLOCK_CONFIG](#ac43af3a4a22fac987df9725e4844a4b3)。

编码复位与时钟控制（RCC）寄存器偏移量和配置位。

## 45.2\_详细说明（Detailed Documentation）

<a id="ac43af3a4a22fac987df9725e4844a4b3"></a>

### `SF32LB_CLOCK_CONFIG`

```c
#define SF32LB_CLOCK_CONFIG ( offset, bit )
```

展开值（Value）：

```c
((((offset) << SF32LB_CLOCK_OFFSET_POS) & SF32LB_CLOCK_OFFSET_MSK) | \
 (((bit) << SF32LB_CLOCK_BIT_POS) & SF32LB_CLOCK_BIT_MSK))
```

编码复位与时钟控制（RCC）寄存器偏移量和配置位。

位图（Bitmap）：

- 位 0–7：偏移量（offset）。
- 位 8–12：位编号（bit number）。
- 位 13–15：保留（reserved）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `offset` | RCC 寄存器相对于 ENRx 寄存器的偏移量。 |
| `bit` | 配置位（configuration bit）。 |


## 45.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P773_sf32lb-clocks-common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P044_zephyr__dt-bindings__sensor__sensor_axis_align.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_zephyr__mgmt__mcumgr__transport__smp_bt.h_文件参考.md)
