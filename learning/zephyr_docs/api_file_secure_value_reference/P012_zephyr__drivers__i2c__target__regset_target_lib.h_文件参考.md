---
id: learning.zephyr-docs.api-file-secure-value-reference.page-12
title: zephyr__drivers__i2c__target__regset_target_lib.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_i2c\_\_target\_\_regset\_target\_lib.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

I2C目标库（Target Library）的公共API。

<a id="details"></a>

```c
#include <stddef.h>
#include <sys/types.h>
```

查看此文件的源码。

I2C目标库（Target Library）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_regset_5Ftarget_5Flib_5Fdata"></a>

```c
struct regset_target_lib_data
```

相关声明：[regset_target_lib_data](../system_service_model_reference/P076_regset_target_lib_data_结构体.md)。

寄存器集合库（Register Set Library）的配置。

<a id="r_regset_5Ftarget_5Flib_5Fconfig"></a>

```c
struct regset_target_lib_config
```

相关声明：[regset_target_lib_config](../system_service_model_reference/P075_regset_target_lib_config_结构体.md)。

寄存器集合库（Register Set Library）的数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_a79943b8ddec7743a042654b9ff166493"></a>

```c
#define REGSET_TARGET_LIB_STRUCT_CHECK(config, data)
```

相关声明：[REGSET_TARGET_LIB_STRUCT_CHECK](#a79943b8ddec7743a042654b9ff166493)。

验证寄存器集（Regset）数据结构的偏移量（Offset）。

<a id="r_a9e5bceef34dca7003b5b0f146a92a4de"></a>

```c
#define REGSET_TARGET_LIB_DT_BUILD_ASSERT(node_id)
```

相关声明：[REGSET_TARGET_LIB_DT_BUILD_ASSERT](#a9e5bceef34dca7003b5b0f146a92a4de)。

验证设备树（Devicetree）中的节点属性。

<a id="r_a281d7131af504497936d38691370da63"></a>

```c
#define REGSET_TARGET_LIB_DT_INST_BUILD_ASSERT(inst)
```

相关声明：[REGSET_TARGET_LIB_DT_INST_BUILD_ASSERT](#a281d7131af504497936d38691370da63)。

验证设备树实例（Devicetree Instance）中的节点属性。

<a id="r_a7c1c2ac8ae4179734f4243d53038a0a2"></a>

```c
#define REGSET_TARGET_LIB_DT_CONFIG_INIT(node_id)
```

相关声明：[REGSET_TARGET_LIB_DT_CONFIG_INIT](#a7c1c2ac8ae4179734f4243d53038a0a2)。

根据设备树（Devicetree）定义公共数据结构。

<a id="r_af35888a8fc2afc342c1316c4fa5ae966"></a>

```c
#define REGSET_TARGET_LIB_DT_INST_CONFIG_INIT(inst)
```

相关声明：[REGSET_TARGET_LIB_DT_INST_CONFIG_INIT](#af35888a8fc2afc342c1316c4fa5ae966)。

根据设备树实例（Devicetree Instance）定义公共数据结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ae9e6dd062981be4f7c429ffb12452745"></a>

```c
typedef void(* regset_target_lib_changed_handler_t) (const struct device *dev, void *user_data)
```

相关声明：[regset_target_lib_changed_handler_t](#ae9e6dd062981be4f7c429ffb12452745)、[device](../device_reference/P002_设备对象结构.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ad92d2e54bdf7426ea49cea95930fa142"></a>

```c
void regset_target_lib_set_changed_callback (const struct device *dev, regset_target_lib_changed_handler_t handler, void *user_data)
```

相关声明：[regset_target_lib_set_changed_callback](#ad92d2e54bdf7426ea49cea95930fa142)、[device](../device_reference/P002_设备对象结构.md)、[regset_target_lib_changed_handler_t](#ae9e6dd062981be4f7c429ffb12452745)。

设置寄存器集变化回调处理函数（Regset Changed Callback Handler）。

<a id="r_ace6db98c44d46daff92c8d7f29fd4f54"></a>

```c
size_t regset_target_lib_get_size (const struct device *dev)
```

相关声明：[regset_target_lib_get_size](#ace6db98c44d46daff92c8d7f29fd4f54)、[device](../device_reference/P002_设备对象结构.md)。

获取寄存器集大小（Register Set Size）。

<a id="r_aff17ae03f428fd989be2b108f87d3f49"></a>

```c
int regset_target_lib_read_data (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[regset_target_lib_read_data](#aff17ae03f428fd989be2b108f87d3f49)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

从寄存器集（Register Set）读取数据。

<a id="r_a746682f1490935846f189fddae22f4ac"></a>

```c
int regset_target_lib_write_data (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[regset_target_lib_write_data](#a746682f1490935846f189fddae22f4ac)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

向寄存器集（Register Set）写入数据。

<a id="r_aab1502efe79713b23cc9b66add677c1a"></a>

```c
int regset_target_lib_set_addr (const struct device *dev, uint8_t addr)
```

相关声明：[regset_target_lib_set_addr](#aab1502efe79713b23cc9b66add677c1a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在运行时改变寄存器集目标设备地址（Register Set Target Address）。

<a id="r_afb1e7a6fe4e25d22f335c00da29c2378"></a>

```c
int regset_target_lib_init (const struct device *dev)
```

相关声明：[regset_target_lib_init](#afb1e7a6fe4e25d22f335c00da29c2378)、[device](../device_reference/P002_设备对象结构.md)。

初始化寄存器集数据结构（Register Set Data Structures）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 12.5\_变量（Variables）

<a id="r_af4882a009f613f2adccabd25019ee44a"></a>

```c
const struct i2c_target_driver_api regset_target_api
```

相关声明：[i2c_target_driver_api](../hardware/P315_I2C目标驱动函数表.md)、[regset_target_api](#af4882a009f613f2adccabd25019ee44a)。

通用寄存器集库的 I2C 目标设备 API（I2C Target API）。

## 12.6\_详细说明（Detailed Documentation）

<a id="a9e5bceef34dca7003b5b0f146a92a4de"></a>

### `REGSET_TARGET_LIB_DT_BUILD_ASSERT`

```c
#define REGSET_TARGET_LIB_DT_BUILD_ASSERT ( node_id)
```

展开值（Value）：

```c
BUILD_ASSERT(DT_PROP(node_id, size) <= (1 << DT_PROP_OR(node_id, address_width, 8)),    \
             "size must be <= than 2^address_width");
```

验证设备树（Devicetree）中的节点属性。

<a id="a7c1c2ac8ae4179734f4243d53038a0a2"></a>

### `REGSET_TARGET_LIB_DT_CONFIG_INIT`

```c
#define REGSET_TARGET_LIB_DT_CONFIG_INIT ( node_id)
```

展开值（Value）：

```c
{                                                               \
        .bus = I2C_DT_SPEC_GET(node_id),                        \
        .buffer_size = DT_PROP(node_id, size),                  \
        .buffer = (uint8_t[DT_PROP(node_id, size)]) {},         \
        .address_width = DT_PROP_OR(node_id, address_width, 8), \
        .auto_register = DT_PROP(node_id, auto_register),       \
}
```

根据设备树（Devicetree）定义公共数据结构。

<a id="a281d7131af504497936d38691370da63"></a>

### `REGSET_TARGET_LIB_DT_INST_BUILD_ASSERT`

```c
#define REGSET_TARGET_LIB_DT_INST_BUILD_ASSERT ( inst)
```

展开值（Value）：

```c
REGSET_TARGET_LIB_DT_BUILD_ASSERT(DT_DRV_INST(inst))
```

验证设备树实例（Devicetree Instance）中的节点属性。

<a id="af35888a8fc2afc342c1316c4fa5ae966"></a>

### `REGSET_TARGET_LIB_DT_INST_CONFIG_INIT`

```c
#define REGSET_TARGET_LIB_DT_INST_CONFIG_INIT ( inst)
```

展开值（Value）：

```c
REGSET_TARGET_LIB_DT_CONFIG_INIT(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）定义公共数据结构。

<a id="a79943b8ddec7743a042654b9ff166493"></a>

### `REGSET_TARGET_LIB_STRUCT_CHECK`

```c
#define REGSET_TARGET_LIB_STRUCT_CHECK ( config, data )
```

展开值（Value）：

```c
BUILD_ASSERT(offsetof(config, regset_cfg) == 0,                         \
             "struct regset_target_lib_config must be placed first");   \
BUILD_ASSERT(offsetof(data, regset_data) == 0,                          \
             "struct regset_target_lib_data must be placed first")
```

验证寄存器集（Regset）数据结构的偏移量（Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置结构体（config structure）的名称。 |
| `data` | 数据结构名称（Data Structure Name）。 |

<a id="ae9e6dd062981be4f7c429ffb12452745"></a>

### `regset_target_lib_changed_handler_t`

```c
typedef void(* regset_target_lib_changed_handler_t) (const struct device *dev, void *user_data)
```

定义应用程序回调处理函数的签名（Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `user_data` | 设置回调时提供的可选用户数据（Optional User Data）。 |

<a id="ace6db98c44d46daff92c8d7f29fd4f54"></a>

### `regset_target_lib_get_size()`

```c
size_t regset_target_lib_get_size ( const struct device * dev)
```

获取寄存器集大小（Register Set Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：寄存器集大小（Register Set Size），单位为字节。

<a id="afb1e7a6fe4e25d22f335c00da29c2378"></a>

### `regset_target_lib_init()`

```c
int regset_target_lib_init ( const struct device * dev)
```

初始化寄存器集数据结构（Register Set Data Structures）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="aff17ae03f428fd989be2b108f87d3f49"></a>

### `regset_target_lib_read_data()`

```c
int regset_target_lib_read_data ( const struct device * dev, off_t offset, void * data, size_t len )
```

从寄存器集（Register Set）读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `offset` | 要读取的地址偏移量。 |
| `data` | 用于保存所读数据的缓冲区。 |
| `len` | 要读取的字节数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="aab1502efe79713b23cc9b66add677c1a"></a>

### `regset_target_lib_set_addr()`

```c
int regset_target_lib_set_addr ( const struct device * dev, uint8_t addr )
```

在运行时改变寄存器集目标设备地址（Register Set Target Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `addr` | 要赋给寄存器集目标设备的新地址（New Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时（Successful）。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `-EIO` | 执行 `i2c_taget_register` 时发生一般输入／输出错误（General I/O Error）。译注：函数名拼写按原文保留。 |
| `-ENOSYS` | 未实现目标模式（Target Mode）时。 |

<a id="ad92d2e54bdf7426ea49cea95930fa142"></a>

### `regset_target_lib_set_changed_callback()`

```c
void regset_target_lib_set_changed_callback ( const struct device * dev, regset_target_lib_changed_handler_t handler, void * user_data )
```

设置寄存器集变化回调处理函数（Regset Changed Callback Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `handler` | 寄存器集变化时调用的处理函数（Handler）。 |
| `user_data` | 传给回调的可选用户数据（Optional User Data）。 |

<a id="a746682f1490935846f189fddae22f4ac"></a>

### `regset_target_lib_write_data()`

```c
int regset_target_lib_write_data ( const struct device * dev, off_t offset, const void * data, size_t len )
```

向寄存器集（Register Set）写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `offset` | 要写入数据的地址偏移量（Address Offset）。 |
| `data` | 包含待写入数据的缓冲区（Buffer）。 |
| `len` | 要写入的字节数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="af4882a009f613f2adccabd25019ee44a"></a>

### `regset_target_api`

```c
const struct i2c_target_driver_api regset_target_api
```

声明属性：`extern`。

通用寄存器集库的 I2C 目标设备 API（I2C Target API）。


## 12.7\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P700_regset_target_lib.h_源码浏览.md)
- [regset_target_lib_data](../system_service_model_reference/P076_regset_target_lib_data_结构体.md)
- [regset_target_lib_config](../system_service_model_reference/P075_regset_target_lib_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i2c_target_driver_api](../hardware/P315_I2C目标驱动函数表.md)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [I2C_DT_SPEC_GET](../hardware/P305_I2C公共接口.md#gabb3ae5225cea677f3f3b36e4477ed045)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__i2c__interface_html_gabb3ae5225cea677f3f3b36e4477ed045"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="aregset__target__lib_8h_html_a9e5bceef34dca7003b5b0f146a92a4de"></a>
<a id="aregset__target__lib_8h_html_a7c1c2ac8ae4179734f4243d53038a0a2"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P011_zephyr__posix__pthread.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__pinctrl__v2m-musca-b1-pinctrl.h_文件参考.md)
