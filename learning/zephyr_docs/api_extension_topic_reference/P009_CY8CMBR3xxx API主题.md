---
id: learning.zephyr-docs.api-extension-topic-reference.page-9
title: CY8CMBR3xxx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_CY8CMBR3xxx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CY8CMBR3xxx 电容触摸传感器（Capacitive touch sensor）。

<a id="details"></a>

CY8CMBR3xxx 电容触摸传感器（Capacitive touch sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_cy8cmbr3xxx_2Eh"></a>

```c
file cy8cmbr3xxx.h
```

相关声明：[cy8cmbr3xxx.h](../api_file_configuration_reference/P014_zephyr__input__cy8cmbr3xxx.h_文件参考.md)。

CY8CMBR3xxx输入（Input）驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_cy8cmbr3xxx_5Fconfig_5Fdata"></a>

```c
struct cy8cmbr3xxx_config_data
```

相关声明：[cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)。

CY8CMBR3xxx设备的配置数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.3\_宏定义（Macros）

<a id="r_ga0d8534cc7dc74a6b17cf30ecb4ac1bfd"></a>

```c
#define CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE 128
```

相关声明：[CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE](#ga0d8534cc7dc74a6b17cf30ecb4ac1bfd)。

EZ-Click 配置数据（Configuration Data）的大小。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_ga26da2ccc3ff92bc2c29021f66f184448"></a>

```c
int cy8cmbr3xxx_configure (const struct device *dev, const struct cy8cmbr3xxx_config_data *config_data)
```

相关声明：[cy8cmbr3xxx_configure](#ga26da2ccc3ff92bc2c29021f66f184448)、[device](../device_reference/P002_设备对象结构.md)、[cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)。

使用 EZ-Click 生成的配置（Configuration）配置 CY8CMBR3xxx 设备。

## 9.5\_详细说明（Detailed Documentation）

<a id="ga0d8534cc7dc74a6b17cf30ecb4ac1bfd"></a>

### `CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE`

```c
#define CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE 128
```

```c
#include <zephyr/input/cy8cmbr3xxx.h>
```

EZ-Click 配置数据（Configuration Data）的大小。

<a id="ga26da2ccc3ff92bc2c29021f66f184448"></a>

### `cy8cmbr3xxx_configure()`

```c
int cy8cmbr3xxx_configure ( const struct device * dev, const struct cy8cmbr3xxx_config_data * config_data )
```

```c
#include <zephyr/input/cy8cmbr3xxx.h>
```

使用 EZ-Click 生成的配置（Configuration）配置 CY8CMBR3xxx 设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向输入设备实例（Input Device Instance）的指针（Pointer）。 |
| `config_data` | 指向设备配置数据（Configuration Data）的指针（Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `<0` | 失败时（If Failed）。 |


## 9.6\_原页交叉引用（Cross References）

- [cy8cmbr3xxx.h](../api_file_configuration_reference/P014_zephyr__input__cy8cmbr3xxx.h_文件参考.md)
- [cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_树莓派 Pico（Raspberry Pi Pico）.md) · [返回大纲](大纲.md) · [下一章](P010_DALI 驱动后端 API（Driver Backend API）.md)
