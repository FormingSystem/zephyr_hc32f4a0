---
id: learning.zephyr-docs.api-file-system-device-reference.page-6
title: zephyr__dt-bindings__input__cst8xx-gesture-codes.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_input\_\_cst8xx-gesture-codes.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Hynitron CST8xx触摸控制器（Touch Controllers）的手势代码定义。

查看此文件的源码。

<a id="details"></a>

Hynitron CST8xx触摸控制器（Touch Controllers）的手势代码定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_a97c3d7f42ee5f69e3979d751f4478198"></a>

```c
#define CST8XX_GESTURE_CODE_NONE 0x00
```

相关声明：[CST8XX_GESTURE_CODE_NONE](#a97c3d7f42ee5f69e3979d751f4478198)。

未检测到手势（gesture）。

<a id="r_adc31529e046cc1536ba14786d42a4843"></a>

```c
#define CST8XX_GESTURE_CODE_SWIPE_UP 0x01
```

相关声明：[CST8XX_GESTURE_CODE_SWIPE_UP](#adc31529e046cc1536ba14786d42a4843)。

向上滑动手势（swipe up gesture）。

<a id="r_a559b43b4cd2e793779446cad77ac2d19"></a>

```c
#define CST8XX_GESTURE_CODE_SWIPE_DOWN 0x02
```

相关声明：[CST8XX_GESTURE_CODE_SWIPE_DOWN](#a559b43b4cd2e793779446cad77ac2d19)。

向下滑动手势（swipe down gesture）。

<a id="r_a3db7829dd05361620aa6d9a6fb1147c6"></a>

```c
#define CST8XX_GESTURE_CODE_SWIPE_LEFT 0x03
```

相关声明：[CST8XX_GESTURE_CODE_SWIPE_LEFT](#a3db7829dd05361620aa6d9a6fb1147c6)。

向左滑动手势（swipe left gesture）。

<a id="r_ab10893a78840ce21b0636942382885af"></a>

```c
#define CST8XX_GESTURE_CODE_SWIPE_RIGHT 0x04
```

相关声明：[CST8XX_GESTURE_CODE_SWIPE_RIGHT](#ab10893a78840ce21b0636942382885af)。

向右滑动手势（swipe right gesture）。

<a id="r_a334290d60f9374ef0378bee457472b09"></a>

```c
#define CST8XX_GESTURE_CODE_SINGLE_CLICK 0x05
```

相关声明：[CST8XX_GESTURE_CODE_SINGLE_CLICK](#a334290d60f9374ef0378bee457472b09)。

单击手势（single tap/click gesture）。

<a id="r_ab24768c9b76cd1b7adcd0bacd3f2351e"></a>

```c
#define CST8XX_GESTURE_CODE_DOUBLE_CLICK 0x0B
```

相关声明：[CST8XX_GESTURE_CODE_DOUBLE_CLICK](#ab24768c9b76cd1b7adcd0bacd3f2351e)。

双击手势（double tap/click gesture）。

<a id="r_a47eb66fa52768f5dd53e8a01834c63f9"></a>

```c
#define CST8XX_GESTURE_CODE_LONG_PRESS 0x0C
```

相关声明：[CST8XX_GESTURE_CODE_LONG_PRESS](#a47eb66fa52768f5dd53e8a01834c63f9)。

长按手势（long press gesture）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ab24768c9b76cd1b7adcd0bacd3f2351e"></a>

### `CST8XX_GESTURE_CODE_DOUBLE_CLICK`

```c
#define CST8XX_GESTURE_CODE_DOUBLE_CLICK 0x0B
```

双击手势（double tap/click gesture）。

<a id="a47eb66fa52768f5dd53e8a01834c63f9"></a>

### `CST8XX_GESTURE_CODE_LONG_PRESS`

```c
#define CST8XX_GESTURE_CODE_LONG_PRESS 0x0C
```

长按手势（long press gesture）。

<a id="a97c3d7f42ee5f69e3979d751f4478198"></a>

### `CST8XX_GESTURE_CODE_NONE`

```c
#define CST8XX_GESTURE_CODE_NONE 0x00
```

未检测到手势（gesture）。

<a id="a334290d60f9374ef0378bee457472b09"></a>

### `CST8XX_GESTURE_CODE_SINGLE_CLICK`

```c
#define CST8XX_GESTURE_CODE_SINGLE_CLICK 0x05
```

单击手势（single tap/click gesture）。

<a id="a559b43b4cd2e793779446cad77ac2d19"></a>

### `CST8XX_GESTURE_CODE_SWIPE_DOWN`

```c
#define CST8XX_GESTURE_CODE_SWIPE_DOWN 0x02
```

向下滑动手势（swipe down gesture）。

<a id="a3db7829dd05361620aa6d9a6fb1147c6"></a>

### `CST8XX_GESTURE_CODE_SWIPE_LEFT`

```c
#define CST8XX_GESTURE_CODE_SWIPE_LEFT 0x03
```

向左滑动手势（swipe left gesture）。

<a id="ab10893a78840ce21b0636942382885af"></a>

### `CST8XX_GESTURE_CODE_SWIPE_RIGHT`

```c
#define CST8XX_GESTURE_CODE_SWIPE_RIGHT 0x04
```

向右滑动手势（swipe right gesture）。

<a id="adc31529e046cc1536ba14786d42a4843"></a>

### `CST8XX_GESTURE_CODE_SWIPE_UP`

```c
#define CST8XX_GESTURE_CODE_SWIPE_UP 0x01
```

向上滑动手势（swipe up gesture）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P119_cst8xx-gesture-codes.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__drivers__clock_control__clock_control_bflb_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__storage__disk_access.h_文件参考.md)
