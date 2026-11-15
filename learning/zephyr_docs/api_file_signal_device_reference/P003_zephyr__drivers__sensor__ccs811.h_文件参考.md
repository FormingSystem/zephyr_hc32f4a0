---
id: learning.zephyr-docs.api-file-signal-device-reference.page-3
title: zephyr__drivers__sensor__ccs811.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccs811_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_sensor\_\_ccs811.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ccs811_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CCS811室内空气质量传感器（Indoor Air Quality Sensor）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

CCS811 室内空气质量传感器（Indoor Air Quality Sensor）的扩展公共 API。该传感器的部分能力与运行要求无法通过传感器驱动抽象层（Sensor Driver Abstraction）表达。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_ccs811_5Fresult_5Ftype"></a>

```c
struct ccs811_result_type
```

相关声明：[ccs811_result_type](../sensor_navigation_model_reference/P002_ccs811_result_type_结构体.md)。

每次获取（Fetch）操作从传感器收集的信息。

<a id="r_ccs811_5Fconfigver_5Ftype"></a>

```c
struct ccs811_configver_type
```

相关声明：[ccs811_configver_type](../sensor_navigation_model_reference/P001_ccs811_configver_type_结构体.md)。

获取CCS811静态状态的信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_a20384d881a191499e059822188096a3f"></a>

```c
#define CCS811_STATUS_ERROR BIT(0)
```

相关声明：[CCS811_STATUS_ERROR](#a20384d881a191499e059822188096a3f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6020157cec1ebbae138262d0c0f4de88"></a>

```c
#define CCS811_STATUS_DATA_READY BIT(3)
```

相关声明：[CCS811_STATUS_DATA_READY](#a6020157cec1ebbae138262d0c0f4de88)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a30dbcc60ace45a6deeb4d7b4254713e6"></a>

```c
#define CCS811_STATUS_APP_VALID BIT(4)
```

相关声明：[CCS811_STATUS_APP_VALID](#a30dbcc60ace45a6deeb4d7b4254713e6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afb4bbabdc1c3df8fae10986f14974cdf"></a>

```c
#define CCS811_STATUS_FW_MODE BIT(7)
```

相关声明：[CCS811_STATUS_FW_MODE](#afb4bbabdc1c3df8fae10986f14974cdf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aea6a55c33babbec3613074233ed59e87"></a>

```c
#define CCS811_ERROR_WRITE_REG_INVALID BIT(0)
```

相关声明：[CCS811_ERROR_WRITE_REG_INVALID](#aea6a55c33babbec3613074233ed59e87)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a362e9ebd07dd4e3b08e19b51ef1e80c3"></a>

```c
#define CCS811_ERROR_READ_REG_INVALID BIT(1)
```

相关声明：[CCS811_ERROR_READ_REG_INVALID](#a362e9ebd07dd4e3b08e19b51ef1e80c3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a86174804458c701304aac10e0f79395d"></a>

```c
#define CCS811_ERROR_MEASMODE_INVALID BIT(2)
```

相关声明：[CCS811_ERROR_MEASMODE_INVALID](#a86174804458c701304aac10e0f79395d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8df212e550d4722a9588d2afb0353423"></a>

```c
#define CCS811_ERROR_MAX_RESISTANCE BIT(3)
```

相关声明：[CCS811_ERROR_MAX_RESISTANCE](#a8df212e550d4722a9588d2afb0353423)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaf6643eca6856def154c5c3b27a47722"></a>

```c
#define CCS811_ERROR_HEATER_FAULT BIT(4)
```

相关声明：[CCS811_ERROR_HEATER_FAULT](#aaf6643eca6856def154c5c3b27a47722)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_add1eea491f4fa321455bf450de9523ff"></a>

```c
#define CCS811_ERROR_HEATER_SUPPLY BIT(5)
```

相关声明：[CCS811_ERROR_HEATER_SUPPLY](#add1eea491f4fa321455bf450de9523ff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaf3104eccd057fb02e2e3bd690d033bf"></a>

```c
#define CCS811_MODE_IDLE 0x00
```

相关声明：[CCS811_MODE_IDLE](#aaf3104eccd057fb02e2e3bd690d033bf)。

<a id="r_a0ae923f15a5dff2eeb9bb6a4c322a846"></a>

```c
#define CCS811_MODE_IAQ_1SEC 0x10
```

相关声明：[CCS811_MODE_IAQ_1SEC](#a0ae923f15a5dff2eeb9bb6a4c322a846)。

<a id="r_a50ba73c3faf9be67ca8503185212d646"></a>

```c
#define CCS811_MODE_IAQ_10SEC 0x20
```

相关声明：[CCS811_MODE_IAQ_10SEC](#a50ba73c3faf9be67ca8503185212d646)。

<a id="r_aba48acebce3be106f2baf4d138ba10ae"></a>

```c
#define CCS811_MODE_IAQ_60SEC 0x30
```

相关声明：[CCS811_MODE_IAQ_60SEC](#aba48acebce3be106f2baf4d138ba10ae)。

<a id="r_a7f2d13d60b58cd38d2e1faed34783e8f"></a>

```c
#define CCS811_MODE_IAQ_250MSEC 0x40
```

相关声明：[CCS811_MODE_IAQ_250MSEC](#a7f2d13d60b58cd38d2e1faed34783e8f)。

<a id="r_a2da34b0adb925734239288c97ec1224a"></a>

```c
#define CCS811_MODE_MSK 0x70
```

相关声明：[CCS811_MODE_MSK](#a2da34b0adb925734239288c97ec1224a)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_a96979437b70cdab86a9a09a6e8876c0b"></a>

```c
const struct ccs811_result_type * ccs811_result (const struct device *dev)
```

相关声明：[ccs811_result_type](../sensor_navigation_model_reference/P002_ccs811_result_type_结构体.md)、[ccs811_result](#a96979437b70cdab86a9a09a6e8876c0b)、[device](../device_reference/P002_设备对象结构.md)。

访问保存最近一次传感器读数（Sensor Data）的存储区域。

<a id="r_a89d51f90a25cfa3437eed843f0f3da20"></a>

```c
int ccs811_configver_fetch (const struct device *dev, struct ccs811_configver_type *ptr)
```

相关声明：[ccs811_configver_fetch](#a89d51f90a25cfa3437eed843f0f3da20)、[device](../device_reference/P002_设备对象结构.md)、[ccs811_configver_type](../sensor_navigation_model_reference/P001_ccs811_configver_type_结构体.md)。

获取运行模式（Operating Mode）和版本信息（Version Information）。

<a id="r_a313fc541226b986eb098b88355c75ab0"></a>

```c
int ccs811_baseline_fetch (const struct device *dev)
```

相关声明：[ccs811_baseline_fetch](#a313fc541226b986eb098b88355c75ab0)、[device](../device_reference/P002_设备对象结构.md)。

获取 `BASELINE` 寄存器的当前值。

<a id="r_af6ed9f060f3bda5e867a772caf8cd333"></a>

```c
int ccs811_baseline_update (const struct device *dev, uint16_t baseline)
```

相关声明：[ccs811_baseline_update](#af6ed9f060f3bda5e867a772caf8cd333)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新 `BASELINE` 寄存器。

<a id="r_ac50d59a4f6ed8af7b62cb381c2aa7b22"></a>

```c
int ccs811_envdata_update (const struct device *dev, const struct sensor_value *temperature, const struct sensor_value *humidity)
```

相关声明：[ccs811_envdata_update](#ac50d59a4f6ed8af7b62cb381c2aa7b22)、[device](../device_reference/P002_设备对象结构.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

更新 `ENV_DATA` 寄存器。

## 3.4\_详细说明（Detailed Documentation）

<a id="aaf6643eca6856def154c5c3b27a47722"></a>

### `CCS811_ERROR_HEATER_FAULT`

```c
#define CCS811_ERROR_HEATER_FAULT BIT(4)
```

<a id="add1eea491f4fa321455bf450de9523ff"></a>

### `CCS811_ERROR_HEATER_SUPPLY`

```c
#define CCS811_ERROR_HEATER_SUPPLY BIT(5)
```

<a id="a8df212e550d4722a9588d2afb0353423"></a>

### `CCS811_ERROR_MAX_RESISTANCE`

```c
#define CCS811_ERROR_MAX_RESISTANCE BIT(3)
```

<a id="a86174804458c701304aac10e0f79395d"></a>

### `CCS811_ERROR_MEASMODE_INVALID`

```c
#define CCS811_ERROR_MEASMODE_INVALID BIT(2)
```

<a id="a362e9ebd07dd4e3b08e19b51ef1e80c3"></a>

### `CCS811_ERROR_READ_REG_INVALID`

```c
#define CCS811_ERROR_READ_REG_INVALID BIT(1)
```

<a id="aea6a55c33babbec3613074233ed59e87"></a>

### `CCS811_ERROR_WRITE_REG_INVALID`

```c
#define CCS811_ERROR_WRITE_REG_INVALID BIT(0)
```

<a id="a50ba73c3faf9be67ca8503185212d646"></a>

### `CCS811_MODE_IAQ_10SEC`

```c
#define CCS811_MODE_IAQ_10SEC 0x20
```

<a id="a0ae923f15a5dff2eeb9bb6a4c322a846"></a>

### `CCS811_MODE_IAQ_1SEC`

```c
#define CCS811_MODE_IAQ_1SEC 0x10
```

<a id="a7f2d13d60b58cd38d2e1faed34783e8f"></a>

### `CCS811_MODE_IAQ_250MSEC`

```c
#define CCS811_MODE_IAQ_250MSEC 0x40
```

<a id="aba48acebce3be106f2baf4d138ba10ae"></a>

### `CCS811_MODE_IAQ_60SEC`

```c
#define CCS811_MODE_IAQ_60SEC 0x30
```

<a id="aaf3104eccd057fb02e2e3bd690d033bf"></a>

### `CCS811_MODE_IDLE`

```c
#define CCS811_MODE_IDLE 0x00
```

<a id="a2da34b0adb925734239288c97ec1224a"></a>

### `CCS811_MODE_MSK`

```c
#define CCS811_MODE_MSK 0x70
```

<a id="a30dbcc60ace45a6deeb4d7b4254713e6"></a>

### `CCS811_STATUS_APP_VALID`

```c
#define CCS811_STATUS_APP_VALID BIT(4)
```

<a id="a6020157cec1ebbae138262d0c0f4de88"></a>

### `CCS811_STATUS_DATA_READY`

```c
#define CCS811_STATUS_DATA_READY BIT(3)
```

<a id="a20384d881a191499e059822188096a3f"></a>

### `CCS811_STATUS_ERROR`

```c
#define CCS811_STATUS_ERROR BIT(0)
```

<a id="afb4bbabdc1c3df8fae10986f14974cdf"></a>

### `CCS811_STATUS_FW_MODE`

```c
#define CCS811_STATUS_FW_MODE BIT(7)
```

<a id="a313fc541226b986eb098b88355c75ab0"></a>

### `ccs811_baseline_fetch()`

```c
int ccs811_baseline_fetch ( const struct device * dev)
```

获取 `BASELINE` 寄存器的当前值。

`BASELINE` 寄存器编码的数据用于依据单个设备配置和随时间的变化，校正传感器读数（Sensor Readings）。

正确管理 `BASELINE` 寄存器的方法，参见 AN000370《CCS811 基线保存与恢复》（Baseline Save and Restore on CCS811）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：**返回值（Returns）：**非负 16 位寄存器值，失败时返回负 `errno`。

<a id="af6ed9f060f3bda5e867a772caf8cd333"></a>

### `ccs811_baseline_update()`

```c
int ccs811_baseline_update ( const struct device * dev, uint16_t baseline )
```

更新 `BASELINE` 寄存器。

正确管理 `BASELINE` 寄存器的方法，参见 AN000370《CCS811 基线保存与恢复》（Baseline Save and Restore on CCS811）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `baseline` | 要存入 `BASELINE` 寄存器的值。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a89d51f90a25cfa3437eed843f0f3da20"></a>

### `ccs811_configver_fetch()`

```c
int ccs811_configver_fetch ( const struct device * dev, struct ccs811_configver_type * ptr )
```

获取运行模式（Operating Mode）和版本信息（Version Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `ptr` | 指向存储返回信息（Returned Information）位置的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`。

<a id="ac50d59a4f6ed8af7b62cb381c2aa7b22"></a>

### `ccs811_envdata_update()`

```c
int ccs811_envdata_update ( const struct device * dev, const struct sensor_value * temperature, const struct sensor_value * humidity )
```

更新 `ENV_DATA` 寄存器。

准确计算气体水平（Gas Levels）需要准确的环境数据（Environment Data）。测量精度仅达到 `0.5 Cel` 和 `0.5 RH`，单位标记按原文保留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `temperature` | 传感器处的当前温度（Current Temperature）。 |
| `humidity` | 传感器处的当前湿度（Current Humidity）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a96979437b70cdab86a9a09a6e8876c0b"></a>

### `ccs811_result()`

```c
const struct ccs811_result_type * ccs811_result ( const struct device * dev)
```

访问保存最近一次传感器读数（Sensor Data）的存储区域。

所引用对象的内容由 `sensor_fetch_sample()` 更新，但 `ccs811_result_type::mode` 除外，它在驱动初始化时设置。函数名按原文保留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：**返回值（Returns）：**指向结果信息（Result Information）的指针。


## 3.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P005_ccs811.h_源码浏览.md)
- [ccs811_result_type](../sensor_navigation_model_reference/P002_ccs811_result_type_结构体.md)
- [ccs811_configver_type](../sensor_navigation_model_reference/P001_ccs811_configver_type_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_zephyr__bluetooth__audio__ccp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__cellular.h_文件参考.md)
