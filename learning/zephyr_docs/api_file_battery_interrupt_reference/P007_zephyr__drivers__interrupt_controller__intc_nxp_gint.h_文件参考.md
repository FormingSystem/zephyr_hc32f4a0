---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-7
title: zephyr__drivers__interrupt_controller__intc_nxp_gint.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_nxp\_gint.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP分组GPIO输入中断（Grouped GPIO Input Interrupt，GINT）的驱动API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
```

查看此文件的源码。

NXP分组GPIO输入中断（Grouped GPIO Input Interrupt，GINT）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_nxp_5Fgint_5Fgroup_5Fconfig"></a>

```c
struct nxp_gint_group_config
```

相关声明：[nxp_gint_group_config](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md)。

分组中断（GINT）的组配置。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.2\_类型定义（Typedefs）

<a id="r_ab2bb2c06c72c6dd81a3e6616296d3d7e"></a>

```c
typedef void(* nxp_gint_callback_t) (const struct device *dev, void *user_data)
```

相关声明：[nxp_gint_callback_t](#ab2bb2c06c72c6dd81a3e6616296d3d7e)、[device](../device_reference/P002_设备对象结构.md)。

GINT 回调函数类型（Callback Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.3\_枚举（Enumerations）

<a id="r_a07f2264ca2366594a571858cc5ee6b9a"></a>

```c
enum nxp_gint_trigger_type { NXP_GINT_TRIG_EDGE = 0 , NXP_GINT_TRIG_LEVEL = 1 }
```

相关声明：[nxp_gint_trigger_type](#a07f2264ca2366594a571858cc5ee6b9a)、[NXP_GINT_TRIG_EDGE](#a07f2264ca2366594a571858cc5ee6b9aa9199715bc7fa26a7936e167b57dc81b6)、[NXP_GINT_TRIG_LEVEL](#a07f2264ca2366594a571858cc5ee6b9aaed72091eeef574afdae0d9b576980bad)。

GINT 触发类型（Trigger Types）。

<a id="r_abc9f321deac34cacd128dc16c2db3df6"></a>

```c
enum nxp_gint_combination_type { NXP_GINT_COMB_OR = 0 , NXP_GINT_COMB_AND = 1 }
```

相关声明：[nxp_gint_combination_type](#abc9f321deac34cacd128dc16c2db3df6)、[NXP_GINT_COMB_OR](#abc9f321deac34cacd128dc16c2db3df6a3a05e0f414cd4401b2858650598a3f66)、[NXP_GINT_COMB_AND](#abc9f321deac34cacd128dc16c2db3df6a68ac19cd2c60a8b5413a34a5305630f2)。

GINT 组合逻辑（Combination Logic）。

<a id="r_ad046213e6efeea292323f1af3b3df4fa"></a>

```c
enum nxp_gint_polarity_type { NXP_GINT_POL_LOW = 0 , NXP_GINT_POL_HIGH = 1 }
```

相关声明：[nxp_gint_polarity_type](#ad046213e6efeea292323f1af3b3df4fa)、[NXP_GINT_POL_LOW](#ad046213e6efeea292323f1af3b3df4faacdaa397042505f1f90b15ff3c8d4b64d)、[NXP_GINT_POL_HIGH](#ad046213e6efeea292323f1af3b3df4faa98c4639c9ce35ecfd855f8604c8c86b4)。

GINT 引脚极性（Pin Polarity）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_a5e4f2bdb5749f1a582ef3ee407cb8bdc"></a>

```c
int nxp_gint_configure_group (const struct device *dev, const struct nxp_gint_group_config *config)
```

相关声明：[nxp_gint_configure_group](#a5e4f2bdb5749f1a582ef3ee407cb8bdc)、[device](../device_reference/P002_设备对象结构.md)、[nxp_gint_group_config](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md)。

配置 GINT 设置。

<a id="r_a3ca522907628e534477c45e1faef89cf"></a>

```c
int nxp_gint_enable_pin (const struct device *dev, uint8_t port, uint8_t pin, nxp_gint_polarity_type polarity)
```

相关声明：[nxp_gint_enable_pin](#a3ca522907628e534477c45e1faef89cf)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nxp_gint_polarity_type](#ad046213e6efeea292323f1af3b3df4fa)。

为 GINT 启用一个引脚（Pin）。

<a id="r_a76a33bc514ae1e0b7923ef8610614ddb"></a>

```c
int nxp_gint_disable_pin (const struct device *dev, uint8_t port, uint8_t pin)
```

相关声明：[nxp_gint_disable_pin](#a76a33bc514ae1e0b7923ef8610614ddb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为 GINT 禁用一个引脚（Pin）。

<a id="r_a04d305e582dc9babc28a5d01edd9963d"></a>

```c
bool nxp_gint_is_pending (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[nxp_gint_is_pending](#a04d305e582dc9babc28a5d01edd9963d)、[device](../device_reference/P002_设备对象结构.md)。

检查 GINT 中断是否挂起（Pending）。

<a id="r_a5371cc92fc4a3516784601a0f060699e"></a>

```c
int nxp_gint_clear_pending (const struct device *dev)
```

相关声明：[nxp_gint_clear_pending](#a5371cc92fc4a3516784601a0f060699e)、[device](../device_reference/P002_设备对象结构.md)。

清除 GINT 中断挂起状态（Interrupt Pending Status）。

<a id="r_a9df8c215c7b27faef4ce781d253a217a"></a>

```c
int nxp_gint_register_callback (const struct device *dev, nxp_gint_callback_t callback, void *user_data)
```

相关声明：[nxp_gint_register_callback](#a9df8c215c7b27faef4ce781d253a217a)、[device](../device_reference/P002_设备对象结构.md)、[nxp_gint_callback_t](#ab2bb2c06c72c6dd81a3e6616296d3d7e)。

注册 GINT 回调（Callback）。

## 7.5\_详细说明（Detailed Documentation）

<a id="ab2bb2c06c72c6dd81a3e6616296d3d7e"></a>

### `nxp_gint_callback_t`

```c
typedef void(* nxp_gint_callback_t) (const struct device *dev, void *user_data)
```

GINT 回调函数类型（Callback Function Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |
| `user_data` | 用户定义的数据。 |

<a id="abc9f321deac34cacd128dc16c2db3df6"></a>

### `nxp_gint_combination_type`

```c
enum nxp_gint_combination_type
```

GINT 组合逻辑（Combination Logic）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_GINT_COMB_OR` | 或逻辑（OR Logic）：任一已启用引脚均可触发中断。 |
| `NXP_GINT_COMB_AND` | 与逻辑（AND Logic）：所有已启用引脚都必须满足触发条件，才触发中断。 |

<a id="ad046213e6efeea292323f1af3b3df4fa"></a>

### `nxp_gint_polarity_type`

```c
enum nxp_gint_polarity_type
```

GINT 引脚极性（Pin Polarity）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_GINT_POL_LOW` | 低电平有效（Active LOW）。 |
| `NXP_GINT_POL_HIGH` | 高电平有效（Active HIGH）。 |

<a id="a07f2264ca2366594a571858cc5ee6b9a"></a>

### `nxp_gint_trigger_type`

```c
enum nxp_gint_trigger_type
```

GINT 触发类型（Trigger Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_GINT_TRIG_EDGE` | 边沿触发（Edge Triggered）。 |
| `NXP_GINT_TRIG_LEVEL` | 电平触发（Level Triggered）。 |

<a id="a5371cc92fc4a3516784601a0f060699e"></a>

### `nxp_gint_clear_pending()`

```c
int nxp_gint_clear_pending ( const struct device * dev)
```

清除 GINT 中断挂起状态（Interrupt Pending Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a5e4f2bdb5749f1a582ef3ee407cb8bdc"></a>

### `nxp_gint_configure_group()`

```c
int nxp_gint_configure_group ( const struct device * dev, const struct nxp_gint_group_config * config )
```

配置 GINT 设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |
| `config` | 组配置（Group Configuration） |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a76a33bc514ae1e0b7923ef8610614ddb"></a>

### `nxp_gint_disable_pin()`

```c
int nxp_gint_disable_pin ( const struct device * dev, uint8_t port, uint8_t pin )
```

为 GINT 禁用一个引脚（Pin）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |
| `port` | 端口号（Port number）。 |
| `pin` | 引脚编号（Pin Number，0～31） |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a3ca522907628e534477c45e1faef89cf"></a>

### `nxp_gint_enable_pin()`

```c
int nxp_gint_enable_pin ( const struct device * dev, uint8_t port, uint8_t pin, nxp_gint_polarity_type polarity )
```

为 GINT 启用一个引脚（Pin）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |
| `port` | 端口号（Port number）。 |
| `pin` | 引脚编号（Pin Number，0～31） |
| `polarity` | 引脚极性（Pin Polarity） |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="a04d305e582dc9babc28a5d01edd9963d"></a>

### `nxp_gint_is_pending()`

```c
bool nxp_gint_is_pending ( const struct device * dev)
```

检查 GINT 中断是否挂起（Pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |

**返回（Returns）**：返回值（Returns）：中断已挂起时返回 true，否则返回 false。

<a id="a9df8c215c7b27faef4ce781d253a217a"></a>

### `nxp_gint_register_callback()`

```c
int nxp_gint_register_callback ( const struct device * dev, nxp_gint_callback_t callback, void * user_data )
```

注册 GINT 回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GINT 设备（Device） |
| `callback` | 待注册的回调函数（Callback Function） |
| `user_data` | 传递给回调的用户自定义数据（User Defined Data） |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 7.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P397_intc_nxp_gint.h_源码浏览.md)
- [nxp_gint_group_config](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="abc9f321deac34cacd128dc16c2db3df6a3a05e0f414cd4401b2858650598a3f66"></a>
<a id="abc9f321deac34cacd128dc16c2db3df6a68ac19cd2c60a8b5413a34a5305630f2"></a>
<a id="ad046213e6efeea292323f1af3b3df4faacdaa397042505f1f90b15ff3c8d4b64d"></a>
<a id="ad046213e6efeea292323f1af3b3df4faa98c4639c9ce35ecfd855f8604c8c86b4"></a>
<a id="a07f2264ca2366594a571858cc5ee6b9aa9199715bc7fa26a7936e167b57dc81b6"></a>
<a id="a07f2264ca2366594a571858cc5ee6b9aaed72091eeef574afdae0d9b576980bad"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_zephyr__dt-bindings__sensor__adxl355.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__net__ppp.h_文件参考.md)
