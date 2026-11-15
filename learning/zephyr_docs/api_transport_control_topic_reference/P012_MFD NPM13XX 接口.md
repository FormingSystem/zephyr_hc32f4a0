---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-12
title: MFD NPM13XX 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_MFD NPM13XX 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.1\_枚举（Enumerations）

<a id="r_ga4ac9f47283f10ea1d847cbd0038aad7a"></a>

```c
enum mfd_npm13xx_event_t { NPM13XX_EVENT_CHG_COMPLETED , NPM13XX_EVENT_CHG_ERROR , NPM13XX_EVENT_BATTERY_DETECTED , NPM13XX_EVENT_BATTERY_REMOVED , NPM13XX_EVENT_SHIPHOLD_PRESS , NPM13XX_EVENT_SHIPHOLD_RELEASE , NPM13XX_EVENT_WATCHDOG_WARN , NPM13XX_EVENT_VBUS_DETECTED , NPM13XX_EVENT_VBUS_REMOVED , NPM13XX_EVENT_GPIO0_EDGE , NPM13XX_EVENT_GPIO1_EDGE , NPM13XX_EVENT_GPIO2_EDGE , NPM13XX_EVENT_GPIO3_EDGE , NPM13XX_EVENT_GPIO4_EDGE , NPM13XX_EVENT_MAX }
```

相关声明：[mfd_npm13xx_event_t](#ga4ac9f47283f10ea1d847cbd0038aad7a)、[NPM13XX_EVENT_CHG_COMPLETED](#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858)、[NPM13XX_EVENT_CHG_ERROR](#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6)、[NPM13XX_EVENT_BATTERY_DETECTED](#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c)、[NPM13XX_EVENT_BATTERY_REMOVED](#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d)、[NPM13XX_EVENT_SHIPHOLD_PRESS](#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646)、[NPM13XX_EVENT_SHIPHOLD_RELEASE](#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5)、[NPM13XX_EVENT_WATCHDOG_WARN](#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7)、[NPM13XX_EVENT_VBUS_DETECTED](#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b)、[NPM13XX_EVENT_VBUS_REMOVED](#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e)、[NPM13XX_EVENT_GPIO0_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8)、[NPM13XX_EVENT_GPIO1_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c)、[NPM13XX_EVENT_GPIO2_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25)、[NPM13XX_EVENT_GPIO3_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b)、[NPM13XX_EVENT_GPIO4_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35)、[NPM13XX_EVENT_MAX](#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.2\_函数（Functions）

<a id="r_gabba0559ce29b71e1ce7065bf5d36f8d8"></a>

```c
int mfd_npm13xx_reg_read_burst (const struct device *dev, uint8_t base, uint8_t offset, void *data, size_t len)
```

相关声明：[mfd_npm13xx_reg_read_burst](#gabba0559ce29b71e1ce7065bf5d36f8d8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 npm13xx 读取多个寄存器（Registers）。

<a id="r_ga154c4c48888ff1587d157b16e38d2584"></a>

```c
int mfd_npm13xx_reg_read (const struct device *dev, uint8_t base, uint8_t offset, uint8_t *data)
```

相关声明：[mfd_npm13xx_reg_read](#ga154c4c48888ff1587d157b16e38d2584)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 npm13xx 读取单个寄存器（Register）。

<a id="r_gac1c7815a4bcfb2262fd4f02d28f2f781"></a>

```c
int mfd_npm13xx_reg_write (const struct device *dev, uint8_t base, uint8_t offset, uint8_t data)
```

相关声明：[mfd_npm13xx_reg_write](#gac1c7815a4bcfb2262fd4f02d28f2f781)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 npm13xx 写入单个寄存器（Register）。

<a id="r_ga2a4ef39c1703b3014d29e6e4412f1eae"></a>

```c
int mfd_npm13xx_reg_write_burst (const struct device *dev, uint8_t base, uint8_t offset, void *data, size_t len)
```

相关声明：[mfd_npm13xx_reg_write_burst](#ga2a4ef39c1703b3014d29e6e4412f1eae)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 npm13xx 写入多个寄存器（Registers）。

<a id="r_ga239cfcef1ab91e3ccc8fb7f39f11dfd2"></a>

```c
int mfd_npm13xx_reg_update (const struct device *dev, uint8_t base, uint8_t offset, uint8_t data, uint8_t mask)
```

相关声明：[mfd_npm13xx_reg_update](#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新 npm13xx 寄存器（Register）中的选定位。

<a id="r_ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9"></a>

```c
int mfd_npm13xx_set_timer (const struct device *dev, uint32_t time_ms)
```

相关声明：[mfd_npm13xx_set_timer](#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入 npm13xx 定时器寄存器（Timer Register）。

<a id="r_ga43c5a5225a0cc2738506d5556ecb06ba"></a>

```c
int mfd_npm13xx_reset (const struct device *dev)
```

相关声明：[mfd_npm13xx_reset](#ga43c5a5225a0cc2738506d5556ecb06ba)、[device](../device_reference/P002_设备对象结构.md)。

npm13xx 完全电源复位（Full Power Reset）。

<a id="r_gaf23758d56ac58f814bc2f093ebfa1282"></a>

```c
int mfd_npm13xx_hibernate (const struct device *dev, uint32_t time_ms)
```

相关声明：[mfd_npm13xx_hibernate](#gaf23758d56ac58f814bc2f093ebfa1282)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

npm13xx 休眠（Hibernate）。

<a id="r_ga3cac4a85cee20242d3a988d9830ea547"></a>

```c
int mfd_npm13xx_add_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm13xx_add_callback](#ga3cac4a85cee20242d3a988d9830ea547)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

添加 npm13xx 事件回调（Event Callback）。

<a id="r_ga35fbc854545b9113f6ec36677491b151"></a>

```c
int mfd_npm13xx_remove_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm13xx_remove_callback](#ga35fbc854545b9113f6ec36677491b151)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

移除 npm13xx 事件回调（Event Callback）。

## 12.3\_详细说明（Detailed Documentation）

<a id="ga4ac9f47283f10ea1d847cbd0038aad7a"></a>

### `mfd_npm13xx_event_t`

```c
enum mfd_npm13xx_event_t
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM13XX_EVENT_CHG_COMPLETED` |  |
| `NPM13XX_EVENT_CHG_ERROR` |  |
| `NPM13XX_EVENT_BATTERY_DETECTED` |  |
| `NPM13XX_EVENT_BATTERY_REMOVED` |  |
| `NPM13XX_EVENT_SHIPHOLD_PRESS` |  |
| `NPM13XX_EVENT_SHIPHOLD_RELEASE` |  |
| `NPM13XX_EVENT_WATCHDOG_WARN` |  |
| `NPM13XX_EVENT_VBUS_DETECTED` |  |
| `NPM13XX_EVENT_VBUS_REMOVED` |  |
| `NPM13XX_EVENT_GPIO0_EDGE` |  |
| `NPM13XX_EVENT_GPIO1_EDGE` |  |
| `NPM13XX_EVENT_GPIO2_EDGE` |  |
| `NPM13XX_EVENT_GPIO3_EDGE` |  |
| `NPM13XX_EVENT_GPIO4_EDGE` |  |
| `NPM13XX_EVENT_MAX` |  |

<a id="ga3cac4a85cee20242d3a988d9830ea547"></a>

### `mfd_npm13xx_add_callback()`

```c
int mfd_npm13xx_add_callback ( const struct device * dev, struct gpio_callback * callback )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

添加 npm13xx 事件回调（Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `callback` | 回调（Callback）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回 `-errno`。

<a id="gaf23758d56ac58f814bc2f093ebfa1282"></a>

### `mfd_npm13xx_hibernate()`

```c
int mfd_npm13xx_hibernate ( const struct device * dev, uint32_t time_ms )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

npm13xx 休眠（Hibernate）。

进入低功耗状态（Low Power State），并在指定时间后唤醒。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `time_ms` | 定时器时间值，单位为毫秒（ms）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 时间值过大。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回负的 `errno` 值，参见 `i2c_write_dt()`。

<a id="ga154c4c48888ff1587d157b16e38d2584"></a>

### `mfd_npm13xx_reg_read()`

```c
int mfd_npm13xx_reg_read ( const struct device * dev, uint8_t base, uint8_t offset, uint8_t * data )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

从 npm13xx 读取单个寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `base` | 寄存器基地址（Register Base Address），即 16 位地址的位 `15..8`。 |
| `offset` | 寄存器偏移地址（Register Offset Address），即 16 位地址的位 `7..0`。 |
| `data` | 指向接收数据缓冲区的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `i2c_write_read_dt()`。

<a id="gabba0559ce29b71e1ce7065bf5d36f8d8"></a>

### `mfd_npm13xx_reg_read_burst()`

```c
int mfd_npm13xx_reg_read_burst ( const struct device * dev, uint8_t base, uint8_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

从 npm13xx 读取多个寄存器（Registers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `base` | 寄存器基地址（Register Base Address），即 16 位地址的位 `15..8`。 |
| `offset` | 寄存器偏移地址（Register Offset Address），即 16 位地址的位 `7..0`。 |
| `data` | 指向接收数据缓冲区的指针。 |
| `len` | 要读取的字节数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `i2c_write_read_dt()`。

<a id="ga239cfcef1ab91e3ccc8fb7f39f11dfd2"></a>

### `mfd_npm13xx_reg_update()`

```c
int mfd_npm13xx_reg_update ( const struct device * dev, uint8_t base, uint8_t offset, uint8_t data, uint8_t mask )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

更新 npm13xx 寄存器（Register）中的选定位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `base` | 寄存器基地址（Register Base Address），即 16 位地址的位 `15..8`。 |
| `offset` | 寄存器偏移地址（Register Offset Address），即 16 位地址的位 `7..0`。 |
| `data` | 要写入的数据。 |
| `mask` | 待修改位的掩码（Bit Mask）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `i2c_write_read_dt()`、`i2c_write_dt()`。

<a id="gac1c7815a4bcfb2262fd4f02d28f2f781"></a>

### `mfd_npm13xx_reg_write()`

```c
int mfd_npm13xx_reg_write ( const struct device * dev, uint8_t base, uint8_t offset, uint8_t data )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

向 npm13xx 写入单个寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `base` | 寄存器基地址（Register Base Address），即 16 位地址的位 `15..8`。 |
| `offset` | 寄存器偏移地址（Register Offset Address），即 16 位地址的位 `7..0`。 |
| `data` | 要写入的数据。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回负的 `errno` 值，参见 `i2c_write_dt()`。

<a id="ga2a4ef39c1703b3014d29e6e4412f1eae"></a>

### `mfd_npm13xx_reg_write_burst()`

```c
int mfd_npm13xx_reg_write_burst ( const struct device * dev, uint8_t base, uint8_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

向 npm13xx 写入多个寄存器（Registers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `base` | 寄存器基地址（Register Base Address），即 16 位地址的位 `15..8`。 |
| `offset` | 首个寄存器的偏移地址（Register Offset Address），即 16 位地址的位 `7..0`。 |
| `data` | 指向要写入的缓冲区（Buffer）的指针。 |
| `len` | 要写入的字节数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回负的 `errno` 值，参见 `i2c_write_dt()`。

<a id="ga35fbc854545b9113f6ec36677491b151"></a>

### `mfd_npm13xx_remove_callback()`

```c
int mfd_npm13xx_remove_callback ( const struct device * dev, struct gpio_callback * callback )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

移除 npm13xx 事件回调（Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `callback` | 回调（Callback）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回 `-errno`。

<a id="ga43c5a5225a0cc2738506d5556ecb06ba"></a>

### `mfd_npm13xx_reset()`

```c
int mfd_npm13xx_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

npm13xx 完全电源复位（Full Power Reset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回负的 `errno` 值，参见 `i2c_write_dt()`。

<a id="ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9"></a>

### `mfd_npm13xx_set_timer()`

```c
int mfd_npm13xx_set_timer ( const struct device * dev, uint32_t time_ms )
```

```c
#include <zephyr/drivers/mfd/npm13xx.h>
```

写入 npm13xx 定时器寄存器（Timer Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | npm13xx 多功能设备（MFD）。 |
| `time_ms` | 定时器时间值，单位为毫秒（ms）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 时间值过大。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回负的 `errno` 值，参见 `i2c_write_dt()`。


## 12.4\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [zephyr/drivers/mfd/npm13xx.h](../api_file_transfer_device_reference/P008_zephyr__drivers__mfd__npm13xx.h_文件参考.md)
- [i2c_write_dt()](../hardware/P305_I2C公共接口.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f)
- [i2c_write_read_dt()](../hardware/P305_I2C公共接口.md#ga301733586dcc2a353bdf149b49df5758)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35"></a>
<a id="gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_串行传输（Serial transport）.md) · [返回大纲](大纲.md) · [下一章](P013_MLX90394 API主题.md)
