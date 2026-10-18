---
id: learning.zephyr-docs.api-file-reference.page-139
title: zephyr__drivers__i2c__stm32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c_2stm32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_zephyr\_\_drivers\_\_i2c\_\_stm32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i2c_2stm32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 139.1\_枚举（Enumerations）

<a id="r_a1e3b0af0114531103001ffac5dc10730"></a>

```c
enum i2c_stm32_mode { I2CSTM32MODE_I2C , I2CSTM32MODE_SMBUSHOST , I2CSTM32MODE_SMBUSDEVICE , I2CSTM32MODE_SMBUSDEVICEARP }
```

相关声明：[i2c_stm32_mode](#a1e3b0af0114531103001ffac5dc10730)、[I2CSTM32MODE_I2C](#a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250)、[I2CSTM32MODE_SMBUSHOST](#a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b)、[I2CSTM32MODE_SMBUSDEVICE](#a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b)、[I2CSTM32MODE_SMBUSDEVICEARP](#a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 139.2\_函数（Functions）

<a id="r_ae82dc3ada1276b676169c95c6d239d82"></a>

```c
void i2c_stm32_set_smbus_mode (const struct device *dev, enum i2c_stm32_mode mode)
```

相关声明：[i2c_stm32_set_smbus_mode](#ae82dc3ada1276b676169c95c6d239d82)、[device](../device_reference/P002_设备对象结构.md)、[i2c_stm32_mode](#a1e3b0af0114531103001ffac5dc10730)。

## 139.3\_详细说明（Detailed Documentation）

<a id="a1e3b0af0114531103001ffac5dc10730"></a>

### `i2c_stm32_mode`

```c
enum i2c_stm32_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `I2CSTM32MODE_I2C` |  |
| `I2CSTM32MODE_SMBUSHOST` |  |
| `I2CSTM32MODE_SMBUSDEVICE` |  |
| `I2CSTM32MODE_SMBUSDEVICEARP` |  |

<a id="ae82dc3ada1276b676169c95c6d239d82"></a>

### `i2c_stm32_set_smbus_mode()`

```c
void i2c_stm32_set_smbus_mode ( const struct device * dev, enum i2c_stm32_mode mode )
```


## 139.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P327_stm32.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250"></a>
<a id="a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b"></a>
<a id="a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b"></a>
<a id="a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P138_zephyr__net__http__hpack.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P140_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain__iar.h_文件参考.md)
