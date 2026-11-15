---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-8
title: MFD AXP192 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_MFD AXP192 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__axp192.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AXP192 的引脚支持多种不同功能。

<a id="details"></a>

AXP192 引脚支持多种功能（Functions）。多功能设备（MFD）接口提供用于配置和控制这些功能的 API。6 个 GPIO 的映射如下：

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga61c3f46791f4efa08ee45fc85dc32c81"></a>

```c
int mfd_axp192_gpio_func_ctrl (const struct device *dev, const struct device *client_dev, uint8_t gpio, enum axp192_gpio_func func)
```

相关声明：[mfd_axp192_gpio_func_ctrl](#ga61c3f46791f4efa08ee45fc85dc32c81)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[axp192_gpio_func](../api_file_transfer_device_reference/P007_zephyr__drivers__mfd__axp192.h_文件参考.md#ac92e5fa77591e02e49570d1a1c38e249)。

请求将 GPIO 引脚（Pin）配置为指定功能（Function）。

<a id="r_ga29db6e44c801fecfa1df2d9da93c2e0b"></a>

```c
int mfd_axp192_gpio_func_get (const struct device *dev, uint8_t gpio, enum axp192_gpio_func *func)
```

相关声明：[mfd_axp192_gpio_func_get](#ga29db6e44c801fecfa1df2d9da93c2e0b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[axp192_gpio_func](../api_file_transfer_device_reference/P007_zephyr__drivers__mfd__axp192.h_文件参考.md#ac92e5fa77591e02e49570d1a1c38e249)。

读取指定 GPIO 引脚（Pin）的当前配置（Configuration）。

<a id="r_ga8db91c44adbf8ca6f727e2deb0aa96dd"></a>

```c
int mfd_axp192_gpio_pd_ctrl (const struct device *dev, uint8_t gpio, bool enable)
```

相关声明：[mfd_axp192_gpio_pd_ctrl](#ga8db91c44adbf8ca6f727e2deb0aa96dd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用指定 GPIO 引脚（Pin）的下拉（Pull-down）。

<a id="r_gabdacd1e10bacf9f0393beb65327eaeea"></a>

```c
int mfd_axp192_gpio_pd_get (const struct device *dev, uint8_t gpio, bool *enabled)
```

相关声明：[mfd_axp192_gpio_pd_get](#gabdacd1e10bacf9f0393beb65327eaeea)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

读取指定 GPIO 的当前下拉配置（Pull-down Configuration）。

<a id="r_gaa12241d0655122f05da06dc506d2a5c0"></a>

```c
int mfd_axp192_gpio_read_port (const struct device *dev, uint8_t *value)
```

相关声明：[mfd_axp192_gpio_read_port](#gaa12241d0655122f05da06dc506d2a5c0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 GPIO 端口（Port）。

<a id="r_ga7570c8657918c15c71fddca264bce10e"></a>

```c
int mfd_axp192_gpio_write_port (const struct device *dev, uint8_t value, uint8_t mask)
```

相关声明：[mfd_axp192_gpio_write_port](#ga7570c8657918c15c71fddca264bce10e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 GPIO 端口（Port）。

## 8.2\_详细说明（Detailed Documentation）

<a id="ga61c3f46791f4efa08ee45fc85dc32c81"></a>

### `mfd_axp192_gpio_func_ctrl()`

```c
int mfd_axp192_gpio_func_ctrl ( const struct device * dev, const struct device * client_dev, uint8_t gpio, enum axp192_gpio_func func )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

请求将 GPIO 引脚（Pin）配置为指定功能（Function）。

AXP192 的 GPIO0..5 支持不同功能，详情参见 `axp192_gpio_func`。每个 GPIO 只能由一个驱动实例使用；对同一 GPIO 的后续调用会覆盖其相应功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `client_dev` | 使用该 GPIO 的客户端设备（Client Device）。 |
| `gpio` | 要配置的 GPIO，范围 `0..5`。 |
| `func` | 要配置的功能（Function），详情参见 `axp192_gpio_func`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 传入的 GPIO 编号（Number）无效。 |
| `-ENOTSUP` | 给定 GPIO 不支持所请求的功能（Function）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga29db6e44c801fecfa1df2d9da93c2e0b"></a>

### `mfd_axp192_gpio_func_get()`

```c
int mfd_axp192_gpio_func_get ( const struct device * dev, uint8_t gpio, enum axp192_gpio_func * func )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

读取指定 GPIO 引脚（Pin）的当前配置（Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `gpio` | 要读取配置（Configuration）的 GPIO。 |
| `func` | 用于存储当前功能配置（Function Configuration）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 传入的 GPIO 编号（Number）无效。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga8db91c44adbf8ca6f727e2deb0aa96dd"></a>

### `mfd_axp192_gpio_pd_ctrl()`

```c
int mfd_axp192_gpio_pd_ctrl ( const struct device * dev, uint8_t gpio, bool enable )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

启用指定 GPIO 引脚（Pin）的下拉（Pull-down）。

AXP192 仅支持 GPIO3..5 下拉（Pull-down），不支持上拉（Pull-up）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `gpio` | 要控制下拉（Pull-down）的 GPIO。 |
| `enable` | `true` 启用下拉（Pull-down），`false` 禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 给定参数无效（Invalid Argument），例如 GPIO 编号无效。 |
| `-ENOTSUP` | 给定 GPIO 不支持下拉（Pull-down）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gabdacd1e10bacf9f0393beb65327eaeea"></a>

### `mfd_axp192_gpio_pd_get()`

```c
int mfd_axp192_gpio_pd_get ( const struct device * dev, uint8_t gpio, bool * enabled )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

读取指定 GPIO 的当前下拉配置（Pull-down Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `gpio` | 要控制下拉（Pull-down）的 GPIO。 |
| `enabled` | 指向当前下拉配置（Pull-down Configuration）的指针，`true` 表示已启用，`false` 表示已禁用。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 给定参数无效（Invalid Argument），例如 GPIO 编号无效。 |
| `-ENOTSUP` | 给定 GPIO 不支持下拉（Pull-down）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa12241d0655122f05da06dc506d2a5c0"></a>

### `mfd_axp192_gpio_read_port()`

```c
int mfd_axp192_gpio_read_port ( const struct device * dev, uint8_t * value )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

读取 GPIO 端口（Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `value` | 指向端口值（Port Value）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7570c8657918c15c71fddca264bce10e"></a>

### `mfd_axp192_gpio_write_port()`

```c
int mfd_axp192_gpio_write_port ( const struct device * dev, uint8_t value, uint8_t mask )
```

```c
#include <zephyr/drivers/mfd/axp192.h>
```

写入 GPIO 端口（Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | AXP192 多功能设备（MFD）。 |
| `value` | 端口值（Port Value）。 |
| `mask` | 端口内的引脚掩码（Pin Mask）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 8.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [axp192_gpio_func](../api_file_transfer_device_reference/P007_zephyr__drivers__mfd__axp192.h_文件参考.md#ac92e5fa77591e02e49570d1a1c38e249)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/drivers/mfd/axp192.h](../api_file_transfer_device_reference/P007_zephyr__drivers__mfd__axp192.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_LPS2xDF API主题.md) · [返回大纲](大纲.md) · [下一章](P009_基本过滤条件（Basic Filter Conditions）.md)
