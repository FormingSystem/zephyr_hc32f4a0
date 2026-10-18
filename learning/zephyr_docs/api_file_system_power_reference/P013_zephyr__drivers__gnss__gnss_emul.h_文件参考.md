---
id: learning.zephyr-docs.api-file-system-power-reference.page-13
title: zephyr__drivers__gnss__gnss_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_gnss\_\_gnss\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gnss.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.1\_函数（Functions）

<a id="r_a9a94d20cae75b015b5903ace386ceeb8"></a>

```c
void gnss_emul_clear_data (const struct device *dev)
```

相关声明：[gnss_emul_clear_data](#a9a94d20cae75b015b5903ace386ceeb8)、[device](../device_reference/P002_设备对象结构.md)。

清除仿真器（Emulator）内部的全部 GNSS 数据。

<a id="r_a6616b032895a90cfe1e8128108bf051b"></a>

```c
void gnss_emul_set_data (const struct device *dev, const struct navigation_data *nav, const struct gnss_info *info, int64_t boot_realtime_ms)
```

相关声明：[gnss_emul_set_data](#a6616b032895a90cfe1e8128108bf051b)、[device](../device_reference/P002_设备对象结构.md)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)、[gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

设置仿真器（Emulator）内部的 GNSS 数据。

<a id="r_a49059255c56cae6e9e774f66f74ff659"></a>

```c
int gnss_emul_get_fix_rate (const struct device *dev, uint32_t *fix_interval_ms)
```

相关声明：[gnss_emul_get_fix_rate](#a49059255c56cae6e9e774f66f74ff659)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取最近配置的定位更新速率（Fix Rate），不受电源管理（PM）状态影响。

<a id="r_ad81023468758a4a07a69a0509e002b10"></a>

```c
int gnss_emul_get_navigation_mode (const struct device *dev, enum gnss_navigation_mode *mode)
```

相关声明：[gnss_emul_get_navigation_mode](#ad81023468758a4a07a69a0509e002b10)、[device](../device_reference/P002_设备对象结构.md)、[gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)。

获取最近配置的导航模式（Navigation Mode），不受电源管理（PM）状态影响。

<a id="r_a42f9dcdcc01e72d4d5d602aaf5f5a110"></a>

```c
int gnss_emul_get_enabled_systems (const struct device *dev, gnss_systems_t *systems)
```

相关声明：[gnss_emul_get_enabled_systems](#a42f9dcdcc01e72d4d5d602aaf5f5a110)、[device](../device_reference/P002_设备对象结构.md)、[gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)。

获取最近配置的卫星系统（Systems），不受电源管理（PM）状态影响。

## 13.2\_详细说明（Detailed Documentation）

<a id="a9a94d20cae75b015b5903ace386ceeb8"></a>

### `gnss_emul_clear_data()`

```c
void gnss_emul_clear_data ( const struct device * dev)
```

清除仿真器（Emulator）内部的全部 GNSS 数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GNSS 仿真器设备（Emulator Device）。 |

<a id="a42f9dcdcc01e72d4d5d602aaf5f5a110"></a>

### `gnss_emul_get_enabled_systems()`

```c
int gnss_emul_get_enabled_systems ( const struct device * dev, gnss_systems_t * systems )
```

获取最近配置的卫星系统（Systems），不受电源管理（PM）状态影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GNSS 仿真器设备（Emulator Device）。 |
| `systems` | 输出 GNSS 卫星系统（Systems）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="a49059255c56cae6e9e774f66f74ff659"></a>

### `gnss_emul_get_fix_rate()`

```c
int gnss_emul_get_fix_rate ( const struct device * dev, uint32_t * fix_interval_ms )
```

获取最近配置的定位更新速率（Fix Rate），不受电源管理（PM）状态影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GNSS 仿真器设备（Emulator Device）。 |
| `fix_interval_ms` | 输出定位间隔（Fix Interval）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="ad81023468758a4a07a69a0509e002b10"></a>

### `gnss_emul_get_navigation_mode()`

```c
int gnss_emul_get_navigation_mode ( const struct device * dev, enum gnss_navigation_mode * mode )
```

获取最近配置的导航模式（Navigation Mode），不受电源管理（PM）状态影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GNSS 仿真器设备（Emulator Device）。 |
| `mode` | 输出导航模式（Navigation Mode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="a6616b032895a90cfe1e8128108bf051b"></a>

### `gnss_emul_set_data()`

```c
void gnss_emul_set_data ( const struct device * dev, const struct navigation_data * nav, const struct gnss_info * info, int64_t boot_realtime_ms )
```

设置仿真器（Emulator）内部的 GNSS 数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | GNSS 仿真器设备（Emulator Device）。 |
| `nav` | 更新后的导航状态（Navigation State）。 |
| `info` | 更新后的 GNSS 定位信息（Fix Information）。 |
| `boot_realtime_ms` | 与系统启动（System Boot）对应的 Unix 时间戳（Timestamp）。 |


## 13.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gnss.h](../api_source_reference/P291_gnss.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P292_gnss_emul.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)
- [gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_zephyr__dt-bindings__pinctrl__gecko-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__misc__grove_lcd__grove_lcd.h_文件参考.md)
