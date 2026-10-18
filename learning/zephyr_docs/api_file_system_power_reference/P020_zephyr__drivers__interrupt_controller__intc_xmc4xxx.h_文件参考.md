---
id: learning.zephyr-docs.api-file-system-power-reference.page-20
title: zephyr__drivers__interrupt_controller__intc_xmc4xxx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_xmc4xxx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_a0203ccc3d0edc6be506752682afcc30c"></a>

```c
int intc_xmc4xxx_gpio_enable_interrupt (int port_id, int pin, enum gpio_int_mode mode, enum gpio_int_trig trig, void(*fn)(const struct device *dev, int pin), void *user_data)
```

相关声明：[intc_xmc4xxx_gpio_enable_interrupt](#a0203ccc3d0edc6be506752682afcc30c)、[gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)、[gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)、[device](../device_reference/P002_设备对象结构.md)。

启用指定 `port_id` 与 `pin` 组合的中断（Interrupt）。

<a id="r_a1583d09e4b260c07763e5419ca3411d1"></a>

```c
int intc_xmc4xxx_gpio_disable_interrupt (int port_id, int pin)
```

相关声明：[intc_xmc4xxx_gpio_disable_interrupt](#a1583d09e4b260c07763e5419ca3411d1)。

禁用指定 `port_id` 与 `pin` 组合的中断（Interrupt）。

## 20.2\_详细说明（Detailed Documentation）

<a id="a1583d09e4b260c07763e5419ca3411d1"></a>

### `intc_xmc4xxx_gpio_disable_interrupt()`

```c
int intc_xmc4xxx_gpio_disable_interrupt ( int port_id, int pin )
```

禁用指定 `port_id` 与 `pin` 组合的中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port_id` | 端口索引。 |
| `pin` | `pin`：端口（Port）中的引脚（Pin）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（On Success）。 |
| `-EINVAL` | 指定 `port_id` 与 `pin` 组合未启用任何中断（Interrupt）时。 |

<a id="a0203ccc3d0edc6be506752682afcc30c"></a>

### `intc_xmc4xxx_gpio_enable_interrupt()`

```c
int intc_xmc4xxx_gpio_enable_interrupt ( int port_id, int pin, enum gpio_int_mode mode, enum gpio_int_trig trig, void(* fn )(const struct device *dev, int pin), void * user_data )
```

启用指定 `port_id` 与 `pin` 组合的中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port_id` | 端口索引。 |
| `pin` | `pin`：端口（Port）中的引脚（Pin）。 |
| `mode` | 电平或边沿中断（Level or Edge Interrupt）。 |
| `trig` | 触发边沿类型（Trigger Edge Type）：下降沿、上升沿或双边沿（Falling、Rising、Both）。 |
| `fn` | 回调函数（Callback function）。 |
| `user_data` | 传递给中断回调（Interrupt Callback）的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | 不支持指定 `port_id`／`pin` 组合，或 DTS 中未定义该组合时。 |
| `-EBUSY` | 中断线（Interrupt Line）已被另一个 `port_id`／`pin` 使用时。 |
| `-EINVAL` | 触发组合（Trigger Combination）无效时。 |


## 20.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P405_intc_xmc4xxx.h_源码浏览.md)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_zephyr__drivers__interrupt_controller__intc_rz_tint.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__kernel__smp.h_文件参考.md)
