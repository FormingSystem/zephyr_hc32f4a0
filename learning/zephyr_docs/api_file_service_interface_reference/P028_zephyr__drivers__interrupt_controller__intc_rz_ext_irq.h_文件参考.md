---
id: learning.zephyr-docs.api-file-service-interface-reference.page-28
title: zephyr__drivers__interrupt_controller__intc_rz_ext_irq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_rz\_ext\_irq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.1\_宏定义（Macros）

<a id="r_a17f720465c2865fd41086d7529b58065"></a>

```c
#define RZ_EXT_IRQ_TRIG_FALLING 0
```

相关声明：[RZ_EXT_IRQ_TRIG_FALLING](#a17f720465c2865fd41086d7529b58065)。

<a id="r_ae86170a06f383179bee5d69b37021205"></a>

```c
#define RZ_EXT_IRQ_TRIG_RISING 1
```

相关声明：[RZ_EXT_IRQ_TRIG_RISING](#ae86170a06f383179bee5d69b37021205)。

<a id="r_acde0f849883aa9b57e93b056754d4dbb"></a>

```c
#define RZ_EXT_IRQ_TRIG_BOTH_EDGE 2
```

相关声明：[RZ_EXT_IRQ_TRIG_BOTH_EDGE](#acde0f849883aa9b57e93b056754d4dbb)。

<a id="r_a2ac25bcef358c7dad3620ba42ff0fc2c"></a>

```c
#define RZ_EXT_IRQ_TRIG_LEVEL_LOW 3
```

相关声明：[RZ_EXT_IRQ_TRIG_LEVEL_LOW](#a2ac25bcef358c7dad3620ba42ff0fc2c)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 28.2\_类型定义（Typedefs）

<a id="r_a1c6d9f3910b3d82378ab40219828184a"></a>

```c
typedef void(* intc_rz_ext_irq_callback_t) (void *arg)
```

相关声明：[intc_rz_ext_irq_callback_t](#a1c6d9f3910b3d82378ab40219828184a)。

RZ 外部中断回调（External Interrupt Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_a08eb727b662be3e71d70c5fa88e95b7a"></a>

```c
int intc_rz_ext_irq_enable (const struct device *dev)
```

相关声明：[intc_rz_ext_irq_enable](#a08eb727b662be3e71d70c5fa88e95b7a)、[device](../device_reference/P002_设备对象结构.md)。

启用指定通道的外部中断（External Interrupt）。

<a id="r_a9a372d975e6507a4d34c0766f22a368a"></a>

```c
int intc_rz_ext_irq_disable (const struct device *dev)
```

相关声明：[intc_rz_ext_irq_disable](#a9a372d975e6507a4d34c0766f22a368a)、[device](../device_reference/P002_设备对象结构.md)。

禁用指定通道的外部中断（External Interrupt）。

<a id="r_af40022fc3bb2e30df6513c4172672235"></a>

```c
int intc_rz_ext_irq_set_callback (const struct device *dev, intc_rz_ext_irq_callback_t cb, void *arg)
```

相关声明：[intc_rz_ext_irq_set_callback](#af40022fc3bb2e30df6513c4172672235)、[device](../device_reference/P002_设备对象结构.md)、[intc_rz_ext_irq_callback_t](#a1c6d9f3910b3d82378ab40219828184a)。

更新用户回调（User Callback）。

<a id="r_a913bfcbf3ff2161da4c2a45a77781452"></a>

```c
int intc_rz_ext_irq_set_type (const struct device *dev, uint8_t trig)
```

相关声明：[intc_rz_ext_irq_set_type](#a913bfcbf3ff2161da4c2a45a77781452)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改指定通道的外部中断触发类型（Trigger Type）。

## 28.4\_详细说明（Detailed Documentation）

<a id="acde0f849883aa9b57e93b056754d4dbb"></a>

### `RZ_EXT_IRQ_TRIG_BOTH_EDGE`

```c
#define RZ_EXT_IRQ_TRIG_BOTH_EDGE 2
```

<a id="a17f720465c2865fd41086d7529b58065"></a>

### `RZ_EXT_IRQ_TRIG_FALLING`

```c
#define RZ_EXT_IRQ_TRIG_FALLING 0
```

<a id="a2ac25bcef358c7dad3620ba42ff0fc2c"></a>

### `RZ_EXT_IRQ_TRIG_LEVEL_LOW`

```c
#define RZ_EXT_IRQ_TRIG_LEVEL_LOW 3
```

<a id="ae86170a06f383179bee5d69b37021205"></a>

### `RZ_EXT_IRQ_TRIG_RISING`

```c
#define RZ_EXT_IRQ_TRIG_RISING 1
```

<a id="a1c6d9f3910b3d82378ab40219828184a"></a>

### `intc_rz_ext_irq_callback_t`

```c
typedef void(* intc_rz_ext_irq_callback_t) (void *arg)
```

RZ 外部中断回调（External Interrupt Callback）。

<a id="a9a372d975e6507a4d34c0766f22a368a"></a>

### `intc_rz_ext_irq_disable()`

```c
int intc_rz_ext_irq_disable ( const struct device * dev)
```

禁用指定通道的外部中断（External Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a08eb727b662be3e71d70c5fa88e95b7a"></a>

### `intc_rz_ext_irq_enable()`

```c
int intc_rz_ext_irq_enable ( const struct device * dev)
```

启用指定通道的外部中断（External Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="af40022fc3bb2e30df6513c4172672235"></a>

### `intc_rz_ext_irq_set_callback()`

```c
int intc_rz_ext_irq_set_callback ( const struct device * dev, intc_rz_ext_irq_callback_t cb, void * arg )
```

更新用户回调（User Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |
| `cb` | 要设置的回调（Callback）。 |
| `arg` | 传给回调的用户数据。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a913bfcbf3ff2161da4c2a45a77781452"></a>

### `intc_rz_ext_irq_set_type()`

```c
int intc_rz_ext_irq_set_type ( const struct device * dev, uint8_t trig )
```

更改指定通道的外部中断触发类型（Trigger Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |
| `trig` | 要更改的触发类型（Trigger Type）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。


## 28.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P400_intc_rz_ext_irq.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_zephyr__dt-bindings__clock__imx_ccm_rev2.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__dt-bindings__sensor__ism330dhcx.h_文件参考.md)
