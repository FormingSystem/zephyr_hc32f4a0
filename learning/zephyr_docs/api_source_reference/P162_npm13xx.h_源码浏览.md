---
id: learning.zephyr-docs.api-source-reference.page-162
title: npm13xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_npm13xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h.html)。

## 162.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga154c4c48888ff1587d157b16e38d2584"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga239cfcef1ab91e3ccc8fb7f39f11dfd2"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga2a4ef39c1703b3014d29e6e4412f1eae"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga35fbc854545b9113f6ec36677491b151"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga3cac4a85cee20242d3a988d9830ea547"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga43c5a5225a0cc2738506d5556ecb06ba"></a>
<a id="agroup__mfd__interface__npm13xx_html_ga4ac9f47283f10ea1d847cbd0038aad7a"></a>
<a id="agroup__mfd__interface__npm13xx_html_gabba0559ce29b71e1ce7065bf5d36f8d8"></a>
<a id="agroup__mfd__interface__npm13xx_html_gac1c7815a4bcfb2262fd4f02d28f2f781"></a>
<a id="agroup__mfd__interface__npm13xx_html_gaf23758d56ac58f814bc2f093ebfa1282"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c"></a>
<a id="agroup__mfd__interface__npm13xx_html_gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__callback_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MFD_NPM13XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MFD_NPM13XX_H_

#ifdef __cplusplus
extern "C" {
#endif


#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>

enum mfd_npm13xx_event_t {
        NPM13XX_EVENT_CHG_COMPLETED,
        NPM13XX_EVENT_CHG_ERROR,
        NPM13XX_EVENT_BATTERY_DETECTED,
        NPM13XX_EVENT_BATTERY_REMOVED,
        NPM13XX_EVENT_SHIPHOLD_PRESS,
        NPM13XX_EVENT_SHIPHOLD_RELEASE,
        NPM13XX_EVENT_WATCHDOG_WARN,
        NPM13XX_EVENT_VBUS_DETECTED,
        NPM13XX_EVENT_VBUS_REMOVED,
        NPM13XX_EVENT_GPIO0_EDGE,
        NPM13XX_EVENT_GPIO1_EDGE,
        NPM13XX_EVENT_GPIO2_EDGE,
        NPM13XX_EVENT_GPIO3_EDGE,
        NPM13XX_EVENT_GPIO4_EDGE,
        NPM13XX_EVENT_MAX
};

int mfd_npm13xx_reg_read_burst(const struct device *dev, uint8_t base, uint8_t offset, void *data,
                               size_t len);

int mfd_npm13xx_reg_read(const struct device *dev, uint8_t base, uint8_t offset, uint8_t *data);

int mfd_npm13xx_reg_write(const struct device *dev, uint8_t base, uint8_t offset, uint8_t data);

int mfd_npm13xx_reg_write_burst(const struct device *dev, uint8_t base, uint8_t offset, void *data,
                                size_t len);

int mfd_npm13xx_reg_update(const struct device *dev, uint8_t base, uint8_t offset, uint8_t data,
                           uint8_t mask);

int mfd_npm13xx_set_timer(const struct device *dev, uint32_t time_ms);

int mfd_npm13xx_reset(const struct device *dev);

int mfd_npm13xx_hibernate(const struct device *dev, uint32_t time_ms);

int mfd_npm13xx_add_callback(const struct device *dev, struct gpio_callback *callback);

int mfd_npm13xx_remove_callback(const struct device *dev, struct gpio_callback *callback);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MFD_NPM13XX_H_ */
```

## 162.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 158 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MFD_NPM13XX_H_`。

## 162.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm13xx_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
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
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mfd_npm13xx_reg_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga154c4c48888ff1587d157b16e38d2584)
- [mfd_npm13xx_reg_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gac1c7815a4bcfb2262fd4f02d28f2f781)
- [mfd_npm13xx_reg_write_burst](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga2a4ef39c1703b3014d29e6e4412f1eae)
- [mfd_npm13xx_reg_update](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)
- [mfd_npm13xx_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mfd_npm13xx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga43c5a5225a0cc2738506d5556ecb06ba)
- [mfd_npm13xx_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#gaf23758d56ac58f814bc2f093ebfa1282)
- [mfd_npm13xx_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga3cac4a85cee20242d3a988d9830ea547)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [mfd_npm13xx_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm13xx.html#ga35fbc854545b9113f6ec36677491b151)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)

---

[上一章](P161_npm10xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P163_npm2100.h_源码浏览.md)
