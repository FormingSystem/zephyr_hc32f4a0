---
id: learning.zephyr-docs.api-file-reference.page-176
title: zephyr__dt-bindings__i2c__it8xxx2-i2c.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_zephyr\_\_dt-bindings\_\_i2c\_\_it8xxx2-i2c.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-i2c_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 176.1\_宏定义（Macros）

<a id="r_a9f78924cf5b262f18222242fb9c95953"></a>

```c
#define IT8XXX2_ECPM_CGCTRL4R_OFF 0x09
```

相关声明：[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_ad4ed6083b062932a8c9dd759b688f6de"></a>

```c
#define CGC_OFFSET_SMBF ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x80)
```

相关声明：[CGC_OFFSET_SMBF](#ad4ed6083b062932a8c9dd759b688f6de)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_a330c86262342d98ccb02ad13ae2f137d"></a>

```c
#define CGC_OFFSET_SMBE ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x40)
```

相关声明：[CGC_OFFSET_SMBE](#a330c86262342d98ccb02ad13ae2f137d)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_a8e413daf97c14719910d2e662c0eca75"></a>

```c
#define CGC_OFFSET_SMBD ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x20)
```

相关声明：[CGC_OFFSET_SMBD](#a8e413daf97c14719910d2e662c0eca75)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_ab55d020323d4cd67f71e228913a567e6"></a>

```c
#define CGC_OFFSET_SMBC ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x10)
```

相关声明：[CGC_OFFSET_SMBC](#ab55d020323d4cd67f71e228913a567e6)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_a7e2921ab27adcdab5494194f41085f8d"></a>

```c
#define CGC_OFFSET_SMBB ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x08)
```

相关声明：[CGC_OFFSET_SMBB](#a7e2921ab27adcdab5494194f41085f8d)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_ab6bf39556df2289991cc268d38cfb45c"></a>

```c
#define CGC_OFFSET_SMBA ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x04)
```

相关声明：[CGC_OFFSET_SMBA](#ab6bf39556df2289991cc268d38cfb45c)、[IT8XXX2_ECPM_CGCTRL4R_OFF](#a9f78924cf5b262f18222242fb9c95953)。

<a id="r_acbbd55b831e98ea4919e1fd13fedcb7a"></a>

```c
#define I2C_CHA_LOCATE 0
```

相关声明：[I2C_CHA_LOCATE](#acbbd55b831e98ea4919e1fd13fedcb7a)。

<a id="r_aebaf0e97ddd1e9e11495467c3553aba9"></a>

```c
#define I2C_CHB_LOCATE 1
```

相关声明：[I2C_CHB_LOCATE](#aebaf0e97ddd1e9e11495467c3553aba9)。

<a id="r_a96de9ecb61d81496b247a90cad938761"></a>

```c
#define I2C_CHC_LOCATE 2
```

相关声明：[I2C_CHC_LOCATE](#a96de9ecb61d81496b247a90cad938761)。

<a id="r_ae21cc6587cd40acd96c177e69b8c806d"></a>

```c
#define I2C_CHD_LOCATE 3
```

相关声明：[I2C_CHD_LOCATE](#ae21cc6587cd40acd96c177e69b8c806d)。

<a id="r_a9810b4bfaa5f1892fe9fe4aa05dce5c8"></a>

```c
#define I2C_CHE_LOCATE 4
```

相关声明：[I2C_CHE_LOCATE](#a9810b4bfaa5f1892fe9fe4aa05dce5c8)。

<a id="r_ae488c1cf89f783e12f975b446bc90b23"></a>

```c
#define I2C_CHF_LOCATE 5
```

相关声明：[I2C_CHF_LOCATE](#ae488c1cf89f783e12f975b446bc90b23)。

## 176.2\_详细说明（Detailed Documentation）

<a id="ab6bf39556df2289991cc268d38cfb45c"></a>

### `CGC_OFFSET_SMBA`

```c
#define CGC_OFFSET_SMBA ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x04)
```

<a id="a7e2921ab27adcdab5494194f41085f8d"></a>

### `CGC_OFFSET_SMBB`

```c
#define CGC_OFFSET_SMBB ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x08)
```

<a id="ab55d020323d4cd67f71e228913a567e6"></a>

### `CGC_OFFSET_SMBC`

```c
#define CGC_OFFSET_SMBC ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x10)
```

<a id="a8e413daf97c14719910d2e662c0eca75"></a>

### `CGC_OFFSET_SMBD`

```c
#define CGC_OFFSET_SMBD ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x20)
```

<a id="a330c86262342d98ccb02ad13ae2f137d"></a>

### `CGC_OFFSET_SMBE`

```c
#define CGC_OFFSET_SMBE ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x40)
```

<a id="ad4ed6083b062932a8c9dd759b688f6de"></a>

### `CGC_OFFSET_SMBF`

```c
#define CGC_OFFSET_SMBF ((IT8XXX2_ECPM_CGCTRL4R_OFF << 8) | 0x80)
```

<a id="acbbd55b831e98ea4919e1fd13fedcb7a"></a>

### `I2C_CHA_LOCATE`

```c
#define I2C_CHA_LOCATE 0
```

<a id="aebaf0e97ddd1e9e11495467c3553aba9"></a>

### `I2C_CHB_LOCATE`

```c
#define I2C_CHB_LOCATE 1
```

<a id="a96de9ecb61d81496b247a90cad938761"></a>

### `I2C_CHC_LOCATE`

```c
#define I2C_CHC_LOCATE 2
```

<a id="ae21cc6587cd40acd96c177e69b8c806d"></a>

### `I2C_CHD_LOCATE`

```c
#define I2C_CHD_LOCATE 3
```

<a id="a9810b4bfaa5f1892fe9fe4aa05dce5c8"></a>

### `I2C_CHE_LOCATE`

```c
#define I2C_CHE_LOCATE 4
```

<a id="ae488c1cf89f783e12f975b446bc90b23"></a>

### `I2C_CHF_LOCATE`

```c
#define I2C_CHF_LOCATE 5
```

<a id="a9f78924cf5b262f18222242fb9c95953"></a>

### `IT8XXX2_ECPM_CGCTRL4R_OFF`

```c
#define IT8XXX2_ECPM_CGCTRL4R_OFF 0x09
```


## 176.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P044_it8xxx2-i2c.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P175_zephyr__dt-bindings__comparator__it51xxx-vcmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P177_zephyr__dt-bindings__pwm__it8xxx2_pwm.h_文件参考.md)
