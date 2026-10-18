---
id: learning.zephyr-docs.api-file-reference.page-232
title: zephyr__usb__msos_desc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第232章\_zephyr\_\_usb\_\_msos\_desc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microsoft OS 2.0描述符（Descriptor）的定义。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

Microsoft OS 2.0描述符（Descriptor）的定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 232.1\_数据结构（Data Structures）

<a id="r_msosv2_5Fdescriptor_5Fset_5Fheader"></a>

```c
struct msosv2_descriptor_set_header
```

相关声明：[msosv2_descriptor_set_header](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md)。

<a id="r_msosv2_5Fconfiguration_5Fsubset_5Fheader"></a>

```c
struct msosv2_configuration_subset_header
```

相关声明：[msosv2_configuration_subset_header](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md)。

<a id="r_msosv2_5Ffunction_5Fsubset_5Fheader"></a>

```c
struct msosv2_function_subset_header
```

相关声明：[msosv2_function_subset_header](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md)。

<a id="r_msosv2_5Fcompatible_5Fid"></a>

```c
struct msosv2_compatible_id
```

相关声明：[msosv2_compatible_id](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md)。

<a id="r_msosv2_5Fguids_5Fproperty"></a>

```c
struct msosv2_guids_property
```

相关声明：[msosv2_guids_property](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md)。

<a id="r_msosv2_5Fresume_5Ftime"></a>

```c
struct msosv2_resume_time
```

相关声明：[msosv2_resume_time](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md)。

<a id="r_msosv2_5Fmodel_5Fid"></a>

```c
struct msosv2_model_id
```

相关声明：[msosv2_model_id](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md)。

<a id="r_msosv2_5Fccgp_5Fdevice"></a>

```c
struct msosv2_ccgp_device
```

相关声明：[msosv2_ccgp_device](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md)。

<a id="r_msosv2_5Fvendor_5Frevision"></a>

```c
struct msosv2_vendor_revision
```

相关声明：[msosv2_vendor_revision](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 232.2\_宏定义（Macros）

<a id="r_a927c65f355232352e67c60efdd293cff"></a>

```c
#define DEVICE_INTERFACE_GUIDS_PROPERTY_NAME
```

相关声明：[DEVICE_INTERFACE_GUIDS_PROPERTY_NAME](#a927c65f355232352e67c60efdd293cff)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 232.3\_枚举（Enumerations）

<a id="r_ab443ad91634b7a8fb19fc2aa7108e631"></a>

```c
enum msosv2_descriptor_index { MS_OS_20_DESCRIPTOR_INDEX = 0x07 , MS_OS_20_SET_ALT_ENUMERATION = 0x08 }
```

相关声明：[msosv2_descriptor_index](#ab443ad91634b7a8fb19fc2aa7108e631)、[MS_OS_20_DESCRIPTOR_INDEX](#ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5)、[MS_OS_20_SET_ALT_ENUMERATION](#ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116)。

<a id="r_ae46389cacf4c5cca962702fcf0f6feb5"></a>

```c
enum msosv2_descriptor_type { MS_OS_20_SET_HEADER_DESCRIPTOR = 0x00 , MS_OS_20_SUBSET_HEADER_CONFIGURATION = 0x01 , MS_OS_20_SUBSET_HEADER_FUNCTION = 0x02 , MS_OS_20_FEATURE_COMPATIBLE_ID = 0x03 , MS_OS_20_FEATURE_REG_PROPERTY = 0x04 , MS_OS_20_FEATURE_MIN_RESUME_TIME = 0x05 , MS_OS_20_FEATURE_MODEL_ID = 0x06 , MS_OS_20_FEATURE_CCGP_DEVICE = 0x07 , MS_OS_20_FEATURE_VENDOR_REVISION = 0x08 }
```

相关声明：[msosv2_descriptor_type](#ae46389cacf4c5cca962702fcf0f6feb5)、[MS_OS_20_SET_HEADER_DESCRIPTOR](#ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d)、[MS_OS_20_SUBSET_HEADER_CONFIGURATION](#ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc)、[MS_OS_20_SUBSET_HEADER_FUNCTION](#ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7)、[MS_OS_20_FEATURE_COMPATIBLE_ID](#ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265)、[MS_OS_20_FEATURE_REG_PROPERTY](#ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62)、[MS_OS_20_FEATURE_MIN_RESUME_TIME](#ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009)、[MS_OS_20_FEATURE_MODEL_ID](#ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c)、[MS_OS_20_FEATURE_CCGP_DEVICE](#ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004)、[MS_OS_20_FEATURE_VENDOR_REVISION](#ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6)。

<a id="r_a1afad4029116a837d4430a0ea976254f"></a>

```c
enum msosv2_property_data_type { MS_OS_20_PROPERTY_DATA_RESERVED = 0 , MS_OS_20_PROPERTY_DATA_REG_SZ = 1 , MS_OS_20_PROPERTY_DATA_REG_EXPAND_SZ = 2 , MS_OS_20_PROPERTY_DATA_REG_BINARY = 3 , MS_OS_20_PROPERTY_DATA_REG_DWORD_LITTLE_ENDIAN = 4 , MS_OS_20_PROPERTY_DATA_REG_DWORD_BIG_ENDIAN = 5 , MS_OS_20_PROPERTY_DATA_REG_LINK = 6 , MS_OS_20_PROPERTY_DATA_REG_MULTI_SZ = 7 }
```

相关声明：[msosv2_property_data_type](#a1afad4029116a837d4430a0ea976254f)、[MS_OS_20_PROPERTY_DATA_RESERVED](#a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17)、[MS_OS_20_PROPERTY_DATA_REG_SZ](#a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489)、[MS_OS_20_PROPERTY_DATA_REG_EXPAND_SZ](#a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c)、[MS_OS_20_PROPERTY_DATA_REG_BINARY](#a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1)、[MS_OS_20_PROPERTY_DATA_REG_DWORD_LITTLE_ENDIAN](#a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10)、[MS_OS_20_PROPERTY_DATA_REG_DWORD_BIG_ENDIAN](#a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670)、[MS_OS_20_PROPERTY_DATA_REG_LINK](#a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81)、[MS_OS_20_PROPERTY_DATA_REG_MULTI_SZ](#a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5)。

## 232.4\_详细说明（Detailed Documentation）

<a id="a927c65f355232352e67c60efdd293cff"></a>

### `DEVICE_INTERFACE_GUIDS_PROPERTY_NAME`

```c
#define DEVICE_INTERFACE_GUIDS_PROPERTY_NAME
```

展开值（Value）：

```c
'D', 0x00, 'e', 0x00, 'v', 0x00, 'i', 0x00, 'c', 0x00, 'e', 0x00, \
'I', 0x00, 'n', 0x00, 't', 0x00, 'e', 0x00, 'r', 0x00, 'f', 0x00, \
'a', 0x00, 'c', 0x00, 'e', 0x00, 'G', 0x00, 'U', 0x00, 'I', 0x00, \
'D', 0x00, 's', 0x00, 0x00, 0x00
```

<a id="ab443ad91634b7a8fb19fc2aa7108e631"></a>

### `msosv2_descriptor_index`

```c
enum msosv2_descriptor_index
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MS_OS_20_DESCRIPTOR_INDEX` |  |
| `MS_OS_20_SET_ALT_ENUMERATION` |  |

<a id="ae46389cacf4c5cca962702fcf0f6feb5"></a>

### `msosv2_descriptor_type`

```c
enum msosv2_descriptor_type
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MS_OS_20_SET_HEADER_DESCRIPTOR` |  |
| `MS_OS_20_SUBSET_HEADER_CONFIGURATION` |  |
| `MS_OS_20_SUBSET_HEADER_FUNCTION` |  |
| `MS_OS_20_FEATURE_COMPATIBLE_ID` |  |
| `MS_OS_20_FEATURE_REG_PROPERTY` |  |
| `MS_OS_20_FEATURE_MIN_RESUME_TIME` |  |
| `MS_OS_20_FEATURE_MODEL_ID` |  |
| `MS_OS_20_FEATURE_CCGP_DEVICE` |  |
| `MS_OS_20_FEATURE_VENDOR_REVISION` |  |

<a id="a1afad4029116a837d4430a0ea976254f"></a>

### `msosv2_property_data_type`

```c
enum msosv2_property_data_type
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MS_OS_20_PROPERTY_DATA_RESERVED` |  |
| `MS_OS_20_PROPERTY_DATA_REG_SZ` |  |
| `MS_OS_20_PROPERTY_DATA_REG_EXPAND_SZ` |  |
| `MS_OS_20_PROPERTY_DATA_REG_BINARY` |  |
| `MS_OS_20_PROPERTY_DATA_REG_DWORD_LITTLE_ENDIAN` |  |
| `MS_OS_20_PROPERTY_DATA_REG_DWORD_BIG_ENDIAN` |  |
| `MS_OS_20_PROPERTY_DATA_REG_LINK` |  |
| `MS_OS_20_PROPERTY_DATA_REG_MULTI_SZ` |  |


## 232.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/msos__desc_8h_source.html)
- [msosv2_descriptor_set_header](../device_power_control_model_reference/P037_msosv2_descriptor_set_header_结构体.md)
- [msosv2_configuration_subset_header](../device_power_control_model_reference/P036_msosv2_configuration_subset_header_结构体.md)
- [msosv2_function_subset_header](../device_power_control_model_reference/P038_msosv2_function_subset_header_结构体.md)
- [msosv2_compatible_id](../device_power_control_model_reference/P035_msosv2_compatible_id_结构体.md)
- [msosv2_guids_property](../device_power_control_model_reference/P039_msosv2_guids_property_结构体.md)
- [msosv2_resume_time](../device_power_control_model_reference/P041_msosv2_resume_time_结构体.md)
- [msosv2_model_id](../device_power_control_model_reference/P040_msosv2_model_id_结构体.md)
- [msosv2_ccgp_device](../device_power_control_model_reference/P034_msosv2_ccgp_device_结构体.md)
- [msosv2_vendor_revision](../device_power_control_model_reference/P042_msosv2_vendor_revision_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ab443ad91634b7a8fb19fc2aa7108e631abe0e6e00164db250e4ad900f418a57d5"></a>
<a id="ab443ad91634b7a8fb19fc2aa7108e631a2ae9d4948f03b7d9623c547daa0a9116"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5ac74a28d4e873b255d5b027af5ffffb5d"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5afe117782c0101a880e152a8a1110ecbc"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5a1200730075635cba8dea3420be41d1a7"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5adf3b0e226fd373b882e27ed494fba265"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5ad49ae449e2e2ff519a69018612ab5e62"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5a7061acf1dbbeb7e2fbb88d149d295009"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5ac7fc46a0124656e986871ae3b085536c"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5ab457a91ffd658376d87d7d32ad770004"></a>
<a id="ae46389cacf4c5cca962702fcf0f6feb5a2f7940f495e1a996692f474a456d63d6"></a>
<a id="a1afad4029116a837d4430a0ea976254fac1e0035b4badb15f714bff249514ef17"></a>
<a id="a1afad4029116a837d4430a0ea976254fa404430118680c625a399662e981c4489"></a>
<a id="a1afad4029116a837d4430a0ea976254fa9245e361cbe8425c1b54958ba0c0902c"></a>
<a id="a1afad4029116a837d4430a0ea976254fae8bd325ca3f9cc1d33d229d0de14aba1"></a>
<a id="a1afad4029116a837d4430a0ea976254faa831bf4ba88de3eb768745c41a8dee10"></a>
<a id="a1afad4029116a837d4430a0ea976254fa969e1f96f1582db317bbf96d183ae670"></a>
<a id="a1afad4029116a837d4430a0ea976254fa4050949a26b3a61f1aeecc996eb02d81"></a>
<a id="a1afad4029116a837d4430a0ea976254fa89b2d8dfbddc343879edc14a5c9f93f5"></a>

---

[上一章](P231_zephyr__posix__mqueue.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P233_zephyr__dt-bindings__pinctrl__mspm0-pinctrl.h_文件参考.md)
