---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-29
title: zephyr__drivers__w1.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/w1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_drivers\_\_w1.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单总线（1-Wire）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/crc.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/syscalls/w1.h>
```

查看此文件的源码。

单总线（1-Wire）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 29.1\_数据结构（Data Structures）

<a id="r_w1_5Fmaster_5Fconfig"></a>

```c
struct w1_master_config
```

相关声明：[w1_master_config](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md)。

全部单总线（1-Wire）主机实现共用的配置。

<a id="r_w1_5Fmaster_5Fdata"></a>

```c
struct w1_master_data
```

相关声明：[w1_master_data](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md)。

全部单总线（1-Wire）主机实现共用的数据。

<a id="r_w1_5Fdriver_5Fapi"></a>

```c
struct w1_driver_api
```

相关声明：[w1_driver_api](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md)。

驱动操作（Driver Operations）：单总线（1-Wire）驱动操作。

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

## 29.2\_宏定义（Macros）

<a id="r_ga909502b9b18c15a9ab0da8d3605e8c37"></a>

```c
#define W1_SEARCH_ALL_FAMILIES 0x00
```

相关声明：[W1_SEARCH_ALL_FAMILIES](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga909502b9b18c15a9ab0da8d3605e8c37)。

可将此标志传给搜索操作，表示不按家族 ID（Family ID）过滤。

<a id="r_ga17770ecebad7170e9004afd9a7735c73"></a>

```c
#define W1_ROM_INIT_ZERO
```

相关声明：[W1_ROM_INIT_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga17770ecebad7170e9004afd9a7735c73)。

将 `w1_rom` 结构体的所有成员初始化为零。

<a id="define-members-0"></a>

### 1-Wire ROM 命令（Commands）

<a id="r_ga9792cb2093e911a4722b7fa9457093dc"></a>

```c
#define W1_CMD_SKIP_ROM 0xCC
```

相关声明：[W1_CMD_SKIP_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga9792cb2093e911a4722b7fa9457093dc)。

此命令允许总线主机在不提供 ROM 代码的情况下读取从设备。

<a id="r_gae97f7ecda699ccf9b63030f2af632bc8"></a>

```c
#define W1_CMD_MATCH_ROM 0x55
```

相关声明：[W1_CMD_MATCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gae97f7ecda699ccf9b63030f2af632bc8)。

此命令允许总线主机通过提供 ROM 代码寻址特定从设备。

<a id="r_ga31230559122289c179f01e09e3847830"></a>

```c
#define W1_CMD_RESUME 0xA5
```

相关声明：[W1_CMD_RESUME](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga31230559122289c179f01e09e3847830)。

此命令允许总线主机从之前中断的位置继续读出。

<a id="r_ga9e1a9a38889bf165370670c28778028b"></a>

```c
#define W1_CMD_READ_ROM 0x33
```

相关声明：[W1_CMD_READ_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga9e1a9a38889bf165370670c28778028b)。

此命令允许总线主机从单个从设备读取 ROM 代码。

<a id="r_ga57f17871edab0b771f2f664bf9bafb79"></a>

```c
#define W1_CMD_SEARCH_ROM 0xF0
```

相关声明：[W1_CMD_SEARCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga57f17871edab0b771f2f664bf9bafb79)。

此命令允许总线主机发现总线上所有从设备的地址，即 ROM 代码。

<a id="r_gafc7a257428c69bb4549c6cd05a928957"></a>

```c
#define W1_CMD_SEARCH_ALARM 0xEC
```

相关声明：[W1_CMD_SEARCH_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gafc7a257428c69bb4549c6cd05a928957)。

此命令允许总线主机识别哪些设备出现了告警条件（Alarm condition）。

<a id="r_ga8b61b2308f2681801894f24ea2c95b12"></a>

```c
#define W1_CMD_OVERDRIVE_SKIP_ROM 0x3C
```

相关声明：[W1_CMD_OVERDRIVE_SKIP_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga8b61b2308f2681801894f24ea2c95b12)。

此命令允许总线主机寻址总线上所有设备，然后将它们切换为超速模式（Overdrive speed）。

<a id="r_ga3e3f9fa70074188a2e489f34555b519b"></a>

```c
#define W1_CMD_OVERDRIVE_MATCH_ROM 0x69
```

相关声明：[W1_CMD_OVERDRIVE_MATCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga3e3f9fa70074188a2e489f34555b519b)。

此命令允许总线主机寻址特定设备，并将其切换为超速模式。

<a id="define-members-1"></a>

### CRC 定义（Defines）

<a id="r_gaa4ad8d9a3791fbca6c99d49b9793a002"></a>

```c
#define W1_CRC8_SEED 0x00
```

相关声明：[W1_CRC8_SEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa4ad8d9a3791fbca6c99d49b9793a002)。

计算 1-Wire 8 位 CRC 使用的初始值（Seed value）。

<a id="r_gabe56ffbe20c2ba7e0a5c87c8e36c45e5"></a>

```c
#define W1_CRC8_POLYNOMIAL 0x8C
```

相关声明：[W1_CRC8_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)。

计算 1-Wire 8 位 CRC 使用的多项式（Polynomial）。

<a id="r_ga324f30f17c6cd1b33650b58055a3a57f"></a>

```c
#define W1_CRC16_SEED 0x0000
```

相关声明：[W1_CRC16_SEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga324f30f17c6cd1b33650b58055a3a57f)。

计算 1-Wire 16 位 CRC 使用的初始值。

<a id="r_gab94362fbf4eec5f115f93fc8976cff0d"></a>

```c
#define W1_CRC16_POLYNOMIAL 0xa001
```

相关声明：[W1_CRC16_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gab94362fbf4eec5f115f93fc8976cff0d)。

计算 1-Wire 16 位 CRC 使用的多项式。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 29.3\_类型定义（Typedefs）

<a id="r_ga87232322cd487772d377aa0a8e9e5bfc"></a>

```c
typedef int(* w1_reset_bus_t) (const struct device *dev)
```

相关声明：[w1_reset_bus_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga87232322cd487772d377aa0a8e9e5bfc)、[device](../device_reference/P002_设备对象结构.md)。

复位单总线（1-Wire），使从设备准备通信。

<a id="r_gabb495014dd7b9583009b34d9eba02ddc"></a>

```c
typedef int(* w1_read_bit_t) (const struct device *dev)
```

相关声明：[w1_read_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gabb495014dd7b9583009b34d9eba02ddc)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个位。

<a id="r_ga126e501ef9a74cbc3c375ca64025cdbc"></a>

```c
typedef int(* w1_write_bit_t) (const struct device *dev, bool bit)
```

相关声明：[w1_write_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga126e501ef9a74cbc3c375ca64025cdbc)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向 1-Wire 总线写入单个位。

<a id="r_ga861af0744a5f102558294422de50f6ae"></a>

```c
typedef int(* w1_read_byte_t) (const struct device *dev)
```

相关声明：[w1_read_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga861af0744a5f102558294422de50f6ae)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个字节。

<a id="r_ga18924f833820d5f70d73ab33de6615dd"></a>

```c
typedef int(* w1_write_byte_t) (const struct device *dev, const uint8_t byte)
```

相关声明：[w1_write_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga18924f833820d5f70d73ab33de6615dd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入单个字节。

<a id="r_gae2673a21841ad196af69e5b4e6769ea8"></a>

```c
typedef int(* w1_read_block_t) (const struct device *dev, uint8_t *buffer, size_t len)
```

相关声明：[w1_read_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gae2673a21841ad196af69e5b4e6769ea8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 1-Wire 总线读取一个数据块。

<a id="r_gafbbba20705697154d29a91ac94cc3747"></a>

```c
typedef int(* w1_write_block_t) (const struct device *dev, const uint8_t *buffer, size_t len)
```

相关声明：[w1_write_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gafbbba20705697154d29a91ac94cc3747)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入一个数据块。

<a id="r_ga5d3ee84858e35cdac923a6238a22e9a2"></a>

```c
typedef size_t(* w1_get_slave_count_t) (const struct device *dev)
```

相关声明：[w1_get_slave_count_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga5d3ee84858e35cdac923a6238a22e9a2)、[device](../device_reference/P002_设备对象结构.md)。

获取总线上的从设备数量。

<a id="r_gab831da9314fce3e6ec10526ca5224515"></a>

```c
typedef int(* w1_configure_t) (const struct device *dev, enum w1_settings_type type, uint32_t value)
```

相关声明：[w1_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gab831da9314fce3e6ec10526ca5224515)、[device](../device_reference/P002_设备对象结构.md)、[w1_settings_type](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga382989ef707709b5d26c40a394833612)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 1-Wire 主机的参数。

<a id="r_gaa64e8b894df8a3a44f3b91ea647cc0c1"></a>

```c
typedef int(* w1_change_bus_lock_t) (const struct device *dev, bool lock)
```

相关声明：[w1_change_bus_lock_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gaa64e8b894df8a3a44f3b91ea647cc0c1)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

锁定或解锁 1-Wire 总线。

<a id="r_ga2f5540f2a86fd55edcd7a8ffecbfd786"></a>

```c
typedef void(* w1_search_callback_t) (struct w1_rom rom, void *user_data)
```

相关声明：[w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

定义搜索操作的应用程序回调处理函数签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 29.4\_枚举（Enumerations）

<a id="r_ga382989ef707709b5d26c40a394833612"></a>

```c
enum w1_settings_type { W1_SETTING_SPEED , W1_SETTING_STRONG_PULLUP , W1_SETINGS_TYPE_COUNT }
```

相关声明：[w1_settings_type](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga382989ef707709b5d26c40a394833612)、[W1_SETTING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5)、[W1_SETTING_STRONG_PULLUP](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811)、[W1_SETINGS_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22)。

定义可在运行时配置的 1-Wire 主机设置类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.5\_函数（Functions）

<a id="r_gab18b0f60a126d38c982730d3ad9756c1"></a>

```c
static int w1_lock_bus (const struct device *dev)
```

相关声明：[w1_lock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gab18b0f60a126d38c982730d3ad9756c1)、[device](../device_reference/P002_设备对象结构.md)。

锁定 1-Wire 总线，防止同时访问。

<a id="r_ga7230fad2428ab62fa963b50e67388c19"></a>

```c
static int w1_unlock_bus (const struct device *dev)
```

相关声明：[w1_unlock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga7230fad2428ab62fa963b50e67388c19)、[device](../device_reference/P002_设备对象结构.md)。

解锁 1-Wire 总线。

<a id="r_gab4eccd585c6f14330807055ccc151fd6"></a>

```c
int w1_reset_bus (const struct device *dev)
```

相关声明：[w1_reset_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab4eccd585c6f14330807055ccc151fd6)、[device](../device_reference/P002_设备对象结构.md)。

复位单总线（1-Wire），使从设备准备通信。

<a id="r_ga0f2b37163f3d7c9816371942765509b4"></a>

```c
int w1_read_bit (const struct device *dev)
```

相关声明：[w1_read_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga0f2b37163f3d7c9816371942765509b4)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个位。

<a id="r_ga3671d8bbf9d044c60d7e96e4190ba2fa"></a>

```c
int w1_write_bit (const struct device *dev, const bool bit)
```

相关声明：[w1_write_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga3671d8bbf9d044c60d7e96e4190ba2fa)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向 1-Wire 总线写入单个位。

<a id="r_ga868980684bb98149af5b59e3fa8a83b6"></a>

```c
int w1_read_byte (const struct device *dev)
```

相关声明：[w1_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga868980684bb98149af5b59e3fa8a83b6)、[device](../device_reference/P002_设备对象结构.md)。

从 1-Wire 总线读取单个字节。

<a id="r_ga978a8f14fb8cb3a569f8b731b20cc840"></a>

```c
int w1_write_byte (const struct device *dev, uint8_t byte)
```

相关声明：[w1_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga978a8f14fb8cb3a569f8b731b20cc840)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入单个字节。

<a id="r_ga2967c99ec93b7c31beb9cf2a327a23f4"></a>

```c
int w1_read_block (const struct device *dev, uint8_t *buffer, size_t len)
```

相关声明：[w1_read_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga2967c99ec93b7c31beb9cf2a327a23f4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 1-Wire 总线读取一个数据块。

<a id="r_gab30a58c42c06088da9e0845de7d089ce"></a>

```c
int w1_write_block (const struct device *dev, const uint8_t *buffer, size_t len)
```

相关声明：[w1_write_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab30a58c42c06088da9e0845de7d089ce)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 1-Wire 总线写入一个数据块。

<a id="r_ga65892855c763dccc27b508d870c1d144"></a>

```c
size_t w1_get_slave_count (const struct device *dev)
```

相关声明：[w1_get_slave_count](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga65892855c763dccc27b508d870c1d144)、[device](../device_reference/P002_设备对象结构.md)。

获取总线上的从设备数量。

<a id="r_gae989e0deebe5666edc9ff8a3839cf216"></a>

```c
int w1_configure (const struct device *dev, enum w1_settings_type type, uint32_t value)
```

相关声明：[w1_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gae989e0deebe5666edc9ff8a3839cf216)、[device](../device_reference/P002_设备对象结构.md)、[w1_settings_type](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga382989ef707709b5d26c40a394833612)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 1-Wire 主机的参数。

<a id="r_ga93abefbd0e7067db474e6480301a0c4c"></a>

```c
int w1_read_rom (const struct device *dev, struct w1_rom *rom)
```

相关声明：[w1_read_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga93abefbd0e7067db474e6480301a0c4c)、[device](../device_reference/P002_设备对象结构.md)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

读取外设的 64 位 ROM。

<a id="r_ga53f34d64504498dbb194bc2119727908"></a>

```c
int w1_match_rom (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_match_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga53f34d64504498dbb194bc2119727908)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

通过广播选定的 ROM 代码选择特定从设备。

<a id="r_ga67c815bb99b75c862a483d4f8556b24a"></a>

```c
int w1_resume_command (const struct device *dev)
```

相关声明：[w1_resume_command](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga67c815bb99b75c862a483d4f8556b24a)、[device](../device_reference/P002_设备对象结构.md)。

选择上次通过匹配 ROM（Match ROM）或搜索 ROM（Search ROM）命令寻址的从设备。

<a id="r_gaba2be4e87ff472e90b705dbd73b913de"></a>

```c
int w1_skip_rom (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_skip_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaba2be4e87ff472e90b705dbd73b913de)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

选择所有从设备，不考虑 ROM。

<a id="r_gaa0acc88fe02535a3d512b866b6d34b8a"></a>

```c
int w1_reset_select (const struct device *dev, const struct w1_slave_config *config)
```

相关声明：[w1_reset_select](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa0acc88fe02535a3d512b866b6d34b8a)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)。

单从设备（Single drop）配置使用跳过选择（Skip Select）命令，否则使用匹配 ROM（Match ROM）命令。

<a id="r_ga1cf8c016ac66c3970f72fa1f409fa680"></a>

```c
int w1_write_read (const struct device *dev, const struct w1_slave_config *config, const uint8_t *write_buf, size_t write_len, uint8_t *read_buf, size_t read_len)
```

相关声明：[w1_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga1cf8c016ac66c3970f72fa1f409fa680)、[device](../device_reference/P002_设备对象结构.md)、[w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 ROM 匹配的 1-Wire 从设备先写入再读取数据。

<a id="r_ga19533f445029a69aac7d4ca5a7aeedcd"></a>

```c
int w1_search_bus (const struct device *dev, uint8_t command, uint8_t family, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga19533f445029a69aac7d4ca5a7aeedcd)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索总线上的 1-Wire 从设备。

<a id="r_ga024af0ee5018d7078808cc0a544cfd26"></a>

```c
static int w1_search_rom (const struct device *dev, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga024af0ee5018d7078808cc0a544cfd26)、[device](../device_reference/P002_设备对象结构.md)、[w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索总线上的 1-Wire 从设备。

<a id="r_ga0f510bd3720e54b4eeb4e368934db7f0"></a>

```c
static int w1_search_alarm (const struct device *dev, w1_search_callback_t callback, void *user_data)
```

相关声明：[w1_search_alarm](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga0f510bd3720e54b4eeb4e368934db7f0)、[device](../device_reference/P002_设备对象结构.md)、[w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)。

搜索具有有效告警的 1-Wire 从设备。

<a id="r_ga178a88d0c585d5df0405aadde3ea9178"></a>

```c
static uint64_t w1_rom_to_uint64 (const struct w1_rom *rom)
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[w1_rom_to_uint64](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga178a88d0c585d5df0405aadde3ea9178)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `w1_rom` 结构体转换为 `uint64_t` 的函数。

<a id="r_ga6e4dba051a6b29c974e499db17315034"></a>

```c
static void w1_uint64_to_rom (const uint64_t rom64, struct w1_rom *rom)
```

相关声明：[w1_uint64_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga6e4dba051a6b29c974e499db17315034)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `uint64_t` 写入 `struct w1_rom` 指针所指对象的函数。

<a id="r_ga350a384a6040d1fbb86bfb804013ade3"></a>

```c
static uint8_t w1_crc8 (const uint8_t *src, size_t len)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[w1_crc8](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga350a384a6040d1fbb86bfb804013ade3)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

按 1-Wire 规范计算 CRC-8 校验值。

<a id="r_ga5635f79a54a2e5b96c8b7ca9a8ab8366"></a>

```c
static uint16_t w1_crc16 (const uint16_t seed, const uint8_t *src, const size_t len)
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[w1_crc16](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga5635f79a54a2e5b96c8b7ca9a8ab8366)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

计算 1-Wire 变体的 CRC-16。


## 29.6\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/crc.h](../data_utilities/P005_CRC系统头文件源码.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P002_系统字节序头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [w1_master_config](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md)
- [w1_master_data](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md)
- [w1_driver_api](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md)
- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)
- [W1_SEARCH_ALL_FAMILIES](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga909502b9b18c15a9ab0da8d3605e8c37)
- [W1_ROM_INIT_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga17770ecebad7170e9004afd9a7735c73)
- [W1_CMD_SKIP_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga9792cb2093e911a4722b7fa9457093dc)
- [W1_CMD_MATCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gae97f7ecda699ccf9b63030f2af632bc8)
- [W1_CMD_RESUME](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga31230559122289c179f01e09e3847830)
- [W1_CMD_READ_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga9e1a9a38889bf165370670c28778028b)
- [W1_CMD_SEARCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga57f17871edab0b771f2f664bf9bafb79)
- [W1_CMD_SEARCH_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gafc7a257428c69bb4549c6cd05a928957)
- [W1_CMD_OVERDRIVE_SKIP_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga8b61b2308f2681801894f24ea2c95b12)
- [W1_CMD_OVERDRIVE_MATCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga3e3f9fa70074188a2e489f34555b519b)
- [W1_CRC8_SEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa4ad8d9a3791fbca6c99d49b9793a002)
- [W1_CRC8_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)
- [W1_CRC16_SEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga324f30f17c6cd1b33650b58055a3a57f)
- [W1_CRC16_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gab94362fbf4eec5f115f93fc8976cff0d)
- [w1_reset_bus_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga87232322cd487772d377aa0a8e9e5bfc)
- [device](../device_reference/P002_设备对象结构.md)
- [w1_read_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gabb495014dd7b9583009b34d9eba02ddc)
- [w1_write_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga126e501ef9a74cbc3c375ca64025cdbc)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [w1_read_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga861af0744a5f102558294422de50f6ae)
- [w1_write_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga18924f833820d5f70d73ab33de6615dd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [w1_read_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gae2673a21841ad196af69e5b4e6769ea8)
- [w1_write_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gafbbba20705697154d29a91ac94cc3747)
- [w1_get_slave_count_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga5d3ee84858e35cdac923a6238a22e9a2)
- [w1_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gab831da9314fce3e6ec10526ca5224515)
- [w1_settings_type](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga382989ef707709b5d26c40a394833612)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [w1_change_bus_lock_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gaa64e8b894df8a3a44f3b91ea647cc0c1)
- [w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)
- [W1_SETTING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5)
- [W1_SETTING_STRONG_PULLUP](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811)
- [W1_SETINGS_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22)
- [w1_lock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gab18b0f60a126d38c982730d3ad9756c1)
- [w1_unlock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga7230fad2428ab62fa963b50e67388c19)
- [w1_reset_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab4eccd585c6f14330807055ccc151fd6)
- [w1_read_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga0f2b37163f3d7c9816371942765509b4)
- [w1_write_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga3671d8bbf9d044c60d7e96e4190ba2fa)
- [w1_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga868980684bb98149af5b59e3fa8a83b6)
- [w1_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga978a8f14fb8cb3a569f8b731b20cc840)
- [w1_read_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga2967c99ec93b7c31beb9cf2a327a23f4)
- [w1_write_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab30a58c42c06088da9e0845de7d089ce)
- [w1_get_slave_count](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga65892855c763dccc27b508d870c1d144)
- [w1_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gae989e0deebe5666edc9ff8a3839cf216)
- [w1_read_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga93abefbd0e7067db474e6480301a0c4c)
- [w1_match_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga53f34d64504498dbb194bc2119727908)
- [w1_resume_command](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga67c815bb99b75c862a483d4f8556b24a)
- [w1_skip_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaba2be4e87ff472e90b705dbd73b913de)
- [w1_reset_select](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa0acc88fe02535a3d512b866b6d34b8a)
- [w1_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga1cf8c016ac66c3970f72fa1f409fa680)
- [w1_search_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga19533f445029a69aac7d4ca5a7aeedcd)
- [w1_search_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga024af0ee5018d7078808cc0a544cfd26)
- [w1_search_alarm](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga0f510bd3720e54b4eeb4e368934db7f0)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [w1_rom_to_uint64](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga178a88d0c585d5df0405aadde3ea9178)
- [w1_uint64_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga6e4dba051a6b29c974e499db17315034)
- [w1_crc8](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga350a384a6040d1fbb86bfb804013ade3)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [w1_crc16](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga5635f79a54a2e5b96c8b7ca9a8ab8366)

<a id="header-details"></a>

---

[上一章](P028_zephyr__drivers__swdp.h_头文件参考.md) · [返回大纲](大纲.md)
