---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-6
title: 时钟协议（Clock Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_时钟协议（Clock Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__clk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 进行时钟管理的操作。

<a id="details"></a>

通过 SCMI 进行时钟管理的操作。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_clk_2Eh"></a>

```c
file clk.h
```

相关声明：[clk.h](../api_file_secure_value_reference/P004_zephyr__drivers__firmware__scmi__clk.h_文件参考.md)。

系统控制与管理接口（SCMI）时钟协议（Clock Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_scmi_5Fclock_5Fconfig"></a>

```c
struct scmi_clock_config
```

相关声明：[scmi_clock_config](../platform_security_model_reference/P035_scmi_clock_config_结构体.md)。

描述CLOCK_CONFIG_SET命令的参数。

<a id="r_scmi_5Fclock_5Frate_5Fconfig"></a>

```c
struct scmi_clock_rate_config
```

相关声明：[scmi_clock_rate_config](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md)。

描述CLOCK_RATE_SET命令的参数。

<a id="r_scmi_5Fclock_5Fattributes"></a>

```c
struct scmi_clock_attributes
```

相关声明：[scmi_clock_attributes](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md)。

描述CLOCK_ATTRIBUTES命令的应答内容。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga8b14e6d0d7329cb53c57ec21d241c3de"></a>

```c
#define SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK GENMASK(1, 0)
```

相关声明：[SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK](#ga8b14e6d0d7329cb53c57ec21d241c3de)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

`CLOCK_CONFIG_SET` 属性字中使能／禁用字段的掩码（Mask）。

<a id="r_gaf797af4466ae90d17a58527f53d698ce"></a>

```c
#define SCMI_CLK_CONFIG_ENABLE_DISABLE(x)
```

相关声明：[SCMI_CLK_CONFIG_ENABLE_DISABLE](#gaf797af4466ae90d17a58527f53d698ce)。

从 `CLOCK_CONFIG_SET` 值 `x` 中提取使能／禁用字段（Enable/Disable Field）。

<a id="r_ga9c2b446e167d9d5a903c55e4644d85ed"></a>

```c
#define SCMI_CLK_ATTRIBUTES_CLK_NUM(x)
```

相关声明：[SCMI_CLK_ATTRIBUTES_CLK_NUM](#ga9c2b446e167d9d5a903c55e4644d85ed)。

从 `PROTOCOL_ATTRIBUTES` 响应 `x` 中提取时钟数量（Number of Clocks）。

<a id="r_gaab3ca60f158a5dd0b33f1b57e9d9b56f"></a>

```c
#define SCMI_CLK_RATE_SET_FLAGS_ASYNC BIT(0)
```

相关声明：[SCMI_CLK_RATE_SET_FLAGS_ASYNC](#gaab3ca60f158a5dd0b33f1b57e9d9b56f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`CLOCK_RATE_SET` 标志：异步（Asynchronously）执行速率变更。

<a id="r_ga7fa05d27f6a5a31298b2d075ebd83403"></a>

```c
#define SCMI_CLK_RATE_SET_FLAGS_IGNORE_DELEAYED_RESP BIT(1)
```

相关声明：[SCMI_CLK_RATE_SET_FLAGS_IGNORE_DELEAYED_RESP](#ga7fa05d27f6a5a31298b2d075ebd83403)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`CLOCK_RATE_SET` 标志：对于异步请求，不发送延迟响应（Delayed Response）。

<a id="r_ga649ba03b0e0f32db9aa83b568965301a"></a>

```c
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_UP_DOWN BIT(2)
```

相关声明：[SCMI_CLK_RATE_SET_FLAGS_ROUNDS_UP_DOWN](#ga649ba03b0e0f32db9aa83b568965301a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`CLOCK_RATE_SET` 标志：置位时向上取整（Round Up），清零时向下取整（Round Down）。

<a id="r_ga605adf399c70721a68c9c4971d695d3e"></a>

```c
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_AUTO BIT(3)
```

相关声明：[SCMI_CLK_RATE_SET_FLAGS_ROUNDS_AUTO](#ga605adf399c70721a68c9c4971d695d3e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`CLOCK_RATE_SET` 标志：将速率取整到最接近的受支持值（Closest Supported Value）。

<a id="r_ga8e568bda4fc704b5b2d58588021a0b31"></a>

```c
#define SCMI_CLK_PROTOCOL_SUPPORTED_VERSION 0x30000
```

相关声明：[SCMI_CLK_PROTOCOL_SUPPORTED_VERSION](#ga8e568bda4fc704b5b2d58588021a0b31)。

此驱动支持的系统控制与管理接口（SCMI）时钟协议版本。

<a id="r_ga9c1ce70d829b23f17ba775f495421ad2"></a>

```c
#define SCMI_PROTO_VER_MAJOR(v)
```

相关声明：[SCMI_PROTO_VER_MAJOR](#ga9c1ce70d829b23f17ba775f495421ad2)。

时钟名称长度（Clock Name Length），短版本。

<a id="r_ga9cab66cdf72d61ccf10a3f2bc5aaef39"></a>

```c
#define SCMI_PROTO_VER_MINOR(v)
```

相关声明：[SCMI_PROTO_VER_MINOR](#ga9cab66cdf72d61ccf10a3f2bc5aaef39)。

从 SCMI 协议版本中提取次版本号（Minor Version）。

<a id="r_gadac0bacc2404b6be066155c6ce4a0d28"></a>

```c
#define SCMI_CLK_NAME_LEN 16
```

相关声明：[SCMI_CLK_NAME_LEN](#gadac0bacc2404b6be066155c6ce4a0d28)。

时钟名称长度（Clock Name Length），短版本。

<a id="r_ga8debd602b6a0b6ff052eced457bbfaa9"></a>

```c
#define SCMI_CLK_ENABLED(attributes)
```

相关声明：[SCMI_CLK_ENABLED](#ga8debd602b6a0b6ff052eced457bbfaa9)。

根据所给属性获取时钟使能状态（Enabled Status）。

<a id="r_ga5283c1d408d4d53d998942885f6960ab"></a>

```c
#define SCMI_CLK_HAS_RESTRICTIONS(attributes)
```

相关声明：[SCMI_CLK_HAS_RESTRICTIONS](#ga5283c1d408d4d53d998942885f6960ab)。

根据所给属性检查时钟是否受到限制（Restrictions）。

<a id="r_gaec1c736e17e6950aeb5c0aedbea1be44"></a>

```c
#define SCMI_CLK_STATE_CONTROL_ALLOWED(permissions)
```

相关声明：[SCMI_CLK_STATE_CONTROL_ALLOWED](#gaec1c736e17e6950aeb5c0aedbea1be44)。

根据权限检查时钟是否允许门控／解除门控（Gating/Ungating）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gac9fe7f4275895fd9e6a7eada26012efb"></a>

```c
int scmi_clock_config_set (struct scmi_protocol *proto, struct scmi_clock_config *cfg)
```

相关声明：[scmi_clock_config_set](#gac9fe7f4275895fd9e6a7eada26012efb)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_clock_config](../platform_security_model_reference/P035_scmi_clock_config_结构体.md)。

发送 `CLOCK_CONFIG_SET` 命令并获取响应（Reply）。

<a id="r_gaf50ba91139d4de1a7eab9d8b4cebf745"></a>

```c
int scmi_clock_config_get (struct scmi_protocol *proto, uint32_t clk_id, uint32_t flags, uint32_t *config)
```

相关声明：[scmi_clock_config_get](#gaf50ba91139d4de1a7eab9d8b4cebf745)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 `CLOCK_CONFIG_GET` 命令并获取响应（Reply）。

<a id="r_gac69cff69cef158aebf5b40ba2c3c7bb4"></a>

```c
int scmi_clock_rate_get (struct scmi_protocol *proto, uint32_t clk_id, uint32_t *rate)
```

相关声明：[scmi_clock_rate_get](#gac69cff69cef158aebf5b40ba2c3c7bb4)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询时钟速率（Clock Rate）。

<a id="r_gaa0f54c7fba01045a89ef0fd3a0ff16fc"></a>

```c
int scmi_clock_rate_set (struct scmi_protocol *proto, struct scmi_clock_rate_config *cfg)
```

相关声明：[scmi_clock_rate_set](#gaa0f54c7fba01045a89ef0fd3a0ff16fc)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[scmi_clock_rate_config](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md)。

发送 `CLOCK_RATE_SET` 命令并获取响应（Reply）。

<a id="r_ga456618c04934490afffdcd8be71729b3"></a>

```c
int scmi_clock_parent_get (struct scmi_protocol *proto, uint32_t clk_id, uint32_t *parent_id)
```

相关声明：[scmi_clock_parent_get](#ga456618c04934490afffdcd8be71729b3)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询时钟的父时钟（Parent Clock）。

<a id="r_ga57942effe001fdb62a435a51441108e6"></a>

```c
int scmi_clock_parent_set (struct scmi_protocol *proto, uint32_t clk_id, uint32_t parent_id)
```

相关声明：[scmi_clock_parent_set](#ga57942effe001fdb62a435a51441108e6)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 `CLOCK_PARENT_SET` 命令并获取响应（Reply）。

<a id="r_ga9803a171fc12c01b6f29822eb3ccaea7"></a>

```c
int scmi_clock_attributes (struct scmi_protocol *proto, uint32_t clk_id, struct scmi_clock_attributes *attributes)
```

相关声明：[scmi_clock_attributes](#ga9803a171fc12c01b6f29822eb3ccaea7)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 `CLOCK_ATTRIBUTES` 命令并获取响应（Reply）。

<a id="r_ga11fb749832c289730674fb111fdb6a18"></a>

```c
int scmi_clock_get_permissions (struct scmi_protocol *proto, uint32_t clk_id, uint32_t *permissions)
```

相关声明：[scmi_clock_get_permissions](#ga11fb749832c289730674fb111fdb6a18)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

发送 `CLOCK_GET_PERMISSIONS` 命令并获取响应（Reply）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga9c2b446e167d9d5a903c55e4644d85ed"></a>

### `SCMI_CLK_ATTRIBUTES_CLK_NUM`

```c
#define SCMI_CLK_ATTRIBUTES_CLK_NUM ( x)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((x) & GENMASK(15, 0))
```

从 `PROTOCOL_ATTRIBUTES` 响应 `x` 中提取时钟数量（Number of Clocks）。

<a id="ga8b14e6d0d7329cb53c57ec21d241c3de"></a>

### `SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK`

```c
#define SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK GENMASK(1, 0)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

`CLOCK_CONFIG_SET` 属性字中使能／禁用字段的掩码（Mask）。

<a id="gaf797af4466ae90d17a58527f53d698ce"></a>

### `SCMI_CLK_CONFIG_ENABLE_DISABLE`

```c
#define SCMI_CLK_CONFIG_ENABLE_DISABLE ( x)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((uint32_t)(x) & SCMI_CLK_CONFIG_DISABLE_ENABLE_MASK)
```

从 `CLOCK_CONFIG_SET` 值 `x` 中提取使能／禁用字段（Enable/Disable Field）。

<a id="ga8debd602b6a0b6ff052eced457bbfaa9"></a>

### `SCMI_CLK_ENABLED`

```c
#define SCMI_CLK_ENABLED ( attributes)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((attributes) & BIT(0))
```

根据所给属性获取时钟使能状态（Enabled Status）。

<a id="ga5283c1d408d4d53d998942885f6960ab"></a>

### `SCMI_CLK_HAS_RESTRICTIONS`

```c
#define SCMI_CLK_HAS_RESTRICTIONS ( attributes)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((attributes) & BIT(1))
```

根据所给属性检查时钟是否受到限制（Restrictions）。

<a id="gadac0bacc2404b6be066155c6ce4a0d28"></a>

### `SCMI_CLK_NAME_LEN`

```c
#define SCMI_CLK_NAME_LEN 16
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

时钟名称长度（Clock Name Length），短版本。

<a id="ga8e568bda4fc704b5b2d58588021a0b31"></a>

### `SCMI_CLK_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_CLK_PROTOCOL_SUPPORTED_VERSION 0x30000
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

此驱动支持的系统控制与管理接口（SCMI）时钟协议版本。

<a id="gaab3ca60f158a5dd0b33f1b57e9d9b56f"></a>

### `SCMI_CLK_RATE_SET_FLAGS_ASYNC`

```c
#define SCMI_CLK_RATE_SET_FLAGS_ASYNC BIT(0)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

`CLOCK_RATE_SET` 标志：异步（Asynchronously）执行速率变更。

<a id="ga7fa05d27f6a5a31298b2d075ebd83403"></a>

### `SCMI_CLK_RATE_SET_FLAGS_IGNORE_DELEAYED_RESP`

```c
#define SCMI_CLK_RATE_SET_FLAGS_IGNORE_DELEAYED_RESP BIT(1)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

`CLOCK_RATE_SET` 标志：对于异步请求，不发送延迟响应（Delayed Response）。

<a id="ga605adf399c70721a68c9c4971d695d3e"></a>

### `SCMI_CLK_RATE_SET_FLAGS_ROUNDS_AUTO`

```c
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_AUTO BIT(3)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

`CLOCK_RATE_SET` 标志：将速率取整到最接近的受支持值（Closest Supported Value）。

<a id="ga649ba03b0e0f32db9aa83b568965301a"></a>

### `SCMI_CLK_RATE_SET_FLAGS_ROUNDS_UP_DOWN`

```c
#define SCMI_CLK_RATE_SET_FLAGS_ROUNDS_UP_DOWN BIT(2)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

`CLOCK_RATE_SET` 标志：置位时向上取整（Round Up），清零时向下取整（Round Down）。

<a id="gaec1c736e17e6950aeb5c0aedbea1be44"></a>

### `SCMI_CLK_STATE_CONTROL_ALLOWED`

```c
#define SCMI_CLK_STATE_CONTROL_ALLOWED ( permissions)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((permissions) & BIT(31))
```

根据权限检查时钟是否允许门控／解除门控（Gating/Ungating）。

<a id="ga9c1ce70d829b23f17ba775f495421ad2"></a>

### `SCMI_PROTO_VER_MAJOR`

```c
#define SCMI_PROTO_VER_MAJOR ( v)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((v) >> 16)
```

时钟名称长度（Clock Name Length），短版本。

从 SCMI 协议版本中提取主版本号（Major Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 组合后的 32 位协议版本（Protocol Version），格式为 `major << 16 \| minor`。 |

**返回（Returns）**：返回值：主版本号（Major Version Number）。

<a id="ga9cab66cdf72d61ccf10a3f2bc5aaef39"></a>

### `SCMI_PROTO_VER_MINOR`

```c
#define SCMI_PROTO_VER_MINOR ( v)
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

展开值（Value）：

```c
((v) & 0xFFFF)
```

从 SCMI 协议版本中提取次版本号（Minor Version）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `v` | 组合后的 32 位协议版本（Protocol Version），格式为 `major << 16 \| minor`。 |

**返回（Returns）**：返回值：次版本号（Minor Version Number）。

<a id="ga9803a171fc12c01b6f29822eb3ccaea7"></a>

### `scmi_clock_attributes()`

```c
int scmi_clock_attributes ( struct scmi_protocol * proto, uint32_t clk_id, struct scmi_clock_attributes * attributes )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_ATTRIBUTES` 命令并获取响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `attributes` | 命令返回的时钟属性（Clock Attributes）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf50ba91139d4de1a7eab9d8b4cebf745"></a>

### `scmi_clock_config_get()`

```c
int scmi_clock_config_get ( struct scmi_protocol * proto, uint32_t clk_id, uint32_t flags, uint32_t * config )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_CONFIG_GET` 命令并获取响应（Reply）。

查询时钟当前配置，特别是是否已使能。此查询为只读（Read-only），由 SCMI 平台提供服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `flags` | 命令标志（Command Flags）。基本查询使用 0；此处不解析扩展配置位。 |
| `config` | 成功时，此指针指向的值被设置为返回的配置字（Config Word）。使用 `SCMI_CLK_CONFIG_ENABLE_DISABLE()` 检查使能状态。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac9fe7f4275895fd9e6a7eada26012efb"></a>

### `scmi_clock_config_set()`

```c
int scmi_clock_config_set ( struct scmi_protocol * proto, struct scmi_clock_config * cfg )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_CONFIG_SET` 命令并获取响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga11fb749832c289730674fb111fdb6a18"></a>

### `scmi_clock_get_permissions()`

```c
int scmi_clock_get_permissions ( struct scmi_protocol * proto, uint32_t clk_id, uint32_t * permissions )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_GET_PERMISSIONS` 命令并获取响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `permissions` | 命令返回的时钟权限（Clock Permissions）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga456618c04934490afffdcd8be71729b3"></a>

### `scmi_clock_parent_get()`

```c
int scmi_clock_parent_get ( struct scmi_protocol * proto, uint32_t clk_id, uint32_t * parent_id )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

查询时钟的父时钟（Parent Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `parent_id` | 通过此命令设置的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga57942effe001fdb62a435a51441108e6"></a>

### `scmi_clock_parent_set()`

```c
int scmi_clock_parent_set ( struct scmi_protocol * proto, uint32_t clk_id, uint32_t parent_id )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_PARENT_SET` 命令并获取响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `parent_id` | 通过此命令设置的值。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac69cff69cef158aebf5b40ba2c3c7bb4"></a>

### `scmi_clock_rate_get()`

```c
int scmi_clock_rate_get ( struct scmi_protocol * proto, uint32_t clk_id, uint32_t * rate )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

查询时钟速率（Clock Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `clk_id` | 要查询的时钟 ID（Clock ID）。 |
| `rate` | 指向要通过此命令设置的速率（Rate）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa0f54c7fba01045a89ef0fd3a0ff16fc"></a>

### `scmi_clock_rate_set()`

```c
int scmi_clock_rate_set ( struct scmi_protocol * proto, struct scmi_clock_rate_config * cfg )
```

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

发送 `CLOCK_RATE_SET` 命令并获取响应（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 6.6\_原页交叉引用（Cross References）

- [clk.h](../api_file_secure_value_reference/P004_zephyr__drivers__firmware__scmi__clk.h_文件参考.md)
- [scmi_clock_config](../platform_security_model_reference/P035_scmi_clock_config_结构体.md)
- [scmi_clock_rate_config](../platform_security_model_reference/P036_scmi_clock_rate_config_结构体.md)
- [scmi_clock_attributes](../platform_security_model_reference/P034_scmi_clock_attributes_结构体.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="agroup__scmi__clk_html_ga8b14e6d0d7329cb53c57ec21d241c3de"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_PCIe 控制器驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P007_STM32 API主题.md)
