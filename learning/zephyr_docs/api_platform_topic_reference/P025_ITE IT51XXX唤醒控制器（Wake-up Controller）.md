---
id: learning.zephyr-docs.api-platform-topic-reference.page-25
title: ITE IT51XXX唤醒控制器（Wake-up Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__wuc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_ITE IT51XXX唤醒控制器（Wake-up Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ite__it51xxx__wuc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT51XXX 唤醒控制器（Wake-Up Controller，WUC）的设备树宏。

<a id="details"></a>

ITE IT51XXX 唤醒控制器（Wake-Up Controller，WUC）的设备树宏（Devicetree Macros）。这些宏用于描述与 `ite,it51xxx-wuc` 和 `ite,it51xxx-wuc-map` 兼容控制器配合使用的唤醒控制器单元（Cells）。WUC 映射引用 WUC 组节点（Group Node）及该组内唤醒输入（Wake-Up Input）的位掩码（Bit Mask）；当某组没有关联的边沿触发寄存器（Edge-Trigger Register）时，使用 `IT51XXX_WUC_UNUSED_REG`。

```c
wuc_wu20: wu20 {
        wucs = <&wuc2 BIT(0)>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_ite-it51xxx-wuc_2Eh"></a>

```c
file ite-it51xxx-wuc.h
```

相关声明：[ite-it51xxx-wuc.h](../api_file_supplement_reference/P054_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-wuc.h_文件参考.md)。

ITE IT51XXX唤醒控制器（Wake-Up Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.2\_宏定义（Macros）

<a id="r_gae091c41a259c10a5ad0a45f3eba551eb"></a>

```c
#define IT51XXX_WUC_UNUSED_REG 0
```

相关声明：[IT51XXX_WUC_UNUSED_REG](#gae091c41a259c10a5ad0a45f3eba551eb)。

`reg` 属性中的唤醒控制器保留寄存器（WUC Reserved Register）。

## 25.3\_详细说明（Detailed Documentation）

<a id="gae091c41a259c10a5ad0a45f3eba551eb"></a>

### `IT51XXX_WUC_UNUSED_REG`

```c
#define IT51XXX_WUC_UNUSED_REG 0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/ite-it51xxx-wuc.h>
```

`reg` 属性中的唤醒控制器保留寄存器（WUC Reserved Register）。


## 25.4\_原页交叉引用（Cross References）

- [ite-it51xxx-wuc.h](../api_file_supplement_reference/P054_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-wuc.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P024_Espressif ESP32-S3 中断分配器（Interrupt allocator）.md) · [返回大纲](大纲.md) · [下一章](P026_ITE IT8XXX2唤醒控制器（Wake-up Controller）.md)
