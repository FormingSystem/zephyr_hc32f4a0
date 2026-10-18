---
id: learning.zephyr-docs.api-file-network-device-reference.page-2
title: zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bee-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_bee-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bee-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek BEE的引脚控制设备树绑定（Pinctrl Devicetree Bindings）。

查看此文件的源码。

<a id="details"></a>

Realtek BEE的引脚控制设备树绑定（Pinctrl Devicetree Bindings）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_a8b720ca7a90363e78b5877e54b6d6ee2"></a>

```c
#define BEE_FUN_POS 16U
```

相关声明：[BEE_FUN_POS](#a8b720ca7a90363e78b5877e54b6d6ee2)。

功能字段（Function Field）的位位置。

<a id="r_a9d372c7fc8db9959b25c94d1003066e0"></a>

```c
#define BEE_FUN_MSK 0xFFFFU
```

相关声明：[BEE_FUN_MSK](#a9d372c7fc8db9959b25c94d1003066e0)。

功能字段（Function Field）的掩码。

<a id="r_a727529af955388138d528ed3bb79ab62"></a>

```c
#define BEE_PIN_POS 0U
```

相关声明：[BEE_PIN_POS](#a727529af955388138d528ed3bb79ab62)。

引脚字段（Pin Field）的位位置。

<a id="r_a8514aca71581788b4e134f74d81bcd45"></a>

```c
#define BEE_PIN_MSK 0x7FFU
```

相关声明：[BEE_PIN_MSK](#a8514aca71581788b4e134f74d81bcd45)。

引脚字段（Pin Field）的掩码。

<a id="r_a162b03456c93d6efa3bfaa0a6a996e15"></a>

```c
#define BEE_PSEL(fun, pin)
```

相关声明：[BEE_PSEL](#a162b03456c93d6efa3bfaa0a6a996e15)。

构造引脚控制（Pinctrl）配置字段的辅助宏。

<a id="r_a8f41b2c504605d3605c4e57957255168"></a>

```c
#define BEE_PSEL_DISCONNECTED(fun)
```

相关声明：[BEE_PSEL_DISCONNECTED](#a8f41b2c504605d3605c4e57957255168)。

配置没有物理引脚连接的功能的辅助宏。

## 2.2\_详细说明（Detailed Documentation）

<a id="a9d372c7fc8db9959b25c94d1003066e0"></a>

### `BEE_FUN_MSK`

```c
#define BEE_FUN_MSK 0xFFFFU
```

功能字段（Function Field）的掩码。

<a id="a8b720ca7a90363e78b5877e54b6d6ee2"></a>

### `BEE_FUN_POS`

```c
#define BEE_FUN_POS 16U
```

功能字段（Function Field）的位位置。

<a id="a8514aca71581788b4e134f74d81bcd45"></a>

### `BEE_PIN_MSK`

```c
#define BEE_PIN_MSK 0x7FFU
```

引脚字段（Pin Field）的掩码。

<a id="a727529af955388138d528ed3bb79ab62"></a>

### `BEE_PIN_POS`

```c
#define BEE_PIN_POS 0U
```

引脚字段（Pin Field）的位位置。

<a id="a162b03456c93d6efa3bfaa0a6a996e15"></a>

### `BEE_PSEL`

```c
#define BEE_PSEL ( fun, pin )
```

展开值（Value）：

```c
(((((pin) & BEE_PIN_MSK) << BEE_PIN_POS) | (((BEE_##fun) & BEE_FUN_MSK) << BEE_FUN_POS)))
```

构造引脚控制（Pinctrl）配置字段的辅助宏。

本宏生成引脚控制驱动（Pinctrl Driver）配置特定引脚功能所需的编码值（Encoded Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能名称，不带 `BEE_` 前缀；宏会自动为此参数添加 `BEE_`。 |
| `pin` | 焊盘编号／标识（Pad Number/ID）。 |

<a id="a8f41b2c504605d3605c4e57957255168"></a>

### `BEE_PSEL_DISCONNECTED`

```c
#define BEE_PSEL_DISCONNECTED ( fun)
```

展开值（Value）：

```c
(BEE_PIN_DISCONNECTED << BEE_PIN_POS | ((BEE_##fun & BEE_FUN_MSK) << BEE_FUN_POS))
```

配置没有物理引脚连接的功能的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能名称，不带 `BEE_` 前缀；宏会自动为此参数添加 `BEE_`。 |


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P057_bee-pinctrl.h_源码浏览.md)
- [BEE_PIN_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h.html#a52116a87b4f4fd7ce6beeffbb44030da)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="abee-pinctrl_8h_html_a727529af955388138d528ed3bb79ab62"></a>
<a id="abee-pinctrl_8h_html_a8514aca71581788b4e134f74d81bcd45"></a>
<a id="abee-pinctrl_8h_html_a8b720ca7a90363e78b5877e54b6d6ee2"></a>
<a id="abee-pinctrl_8h_html_a9d372c7fc8db9959b25c94d1003066e0"></a>
<a id="artl8752h-pinctrl_8h_html_a52116a87b4f4fd7ce6beeffbb44030da"></a>

---

[上一章](P001_zephyr__drivers__bbram.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__buzzer.h_文件参考.md)
