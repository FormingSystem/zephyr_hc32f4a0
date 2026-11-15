---
id: learning.zephyr-docs.api-file-reference.page-495
title: zephyr__drivers__interrupt_controller__wch_exti.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wch__exti_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第495章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_wch\_exti.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wch__exti_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 495.1\_类型定义（Typedefs）

<a id="r_aa1c9d73d6337b6fd8dc95187f739b768"></a>

```c
typedef void(* wch_exti_callback_handler_t) (uint8_t line, void *user)
```

相关声明：[wch_exti_callback_handler_t](#aa1c9d73d6337b6fd8dc95187f739b768)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 495.2\_枚举（Enumerations）

<a id="r_ab41aa3ea720735eb77fc4aaa59659db1"></a>

```c
enum wch_exti_trigger { WCH_EXTI_TRIGGER_RISING_EDGE = BIT(0) , WCH_EXTI_TRIGGER_FALLING_EDGE = BIT(1) }
```

相关声明：[wch_exti_trigger](#ab41aa3ea720735eb77fc4aaa59659db1)、[WCH_EXTI_TRIGGER_RISING_EDGE](#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28)、[WCH_EXTI_TRIGGER_FALLING_EDGE](#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 495.3\_函数（Functions）

<a id="r_a36723b918e6ddb225e05c041a6127369"></a>

```c
void wch_exti_enable (uint8_t line)
```

相关声明：[wch_exti_enable](#a36723b918e6ddb225e05c041a6127369)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a2b90b358d0ee8445e1257c636cfbd931"></a>

```c
void wch_exti_disable (uint8_t line)
```

相关声明：[wch_exti_disable](#a2b90b358d0ee8445e1257c636cfbd931)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_aa7c5d9dff440158faad0c33da28f8777"></a>

```c
void wch_exti_set_trigger (uint8_t line, enum wch_exti_trigger trigger)
```

相关声明：[wch_exti_set_trigger](#aa7c5d9dff440158faad0c33da28f8777)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wch_exti_trigger](#ab41aa3ea720735eb77fc4aaa59659db1)。

<a id="r_a7ff8c5c40b36a6974c535e54fbff311f"></a>

```c
int wch_exti_configure (uint8_t line, wch_exti_callback_handler_t callback, void *user)
```

相关声明：[wch_exti_configure](#a7ff8c5c40b36a6974c535e54fbff311f)、[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wch_exti_callback_handler_t](#aa1c9d73d6337b6fd8dc95187f739b768)。

## 495.4\_详细说明（Detailed Documentation）

<a id="aa1c9d73d6337b6fd8dc95187f739b768"></a>

### `wch_exti_callback_handler_t`

```c
typedef void(* wch_exti_callback_handler_t) (uint8_t line, void *user)
```

<a id="ab41aa3ea720735eb77fc4aaa59659db1"></a>

### `wch_exti_trigger`

```c
enum wch_exti_trigger
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WCH_EXTI_TRIGGER_RISING_EDGE` |  |
| `WCH_EXTI_TRIGGER_FALLING_EDGE` |  |

<a id="a7ff8c5c40b36a6974c535e54fbff311f"></a>

### `wch_exti_configure()`

```c
int wch_exti_configure ( uint8_t line, wch_exti_callback_handler_t callback, void * user )
```

<a id="a2b90b358d0ee8445e1257c636cfbd931"></a>

### `wch_exti_disable()`

```c
void wch_exti_disable ( uint8_t line)
```

<a id="a36723b918e6ddb225e05c041a6127369"></a>

### `wch_exti_enable()`

```c
void wch_exti_enable ( uint8_t line)
```

<a id="aa7c5d9dff440158faad0c33da28f8777"></a>

### `wch_exti_set_trigger()`

```c
void wch_exti_set_trigger ( uint8_t line, enum wch_exti_trigger trigger )
```


## 495.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/wch__exti_8h_source.html)
- [uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28"></a>
<a id="ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P494_zephyr__net__virtual_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P496_zephyr__dt-bindings__led__worldsemi_ws2812c.h_文件参考.md)
