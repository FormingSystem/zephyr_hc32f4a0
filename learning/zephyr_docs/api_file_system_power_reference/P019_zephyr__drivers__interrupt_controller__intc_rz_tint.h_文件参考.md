---
id: learning.zephyr-docs.api-file-system-power-reference.page-19
title: zephyr__drivers__interrupt_controller__intc_rz_tint.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_rz\_tint.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 19.1\_类型定义（Typedefs）

<a id="r_aa47a09baad3bd3e77a10b90ecda66e9d"></a>

```c
typedef void(* intc_rz_tint_callback_t) (void *arg)
```

相关声明：[intc_rz_tint_callback_t](#aa47a09baad3bd3e77a10b90ecda66e9d)。

RZ GPIO 中断（TINT）回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.2\_枚举（Enumerations）

<a id="r_a905cdb052d714bc9c5a90cfdf1614434"></a>

```c
enum intc_rz_tint_trigger { RZ_TINT_FAILING_EDGE , RZ_TINT_RISING_EDGE , RZ_TINT_BOTH_EDGE , RZ_TINT_LOW_LEVEL , RZ_TINT_HIGH_LEVEL }
```

相关声明：[intc_rz_tint_trigger](#a905cdb052d714bc9c5a90cfdf1614434)、[RZ_TINT_FAILING_EDGE](#a905cdb052d714bc9c5a90cfdf1614434a4aa5928babb7e7b658be714c5df211c2)、[RZ_TINT_RISING_EDGE](#a905cdb052d714bc9c5a90cfdf1614434a35bce08a56a20e67fb028ee74c3331ad)、[RZ_TINT_BOTH_EDGE](#a905cdb052d714bc9c5a90cfdf1614434a3a8c04fc0458b0a96da9b52f22e36eb6)、[RZ_TINT_LOW_LEVEL](#a905cdb052d714bc9c5a90cfdf1614434a9c3971631e16520443a055139f63f604)、[RZ_TINT_HIGH_LEVEL](#a905cdb052d714bc9c5a90cfdf1614434a2f26bfb23aa941ba6c2da19b7387554a)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.3\_函数（Functions）

<a id="r_afee1611e56667148581ed48117cdcfc5"></a>

```c
int intc_rz_tint_connect (const struct device *dev, uint8_t port, uint8_t pin)
```

相关声明：[intc_rz_tint_connect](#afee1611e56667148581ed48117cdcfc5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 TINT 通道（Channel）连接到指定 GPIO 引脚（Pins）。

<a id="r_a4363ce99eee64656d3bbc520dac8c1c8"></a>

```c
int intc_rz_tint_set_type (const struct device *dev, enum intc_rz_tint_trigger trig)
```

相关声明：[intc_rz_tint_set_type](#a4363ce99eee64656d3bbc520dac8c1c8)、[device](../device_reference/P002_设备对象结构.md)、[intc_rz_tint_trigger](#a905cdb052d714bc9c5a90cfdf1614434)。

更改中断触发类型（Trigger Interrupt Type）。

<a id="r_a61a9005f09428a38ba570b5b47f7381e"></a>

```c
int intc_rz_tint_enable (const struct device *dev)
```

相关声明：[intc_rz_tint_enable](#a61a9005f09428a38ba570b5b47f7381e)、[device](../device_reference/P002_设备对象结构.md)。

启用 TINT 中断（Interrupt）。

<a id="r_a60a69e2377b62032b65909d835a1ba6a"></a>

```c
int intc_rz_tint_disable (const struct device *dev)
```

相关声明：[intc_rz_tint_disable](#a60a69e2377b62032b65909d835a1ba6a)、[device](../device_reference/P002_设备对象结构.md)。

禁用 TINT 中断（Interrupt）。

<a id="r_a4e028397cd25a200c7be779339d3c5cc"></a>

```c
int intc_rz_tint_set_callback (const struct device *dev, intc_rz_tint_callback_t cb, void *arg)
```

相关声明：[intc_rz_tint_set_callback](#a4e028397cd25a200c7be779339d3c5cc)、[device](../device_reference/P002_设备对象结构.md)、[intc_rz_tint_callback_t](#aa47a09baad3bd3e77a10b90ecda66e9d)。

更新用户回调（User Callback）。

## 19.4\_详细说明（Detailed Documentation）

<a id="aa47a09baad3bd3e77a10b90ecda66e9d"></a>

### `intc_rz_tint_callback_t`

```c
typedef void(* intc_rz_tint_callback_t) (void *arg)
```

RZ GPIO 中断（TINT）回调（Callback）。

<a id="a905cdb052d714bc9c5a90cfdf1614434"></a>

### `intc_rz_tint_trigger`

```c
enum intc_rz_tint_trigger
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RZ_TINT_FAILING_EDGE` | 下降沿触发的中断（Falling-edge Interrupt）。 |
| `RZ_TINT_RISING_EDGE` | 上升沿触发的中断（Rising-edge Interrupt）。 |
| `RZ_TINT_BOTH_EDGE` | 双边沿触发的中断（Both-edge Interrupt）。 |
| `RZ_TINT_LOW_LEVEL` | 低电平触发的中断（Low-level Interrupt）。 |
| `RZ_TINT_HIGH_LEVEL` | 高电平触发的中断（High-level Interrupt）。 |

<a id="afee1611e56667148581ed48117cdcfc5"></a>

### `intc_rz_tint_connect()`

```c
int intc_rz_tint_connect ( const struct device * dev, uint8_t port, uint8_t pin )
```

将 TINT 通道（Channel）连接到指定 GPIO 引脚（Pins）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |
| `port` | GPIO 端口（Port）。 |
| `pin` | GPIO 引脚（Pin）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a60a69e2377b62032b65909d835a1ba6a"></a>

### `intc_rz_tint_disable()`

```c
int intc_rz_tint_disable ( const struct device * dev)
```

禁用 TINT 中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a61a9005f09428a38ba570b5b47f7381e"></a>

### `intc_rz_tint_enable()`

```c
int intc_rz_tint_enable ( const struct device * dev)
```

启用 TINT 中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a4e028397cd25a200c7be779339d3c5cc"></a>

### `intc_rz_tint_set_callback()`

```c
int intc_rz_tint_set_callback ( const struct device * dev, intc_rz_tint_callback_t cb, void * arg )
```

更新用户回调（User Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |
| `cb` | 要设置的回调（Callback）。 |
| `arg` | 传给回调的用户数据。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="a4363ce99eee64656d3bbc520dac8c1c8"></a>

### `intc_rz_tint_set_type()`

```c
int intc_rz_tint_set_type ( const struct device * dev, enum intc_rz_tint_trigger trig )
```

更改中断触发类型（Trigger Interrupt Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向中断控制器（Interrupt Controller）实例的指针。 |
| `trig` | 要更改的触发类型（Trigger Type）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。


## 19.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P402_intc_rz_tint.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a905cdb052d714bc9c5a90cfdf1614434a4aa5928babb7e7b658be714c5df211c2"></a>
<a id="a905cdb052d714bc9c5a90cfdf1614434a35bce08a56a20e67fb028ee74c3331ad"></a>
<a id="a905cdb052d714bc9c5a90cfdf1614434a3a8c04fc0458b0a96da9b52f22e36eb6"></a>
<a id="a905cdb052d714bc9c5a90cfdf1614434a9c3971631e16520443a055139f63f604"></a>
<a id="a905cdb052d714bc9c5a90cfdf1614434a2f26bfb23aa941ba6c2da19b7387554a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_zephyr__dt-bindings__pinctrl__ifx_cat1-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__drivers__interrupt_controller__intc_xmc4xxx.h_文件参考.md)
