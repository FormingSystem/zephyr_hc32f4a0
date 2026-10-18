---
id: learning.zephyr-docs.api-file-service-interface-reference.page-2
title: zephyr__drivers__mfd__ad559x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ad559x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_mfd\_\_ad559x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ad559x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ade40e7e134b45f33b22758fed430d786"></a>

```c
#define AD559X_REG_SEQ_ADC 0x02U
```

相关声明：[AD559X_REG_SEQ_ADC](#ade40e7e134b45f33b22758fed430d786)。

<a id="r_a9259339213413a4829e7dce58546f131"></a>

```c
#define AD559X_REG_GEN_CTRL 0x03U
```

相关声明：[AD559X_REG_GEN_CTRL](#a9259339213413a4829e7dce58546f131)。

<a id="r_a7a588e6ec9e98cd0530a55414fcc63de"></a>

```c
#define AD559X_REG_ADC_CONFIG 0x04U
```

相关声明：[AD559X_REG_ADC_CONFIG](#a7a588e6ec9e98cd0530a55414fcc63de)。

<a id="r_a513c0ed1982f51edb294ce3c07d92c8f"></a>

```c
#define AD559X_REG_LDAC_EN 0x05U
```

相关声明：[AD559X_REG_LDAC_EN](#a513c0ed1982f51edb294ce3c07d92c8f)。

<a id="r_a843ed93d660cfe363f4b682bd6a574a2"></a>

```c
#define AD559X_REG_GPIO_PULLDOWN 0x06U
```

相关声明：[AD559X_REG_GPIO_PULLDOWN](#a843ed93d660cfe363f4b682bd6a574a2)。

<a id="r_a9f90d05e96f8bf8170d2d461019f71b4"></a>

```c
#define AD559X_REG_READ_AND_LDAC 0x07U
```

相关声明：[AD559X_REG_READ_AND_LDAC](#a9f90d05e96f8bf8170d2d461019f71b4)。

<a id="r_a55717b95bfb5f4d6218dcaa22ce597f8"></a>

```c
#define AD559X_REG_GPIO_OUTPUT_EN 0x08U
```

相关声明：[AD559X_REG_GPIO_OUTPUT_EN](#a55717b95bfb5f4d6218dcaa22ce597f8)。

<a id="r_a257a2ffecc969740e9a15231e05c74d4"></a>

```c
#define AD559X_REG_GPIO_SET 0x09U
```

相关声明：[AD559X_REG_GPIO_SET](#a257a2ffecc969740e9a15231e05c74d4)。

<a id="r_a1b1049f7ab7e768d286e3b599a72745d"></a>

```c
#define AD559X_REG_GPIO_INPUT_EN 0x0AU
```

相关声明：[AD559X_REG_GPIO_INPUT_EN](#a1b1049f7ab7e768d286e3b599a72745d)。

<a id="r_a79a840afe34154908a59e64e7c8526de"></a>

```c
#define AD559X_REG_PD_REF_CTRL 0x0BU
```

相关声明：[AD559X_REG_PD_REF_CTRL](#a79a840afe34154908a59e64e7c8526de)。

<a id="r_a1b52f6038d72362c06531801417c33d8"></a>

```c
#define AD559X_REG_IO_TS_CONFIG 0x0DU
```

相关声明：[AD559X_REG_IO_TS_CONFIG](#a1b52f6038d72362c06531801417c33d8)。

<a id="r_ad23dae3f8100399bd35ee97a23ef8b8f"></a>

```c
#define AD559X_DAC_RANGE BIT(4)
```

相关声明：[AD559X_DAC_RANGE](#ad23dae3f8100399bd35ee97a23ef8b8f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a681d85139d799b2f1c8b29f45af93903"></a>

```c
#define AD559X_ADC_RANGE BIT(5)
```

相关声明：[AD559X_ADC_RANGE](#a681d85139d799b2f1c8b29f45af93903)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8db6c5c634f572cfca2bcb2e2f2cdb73"></a>

```c
#define AD559X_EN_REF BIT(9)
```

相关声明：[AD559X_EN_REF](#a8db6c5c634f572cfca2bcb2e2f2cdb73)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a24da8b1b01da9473bcf1b953727ead1e"></a>

```c
#define AD559X_PIN_MAX 8U
```

相关声明：[AD559X_PIN_MAX](#a24da8b1b01da9473bcf1b953727ead1e)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga9280bf8cdaf3011a53073d189840e58f"></a>

```c
bool mfd_ad559x_has_pointer_byte_map (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mfd_ad559x_has_pointer_byte_map](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga9280bf8cdaf3011a53073d189840e58f)、[device](../device_reference/P002_设备对象结构.md)。

检查芯片是否具有指针字节映射（Pointer Byte Map）。

<a id="r_ga60a3bef4d69b2e5dcde5f15ab10ee607"></a>

```c
int mfd_ad559x_read_raw (const struct device *dev, uint8_t *val, size_t len)
```

相关声明：[mfd_ad559x_read_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga60a3bef4d69b2e5dcde5f15ab10ee607)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从芯片读取原始数据（Raw Data）。

<a id="r_ga0b9f70e3c85e17cd9f556f5cb98baf59"></a>

```c
int mfd_ad559x_write_raw (const struct device *dev, uint8_t *val, size_t len)
```

相关声明：[mfd_ad559x_write_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga0b9f70e3c85e17cd9f556f5cb98baf59)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向芯片写入原始数据（Raw Data）。

<a id="r_ga896686606e114e223ee5afe40518356f"></a>

```c
int mfd_ad559x_read_reg (const struct device *dev, uint8_t reg, uint8_t reg_data, uint16_t *val)
```

相关声明：[mfd_ad559x_read_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga896686606e114e223ee5afe40518356f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从指定寄存器（Register）读取数据。

<a id="r_gac91730fd6126260bc60da7c2637d7ccb"></a>

```c
int mfd_ad559x_write_reg (const struct device *dev, uint8_t reg, uint16_t val)
```

相关声明：[mfd_ad559x_write_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gac91730fd6126260bc60da7c2637d7ccb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向指定寄存器（Register）写入数据。

<a id="r_gace77752024305f468412262f063e2c2a"></a>

```c
int mfd_ad559x_read_adc_chan (const struct device *dev, uint8_t channel, uint16_t *result)
```

相关声明：[mfd_ad559x_read_adc_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gace77752024305f468412262f063e2c2a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从芯片读取模数转换器（ADC）通道数据。

<a id="r_ga9a07f9de00ca00e19daa56ac1fc923bc"></a>

```c
int mfd_ad559x_write_dac_chan (const struct device *dev, uint8_t channel, uint16_t value)
```

相关声明：[mfd_ad559x_write_dac_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga9a07f9de00ca00e19daa56ac1fc923bc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向芯片写入模数转换器（ADC）通道数据。

<a id="r_gacf88f29f46db4293e97f7fbb7a3edeb7"></a>

```c
int mfd_ad559x_gpio_port_get_raw (const struct device *dev, uint8_t gpio, uint16_t *value)
```

相关声明：[mfd_ad559x_gpio_port_get_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gacf88f29f46db4293e97f7fbb7a3edeb7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从芯片读取通用输入输出（GPIO）端口。

## 2.3\_详细说明（Detailed Documentation）

<a id="a681d85139d799b2f1c8b29f45af93903"></a>

### `AD559X_ADC_RANGE`

```c
#define AD559X_ADC_RANGE BIT(5)
```

<a id="ad23dae3f8100399bd35ee97a23ef8b8f"></a>

### `AD559X_DAC_RANGE`

```c
#define AD559X_DAC_RANGE BIT(4)
```

<a id="a8db6c5c634f572cfca2bcb2e2f2cdb73"></a>

### `AD559X_EN_REF`

```c
#define AD559X_EN_REF BIT(9)
```

<a id="a24da8b1b01da9473bcf1b953727ead1e"></a>

### `AD559X_PIN_MAX`

```c
#define AD559X_PIN_MAX 8U
```

<a id="a7a588e6ec9e98cd0530a55414fcc63de"></a>

### `AD559X_REG_ADC_CONFIG`

```c
#define AD559X_REG_ADC_CONFIG 0x04U
```

<a id="a9259339213413a4829e7dce58546f131"></a>

### `AD559X_REG_GEN_CTRL`

```c
#define AD559X_REG_GEN_CTRL 0x03U
```

<a id="a1b1049f7ab7e768d286e3b599a72745d"></a>

### `AD559X_REG_GPIO_INPUT_EN`

```c
#define AD559X_REG_GPIO_INPUT_EN 0x0AU
```

<a id="a55717b95bfb5f4d6218dcaa22ce597f8"></a>

### `AD559X_REG_GPIO_OUTPUT_EN`

```c
#define AD559X_REG_GPIO_OUTPUT_EN 0x08U
```

<a id="a843ed93d660cfe363f4b682bd6a574a2"></a>

### `AD559X_REG_GPIO_PULLDOWN`

```c
#define AD559X_REG_GPIO_PULLDOWN 0x06U
```

<a id="a257a2ffecc969740e9a15231e05c74d4"></a>

### `AD559X_REG_GPIO_SET`

```c
#define AD559X_REG_GPIO_SET 0x09U
```

<a id="a1b52f6038d72362c06531801417c33d8"></a>

### `AD559X_REG_IO_TS_CONFIG`

```c
#define AD559X_REG_IO_TS_CONFIG 0x0DU
```

<a id="a513c0ed1982f51edb294ce3c07d92c8f"></a>

### `AD559X_REG_LDAC_EN`

```c
#define AD559X_REG_LDAC_EN 0x05U
```

<a id="a79a840afe34154908a59e64e7c8526de"></a>

### `AD559X_REG_PD_REF_CTRL`

```c
#define AD559X_REG_PD_REF_CTRL 0x0BU
```

<a id="a9f90d05e96f8bf8170d2d461019f71b4"></a>

### `AD559X_REG_READ_AND_LDAC`

```c
#define AD559X_REG_READ_AND_LDAC 0x07U
```

<a id="ade40e7e134b45f33b22758fed430d786"></a>

### `AD559X_REG_SEQ_ADC`

```c
#define AD559X_REG_SEQ_ADC 0x02U
```


## 2.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P005_ad559x.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mfd_ad559x_has_pointer_byte_map](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga9280bf8cdaf3011a53073d189840e58f)
- [device](../device_reference/P002_设备对象结构.md)
- [mfd_ad559x_read_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga60a3bef4d69b2e5dcde5f15ab10ee607)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_ad559x_write_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga0b9f70e3c85e17cd9f556f5cb98baf59)
- [mfd_ad559x_read_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga896686606e114e223ee5afe40518356f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mfd_ad559x_write_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gac91730fd6126260bc60da7c2637d7ccb)
- [mfd_ad559x_read_adc_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gace77752024305f468412262f063e2c2a)
- [mfd_ad559x_write_dac_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#ga9a07f9de00ca00e19daa56ac1fc923bc)
- [mfd_ad559x_gpio_port_get_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__ad559x.html#gacf88f29f46db4293e97f7fbb7a3edeb7)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__drivers__display__ac057tc1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__clock_control__adi_max32_clock_control.h_文件参考.md)
