---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-15
title: MFD M5PM1 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_MFD M5PM1 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__m5pm1.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

M5Stack M5PM1 电源管理配套微控制器（MCU）接口。

<a id="details"></a>

M5Stack M5PM1 电源管理辅助 MCU 接口（Power Management Companion MCU Interface）。自 4.5 起提供（Since 4.5），版本（Version）0.1.0。M5PM1 是 M5Stack 开发板使用的小型辅助微控制器（Companion Microcontroller），提供电源管理功能，包括电池充电和可切换电源轨（Switchable Rails），以及少量 GPIO 和片上 ADC。此多功能设备驱动（MFD Driver）负责 I2C 传输，并将寄存器访问串行化；同属该设备的 GPIO、ADC 和稳压器驱动（Regulator Drivers）在这些基本操作之上实现各自领域的功能。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_m5pm1_2Eh"></a>

```c
file m5pm1.h
```

相关声明：[m5pm1.h](../api_file_network_device_reference/P019_zephyr__drivers__mfd__m5pm1.h_文件参考.md)。

M5Stack M5PM1多功能设备（MFD）驱动的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.2\_枚举（Enumerations）

<a id="r_ga6fd80cb688aac1023cd6450d83a73567"></a>

```c
enum m5pm1_pin_func { M5PM1_PIN_FUNC_GPIO = 0 , M5PM1_PIN_FUNC_IRQ , M5PM1_PIN_FUNC_ADC , M5PM1_PIN_FUNC_PWM , M5PM1_PIN_FUNC_NEOPIXEL }
```

相关声明：[m5pm1_pin_func](#ga6fd80cb688aac1023cd6450d83a73567)、[M5PM1_PIN_FUNC_GPIO](#gga6fd80cb688aac1023cd6450d83a73567a4f32a038ceb1e138261eb96c5a5beeb7)、[M5PM1_PIN_FUNC_IRQ](#gga6fd80cb688aac1023cd6450d83a73567a77ee83c1164c2f4758024262a746839b)、[M5PM1_PIN_FUNC_ADC](#gga6fd80cb688aac1023cd6450d83a73567acc8f1faa62f4652dcd6ec0d9a11740db)、[M5PM1_PIN_FUNC_PWM](#gga6fd80cb688aac1023cd6450d83a73567ac1e5402b94c064949501a4b719fde33d)、[M5PM1_PIN_FUNC_NEOPIXEL](#gga6fd80cb688aac1023cd6450d83a73567a670d7b4c1f2a184c586a21ad493b7573)。

M5PM1 复用引脚（Multiplexed Pin）的语义功能（Semantic Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga8ffcf8e07c86e9f92359ce7bd10582b2"></a>

```c
int mfd_m5pm1_read_reg (const struct device *dev, uint8_t reg, uint8_t *val)
```

相关声明：[mfd_m5pm1_read_reg](#ga8ffcf8e07c86e9f92359ce7bd10582b2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取一个 8 位 M5PM1 寄存器（Register）。

<a id="r_ga2d0904fa61bedeaf9701b0452569ddb2"></a>

```c
int mfd_m5pm1_write_reg (const struct device *dev, uint8_t reg, uint8_t val)
```

相关声明：[mfd_m5pm1_write_reg](#ga2d0904fa61bedeaf9701b0452569ddb2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入一个 8 位 M5PM1 寄存器（Register）。

<a id="r_ga23c99b53cbff717dc6f754bd007e1d7a"></a>

```c
int mfd_m5pm1_update_reg (const struct device *dev, uint8_t reg, uint8_t mask, uint8_t val)
```

相关声明：[mfd_m5pm1_update_reg](#ga23c99b53cbff717dc6f754bd007e1d7a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对 M5PM1 寄存器的选定位执行读－改－写（Read-modify-write）。

<a id="r_ga126cab6d565399da89293d7fb210354a"></a>

```c
int mfd_m5pm1_toggle_reg (const struct device *dev, uint8_t reg, uint8_t mask)
```

相关声明：[mfd_m5pm1_toggle_reg](#ga126cab6d565399da89293d7fb210354a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

翻转（Toggle）M5PM1 寄存器中的选定位。

<a id="r_gab26e112c7ea5e6349f92d2385e9a7076"></a>

```c
int mfd_m5pm1_burst_read (const struct device *dev, uint8_t reg, uint8_t *buf, size_t len)
```

相关声明：[mfd_m5pm1_burst_read](#gab26e112c7ea5e6349f92d2385e9a7076)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在一次 I2C 事务（Transaction）中读取多个连续的 M5PM1 寄存器。

<a id="r_ga0d1db367f7e6a344ef017c0ddaa878ac"></a>

```c
int mfd_m5pm1_burst_write (const struct device *dev, uint8_t reg, const uint8_t *buf, size_t len)
```

相关声明：[mfd_m5pm1_burst_write](#ga0d1db367f7e6a344ef017c0ddaa878ac)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在一次 I2C 事务（Transaction）中写入多个连续的 M5PM1 寄存器。

<a id="r_gac38c4a90a406952ac7239ccd42fc4439"></a>

```c
int mfd_m5pm1_pin_request (const struct device *dev, const struct device *client, uint8_t pin, enum m5pm1_pin_func func)
```

相关声明：[mfd_m5pm1_pin_request](#gac38c4a90a406952ac7239ccd42fc4439)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[m5pm1_pin_func](#ga6fd80cb688aac1023cd6450d83a73567)。

代表同级驱动（Sibling Driver）为指定功能申请占用引脚（Claim a Pin）。

<a id="r_gad00cc2f47ef55facd42040435bc22fc0"></a>

```c
int mfd_m5pm1_pin_release (const struct device *dev, const struct device *client, uint8_t pin)
```

相关声明：[mfd_m5pm1_pin_release](#gad00cc2f47ef55facd42040435bc22fc0)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

释放此前通过 `mfd_m5pm1_pin_request()` 申请的引脚。

## 15.4\_详细说明（Detailed Documentation）

<a id="ga6fd80cb688aac1023cd6450d83a73567"></a>

### `m5pm1_pin_func`

```c
enum m5pm1_pin_func
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

M5PM1 复用引脚（Multiplexed Pin）的语义功能（Semantic Function）。

每个引脚通过 GPIO_FUNC0/GPIO_FUNC1 中的 2 位字段选择功能。所有引脚都有标准 GPIO 和 IRQ 功能，但“特殊”功能（Special Function，寄存器值 0b11）在各引脚上对应不同外设，因此需要按引脚检查有效性，参见 mfd_m5pm1_pin_request()：

- IO0：NeoPixel 功能（M5PM1_PIN_FUNC_NEOPIXEL）。
- IO1、IO2：ADC 功能（M5PM1_PIN_FUNC_ADC）。
- IO3、IO4：PWM 功能（M5PM1_PIN_FUNC_PWM）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `M5PM1_PIN_FUNC_GPIO` | 标准 GPIO（Standard GPIO），FUNC 字段为 0b00。 |
| `M5PM1_PIN_FUNC_IRQ` | 中断输入（IRQ Input），FUNC 字段为 0b01。 |
| `M5PM1_PIN_FUNC_ADC` | ADC 输入（ADC Input），FUNC 字段为 0b11，仅适用于 IO1/IO2。 |
| `M5PM1_PIN_FUNC_PWM` | PWM 输出（PWM Output），FUNC 字段为 0b11，仅适用于 IO3/IO4。 |
| `M5PM1_PIN_FUNC_NEOPIXEL` | NeoPixel 输出（Output），FUNC 字段为 0b11，仅适用于 IO0。 |

<a id="gab26e112c7ea5e6349f92d2385e9a7076"></a>

### `mfd_m5pm1_burst_read()`

```c
int mfd_m5pm1_burst_read ( const struct device * dev, uint8_t reg, uint8_t * buf, size_t len )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

在一次 I2C 事务（Transaction）中读取多个连续的 M5PM1 寄存器。

使用一次带重复起始条件（Repeated-start）的 I2C 传输，使设备将此次读取视为原子操作（Atomic）。这对于读取低字节时会锁存的寄存器对（Register Pairs）很关键，例如 ADC 采样寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` dev` | M5PM1 多功能设备（MFD Device）。 |
| ` reg` | 要读取的第一个寄存器地址（Register Address）。 |
| `[out] buf` | 用于接收 len 个连续寄存器值（Consecutive Register Values）的缓冲区。 |
| ` len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | I2C 传输错误（Transfer Error），参见 i2c_burst_read_dt()。 |

**说明（Note）**：重要（Important）：M5PM1 仅允许连续读取特定寄存器范围（Register Ranges）；详情请查阅数据手册（Datasheet）。

<a id="ga0d1db367f7e6a344ef017c0ddaa878ac"></a>

### `mfd_m5pm1_burst_write()`

```c
int mfd_m5pm1_burst_write ( const struct device * dev, uint8_t reg, const uint8_t * buf, size_t len )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

在一次 I2C 事务（Transaction）中写入多个连续的 M5PM1 寄存器。

与 mfd_m5pm1_burst_read() 相对应的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `reg` | 要写入的第一个寄存器地址（Register Address）。 |
| `buf` | 保存 len 个连续寄存器值（Consecutive Register Values）的缓冲区。 |
| `len` | 要写入的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | I2C 传输错误（Transfer Error），参见 i2c_burst_write_dt()。 |

**说明（Note）**：重要（Important）：M5PM1 仅允许连续写入特定寄存器范围（Register Ranges）；详情请查阅数据手册（Datasheet）。

<a id="gad00cc2f47ef55facd42040435bc22fc0"></a>

### `mfd_m5pm1_pin_release()`

```c
int mfd_m5pm1_pin_release ( const struct device * dev, const struct device * client, uint8_t pin )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

释放此前通过 `mfd_m5pm1_pin_request()` 申请的引脚。

如果 client 当前拥有 pin，则将引脚功能字段重置为标准 GPIO，并清除所有权（Ownership）。释放不属于 client 的引脚不执行任何操作（No-op）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `client` | 拥有该引脚的设备（Device）。 |
| `pin` | 引脚索引（Pin Index），范围为 0..M5PM1_GPIO_COUNT-1。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，包括无操作（No-op）的情况。 |
| `-EINVAL` | pin 超出范围（Out of Range）。 |
| `-errno` | I2C 传输错误（Transfer Error）。 |

<a id="gac38c4a90a406952ac7239ccd42fc4439"></a>

### `mfd_m5pm1_pin_request()`

```c
int mfd_m5pm1_pin_request ( const struct device * dev, const struct device * client, uint8_t pin, enum m5pm1_pin_func func )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

代表同级驱动（Sibling Driver）为指定功能申请占用引脚（Claim a Pin）。

M5PM1 引脚在 GPIO、ADC、PWM 和 NeoPixel 等多个外设之间复用，同属该设备的各驱动共享 GPIO_FUNC0/GPIO_FUNC1 选择寄存器。本例程集中管理该复用（Mux）：验证 pin 上是否可用 func、编程引脚功能字段，并将 client 记录为引脚所有者（Owner）。一个引脚只能由一个客户端拥有，从而防止开发板意外将同一引脚连接到两个不兼容的使用方（Consumers）。

请求对当前所有者是幂等的（Idempotent）：同一 client 可以再次调用，例如更改自己的功能，而不会出错。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `client` | 请求引脚的设备，用作所有权令牌（Ownership Token）。 |
| `pin` | 引脚索引（Pin Index），范围为 0..M5PM1_GPIO_COUNT-1。 |
| `func` | 要配置的功能（Function），参见 m5pm1_pin_func。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | pin 超出范围（Out of Range）。 |
| `-ENOTSUP` | pin 上不可用 func。 |
| `-EBUSY` | pin 已由另一个客户端（Client）拥有。 |
| `-errno` | I2C 传输错误（Transfer Error）。 |

<a id="ga8ffcf8e07c86e9f92359ce7bd10582b2"></a>

### `mfd_m5pm1_read_reg()`

```c
int mfd_m5pm1_read_reg ( const struct device * dev, uint8_t reg, uint8_t * val )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

读取一个 8 位 M5PM1 寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` dev` | M5PM1 多功能设备（MFD Device）。 |
| ` reg` | 寄存器地址（Register Address）。 |
| `[out] val` | 用于接收寄存器值（Register Value）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | I2C 传输错误（Transfer Error）时，参见 i2c_reg_read_byte_dt()。 |

<a id="ga126cab6d565399da89293d7fb210354a"></a>

### `mfd_m5pm1_toggle_reg()`

```c
int mfd_m5pm1_toggle_reg ( const struct device * dev, uint8_t reg, uint8_t mask )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

翻转（Toggle）M5PM1 寄存器中的选定位。

对 reg 执行原子的、受互斥量保护的读改写操作（Read-modify-write），翻转 mask 选中的位。在读写全过程持有锁，使该翻转操作相对于其他 `mfd_m5pm1_*()` 访问接口具有原子性（Atomicity）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `reg` | 寄存器地址（Register Address）。 |
| `mask` | 要翻转的位的位掩码（Bitmask）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | I2C 传输错误（Transfer Error）。 |

<a id="ga23c99b53cbff717dc6f754bd007e1d7a"></a>

### `mfd_m5pm1_update_reg()`

```c
int mfd_m5pm1_update_reg ( const struct device * dev, uint8_t reg, uint8_t mask, uint8_t val )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

对 M5PM1 寄存器的选定位执行读－改－写（Read-modify-write）。

对 reg 执行原子的、受互斥量保护的读改写操作（Read-modify-write），将 mask 选中的位替换为 val 中对应的位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `reg` | 寄存器地址（Register Address）。 |
| `mask` | 要更新的位的位掩码（Bitmask）。 |
| `val` | mask 选中位的新值（New Value），其他位忽略。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | I2C 传输错误（Transfer Error），参见 i2c_reg_update_byte_dt()。 |

<a id="ga2d0904fa61bedeaf9701b0452569ddb2"></a>

### `mfd_m5pm1_write_reg()`

```c
int mfd_m5pm1_write_reg ( const struct device * dev, uint8_t reg, uint8_t val )
```

```c
#include <zephyr/drivers/mfd/m5pm1.h>
```

写入一个 8 位 M5PM1 寄存器（Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | M5PM1 多功能设备（MFD Device）。 |
| `reg` | 寄存器地址（Register Address）。 |
| `val` | 要写入的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功（Success）时。 |
| `-errno` | I2C 传输错误（Transfer Error），参见 i2c_reg_write_byte_dt()。 |


## 15.5\_原页交叉引用（Cross References）

- [m5pm1.h](../api_file_network_device_reference/P019_zephyr__drivers__mfd__m5pm1.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i2c_burst_read_dt()](../hardware/P305_I2C公共接口.md#ga9d2654bbf80f4d253532adaec8566fc3)
- [i2c_burst_write_dt()](../hardware/P305_I2C公共接口.md#ga0e590c99d3b9c1a7dd8174a318ee5a7d)
- [i2c_reg_read_byte_dt()](../hardware/P305_I2C公共接口.md#ga6fc14d75c41b8c8d9dd2f77c59533640)
- [i2c_reg_update_byte_dt()](../hardware/P305_I2C公共接口.md#ga5000c5e49eabe712b5fd532d3842c3f5)
- [i2c_reg_write_byte_dt()](../hardware/P305_I2C公共接口.md#ga664cd76bf4fae0dba848f5c284699a04)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6fd80cb688aac1023cd6450d83a73567a4f32a038ceb1e138261eb96c5a5beeb7"></a>
<a id="gga6fd80cb688aac1023cd6450d83a73567a77ee83c1164c2f4758024262a746839b"></a>
<a id="gga6fd80cb688aac1023cd6450d83a73567acc8f1faa62f4652dcd6ec0d9a11740db"></a>
<a id="gga6fd80cb688aac1023cd6450d83a73567ac1e5402b94c064949501a4b719fde33d"></a>
<a id="gga6fd80cb688aac1023cd6450d83a73567a670d7b4c1f2a184c586a21ad493b7573"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_LIS2DUX12 API主题.md) · [返回大纲](大纲.md) · [下一章](P016_点对点协议二层_驱动支持函数（PPP L2_driver Support Functions）.md)
