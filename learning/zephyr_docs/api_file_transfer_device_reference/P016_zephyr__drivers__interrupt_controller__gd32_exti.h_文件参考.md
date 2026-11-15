---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-16
title: zephyr__drivers__interrupt_controller__gd32_exti.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32__exti_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_gd32\_exti.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32__exti_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 外部中断触发模式（EXTI Trigger Modes）



<a id="r_aa2b7ef2f0b43317c7c58fe4d53e07a19"></a>

```c
#define GD32_EXTI_TRIG_NONE 0U
```

相关声明：[GD32_EXTI_TRIG_NONE](#aa2b7ef2f0b43317c7c58fe4d53e07a19)。

不触发（No Trigger）。

<a id="r_a8d9e9cd3451d66f8d6df889ea8d50a3c"></a>

```c
#define GD32_EXTI_TRIG_RISING BIT(0)
```

相关声明：[GD32_EXTI_TRIG_RISING](#a8d9e9cd3451d66f8d6df889ea8d50a3c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

上升沿触发（Trigger on Rising Edge）。

<a id="r_aab892d582f9f266f7d942d238786e306"></a>

```c
#define GD32_EXTI_TRIG_FALLING BIT(1)
```

相关声明：[GD32_EXTI_TRIG_FALLING](#aab892d582f9f266f7d942d238786e306)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

下降沿触发（Trigger on Falling Edge）。

<a id="r_a6e09a28174e0c4b9ec7a79e89199f7e4"></a>

```c
#define GD32_EXTI_TRIG_BOTH (GD32_EXTI_TRIG_RISING | GD32_EXTI_TRIG_FALLING)
```

相关声明：[GD32_EXTI_TRIG_BOTH](#a6e09a28174e0c4b9ec7a79e89199f7e4)、[GD32_EXTI_TRIG_RISING](#a8d9e9cd3451d66f8d6df889ea8d50a3c)、[GD32_EXTI_TRIG_FALLING](#aab892d582f9f266f7d942d238786e306)。

在上升沿和下降沿（Rising and Falling Edge）均触发。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.2\_类型定义（Typedefs）

<a id="r_aac1a418b49c19fcf6e0dff2c0a3b7f75"></a>

```c
typedef void(* gd32_exti_cb_t) (uint8_t line, void *user)
```

相关声明：[gd32_exti_cb_t](#aac1a418b49c19fcf6e0dff2c0a3b7f75)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

外部中断（EXTI）的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.3\_函数（Functions）

<a id="r_ad63c2b15a0f2e0f703255b00b9368232"></a>

```c
void gd32_exti_enable (uint8_t line)
```

相关声明：[gd32_exti_enable](#ad63c2b15a0f2e0f703255b00b9368232)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用给定线路（Line）的外部中断（EXTI）。

<a id="r_a3f0333dce2621c7fed721e37a2413d80"></a>

```c
void gd32_exti_disable (uint8_t line)
```

相关声明：[gd32_exti_disable](#a3f0333dce2621c7fed721e37a2413d80)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用给定线路（Line）的外部中断（EXTI）。

<a id="r_ac543badc8874861f866b3bf3eba37e9a"></a>

```c
void gd32_exti_trigger (uint8_t line, uint8_t trigger)
```

相关声明：[gd32_exti_trigger](#ac543badc8874861f866b3bf3eba37e9a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置给定线路（Line）的外部中断（EXTI）触发模式（Trigger Mode）。

<a id="r_a014fba07d150faa8270493bb8257b31b"></a>

```c
int gd32_exti_configure (uint8_t line, gd32_exti_cb_t cb, void *user)
```

相关声明：[gd32_exti_configure](#a014fba07d150faa8270493bb8257b31b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[gd32_exti_cb_t](#aac1a418b49c19fcf6e0dff2c0a3b7f75)。

配置外部中断（EXTI）回调（Callback）。

## 16.4\_详细说明（Detailed Documentation）

<a id="a6e09a28174e0c4b9ec7a79e89199f7e4"></a>

### `GD32_EXTI_TRIG_BOTH`

```c
#define GD32_EXTI_TRIG_BOTH (GD32_EXTI_TRIG_RISING | GD32_EXTI_TRIG_FALLING)
```

在上升沿和下降沿（Rising and Falling Edge）均触发。

<a id="aab892d582f9f266f7d942d238786e306"></a>

### `GD32_EXTI_TRIG_FALLING`

```c
#define GD32_EXTI_TRIG_FALLING BIT(1)
```

下降沿触发（Trigger on Falling Edge）。

<a id="aa2b7ef2f0b43317c7c58fe4d53e07a19"></a>

### `GD32_EXTI_TRIG_NONE`

```c
#define GD32_EXTI_TRIG_NONE 0U
```

不触发（No Trigger）。

<a id="a8d9e9cd3451d66f8d6df889ea8d50a3c"></a>

### `GD32_EXTI_TRIG_RISING`

```c
#define GD32_EXTI_TRIG_RISING BIT(0)
```

上升沿触发（Trigger on Rising Edge）。

<a id="aac1a418b49c19fcf6e0dff2c0a3b7f75"></a>

### `gd32_exti_cb_t`

```c
typedef void(* gd32_exti_cb_t) (uint8_t line, void *user)
```

外部中断（EXTI）的回调。

<a id="a014fba07d150faa8270493bb8257b31b"></a>

### `gd32_exti_configure()`

```c
int gd32_exti_configure ( uint8_t line, gd32_exti_cb_t cb, void * user )
```

配置外部中断（EXTI）回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | 外部中断线路（EXTI Line）。 |
| `cb` | 回调（Callback）；传入 `NULL` 表示禁用。 |
| `user` | 用户数据（User Data），可选。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EALREADY` | 已设置回调（Callback）且 `cb` 不为 `NULL` 时。 |

<a id="a3f0333dce2621c7fed721e37a2413d80"></a>

### `gd32_exti_disable()`

```c
void gd32_exti_disable ( uint8_t line)
```

禁用给定线路（Line）的外部中断（EXTI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | 外部中断线路（EXTI Line）。 |

<a id="ad63c2b15a0f2e0f703255b00b9368232"></a>

### `gd32_exti_enable()`

```c
void gd32_exti_enable ( uint8_t line)
```

启用给定线路（Line）的外部中断（EXTI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | 外部中断线路（EXTI Line）。 |

<a id="ac543badc8874861f866b3bf3eba37e9a"></a>

### `gd32_exti_trigger()`

```c
void gd32_exti_trigger ( uint8_t line, uint8_t trigger )
```

配置给定线路（Line）的外部中断（EXTI）触发模式（Trigger Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line` | 外部中断线路（EXTI Line）。 |
| `trigger` | 触发模式（Trigger Mode），参见 `GD32_EXTI_TRIG`。 |


## 16.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P288_gd32_exti.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="GD32_EXTI_TRIG"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_zephyr__drivers__fuel_gauge.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__bluetooth__hci_nxp_setup.h_文件参考.md)
