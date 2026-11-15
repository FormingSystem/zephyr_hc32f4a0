---
id: learning.zephyr-docs.api-file-interface-reference.page-43
title: zephyr__drivers__pinctrl__pinctrl_rp1_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_drivers\_\_pinctrl\_\_pinctrl\_rp1\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rp1__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RP1引脚控制（Pinctrl）驱动的通用定义。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/dt-bindings/pinctrl/rp1-pinctrl.h>
```

查看此文件的源码。

RP1引脚控制（Pinctrl）驱动的通用定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 43.1\_宏定义（Macros）

<a id="r_a82b13f075f77ce615660a46386be0532"></a>

```c
#define RP1_GET_PIN_NUM(pinctrl)
```

相关声明：[RP1_GET_PIN_NUM](#a82b13f075f77ce615660a46386be0532)。

从已编码的 RP1 引脚复用（pinmux）值中提取 GPIO 编号。

<a id="r_ac75fec02141d7c4db21e7095f1892b0f"></a>

```c
#define RP1_GET_ALT_FUNC(pinctrl)
```

相关声明：[RP1_GET_ALT_FUNC](#ac75fec02141d7c4db21e7095f1892b0f)。

从已编码的 RP1 引脚复用值中提取复用功能选择值（alternate function selector）。

## 43.2\_详细说明（Detailed Documentation）

<a id="ac75fec02141d7c4db21e7095f1892b0f"></a>

### `RP1_GET_ALT_FUNC`

```c
#define RP1_GET_ALT_FUNC ( pinctrl)
```

展开值（Value）：

```c
(((pinctrl) >> RP1_ALT_FUNC_POS) & RP1_ALT_FUNC_MASK)
```

从已编码的 RP1 引脚复用值中提取复用功能选择值（alternate function selector）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pinctrl` | 设备树（devicetree）中定义的引脚配置值。 |

**返回（Returns）**：返回值：GPIO 复用功能编号（alternate function number）。

<a id="a82b13f075f77ce615660a46386be0532"></a>

### `RP1_GET_PIN_NUM`

```c
#define RP1_GET_PIN_NUM ( pinctrl)
```

展开值（Value）：

```c
(((pinctrl) >> RP1_PIN_NUM_POS) & RP1_PIN_NUM_MASK)
```

从已编码的 RP1 引脚复用（pinmux）值中提取 GPIO 编号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pinctrl` | 设备树（devicetree）中定义的引脚配置值。 |

**返回（Returns）**：返回值：GPIO 编号。


## 43.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/dt-bindings/pinctrl/rp1-pinctrl.h](../api_source_supplement_reference/P165_rp1-pinctrl.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P049_pinctrl_rp1_common.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P042_zephyr__dt-bindings__gpio__pca-series-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__drivers__firmware__qemu_fwcfg__qemu_fwcfg.h_文件参考.md)
