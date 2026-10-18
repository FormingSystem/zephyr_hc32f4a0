---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-18
title: 1-Wire 网络层（Network layer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_1-Wire 网络层（Network layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

1-Wire 网络层（Network layer）

<a id="details"></a>

1-Wire 网络层（Network layer）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_w1_5From"></a>

```c
struct w1_rom
```

相关声明：[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

W1_rom结构。

<a id="r_w1_5Fslave_5Fconfig"></a>

```c
struct w1_slave_config
```

相关声明：[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

节点专用的单总线（1-Wire）配置结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_ga909502b9b18c15a9ab0da8d3605e8c37"></a>

```c
#define W1_SEARCH_ALL_FAMILIES 0x00
```

相关声明：[W1_SEARCH_ALL_FAMILIES](#ga909502b9b18c15a9ab0da8d3605e8c37)。

可将此标志传给搜索操作，表示不按家族 ID（Family ID）过滤。

<a id="r_ga17770ecebad7170e9004afd9a7735c73"></a>

```c
#define W1_ROM_INIT_ZERO
```

相关声明：[W1_ROM_INIT_ZERO](#ga17770ecebad7170e9004afd9a7735c73)。

将 `w1_rom` 结构体的所有成员初始化为零。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.3\_类型定义（Typedefs）

<a id="r_ga2f5540f2a86fd55edcd7a8ffecbfd786"></a>

```c
typedef void(* w1_search_callback_t) (struct w1_rom rom, void *user_data)
```

相关声明：[w1_search_callback_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

定义搜索操作的应用程序回调处理函数签名。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_ga93abefbd0e7067db474e6480301a0c4c"></a>

```c
int w1_read_rom (const struct device *dev, struct w1_rom *rom)
```

相关声明：[w1_read_rom](#ga93abefbd0e7067db474e6480301a0c4c)、[device](../device_reference/P002_设备对象结构.md)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

读取外设的 64 位 ROM。

<a id="r_ga53f34d64504498dbb194bc2119727908"></a>

```c
int w1_match_rom (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_match_rom](#ga53f34d64504498dbb194bc2119727908)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

通过广播选定的 ROM 代码选择特定从设备。

<a id="r_ga67c815bb99b75c862a483d4f8556b24a"></a>

```c
int w1_resume_command (const struct device *dev)
```

相关声明：[w1_resume_command](#ga67c815bb99b75c862a483d4f8556b24a)、[device](../device_reference/P002_设备对象结构.md)。

选择上次通过匹配 ROM（Match ROM）或搜索 ROM（Search ROM）命令寻址的从设备。

<a id="r_gaba2be4e87ff472e90b705dbd73b913de"></a>

```c
int w1_skip_rom (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_skip_rom](#gaba2be4e87ff472e90b705dbd73b913de)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

选择所有从设备，不考虑 ROM。

<a id="r_gaa0acc88fe02535a3d512b866b6d34b8a"></a>

```c
int w1_reset_select (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_reset_select](#gaa0acc88fe02535a3d512b866b6d34b8a)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

单从设备（Single drop）配置使用跳过选择（Skip Select）命令，否则使用匹配 ROM（Match ROM）命令。

<a id="r_ga1cf8c016ac66c3970f72fa1f409fa680"></a>

```c
int w1_write_read (const struct device *dev, const struct w1_slave_config *config, const uint8_t *write_buf, size_t write_len, uint8_t *read_buf, size_t read_len)
```

相关声明：[w1_write_read](#ga1cf8c016ac66c3970f72fa1f409fa680)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 ROM 匹配的 1-Wire 从设备先写入再读取数据。

<a id="r_ga19533f445029a69aac7d4ca5a7aeedcd"></a>

```c
int w1_search_bus (const struct device *dev, uint8_t command, uint8_t family, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_bus](#ga19533f445029a69aac7d4ca5a7aeedcd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[w1_search_callback_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索总线上的 1-Wire 从设备。

<a id="r_ga024af0ee5018d7078808cc0a544cfd26"></a>

```c
static int w1_search_rom (const struct device *dev, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_rom](#ga024af0ee5018d7078808cc0a544cfd26)、[device](../device_reference/P002_设备对象结构.md)、[w1_search_callback_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索总线上的 1-Wire 从设备。

<a id="r_ga0f510bd3720e54b4eeb4e368934db7f0"></a>

```c
static int w1_search_alarm (const struct device *dev, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_alarm](#ga0f510bd3720e54b4eeb4e368934db7f0)、[device](../device_reference/P002_设备对象结构.md)、[w1_search_callback_t](#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索具有有效告警的 1-Wire 从设备。

<a id="r_ga178a88d0c585d5df0405aadde3ea9178"></a>

```c
static uint64_t w1_rom_to_uint64 (const struct w1_rom *rom)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[w1_rom_to_uint64](#ga178a88d0c585d5df0405aadde3ea9178)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `w1_rom` 结构体转换为 `uint64_t` 的函数。

<a id="r_ga6e4dba051a6b29c974e499db17315034"></a>

```c
static void w1_uint64_to_rom (const uint64_t rom64, struct w1_rom *rom)
```

相关声明：[w1_uint64_to_rom](#ga6e4dba051a6b29c974e499db17315034)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `uint64_t` 写入 `struct w1_rom` 指针所指对象的函数。

<a id="r_ga350a384a6040d1fbb86bfb804013ade3"></a>

```c
static uint8_t w1_crc8 (const uint8_t *src, size_t len)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[w1_crc8](#ga350a384a6040d1fbb86bfb804013ade3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

按 1-Wire 规范计算 CRC-8 校验值。

<a id="r_ga5635f79a54a2e5b96c8b7ca9a8ab8366"></a>

```c
static uint16_t w1_crc16 (const uint16_t seed, const uint8_t *src, const size_t len)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[w1_crc16](#ga5635f79a54a2e5b96c8b7ca9a8ab8366)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

计算 1-Wire 变体的 CRC-16。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.5\_1-Wire ROM 命令（Commands）

<a id="r_ga9792cb2093e911a4722b7fa9457093dc"></a>

```c
#define W1_CMD_SKIP_ROM 0xCC
```

相关声明：[W1_CMD_SKIP_ROM](#ga9792cb2093e911a4722b7fa9457093dc)。

此命令允许总线主机在不提供 ROM 代码的情况下读取从设备。

<a id="r_gae97f7ecda699ccf9b63030f2af632bc8"></a>

```c
#define W1_CMD_MATCH_ROM 0x55
```

相关声明：[W1_CMD_MATCH_ROM](#gae97f7ecda699ccf9b63030f2af632bc8)。

此命令允许总线主机通过提供 ROM 代码寻址特定从设备。

<a id="r_ga31230559122289c179f01e09e3847830"></a>

```c
#define W1_CMD_RESUME 0xA5
```

相关声明：[W1_CMD_RESUME](#ga31230559122289c179f01e09e3847830)。

此命令允许总线主机从之前中断的位置继续读出。

<a id="r_ga9e1a9a38889bf165370670c28778028b"></a>

```c
#define W1_CMD_READ_ROM 0x33
```

相关声明：[W1_CMD_READ_ROM](#ga9e1a9a38889bf165370670c28778028b)。

此命令允许总线主机从单个从设备读取 ROM 代码。

<a id="r_ga57f17871edab0b771f2f664bf9bafb79"></a>

```c
#define W1_CMD_SEARCH_ROM 0xF0
```

相关声明：[W1_CMD_SEARCH_ROM](#ga57f17871edab0b771f2f664bf9bafb79)。

此命令允许总线主机发现总线上所有从设备的地址，即 ROM 代码。

<a id="r_gafc7a257428c69bb4549c6cd05a928957"></a>

```c
#define W1_CMD_SEARCH_ALARM 0xEC
```

相关声明：[W1_CMD_SEARCH_ALARM](#gafc7a257428c69bb4549c6cd05a928957)。

此命令允许总线主机识别哪些设备出现了告警条件（Alarm condition）。

<a id="r_ga8b61b2308f2681801894f24ea2c95b12"></a>

```c
#define W1_CMD_OVERDRIVE_SKIP_ROM 0x3C
```

相关声明：[W1_CMD_OVERDRIVE_SKIP_ROM](#ga8b61b2308f2681801894f24ea2c95b12)。

此命令允许总线主机寻址总线上所有设备，然后将它们切换为超速模式（Overdrive speed）。

<a id="r_ga3e3f9fa70074188a2e489f34555b519b"></a>

```c
#define W1_CMD_OVERDRIVE_MATCH_ROM 0x69
```

相关声明：[W1_CMD_OVERDRIVE_MATCH_ROM](#ga3e3f9fa70074188a2e489f34555b519b)。

此命令允许总线主机寻址特定设备，并将其切换为超速模式。

## 18.6\_CRC 定义（Defines）

<a id="r_gaa4ad8d9a3791fbca6c99d49b9793a002"></a>

```c
#define W1_CRC8_SEED 0x00
```

相关声明：[W1_CRC8_SEED](#gaa4ad8d9a3791fbca6c99d49b9793a002)。

计算 1-Wire 8 位 CRC 使用的初始值（Seed value）。

<a id="r_gabe56ffbe20c2ba7e0a5c87c8e36c45e5"></a>

```c
#define W1_CRC8_POLYNOMIAL 0x8C
```

相关声明：[W1_CRC8_POLYNOMIAL](#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)。

计算 1-Wire 8 位 CRC 使用的多项式（Polynomial）。

<a id="r_ga324f30f17c6cd1b33650b58055a3a57f"></a>

```c
#define W1_CRC16_SEED 0x0000
```

相关声明：[W1_CRC16_SEED](#ga324f30f17c6cd1b33650b58055a3a57f)。

计算 1-Wire 16 位 CRC 使用的初始值。

<a id="r_gab94362fbf4eec5f115f93fc8976cff0d"></a>

```c
#define W1_CRC16_POLYNOMIAL 0xa001
```

相关声明：[W1_CRC16_POLYNOMIAL](#gab94362fbf4eec5f115f93fc8976cff0d)。

计算 1-Wire 16 位 CRC 使用的多项式。

## 18.7\_详细说明（Detailed Documentation）

<a id="gae97f7ecda699ccf9b63030f2af632bc8"></a>

### `W1_CMD_MATCH_ROM`

```c
#define W1_CMD_MATCH_ROM 0x55
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机通过提供 ROM 代码寻址特定从设备。

<a id="ga3e3f9fa70074188a2e489f34555b519b"></a>

### `W1_CMD_OVERDRIVE_MATCH_ROM`

```c
#define W1_CMD_OVERDRIVE_MATCH_ROM 0x69
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机寻址特定设备，并将其切换为超速模式。

<a id="ga8b61b2308f2681801894f24ea2c95b12"></a>

### `W1_CMD_OVERDRIVE_SKIP_ROM`

```c
#define W1_CMD_OVERDRIVE_SKIP_ROM 0x3C
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机寻址总线上所有设备，然后将它们切换为超速模式（Overdrive speed）。

<a id="ga9e1a9a38889bf165370670c28778028b"></a>

### `W1_CMD_READ_ROM`

```c
#define W1_CMD_READ_ROM 0x33
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机从单个从设备读取 ROM 代码。

仅当总线上只有一个从设备（Slave Device）时，才应使用此命令。

<a id="ga31230559122289c179f01e09e3847830"></a>

### `W1_CMD_RESUME`

```c
#define W1_CMD_RESUME 0xA5
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机从之前中断的位置继续读出。

<a id="gafc7a257428c69bb4549c6cd05a928957"></a>

### `W1_CMD_SEARCH_ALARM`

```c
#define W1_CMD_SEARCH_ALARM 0xEC
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机识别哪些设备出现了告警条件（Alarm condition）。

<a id="ga57f17871edab0b771f2f664bf9bafb79"></a>

### `W1_CMD_SEARCH_ROM`

```c
#define W1_CMD_SEARCH_ROM 0xF0
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机发现总线上所有从设备的地址，即 ROM 代码。

<a id="ga9792cb2093e911a4722b7fa9457093dc"></a>

### `W1_CMD_SKIP_ROM`

```c
#define W1_CMD_SKIP_ROM 0xCC
```

```c
#include <zephyr/drivers/w1.h>
```

此命令允许总线主机在不提供 ROM 代码的情况下读取从设备。

<a id="gab94362fbf4eec5f115f93fc8976cff0d"></a>

### `W1_CRC16_POLYNOMIAL`

```c
#define W1_CRC16_POLYNOMIAL 0xa001
```

```c
#include <zephyr/drivers/w1.h>
```

计算 1-Wire 16 位 CRC 使用的多项式。

<a id="ga324f30f17c6cd1b33650b58055a3a57f"></a>

### `W1_CRC16_SEED`

```c
#define W1_CRC16_SEED 0x0000
```

```c
#include <zephyr/drivers/w1.h>
```

计算 1-Wire 16 位 CRC 使用的初始值。

<a id="gabe56ffbe20c2ba7e0a5c87c8e36c45e5"></a>

### `W1_CRC8_POLYNOMIAL`

```c
#define W1_CRC8_POLYNOMIAL 0x8C
```

```c
#include <zephyr/drivers/w1.h>
```

计算 1-Wire 8 位 CRC 使用的多项式（Polynomial）。

<a id="gaa4ad8d9a3791fbca6c99d49b9793a002"></a>

### `W1_CRC8_SEED`

```c
#define W1_CRC8_SEED 0x00
```

```c
#include <zephyr/drivers/w1.h>
```

计算 1-Wire 8 位 CRC 使用的初始值（Seed value）。

<a id="ga17770ecebad7170e9004afd9a7735c73"></a>

### `W1_ROM_INIT_ZERO`

```c
#define W1_ROM_INIT_ZERO
```

```c
#include <zephyr/drivers/w1.h>
```

展开值（Value）：

```c
{                                                       \
        .family = 0, .serial = { 0 }, .crc = 0,         \
}
```

将 `w1_rom` 结构体的所有成员初始化为零。

<a id="ga909502b9b18c15a9ab0da8d3605e8c37"></a>

### `W1_SEARCH_ALL_FAMILIES`

```c
#define W1_SEARCH_ALL_FAMILIES 0x00
```

```c
#include <zephyr/drivers/w1.h>
```

可将此标志传给搜索操作，表示不按家族 ID（Family ID）过滤。

<a id="ga2f5540f2a86fd55edcd7a8ffecbfd786"></a>

### `w1_search_callback_t`

```c
typedef void(* w1_search_callback_t) (struct w1_rom rom, void *user_data)
```

```c
#include <zephyr/drivers/w1.h>
```

定义搜索操作的应用程序回调处理函数签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rom` | found：找到的从设备的 ROM。 |
| `user_data` | 传给 w1_search_bus() 调用的用户数据（User Data）。 |

<a id="ga5635f79a54a2e5b96c8b7ca9a8ab8366"></a>

### `w1_crc16()`

```c
uint16_t w1_crc16 ( const uint16_t seed, const uint8_t * src, const size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

计算 1-Wire 变体的 CRC-16。

16 位 1-Wire 循环冗余校验（CRC）变体采用反射形式多项式（Reflected Polynomial）X^16 + X^15 + X^2 + 1，初始值为 0x0000。另请参阅应用笔记 27（APPLICATION NOTE 27）《理解并使用 Maxim 1-Wire 与 iButton 产品的循环冗余校验》（Understanding and Using Cyclic Redundancy Checks with Maxim 1-Wire and iButton Products）：https://www.analog.com/en/resources/technical-articles/understanding-and-using-cyclic-redundancy-checks-with-maxim-1wire-and-ibutton-products.html 。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` seed` | CRC 初始值（Init Value），通常设为 0x0000。 |
| `[in] src` | 用于计算的输入字节。 |
| ` len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回值（Returns）：计算得到的 CRC16 值。

<a id="ga350a384a6040d1fbb86bfb804013ade3"></a>

### `w1_crc8()`

```c
uint8_t w1_crc8 ( const uint8_t * src, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

按 1-Wire 规范计算 CRC-8 校验值。

1-Wire CRC8 变体使用多项式 0x31，初始值为 0x00。此 CRC 用于检查唯一 56 位 ROM 的正确性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] src` | 用于计算的输入字节。 |
| ` len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回值（Returns）：计算得到的 CRC8 值。

<a id="ga53f34d64504498dbb194bc2119727908"></a>

### `w1_match_rom()`

```c
int w1_match_rom ( const struct device * dev, const struct w1_slave_config * config )
```

```c
#include <zephyr/drivers/w1.h>
```

通过广播选定的 ROM 代码选择特定从设备。

此例程允许 1-Wire 总线主设备（Master）按唯一 ROM 选择从设备（Slave），使下一条命令仅发给选定的单个从设备。

此命令仅在多点总线环境（Multidrop Environments）中必需，否则可发送 Skip ROM 命令。选择从设备后，为减少通信开销，可以使用 resume 命令替代此命令与选定从设备通信。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[in] config` | 指向从设备专用 1-Wire 配置（Slave-specific Config）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga93abefbd0e7067db474e6480301a0c4c"></a>

### `w1_read_rom()`

```c
int w1_read_rom ( const struct device * dev, struct w1_rom * rom )
```

```c
#include <zephyr/drivers/w1.h>
```

读取外设的 64 位 ROM。

此过程允许 1-Wire 总线主设备（Master）不执行 Search ROM 过程，直接读取外设的 64 位 ROM。仅当总线上最多连接一个外设时可用；否则发生数据冲突（Data Collisions），读到错误的 ROM。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[out] rom` | 指向 ROM 结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa0acc88fe02535a3d512b866b6d34b8a"></a>

### `w1_reset_select()`

```c
int w1_reset_select ( const struct device * dev, const struct w1_slave_config * config )
```

```c
#include <zephyr/drivers/w1.h>
```

单从设备（Single drop）配置使用跳过选择（Skip Select）命令，否则使用匹配 ROM（Match ROM）命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[in] config` | 指向从设备专用 1-Wire 配置（Slave-specific Config）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga67c815bb99b75c862a483d4f8556b24a"></a>

### `w1_resume_command()`

```c
int w1_resume_command ( const struct device * dev)
```

```c
#include <zephyr/drivers/w1.h>
```

选择上次通过匹配 ROM（Match ROM）或搜索 ROM（Search ROM）命令寻址的从设备。

此例程允许 1-Wire 总线主设备重新选择先前已通过 Match ROM 或 Search ROM 命令寻址的从设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga178a88d0c585d5df0405aadde3ea9178"></a>

### `w1_rom_to_uint64()`

```c
uint64_t w1_rom_to_uint64 ( const struct w1_rom * rom)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

将 `w1_rom` 结构体转换为 `uint64_t` 的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] rom` | 指向 ROM 结构体的指针。 |

**返回（Returns）**：返回值（Returns）：转换为主机字节序（Host Endianness）无符号整数的 ROM。

<a id="ga0f510bd3720e54b4eeb4e368934db7f0"></a>

### `w1_search_alarm()`

```c
int w1_search_alarm ( const struct device * dev, w1_search_callback_t callback, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

搜索具有有效告警的 1-Wire 从设备。

此例程搜索总线上当前有活动告警（Active Alarm）的 1-Wire 从设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` callback` | 针对每个找到的从设备调用的应用回调处理函数（Application Callback Handler）。 |
| `[in] user_data` | 传给应用回调处理函数的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：找到的从设备数量；失败返回负 errno。

<a id="ga19533f445029a69aac7d4ca5a7aeedcd"></a>

### `w1_search_bus()`

```c
int w1_search_bus ( const struct device * dev, uint8_t command, uint8_t family, w1_search_callback_t callback, void * user_data )
```

```c
#include <zephyr/drivers/w1.h>
```

搜索总线上的 1-Wire 从设备。

此函数搜索 1-Wire 总线上的从设备，可搜索全部从设备或仅搜索处于活动告警状态（Active Alarm State）的从设备。传入回调时，对每个找到的从设备调用该回调。

算法主要遵循 https://www.analog.com/en/resources/app-notes/1wire-search-algorithm.html 中的建议。

注意：不支持按器件族（Families）过滤。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` command` | 可以为 W1_CMD_SEARCH_ALARM 或 W1_CMD_SEARCH_ROM。 |
| ` family` | W1_SEARCH_ALL_FAMILIES 搜索所有器件族（Families）；尚不支持按特定器件族过滤。 |
| ` callback` | 针对每个找到的从设备调用的应用回调处理函数（Application Callback Handler）。 |
| `[in] user_data` | 传给应用回调处理函数的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：找到的从设备数量；失败返回负 errno。

<a id="ga024af0ee5018d7078808cc0a544cfd26"></a>

### `w1_search_rom()`

```c
int w1_search_rom ( const struct device * dev, w1_search_callback_t callback, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

搜索总线上的 1-Wire 从设备。

此例程通过扫描唯一的 64 位注册号（Registration Number）发现总线上的未知从设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| ` callback` | 针对每个找到的从设备调用的应用回调处理函数（Application Callback Handler）。 |
| `[in] user_data` | 传给应用回调处理函数的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：找到的从设备数量；失败返回负 errno。

<a id="gaba2be4e87ff472e90b705dbd73b913de"></a>

### `w1_skip_rom()`

```c
int w1_skip_rom ( const struct device * dev, const struct w1_slave_config * config )
```

```c
#include <zephyr/drivers/w1.h>
```

选择所有从设备，不考虑 ROM。

此例程设置总线从设备，使其准备接收命令。通常在总线上只有一个外设时使用，以避免 Match ROM 命令的开销；也可用于同时向所有从设备写入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[in] config` | 指向从设备专用 1-Wire 配置（Slave-specific Config）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga6e4dba051a6b29c974e499db17315034"></a>

### `w1_uint64_to_rom()`

```c
void w1_uint64_to_rom ( const uint64_t rom64, struct w1_rom * rom )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/w1.h>
```

将 `uint64_t` 写入 `struct w1_rom` 指针所指对象的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` rom64` | 以主机字节序（Host Endianness）表示 ROM 的 64 位无符号整数。 |
| `[out] rom` | ROM 结构体指针。 |

<a id="ga1cf8c016ac66c3970f72fa1f409fa680"></a>

### `w1_write_read()`

```c
int w1_write_read ( const struct device * dev, const struct w1_slave_config * config, const uint8_t * write_buf, size_t write_len, uint8_t * read_buf, size_t read_len )
```

```c
#include <zephyr/drivers/w1.h>
```

向 ROM 匹配的 1-Wire 从设备先写入再读取数据。

此例程使用 w1_reset_select 选择给定 ROM，然后写入给定数据并读回从设备响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `[in] config` | 指向从设备专用 1-Wire 配置（Slave-specific Config）的指针。 |
| `[in] write_buf` | 指向待写入数据的指针。 |
| ` write_len` | 要写入的字节数。 |
| `[out] read_buf` | 指向所读数据存储区的指针。 |
| ` read_len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 没有从设备响应复位（Reset）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 18.8\_原页交叉引用（Cross References）

- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/drivers/w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)
- [https://www.analog.com/en/resources/technical-articles/understanding-and-using-cyclic-redundancy-checks-with-maxim-1wire-and-ibutton-products.html](https://www.analog.com/en/resources/technical-articles/understanding-and-using-cyclic-redundancy-checks-with-maxim-1wire-and-ibutton-products.html)
- [https://www.analog.com/en/resources/app-notes/1wire-search-algorithm.html](https://www.analog.com/en/resources/app-notes/1wire-search-algorithm.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_用户模式 API（User Mode APIs）.md) · [返回大纲](大纲.md) · [下一章](P019_Xen 授权表（Grant tables）.md)
