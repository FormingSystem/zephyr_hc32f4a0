---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-8
title: zephyr__drivers__mfd__npm13xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_mfd\_\_npm13xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.1\_枚举（Enumerations）

<a id="r_ga4ac9f47283f10ea1d847cbd0038aad7a"></a>

```c
enum mfd_npm13xx_event_t { NPM13XX_EVENT_CHG_COMPLETED , NPM13XX_EVENT_CHG_ERROR , NPM13XX_EVENT_BATTERY_DETECTED , NPM13XX_EVENT_BATTERY_REMOVED , NPM13XX_EVENT_SHIPHOLD_PRESS , NPM13XX_EVENT_SHIPHOLD_RELEASE , NPM13XX_EVENT_WATCHDOG_WARN , NPM13XX_EVENT_VBUS_DETECTED , NPM13XX_EVENT_VBUS_REMOVED , NPM13XX_EVENT_GPIO0_EDGE , NPM13XX_EVENT_GPIO1_EDGE , NPM13XX_EVENT_GPIO2_EDGE , NPM13XX_EVENT_GPIO3_EDGE , NPM13XX_EVENT_GPIO4_EDGE , NPM13XX_EVENT_MAX }
```

相关声明：[mfd_npm13xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga4ac9f47283f10ea1d847cbd0038aad7a)、[NPM13XX_EVENT_CHG_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858)、[NPM13XX_EVENT_CHG_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6)、[NPM13XX_EVENT_BATTERY_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c)、[NPM13XX_EVENT_BATTERY_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d)、[NPM13XX_EVENT_SHIPHOLD_PRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646)、[NPM13XX_EVENT_SHIPHOLD_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5)、[NPM13XX_EVENT_WATCHDOG_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7)、[NPM13XX_EVENT_VBUS_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b)、[NPM13XX_EVENT_VBUS_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e)、[NPM13XX_EVENT_GPIO0_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8)、[NPM13XX_EVENT_GPIO1_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c)、[NPM13XX_EVENT_GPIO2_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25)、[NPM13XX_EVENT_GPIO3_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b)、[NPM13XX_EVENT_GPIO4_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35)、[NPM13XX_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_gabba0559ce29b71e1ce7065bf5d36f8d8"></a>

```c
int mfd_npm13xx_reg_read_burst (const struct device *dev, uint8_t base, uint8_t offset, void *data, size_t len)
```

相关声明：[mfd_npm13xx_reg_read_burst](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gabba0559ce29b71e1ce7065bf5d36f8d8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 npm13xx 读取多个寄存器（Registers）。

<a id="r_ga154c4c48888ff1587d157b16e38d2584"></a>

```c
int mfd_npm13xx_reg_read (const struct device *dev, uint8_t base, uint8_t offset, uint8_t *data)
```

相关声明：[mfd_npm13xx_reg_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga154c4c48888ff1587d157b16e38d2584)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 npm13xx 读取单个寄存器（Register）。

<a id="r_gac1c7815a4bcfb2262fd4f02d28f2f781"></a>

```c
int mfd_npm13xx_reg_write (const struct device *dev, uint8_t base, uint8_t offset, uint8_t data)
```

相关声明：[mfd_npm13xx_reg_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gac1c7815a4bcfb2262fd4f02d28f2f781)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 npm13xx 写入单个寄存器（Register）。

<a id="r_ga2a4ef39c1703b3014d29e6e4412f1eae"></a>

```c
int mfd_npm13xx_reg_write_burst (const struct device *dev, uint8_t base, uint8_t offset, void *data, size_t len)
```

相关声明：[mfd_npm13xx_reg_write_burst](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga2a4ef39c1703b3014d29e6e4412f1eae)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 npm13xx 写入多个寄存器（Registers）。

<a id="r_ga239cfcef1ab91e3ccc8fb7f39f11dfd2"></a>

```c
int mfd_npm13xx_reg_update (const struct device *dev, uint8_t base, uint8_t offset, uint8_t data, uint8_t mask)
```

相关声明：[mfd_npm13xx_reg_update](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新 npm13xx 寄存器（Register）中的选定位。

<a id="r_ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9"></a>

```c
int mfd_npm13xx_set_timer (const struct device *dev, uint32_t time_ms)
```

相关声明：[mfd_npm13xx_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入 npm13xx 定时器寄存器（Timer Register）。

<a id="r_ga43c5a5225a0cc2738506d5556ecb06ba"></a>

```c
int mfd_npm13xx_reset (const struct device *dev)
```

相关声明：[mfd_npm13xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga43c5a5225a0cc2738506d5556ecb06ba)、[device](../device_reference/P002_设备对象结构.md)。

npm13xx 完全电源复位（Full Power Reset）。

<a id="r_gaf23758d56ac58f814bc2f093ebfa1282"></a>

```c
int mfd_npm13xx_hibernate (const struct device *dev, uint32_t time_ms)
```

相关声明：[mfd_npm13xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gaf23758d56ac58f814bc2f093ebfa1282)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

npm13xx 休眠（Hibernate）。

<a id="r_ga3cac4a85cee20242d3a988d9830ea547"></a>

```c
int mfd_npm13xx_add_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm13xx_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3cac4a85cee20242d3a988d9830ea547)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

添加 npm13xx 事件回调（Event Callback）。

<a id="r_ga35fbc854545b9113f6ec36677491b151"></a>

```c
int mfd_npm13xx_remove_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm13xx_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga35fbc854545b9113f6ec36677491b151)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

移除 npm13xx 事件回调（Event Callback）。


## 8.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P162_npm13xx.h_源码浏览.md)
- [mfd_npm13xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga4ac9f47283f10ea1d847cbd0038aad7a)
- [NPM13XX_EVENT_CHG_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858)
- [NPM13XX_EVENT_CHG_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6)
- [NPM13XX_EVENT_BATTERY_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c)
- [NPM13XX_EVENT_BATTERY_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d)
- [NPM13XX_EVENT_SHIPHOLD_PRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646)
- [NPM13XX_EVENT_SHIPHOLD_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5)
- [NPM13XX_EVENT_WATCHDOG_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7)
- [NPM13XX_EVENT_VBUS_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b)
- [NPM13XX_EVENT_VBUS_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e)
- [NPM13XX_EVENT_GPIO0_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8)
- [NPM13XX_EVENT_GPIO1_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c)
- [NPM13XX_EVENT_GPIO2_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25)
- [NPM13XX_EVENT_GPIO3_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b)
- [NPM13XX_EVENT_GPIO4_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35)
- [NPM13XX_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)
- [mfd_npm13xx_reg_read_burst](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gabba0559ce29b71e1ce7065bf5d36f8d8)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_npm13xx_reg_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga154c4c48888ff1587d157b16e38d2584)
- [mfd_npm13xx_reg_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gac1c7815a4bcfb2262fd4f02d28f2f781)
- [mfd_npm13xx_reg_write_burst](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga2a4ef39c1703b3014d29e6e4412f1eae)
- [mfd_npm13xx_reg_update](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)
- [mfd_npm13xx_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mfd_npm13xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga43c5a5225a0cc2738506d5556ecb06ba)
- [mfd_npm13xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gaf23758d56ac58f814bc2f093ebfa1282)
- [mfd_npm13xx_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3cac4a85cee20242d3a988d9830ea547)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [mfd_npm13xx_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga35fbc854545b9113f6ec36677491b151)

---

[上一章](P007_zephyr__drivers__mfd__axp192.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__sensor__icm566xx.h_文件参考.md)
