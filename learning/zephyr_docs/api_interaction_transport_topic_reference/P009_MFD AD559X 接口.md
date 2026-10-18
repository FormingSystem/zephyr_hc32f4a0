---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-9
title: MFD AD559X 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_MFD AD559X 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_ga9280bf8cdaf3011a53073d189840e58f"></a>

```c
bool mfd_ad559x_has_pointer_byte_map (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mfd_ad559x_has_pointer_byte_map](#ga9280bf8cdaf3011a53073d189840e58f)、[device](../device_reference/P002_设备对象结构.md)。

检查芯片是否具有指针字节映射（Pointer Byte Map）。

<a id="r_ga60a3bef4d69b2e5dcde5f15ab10ee607"></a>

```c
int mfd_ad559x_read_raw (const struct device *dev, uint8_t *val, size_t len)
```

相关声明：[mfd_ad559x_read_raw](#ga60a3bef4d69b2e5dcde5f15ab10ee607)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从芯片读取原始数据（Raw Data）。

<a id="r_ga0b9f70e3c85e17cd9f556f5cb98baf59"></a>

```c
int mfd_ad559x_write_raw (const struct device *dev, uint8_t *val, size_t len)
```

相关声明：[mfd_ad559x_write_raw](#ga0b9f70e3c85e17cd9f556f5cb98baf59)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向芯片写入原始数据（Raw Data）。

<a id="r_ga896686606e114e223ee5afe40518356f"></a>

```c
int mfd_ad559x_read_reg (const struct device *dev, uint8_t reg, uint8_t reg_data, uint16_t *val)
```

相关声明：[mfd_ad559x_read_reg](#ga896686606e114e223ee5afe40518356f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从指定寄存器（Register）读取数据。

<a id="r_gac91730fd6126260bc60da7c2637d7ccb"></a>

```c
int mfd_ad559x_write_reg (const struct device *dev, uint8_t reg, uint16_t val)
```

相关声明：[mfd_ad559x_write_reg](#gac91730fd6126260bc60da7c2637d7ccb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向指定寄存器（Register）写入数据。

<a id="r_gace77752024305f468412262f063e2c2a"></a>

```c
int mfd_ad559x_read_adc_chan (const struct device *dev, uint8_t channel, uint16_t *result)
```

相关声明：[mfd_ad559x_read_adc_chan](#gace77752024305f468412262f063e2c2a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从芯片读取模数转换器（ADC）通道数据。

<a id="r_ga9a07f9de00ca00e19daa56ac1fc923bc"></a>

```c
int mfd_ad559x_write_dac_chan (const struct device *dev, uint8_t channel, uint16_t value)
```

相关声明：[mfd_ad559x_write_dac_chan](#ga9a07f9de00ca00e19daa56ac1fc923bc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向芯片写入模数转换器（ADC）通道数据。

<a id="r_gacf88f29f46db4293e97f7fbb7a3edeb7"></a>

```c
int mfd_ad559x_gpio_port_get_raw (const struct device *dev, uint8_t gpio, uint16_t *value)
```

相关声明：[mfd_ad559x_gpio_port_get_raw](#gacf88f29f46db4293e97f7fbb7a3edeb7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从芯片读取通用输入输出（GPIO）端口。

## 9.2\_详细说明（Detailed Documentation）

<a id="gacf88f29f46db4293e97f7fbb7a3edeb7"></a>

### `mfd_ad559x_gpio_port_get_raw()`

```c
int mfd_ad559x_gpio_port_get_raw ( const struct device * dev, uint8_t gpio, uint16_t * value )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

从芯片读取通用输入输出（GPIO）端口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] gpio` | 要读取的通用输入输出（GPIO）。 |
| `[in] value` | 数模转换器（DAC）通道值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="ga9280bf8cdaf3011a53073d189840e58f"></a>

### `mfd_ad559x_has_pointer_byte_map()`

```c
bool mfd_ad559x_has_pointer_byte_map ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

检查芯片是否具有指针字节映射（Pointer Byte Map）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 芯片具有指针字节映射（Pointer Byte Map）时成立；若使用普通寄存器映射（Register Map），则为 `false`。 |

<a id="gace77752024305f468412262f063e2c2a"></a>

### `mfd_ad559x_read_adc_chan()`

```c
int mfd_ad559x_read_adc_chan ( const struct device * dev, uint8_t channel, uint16_t * result )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

从芯片读取模数转换器（ADC）通道数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] channel` | 要读取的通道（Channel）。 |
| `[out] result` | 读出的模数转换器（ADC）通道值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="ga60a3bef4d69b2e5dcde5f15ab10ee607"></a>

### `mfd_ad559x_read_raw()`

```c
int mfd_ad559x_read_raw ( const struct device * dev, uint8_t * val, size_t len )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

从芯片读取原始数据（Raw Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] val` | 指向数据缓冲区（Data Buffer）的指针。 |
| `[in] len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="ga896686606e114e223ee5afe40518356f"></a>

### `mfd_ad559x_read_reg()`

```c
int mfd_ad559x_read_reg ( const struct device * dev, uint8_t reg, uint8_t reg_data, uint16_t * val )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

从指定寄存器（Register）读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] reg` | 要读取的寄存器（Register）。 |
| `[in] reg_data` | 传给选定寄存器的附加数据（Additional Data）。 |
| `[in] val` | 指向数据缓冲区（Data Buffer）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="ga9a07f9de00ca00e19daa56ac1fc923bc"></a>

### `mfd_ad559x_write_dac_chan()`

```c
int mfd_ad559x_write_dac_chan ( const struct device * dev, uint8_t channel, uint16_t value )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

向芯片写入模数转换器（ADC）通道数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] channel` | 要写入的通道（Channel）。 |
| `[in] value` | 数模转换器（DAC）通道值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="ga0b9f70e3c85e17cd9f556f5cb98baf59"></a>

### `mfd_ad559x_write_raw()`

```c
int mfd_ad559x_write_raw ( const struct device * dev, uint8_t * val, size_t len )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

向芯片写入原始数据（Raw Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] val` | 要写入的数据（Data to be written）。 |
| `[in] len` | 要写入的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |

<a id="gac91730fd6126260bc60da7c2637d7ccb"></a>

### `mfd_ad559x_write_reg()`

```c
int mfd_ad559x_write_reg ( const struct device * dev, uint8_t reg, uint16_t val )
```

```c
#include <zephyr/drivers/mfd/ad559x.h>
```

向指定寄存器（Register）写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向多功能设备（MFD）的指针。 |
| `[in] reg` | 要写入的寄存器（Register）。 |
| `[in] val` | 要写入的数据（Data to be written）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 失败时的 `errno` 错误码。 |


## 9.3\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/drivers/mfd/ad559x.h](../api_file_service_interface_reference/P002_zephyr__drivers__mfd__ad559x.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_Microchip NVMCTRL G1 API主题.md) · [返回大纲](大纲.md) · [下一章](P010_MFD PCA9422 接口.md)
