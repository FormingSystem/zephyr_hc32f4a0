---
id: learning.zephyr-docs.api-file-configuration-reference.page-14
title: zephyr__input__cy8cmbr3xxx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_input\_\_cy8cmbr3xxx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cy8cmbr3xxx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CY8CMBR3xxx输入（Input）驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

CY8CMBR3xxx输入（Input）驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_cy8cmbr3xxx_5Fconfig_5Fdata"></a>

```c
struct cy8cmbr3xxx_config_data
```

相关声明：[cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)。

CY8CMBR3xxx设备的配置数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga0d8534cc7dc74a6b17cf30ecb4ac1bfd"></a>

```c
#define CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE 128
```

相关声明：[CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga0d8534cc7dc74a6b17cf30ecb4ac1bfd)。

EZ-Click 配置数据（Configuration Data）的大小。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_ga26da2ccc3ff92bc2c29021f66f184448"></a>

```c
int cy8cmbr3xxx_configure (const struct device *dev, const struct cy8cmbr3xxx_config_data *config_data)
```

相关声明：[cy8cmbr3xxx_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga26da2ccc3ff92bc2c29021f66f184448)、[device](../device_reference/P002_设备对象结构.md)、[cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)。

使用 EZ-Click 生成的配置（Configuration）配置 CY8CMBR3xxx 设备。


## 14.4\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P038_cy8cmbr3xxx.h_源码浏览.md)
- [cy8cmbr3xxx_config_data](../sensor_navigation_model_reference/P007_cy8cmbr3xxx_config_data_结构体.md)
- [CY8CMBR3XXX_EZ_CLICK_CONFIG_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga0d8534cc7dc74a6b17cf30ecb4ac1bfd)
- [cy8cmbr3xxx_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__cy8cmbr3xxx__interface.html#ga26da2ccc3ff92bc2c29021f66f184448)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P013_zephyr__drivers__haptics__cs40l26.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__bluetooth__mesh__dfd_srv.h_文件参考.md)
